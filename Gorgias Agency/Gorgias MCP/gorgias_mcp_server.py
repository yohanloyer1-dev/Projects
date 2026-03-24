#!/usr/bin/env python3
"""
Gorgias MCP Server — v3
Multi-account Gorgias REST API integration for Claude via MCP.

Features:
  - Multi-account support via gorgias_accounts.json
  - Cursor-based pagination with rate-limit protection (2 req/s)
  - Pre-computed stats via POST /api/stats/{name} (legacy, sunset Dec 2026)
  - CSAT, ticket volume, and agent performance analytics
  - All tools support optional `account` and `response_format` parameters
  - Persistent HTTP client with connection pooling
  - Cached account credentials (use gorgias_reload_accounts to refresh)

Changelog v3 vs v2:
  - C1: All errors now raise ToolError (isError: true) instead of plain text
  - C2: Content-Type header only sent on POST/PUT/PATCH, not GET
  - C3: Rate-limit sleep (0.55s) between paginated pages
  - C4: Analytics tools capped at 500 items to avoid MCP timeout
  - C5: order_by / order_dir added to gorgias_list_tickets
  - H2/H3/H4: Added gorgias_list_teams, gorgias_list_macros, gorgias_list_custom_fields
  - H5: Accounts cached at module level; gorgias_reload_accounts for hot-reload
  - H6: Persistent httpx.AsyncClient (lazy init, connection pooling)
  - H7: JSON responses include has_more field
  - H8: Integer ID filters use `is not None` checks (not falsy)
  - H9/H10: gorgias_search_tickets and gorgias_list_ticket_messages use cursor pagination
  - M1: response_format validated as Literal["markdown", "json"]
  - M2: extra='forbid' on all Pydantic input models
  - M3: _render_value moved to module level
  - M4: gorgias_list_accounts uses BaseInput with response_format support
  - M5/M6: gorgias_list_tags and gorgias_list_customers use cursor pagination
  - M7: gorgias_list_views response handling made robust
  - M8/M9: All tool annotations include idempotentHint and title
  - M10: auth_email variable name avoids shadowing in customer_tickets
  - M11: mcp.run(transport="stdio") explicit
  - L1: Added gorgias_reload_accounts tool
  - L3: Agent CSAT averages include sample count
  - L4: gorgias_get_csat_stats passes date filters via API params (already done in v2)

Setup: see README.md
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Tuple

import httpx

try:
    from mcp.server.fastmcp import FastMCP, ToolError
except ImportError:
    from mcp.server.fastmcp import FastMCP  # type: ignore

    class ToolError(Exception):  # type: ignore
        """Raised to signal a tool execution error to the MCP client."""
        pass

from pydantic import BaseModel, ConfigDict, Field, field_validator


# ─── Server Initialization ────────────────────────────────────────────────────

mcp = FastMCP("gorgias_mcp")

# Path to the accounts config file (same directory as this script)
ACCOUNTS_FILE = Path(__file__).parent / "gorgias_accounts.json"


# ─── Account Management ───────────────────────────────────────────────────────

_accounts_cache: Optional[Dict[str, Dict[str, str]]] = None


def _load_accounts(force_reload: bool = False) -> Dict[str, Dict[str, str]]:
    """
    Load Gorgias accounts from gorgias_accounts.json (cached after first load).
    Falls back to environment variables for single-account setups.
    Call with force_reload=True to invalidate the cache.
    """
    global _accounts_cache

    if _accounts_cache is not None and not force_reload:
        return _accounts_cache

    # Try JSON config first
    if ACCOUNTS_FILE.exists():
        try:
            with open(ACCOUNTS_FILE) as f:
                data = json.load(f)
            accounts = data.get("accounts", data)  # support both {accounts: {}} and {}
            if accounts:
                _accounts_cache = accounts
                return _accounts_cache
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: Could not parse {ACCOUNTS_FILE}: {e}", file=sys.stderr)

    # Fall back to environment variables
    domain = os.getenv("GORGIAS_DOMAIN")
    env_email = os.getenv("GORGIAS_EMAIL")
    api_key = os.getenv("GORGIAS_API_KEY")
    if domain and env_email and api_key:
        name = os.getenv("GORGIAS_ACCOUNT_NAME", domain)
        _accounts_cache = {name: {"domain": domain, "email": env_email, "api_key": api_key}}
        return _accounts_cache

    _accounts_cache = {}
    return _accounts_cache


def _resolve_account(account: Optional[str]) -> Tuple[str, str, str, str]:
    """
    Resolve an optional account name to (account_name, domain, email, api_key).
    - If account is specified, use that account (exact or case-insensitive match).
    - If only one account is configured, use it automatically.
    - If multiple accounts and none specified, raise ToolError listing options.
    """
    accounts = _load_accounts()

    if not accounts:
        raise ToolError(
            "No Gorgias accounts configured. "
            "Create gorgias_accounts.json next to the server file, "
            "or set GORGIAS_DOMAIN, GORGIAS_EMAIL, GORGIAS_API_KEY environment variables."
        )

    if account:
        # Exact match first
        if account in accounts:
            creds = accounts[account]
            return account, creds["domain"], creds["email"], creds["api_key"]
        # Case-insensitive fallback
        for name, creds in accounts.items():
            if name.lower() == account.lower():
                return name, creds["domain"], creds["email"], creds["api_key"]
        available = ", ".join(f"'{k}'" for k in accounts)
        raise ToolError(
            f"Account '{account}' not found. Available accounts: {available}"
        )

    if len(accounts) == 1:
        name = list(accounts.keys())[0]
        creds = accounts[name]
        return name, creds["domain"], creds["email"], creds["api_key"]

    available = ", ".join(f"'{k}'" for k in accounts)
    raise ToolError(
        f"Multiple accounts configured. Specify which one with the `account` parameter. "
        f"Available: {available}"
    )


# ─── HTTP Client ──────────────────────────────────────────────────────────────

_http_client: Optional[httpx.AsyncClient] = None


def _get_client() -> httpx.AsyncClient:
    """Get the shared HTTP client, creating one lazily on first use."""
    global _http_client
    if _http_client is None or _http_client.is_closed:
        _http_client = httpx.AsyncClient(
            timeout=30.0,
            limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
        )
    return _http_client


async def _api_request(
    endpoint: str,
    domain: str,
    email: str,
    api_key: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
) -> Any:
    """Make an authenticated request to the Gorgias REST API."""
    url = f"https://{domain}.gorgias.com/api{endpoint}"
    client = _get_client()

    # Only send Content-Type when there is a body (POST, PUT, PATCH)
    headers: Dict[str, str] = {"Accept": "application/json"}
    if method.upper() in ("POST", "PUT", "PATCH"):
        headers["Content-Type"] = "application/json"

    try:
        resp = await client.request(
            method=method,
            url=url,
            auth=(email, api_key),
            params=params,
            json=json_body,
            headers=headers,
        )
    except httpx.TimeoutException:
        raise ToolError(
            f"Request to {endpoint} timed out after 30 seconds. "
            "Try narrowing your date range or reducing the limit."
        )
    except httpx.RequestError as exc:
        raise ToolError(f"Network error reaching {domain}.gorgias.com: {exc}")

    if resp.status_code == 429:
        retry_after = resp.headers.get("Retry-After", "60")
        raise ToolError(
            f"Rate limited by Gorgias API. Retry after {retry_after} seconds. "
            "The server makes 2 requests/second; reduce concurrent requests if this recurs."
        )
    if resp.status_code == 401:
        raise ToolError(
            "Authentication failed (401). Check your email and API key in gorgias_accounts.json."
        )
    if resp.status_code == 403:
        raise ToolError(
            f"Forbidden (403) — API key lacks permission for {endpoint}. "
            "Check your API key scopes in Gorgias Settings → You → REST API."
        )
    if resp.status_code == 404:
        raise ToolError(
            f"Not found (404): {endpoint}. "
            "Check that the ID exists and the resource path is correct."
        )
    if resp.status_code >= 400:
        try:
            body = resp.json()
            detail = body.get("error", body.get("message", resp.text[:200]))
        except Exception:
            detail = resp.text[:200]
        raise ToolError(f"API error {resp.status_code} on {endpoint}: {detail}")

    return resp.json()


async def _fetch_all_cursor(
    endpoint: str,
    domain: str,
    email: str,
    api_key: str,
    base_params: Optional[Dict[str, Any]] = None,
    limit_per_page: int = 100,
    max_items: int = 1000,
) -> Tuple[List[dict], int]:
    """
    Fetch items using Gorgias cursor-based pagination.
    Gorgias removed offset/page-based pagination in Feb 2024.

    Includes a 0.55s inter-page delay to respect the 2 req/s rate limit.
    Returns (items_list, total_count).
    """
    all_items: List[dict] = []
    # Copy base_params to avoid mutating the caller's dict
    params = {**(base_params or {}), "limit": limit_per_page}
    cursor: Optional[str] = None
    total: int = 0
    page_count = 0

    while len(all_items) < max_items:
        # Respect Gorgias's 2 req/sec rate limit — sleep between pages
        if page_count > 0:
            await asyncio.sleep(0.55)
        page_count += 1

        if cursor:
            params["cursor"] = cursor
        elif "cursor" in params:
            del params["cursor"]

        data = await _api_request(endpoint, domain, email, api_key, params=params)
        batch = data.get("data", [])
        all_items.extend(batch)

        meta = data.get("meta", {})
        total = meta.get("total_count", 0) or len(all_items)
        next_cursor = meta.get("next_cursor")

        if not next_cursor or not batch or len(batch) < limit_per_page:
            break
        cursor = next_cursor

    return all_items, total


# ─── Shared Helpers ───────────────────────────────────────────────────────────

def _render_value(key: str, value: Any, indent: int = 0) -> List[str]:
    """Recursively render a dict/list/scalar value as Markdown lines."""
    prefix = "  " * indent
    result = []
    if isinstance(value, dict):
        result.append(f"{prefix}**{key}:**")
        for k, v in value.items():
            result.extend(_render_value(k, v, indent + 1))
    elif isinstance(value, list):
        result.append(f"{prefix}**{key}:** ({len(value)} items)")
        for item in value[:20]:
            if isinstance(item, dict):
                for k, v in item.items():
                    result.extend(_render_value(k, v, indent + 1))
                result.append("")
            else:
                result.append(f"{prefix}  - {item}")
    else:
        if isinstance(value, float):
            value = f"{value:.2f}"
        result.append(f"{prefix}**{key}:** {value}")
    return result


# ─── Shared Input Base ────────────────────────────────────────────────────────

class BaseInput(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        validate_assignment=True,
    )

    account: Optional[str] = Field(
        default=None,
        description=(
            "Account name from gorgias_accounts.json. "
            "Required when multiple accounts are configured; "
            "omit when only one account is set up. "
            "Use gorgias_list_accounts to see available account names."
        ),
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description=(
            "Output format: 'markdown' (default, human-readable) "
            "or 'json' (structured data for further processing)."
        ),
    )


# ─── Tool: List Accounts ──────────────────────────────────────────────────────

class ListAccountsInput(BaseInput):
    pass


@mcp.tool(
    name="gorgias_list_accounts",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": False,
        "idempotentHint": True,
        "title": "List Configured Gorgias Accounts",
    },
)
async def gorgias_list_accounts(params: ListAccountsInput) -> str:
    """
    List all configured Gorgias accounts from gorgias_accounts.json.
    Use this to discover available account names before calling other tools.
    """
    accounts = _load_accounts()
    if not accounts:
        raise ToolError(
            "No Gorgias accounts configured.\n\n"
            "Create a `gorgias_accounts.json` file next to the server, "
            "or set GORGIAS_DOMAIN / GORGIAS_EMAIL / GORGIAS_API_KEY environment variables."
        )

    if params.response_format == "json":
        return json.dumps({
            "accounts": [
                {"name": name, "domain": f"{creds.get('domain', '?')}.gorgias.com"}
                for name, creds in accounts.items()
            ]
        }, indent=2)

    lines = ["## Configured Gorgias Accounts\n"]
    for name, creds in accounts.items():
        lines.append(f"- **{name}** → `{creds.get('domain', '?')}.gorgias.com`")
    return "\n".join(lines)


# ─── Tool: Reload Accounts ────────────────────────────────────────────────────

class ReloadAccountsInput(BaseInput):
    pass


@mcp.tool(
    name="gorgias_reload_accounts",
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "openWorldHint": False,
        "idempotentHint": True,
        "title": "Reload Gorgias Account Credentials",
    },
)
async def gorgias_reload_accounts(params: ReloadAccountsInput) -> str:
    """
    Reload account credentials from gorgias_accounts.json without restarting the server.
    Use this after adding new accounts or updating API keys.
    """
    accounts = _load_accounts(force_reload=True)
    count = len(accounts)
    if count == 0:
        raise ToolError(
            "No accounts found after reload. "
            "Check gorgias_accounts.json or set environment variables."
        )
    names = ", ".join(f"'{k}'" for k in accounts)
    return f"✓ Reloaded {count} account(s): {names}"


# ─── Tool: Account Info ───────────────────────────────────────────────────────

class AccountInfoInput(BaseInput):
    pass


@mcp.tool(
    name="gorgias_account_info",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "Get Gorgias Account Info",
    },
)
async def gorgias_account_info(params: AccountInfoInput) -> str:
    """
    Get basic info about the authenticated Gorgias account:
    the current user, domain, and role. Use this to verify connectivity.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    me = await _api_request("/users/0", domain, auth_email, api_key)

    role = (me.get("role") or {}).get("name", "?")

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "domain": f"{domain}.gorgias.com",
            "user_id": me.get("id"),
            "name": f"{me.get('firstname', '')} {me.get('lastname', '')}".strip(),
            "email": me.get("email"),
            "role": role,
        }, indent=2)

    lines = [
        f"## [{acct_name}] Gorgias Account Info\n",
        f"**Domain:** {domain}.gorgias.com",
        f"**Authenticated as:** {me.get('firstname', '')} {me.get('lastname', '')} "
        f"<{me.get('email', '?')}>",
        f"**Role:** {role}",
        f"**Status:** ✓ Connected successfully",
    ]
    return "\n".join(lines)


# ─── Tool: List Tickets ───────────────────────────────────────────────────────

class ListTicketsInput(BaseInput):
    status: Optional[str] = Field(
        default=None,
        description="Filter by status: 'open', 'closed', 'spam', or 'snoozed'.",
    )
    channel: Optional[str] = Field(
        default=None,
        description=(
            "Filter by channel: email, chat, phone, instagram, facebook, "
            "twitter, whatsapp, sms, helpcenter, api, etc."
        ),
    )
    assignee_user_id: Optional[int] = Field(
        default=None,
        description="Filter by assigned agent user ID. Use 0 for the authenticated user.",
    )
    assignee_team_id: Optional[int] = Field(
        default=None, description="Filter by assigned team ID."
    )
    customer_id: Optional[int] = Field(
        default=None, description="Filter by customer ID."
    )
    tags: Optional[List[str]] = Field(
        default=None, description="Filter by tag names (e.g. ['billing', 'refund'])."
    )
    created_after: Optional[str] = Field(
        default=None,
        description=(
            "Return tickets created on or after this ISO 8601 datetime. "
            "Example: '2025-01-01T00:00:00Z'"
        ),
    )
    created_before: Optional[str] = Field(
        default=None,
        description="Return tickets created on or before this ISO 8601 datetime.",
    )
    updated_after: Optional[str] = Field(
        default=None,
        description="Return tickets updated on or after this ISO 8601 datetime.",
    )
    order_by: Optional[str] = Field(
        default="id",
        description=(
            "Sort field: 'id' (default), 'created_datetime', "
            "'updated_datetime', or 'closed_datetime'."
        ),
    )
    order_dir: Optional[str] = Field(
        default="desc",
        description="Sort direction: 'desc' (default, newest first) or 'asc'.",
    )
    limit: int = Field(
        default=50, ge=1, le=500,
        description="Maximum number of tickets to return (1–500, default 50).",
    )


@mcp.tool(
    name="gorgias_list_tickets",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Gorgias Tickets",
    },
)
async def gorgias_list_tickets(params: ListTicketsInput) -> str:
    """
    List tickets from a Gorgias account with optional filters.
    Supports filtering by status, channel, assignee, customer, tags, and date range.
    Defaults to newest tickets first (order_by=id, order_dir=desc).
    Returns key fields: ID, subject, status, channel, customer, assignee, tags, dates.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    query_params: Dict[str, Any] = {}
    if params.status:
        query_params["status"] = params.status
    if params.channel:
        query_params["channel"] = params.channel
    if params.assignee_user_id is not None:
        query_params["assignee_user_id"] = params.assignee_user_id
    if params.assignee_team_id is not None:
        query_params["assignee_team_id"] = params.assignee_team_id
    if params.customer_id is not None:
        query_params["customer_id"] = params.customer_id
    if params.tags:
        query_params["tags"] = ",".join(params.tags)
    if params.created_after:
        query_params["created_datetime[gte]"] = params.created_after
    if params.created_before:
        query_params["created_datetime[lte]"] = params.created_before
    if params.updated_after:
        query_params["updated_datetime[gte]"] = params.updated_after
    if params.order_by:
        query_params["order_by"] = params.order_by
    if params.order_dir:
        query_params["order_dir"] = params.order_dir

    tickets, total = await _fetch_all_cursor(
        "/tickets", domain, auth_email, api_key,
        base_params=query_params,
        max_items=params.limit,
    )

    has_more = len(tickets) < total

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "returned": len(tickets),
            "has_more": has_more,
            "tickets": tickets,
        }, indent=2)

    if not tickets:
        return f"[{acct_name}] No tickets found matching the filters."

    lines = [f"## [{acct_name}] Tickets ({len(tickets)} of {total} total)\n"]
    if has_more:
        lines.append(f"*Note: {total - len(tickets)} more tickets match — narrow filters or increase limit.*\n")

    for t in tickets:
        customer = t.get("customer") or {}
        assignee = t.get("assignee_user") or {}
        tags = [tag.get("name", "") for tag in (t.get("tags") or [])]
        tag_str = ", ".join(tags) if tags else "—"
        csat = t.get("satisfaction_survey") or {}
        csat_score = csat.get("score")
        csat_str = f" | CSAT: {csat_score}/5" if csat_score else ""

        lines.append(
            f"**#{t['id']}** — {t.get('subject', '(no subject)')}\n"
            f"  Status: {t.get('status')} | Channel: {t.get('channel')}{csat_str}\n"
            f"  Customer: {customer.get('firstname', '')} {customer.get('lastname', '')} "
            f"<{customer.get('email', '?')}>\n"
            f"  Assignee: {assignee.get('firstname', '?')} {assignee.get('lastname', '')}\n"
            f"  Tags: {tag_str}\n"
            f"  Created: {t.get('created_datetime', '?')} | "
            f"Updated: {t.get('updated_datetime', '?')}\n"
        )
    return "\n".join(lines)


# ─── Tool: Get Ticket ─────────────────────────────────────────────────────────

class GetTicketInput(BaseInput):
    ticket_id: int = Field(description="The Gorgias ticket ID.")


@mcp.tool(
    name="gorgias_get_ticket",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "Get Gorgias Ticket by ID",
    },
)
async def gorgias_get_ticket(params: GetTicketInput) -> str:
    """
    Get a single ticket by ID, including all fields: subject, status, channel,
    customer, assignee, tags, CSAT score, message count, and timestamps.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    t = await _api_request(f"/tickets/{params.ticket_id}", domain, auth_email, api_key)

    if params.response_format == "json":
        return json.dumps({"account": acct_name, "ticket": t}, indent=2)

    customer = t.get("customer") or {}
    assignee = t.get("assignee_user") or {}
    team = t.get("assignee_team") or {}
    tags = [tag.get("name", "") for tag in (t.get("tags") or [])]
    csat = t.get("satisfaction_survey") or {}

    lines = [
        f"## [{acct_name}] Ticket #{t['id']}: {t.get('subject', '(no subject)')}\n",
        f"**Status:** {t.get('status')} | **Channel:** {t.get('channel')}",
        f"**Messages:** {t.get('messages_count', 0)} | "
        f"**Unread:** {'Yes' if t.get('is_unread') else 'No'}",
        f"\n**Customer:** {customer.get('firstname', '')} {customer.get('lastname', '')} "
        f"<{customer.get('email', '?')}>",
        f"**Assignee:** {assignee.get('firstname', '?')} {assignee.get('lastname', '')} "
        + (f"(Team: {team.get('name', '')})" if team else ""),
        f"**Tags:** {', '.join(tags) if tags else 'none'}",
        f"\n**Created:** {t.get('created_datetime', '?')}",
        f"**Updated:** {t.get('updated_datetime', '?')}",
        f"**Closed:** {t.get('closed_datetime') or 'Not closed'}",
    ]
    if csat:
        score = csat.get("score")
        comment = csat.get("body_text", "")
        lines.append(f"\n**CSAT:** {score}/5" + (f' — "{comment}"' if comment else ""))

    excerpt = t.get("excerpt")
    if excerpt:
        lines.append(f"\n**Last message preview:** {excerpt[:300]}")

    return "\n".join(lines)


# ─── Tool: List Ticket Messages ───────────────────────────────────────────────

class ListMessagesInput(BaseInput):
    ticket_id: int = Field(description="The Gorgias ticket ID to fetch messages for.")
    limit: int = Field(
        default=50, ge=1, le=300,
        description="Maximum number of messages to return (1–300, default 50).",
    )


@mcp.tool(
    name="gorgias_list_ticket_messages",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Ticket Messages",
    },
)
async def gorgias_list_ticket_messages(params: ListMessagesInput) -> str:
    """
    Get all messages (conversation thread) for a specific ticket.
    Returns sender, direction (agent/customer), visibility, timestamp, and message body.
    Uses cursor pagination to handle long threads (>100 messages).
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    messages, total = await _fetch_all_cursor(
        f"/tickets/{params.ticket_id}/messages",
        domain, auth_email, api_key,
        max_items=params.limit,
    )

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "ticket_id": params.ticket_id,
            "total": total,
            "returned": len(messages),
            "has_more": len(messages) < total,
            "messages": messages,
        }, indent=2)

    if not messages:
        return f"[{acct_name}] No messages found for ticket #{params.ticket_id}."

    lines = [
        f"## [{acct_name}] Ticket #{params.ticket_id} — Messages "
        f"({len(messages)} of {total})\n"
    ]
    for msg in messages:
        sender = msg.get("sender") or {}
        direction = "Agent" if msg.get("from_agent") else "Customer"
        visibility = "Public" if msg.get("public") else "Internal note"
        name = f"{sender.get('firstname', '')} {sender.get('lastname', '')}".strip()
        body = msg.get("stripped_text") or msg.get("body_text") or "(no text content)"
        body_preview = body[:500] + ("..." if len(body) > 500 else "")

        lines.append(
            f"---\n**{direction}** — {name or sender.get('email', 'Unknown')} "
            f"({visibility}) — {msg.get('created_datetime', '?')}\n\n{body_preview}\n"
        )
    return "\n".join(lines)


# ─── Tool: Search Tickets ─────────────────────────────────────────────────────

class SearchTicketsInput(BaseInput):
    query: str = Field(
        description="Free-text search query across ticket subjects and messages."
    )
    status: Optional[str] = Field(
        default=None,
        description="Optionally narrow to a specific status: open, closed, spam, snoozed.",
    )
    limit: int = Field(
        default=20, ge=1, le=200,
        description="Max results to return (1–200, default 20).",
    )


@mcp.tool(
    name="gorgias_search_tickets",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "Search Gorgias Tickets",
    },
)
async def gorgias_search_tickets(params: SearchTicketsInput) -> str:
    """
    Full-text search across Gorgias tickets by subject and message content.
    Returns matching tickets with basic metadata. Uses cursor pagination for complete results.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    query_params: Dict[str, Any] = {"q": params.query}
    if params.status:
        query_params["status"] = params.status

    tickets, total = await _fetch_all_cursor(
        "/tickets", domain, auth_email, api_key,
        base_params=query_params,
        max_items=params.limit,
    )

    has_more = len(tickets) < total

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "query": params.query,
            "total": total,
            "returned": len(tickets),
            "has_more": has_more,
            "tickets": tickets,
        }, indent=2)

    if not tickets:
        return f"[{acct_name}] No tickets found matching '{params.query}'."

    lines = [f"## [{acct_name}] Search: '{params.query}' ({len(tickets)} of {total})\n"]
    if has_more:
        lines.append(f"*{total - len(tickets)} more results — increase limit to see more.*\n")
    for t in tickets:
        customer = t.get("customer") or {}
        lines.append(
            f"**#{t['id']}** — {t.get('subject', '(no subject)')} "
            f"[{t.get('status')}] — {customer.get('email', '?')} — {t.get('created_datetime', '?')}"
        )
    return "\n".join(lines)


# ─── Tool: List Satisfaction Surveys ─────────────────────────────────────────

class ListSurveysInput(BaseInput):
    created_after: Optional[str] = Field(
        default=None,
        description=(
            "Return surveys submitted on or after this ISO 8601 date. "
            "Example: '2025-01-01'"
        ),
    )
    created_before: Optional[str] = Field(
        default=None,
        description="Return surveys submitted on or before this ISO 8601 date.",
    )
    limit: int = Field(
        default=100, ge=1, le=1000,
        description="Maximum number of surveys to return (default 100).",
    )

    @field_validator("created_after", "created_before", mode="before")
    @classmethod
    def validate_date_format(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not (len(v) >= 10 and v[4] == "-" and v[7] == "-"):
            raise ValueError(
                f"Invalid date format '{v}'. Use ISO 8601, e.g. '2025-01-01' or '2025-01-01T00:00:00Z'."
            )
        return v


@mcp.tool(
    name="gorgias_list_satisfaction_surveys",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List CSAT Satisfaction Surveys",
    },
)
async def gorgias_list_satisfaction_surveys(params: ListSurveysInput) -> str:
    """
    List CSAT (customer satisfaction) survey responses.
    Each survey has a score (1–5) and optional text comment.
    Scores: 5=very satisfied, 4=satisfied, 3=neutral, 2=dissatisfied, 1=very dissatisfied.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    query_params: Dict[str, Any] = {}
    if params.created_after:
        query_params["created_datetime[gte]"] = params.created_after
    if params.created_before:
        query_params["created_datetime[lte]"] = params.created_before

    surveys, total = await _fetch_all_cursor(
        "/satisfaction-surveys", domain, auth_email, api_key,
        base_params=query_params,
        max_items=params.limit,
    )

    has_more = len(surveys) < total

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "returned": len(surveys),
            "has_more": has_more,
            "surveys": surveys,
        }, indent=2)

    if not surveys:
        return f"[{acct_name}] No satisfaction surveys found for the specified period."

    lines = [f"## [{acct_name}] Satisfaction Surveys ({len(surveys)} of {total})\n"]
    score_label = {5: "Very satisfied", 4: "Satisfied", 3: "Neutral",
                   2: "Dissatisfied", 1: "Very dissatisfied"}
    for s in surveys:
        customer = s.get("customer") or {}
        score = s.get("score")
        label = score_label.get(score, "?")
        comment = s.get("body_text", "")
        lines.append(
            f"**Ticket #{s.get('ticket_id')}** — Score: {score}/5 ({label}) — "
            f"{customer.get('email', '?')} — {s.get('created_datetime', '?')}"
            + (f'\n  Comment: "{comment}"' if comment else "")
        )
    return "\n".join(lines)


# ─── Tool: CSAT Stats ─────────────────────────────────────────────────────────

class CsatStatsInput(BaseInput):
    created_after: Optional[str] = Field(
        default=None, description="Start date (ISO 8601). Example: '2025-01-01'"
    )
    created_before: Optional[str] = Field(
        default=None, description="End date (ISO 8601). Example: '2025-03-31'"
    )

    @field_validator("created_after", "created_before", mode="before")
    @classmethod
    def validate_date_format(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not (len(v) >= 10 and v[4] == "-" and v[7] == "-"):
            raise ValueError(
                f"Invalid date format '{v}'. Use ISO 8601, e.g. '2025-01-01'."
            )
        return v


@mcp.tool(
    name="gorgias_get_csat_stats",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "Get CSAT Summary Statistics",
    },
)
async def gorgias_get_csat_stats(params: CsatStatsInput) -> str:
    """
    Compute CSAT summary statistics for a given period.
    Returns: total responses, average score, positive rate (4–5), negative rate (1–2),
    score distribution, and any written comments.
    Date filters are passed to the Gorgias API for accurate server-side filtering.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    query_params: Dict[str, Any] = {}
    if params.created_after:
        query_params["created_datetime[gte]"] = params.created_after
    if params.created_before:
        query_params["created_datetime[lte]"] = params.created_before

    surveys, _ = await _fetch_all_cursor(
        "/satisfaction-surveys", domain, auth_email, api_key,
        base_params=query_params,
        max_items=500,
    )

    scored = [s for s in surveys if s.get("score") is not None]
    if not scored:
        return f"[{acct_name}] No scored CSAT surveys found for the specified period."

    scores = [s["score"] for s in scored]
    avg = sum(scores) / len(scores)
    dist: Dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for sc in scores:
        dist[sc] = dist.get(sc, 0) + 1

    positive = dist[4] + dist[5]
    negative = dist[1] + dist[2]
    neutral = dist[3]
    positive_rate = positive / len(scored) * 100
    negative_rate = negative / len(scored) * 100

    period_str = ""
    if params.created_after or params.created_before:
        period_str = f" ({params.created_after or '...'} to {params.created_before or '...'})"

    comments = [s for s in scored if s.get("body_text", "").strip()]

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "period": period_str.strip(" ()"),
            "total_responses": len(scored),
            "average_score": round(avg, 2),
            "positive_rate_pct": round(positive_rate, 1),
            "negative_rate_pct": round(negative_rate, 1),
            "distribution": dist,
            "comments_count": len(comments),
        }, indent=2)

    lines = [
        f"## [{acct_name}] CSAT Summary{period_str}\n",
        f"**Total Responses:** {len(scored)}",
        f"**Average Score:** {avg:.2f}/5",
        f"**Positive Rate (4–5):** {positive_rate:.1f}% ({positive} responses)",
        f"**Negative Rate (1–2):** {negative_rate:.1f}% ({negative} responses)",
        f"**Neutral (3):** {neutral} responses",
        f"\n**Score Distribution:**",
        f"  5 (Very satisfied)    — {dist[5]} ({dist[5]/len(scored)*100:.1f}%)",
        f"  4 (Satisfied)         — {dist[4]} ({dist[4]/len(scored)*100:.1f}%)",
        f"  3 (Neutral)           — {dist[3]} ({dist[3]/len(scored)*100:.1f}%)",
        f"  2 (Dissatisfied)      — {dist[2]} ({dist[2]/len(scored)*100:.1f}%)",
        f"  1 (Very dissatisfied) — {dist[1]} ({dist[1]/len(scored)*100:.1f}%)",
    ]

    if comments:
        lines.append(f"\n**Written Comments ({len(comments)}):**")
        for c in comments[:10]:
            customer = c.get("customer") or {}
            lines.append(
                f'  - Score {c["score"]}/5 — {customer.get("email", "?")}: '
                f'"{c["body_text"][:200]}"'
            )
        if len(comments) > 10:
            lines.append(f"  ... and {len(comments) - 10} more comments")

    return "\n".join(lines)


# ─── Tool: Get Stats (legacy pre-computed analytics) ──────────────────────────

class GetStatsInput(BaseInput):
    stat_name: str = Field(
        description=(
            "Name of the pre-computed stat to retrieve. Common values:\n"
            "  - 'overview' — overall support summary\n"
            "  - 'first-response-time' — average/median FRT by period\n"
            "  - 'resolution-time' — average time to close tickets\n"
            "  - 'messages-statistics' — message volume breakdown\n"
            "  - 'created-tickets' — ticket creation volume\n"
            "  - 'replied-tickets' — tickets with agent reply\n"
            "  - 'closed-tickets' — closed ticket count\n"
            "  - 'one-touch-tickets' — tickets closed after 1 response\n"
            "  - 'agent-overview' — per-agent performance summary\n"
            "  - 'satisfaction-surveys' — CSAT score distribution\n"
            "  - 'support-performance' — comprehensive support KPIs\n"
            "Check Gorgias Statistics docs for the full list."
        )
    )
    datetime_start: str = Field(
        description="Start of the period in ISO 8601 format. Example: '2025-01-01T00:00:00'"
    )
    datetime_end: str = Field(
        description="End of the period in ISO 8601 format. Example: '2025-03-31T23:59:59'"
    )
    filters: Optional[Dict[str, Any]] = Field(
        default=None,
        description=(
            "Optional filters dict to narrow the stats. "
            "Examples: {'channel': 'email'}, {'assignee_user': {'id': 42}}, "
            "{'tags': ['billing', 'refund']}"
        ),
    )


@mcp.tool(
    name="gorgias_get_stats",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "Get Pre-Computed Stats (Legacy API)",
    },
)
async def gorgias_get_stats(params: GetStatsInput) -> str:
    """
    Query Gorgias's pre-computed statistics engine via POST /api/stats/{name}.
    Much faster and more accurate than aggregating raw ticket data.
    Use for: response time, resolution time, ticket volume, agent performance, CSAT.

    NOTE: This legacy API (POST /api/stats/{name}) is being sunset December 31, 2026.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    body: Dict[str, Any] = {
        "start_datetime": params.datetime_start,
        "end_datetime": params.datetime_end,
    }
    if params.filters:
        body["filters"] = params.filters

    data = await _api_request(
        f"/stats/{params.stat_name}",
        domain, auth_email, api_key,
        method="POST",
        json_body=body,
    )

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "stat": params.stat_name,
            "period": f"{params.datetime_start} to {params.datetime_end}",
            "data": data,
        }, indent=2)

    lines = [
        f"## [{acct_name}] Stats: {params.stat_name}\n",
        f"**Period:** {params.datetime_start} to {params.datetime_end}\n",
    ]

    if isinstance(data, dict):
        for k, v in data.items():
            lines.extend(_render_value(k, v))
    else:
        lines.append(str(data))

    return "\n".join(lines)


# ─── Tool: Ticket Stats (volume analytics) ────────────────────────────────────

class TicketStatsInput(BaseInput):
    created_after: Optional[str] = Field(
        default=None, description="Start date (ISO 8601). Example: '2025-01-01'"
    )
    created_before: Optional[str] = Field(
        default=None, description="End date (ISO 8601). Example: '2025-03-31'"
    )
    status: Optional[str] = Field(
        default=None,
        description="Filter by status: open, closed, spam, snoozed. Omit for all.",
    )

    @field_validator("created_after", "created_before", mode="before")
    @classmethod
    def validate_date_format(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not (len(v) >= 10 and v[4] == "-" and v[7] == "-"):
            raise ValueError(f"Invalid date format '{v}'. Use ISO 8601, e.g. '2025-01-01'.")
        return v


@mcp.tool(
    name="gorgias_ticket_stats",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "Get Ticket Volume Statistics",
    },
)
async def gorgias_ticket_stats(params: TicketStatsInput) -> str:
    """
    Compute ticket volume statistics: totals by status, channel, and tag.
    Samples up to 500 tickets for performance. For official KPIs (response time,
    resolution time), use gorgias_get_stats with stat_name='created-tickets'.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    query_params: Dict[str, Any] = {"order_by": "id", "order_dir": "desc"}
    if params.created_after:
        query_params["created_datetime[gte]"] = params.created_after
    if params.created_before:
        query_params["created_datetime[lte]"] = params.created_before
    if params.status:
        query_params["status"] = params.status

    tickets, total = await _fetch_all_cursor(
        "/tickets", domain, auth_email, api_key,
        base_params=query_params,
        max_items=500,
    )

    if not tickets:
        return f"[{acct_name}] No tickets found for the specified filters."

    by_status: Dict[str, int] = {}
    by_channel: Dict[str, int] = {}
    by_tag: Dict[str, int] = {}
    has_csat = 0

    for t in tickets:
        s = t.get("status", "unknown")
        by_status[s] = by_status.get(s, 0) + 1
        ch = t.get("channel", "unknown")
        by_channel[ch] = by_channel.get(ch, 0) + 1
        for tag in (t.get("tags") or []):
            tn = tag.get("name", "")
            by_tag[tn] = by_tag.get(tn, 0) + 1
        if t.get("satisfaction_survey") and t["satisfaction_survey"].get("score"):
            has_csat += 1

    period_str = ""
    if params.created_after or params.created_before:
        period_str = f" ({params.created_after or '...'} to {params.created_before or '...'})"

    sampled_note = f" (sampled from {len(tickets)} most recent)" if len(tickets) < total else ""

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "sampled": len(tickets),
            "by_status": by_status,
            "by_channel": by_channel,
            "by_tag": dict(sorted(by_tag.items(), key=lambda x: -x[1])[:20]),
            "with_csat": has_csat,
        }, indent=2)

    lines = [
        f"## [{acct_name}] Ticket Volume{period_str}\n",
        f"**Total tickets (API count):** {total}{sampled_note}\n",
        "**By Status:**",
    ]
    for st, count in sorted(by_status.items(), key=lambda x: -x[1]):
        lines.append(f"  - {st}: {count}")
    lines.append("\n**By Channel:**")
    for ch, count in sorted(by_channel.items(), key=lambda x: -x[1]):
        lines.append(f"  - {ch}: {count}")
    if by_tag:
        lines.append("\n**Top Tags:**")
        for tag, count in sorted(by_tag.items(), key=lambda x: -x[1])[:15]:
            lines.append(f"  - {tag}: {count}")
    lines.append(f"\n**With CSAT score:** {has_csat}")

    return "\n".join(lines)


# ─── Tool: Agent Performance ──────────────────────────────────────────────────

class AgentPerformanceInput(BaseInput):
    created_after: Optional[str] = Field(
        default=None, description="Start date (ISO 8601). Example: '2025-01-01'"
    )
    created_before: Optional[str] = Field(
        default=None, description="End date (ISO 8601). Example: '2025-03-31'"
    )

    @field_validator("created_after", "created_before", mode="before")
    @classmethod
    def validate_date_format(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not (len(v) >= 10 and v[4] == "-" and v[7] == "-"):
            raise ValueError(f"Invalid date format '{v}'. Use ISO 8601, e.g. '2025-01-01'.")
        return v


@mcp.tool(
    name="gorgias_agent_performance",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "Get Agent Performance Summary",
    },
)
async def gorgias_agent_performance(params: AgentPerformanceInput) -> str:
    """
    Compute per-agent ticket counts and CSAT scores from raw ticket data (up to 500 tickets).
    For official response/resolution time metrics, use gorgias_get_stats with
    stat_name='agent-overview'.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    query_params: Dict[str, Any] = {"order_by": "id", "order_dir": "desc"}
    if params.created_after:
        query_params["created_datetime[gte]"] = params.created_after
    if params.created_before:
        query_params["created_datetime[lte]"] = params.created_before

    tickets, total = await _fetch_all_cursor(
        "/tickets", domain, auth_email, api_key,
        base_params=query_params,
        max_items=500,
    )

    agent_data: Dict[int, Dict] = {}
    for t in tickets:
        assignee = t.get("assignee_user")
        if not assignee:
            continue
        aid = assignee.get("id")
        if aid is None:
            continue
        if aid not in agent_data:
            agent_data[aid] = {
                "name": f"{assignee.get('firstname', '')} {assignee.get('lastname', '')}".strip(),
                "email": assignee.get("email", ""),
                "total": 0, "closed": 0, "open": 0,
                "csat_scores": [],
            }
        agent_data[aid]["total"] += 1
        status = t.get("status", "")
        if status == "closed":
            agent_data[aid]["closed"] += 1
        elif status == "open":
            agent_data[aid]["open"] += 1

        csat = t.get("satisfaction_survey") or {}
        score = csat.get("score")
        if score is not None:
            agent_data[aid]["csat_scores"].append(score)

    if not agent_data:
        return f"[{acct_name}] No assigned tickets found for the specified period."

    period_str = ""
    if params.created_after or params.created_before:
        period_str = f" ({params.created_after or '...'} to {params.created_before or '...'})"

    sampled_note = f" (from {len(tickets)} of {total} most recent tickets)" if len(tickets) < total else ""
    sorted_agents = sorted(agent_data.values(), key=lambda x: -x["total"])

    if params.response_format == "json":
        result = []
        for ag in sorted_agents:
            s = ag["csat_scores"]
            result.append({
                "name": ag["name"],
                "email": ag["email"],
                "total": ag["total"],
                "closed": ag["closed"],
                "open": ag["open"],
                "csat_avg": round(sum(s) / len(s), 2) if s else None,
                "csat_responses": len(s),
            })
        return json.dumps({
            "account": acct_name,
            "period": period_str.strip(" ()"),
            "sample_note": sampled_note.strip(),
            "agents": result,
        }, indent=2)

    lines = [f"## [{acct_name}] Agent Performance{period_str}{sampled_note}\n"]
    for ag in sorted_agents:
        s = ag["csat_scores"]
        avg_csat = (
            f"{sum(s)/len(s):.2f}/5 ({len(s)} responses)"
            if s else "No CSAT"
        )
        lines.append(
            f"**{ag['name']}** ({ag['email']})\n"
            f"  Tickets: {ag['total']} total | {ag['closed']} closed | {ag['open']} open\n"
            f"  CSAT: {avg_csat}\n"
        )
    return "\n".join(lines)


# ─── Tool: List Users ─────────────────────────────────────────────────────────

class ListUsersInput(BaseInput):
    limit: int = Field(default=50, ge=1, le=200, description="Max users to return.")


@mcp.tool(
    name="gorgias_list_users",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Gorgias Agents / Users",
    },
)
async def gorgias_list_users(params: ListUsersInput) -> str:
    """
    List all agents/users in the Gorgias account.
    Returns ID, name, email, role, and active status.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    users, total = await _fetch_all_cursor(
        "/users", domain, auth_email, api_key, max_items=params.limit
    )

    has_more = len(users) < total

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "returned": len(users),
            "has_more": has_more,
            "users": users,
        }, indent=2)

    if not users:
        return f"[{acct_name}] No users found."

    lines = [f"## [{acct_name}] Agents & Users ({len(users)} of {total})\n"]
    for u in users:
        role = (u.get("role") or {}).get("name", "?")
        status = "Active" if u.get("active") else "Inactive"
        lines.append(
            f"**#{u['id']}** — {u.get('firstname', '')} {u.get('lastname', '')} "
            f"<{u.get('email', '?')}> | Role: {role} | {status}"
        )
    return "\n".join(lines)


# ─── Tool: Get User ───────────────────────────────────────────────────────────

class GetUserInput(BaseInput):
    user_id: int = Field(
        description="The Gorgias user ID. Use 0 to get the currently authenticated user."
    )


@mcp.tool(
    name="gorgias_get_user",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "Get Gorgias User by ID",
    },
)
async def gorgias_get_user(params: GetUserInput) -> str:
    """
    Get a single agent/user by ID. Use user_id=0 for the authenticated user.
    Returns full profile: name, email, role, timezone, bio, and creation date.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    u = await _api_request(f"/users/{params.user_id}", domain, auth_email, api_key)

    if params.response_format == "json":
        return json.dumps({"account": acct_name, "user": u}, indent=2)

    role = (u.get("role") or {}).get("name", "?")
    lines = [
        f"## [{acct_name}] User #{u['id']}\n",
        f"**Name:** {u.get('firstname', '')} {u.get('lastname', '')}",
        f"**Email:** {u.get('email', '?')}",
        f"**Role:** {role}",
        f"**Active:** {'Yes' if u.get('active') else 'No'}",
        f"**Timezone:** {u.get('timezone', '?')}",
        f"**Bio:** {u.get('bio') or 'None'}",
        f"**Created:** {u.get('created_datetime', '?')}",
    ]
    return "\n".join(lines)


# ─── Tool: List Tags ──────────────────────────────────────────────────────────

class ListTagsInput(BaseInput):
    limit: int = Field(
        default=500, ge=1, le=1000,
        description="Max tags to return (uses cursor pagination for complete results).",
    )


@mcp.tool(
    name="gorgias_list_tags",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Gorgias Tags",
    },
)
async def gorgias_list_tags(params: ListTagsInput) -> str:
    """
    List all tags in the Gorgias account (used to categorize and route tickets).
    Returns tag IDs and names. Uses cursor pagination for accounts with many tags.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    tags, total = await _fetch_all_cursor(
        "/tags", domain, auth_email, api_key, max_items=params.limit
    )

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "returned": len(tags),
            "has_more": len(tags) < total,
            "tags": tags,
        }, indent=2)

    if not tags:
        return f"[{acct_name}] No tags found."

    lines = [f"## [{acct_name}] Tags ({len(tags)} of {total})\n"]
    lines.extend(f"- **#{t['id']}** {t.get('name', '?')}" for t in tags)
    return "\n".join(lines)


# ─── Tool: List Teams ─────────────────────────────────────────────────────────

class ListTeamsInput(BaseInput):
    limit: int = Field(default=100, ge=1, le=500, description="Max teams to return.")


@mcp.tool(
    name="gorgias_list_teams",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Gorgias Teams",
    },
)
async def gorgias_list_teams(params: ListTeamsInput) -> str:
    """
    List all teams in the Gorgias account.
    Returns team IDs, names, and descriptions.
    Use team IDs with gorgias_list_tickets's assignee_team_id filter.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    teams, total = await _fetch_all_cursor(
        "/teams", domain, auth_email, api_key, max_items=params.limit
    )

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "returned": len(teams),
            "teams": teams,
        }, indent=2)

    if not teams:
        return f"[{acct_name}] No teams found."

    lines = [f"## [{acct_name}] Teams ({len(teams)} of {total})\n"]
    for t in teams:
        desc = t.get("description", "")
        desc_str = f" — {desc}" if desc else ""
        lines.append(f"- **#{t.get('id')}** {t.get('name', '?')}{desc_str}")
    return "\n".join(lines)


# ─── Tool: List Macros ────────────────────────────────────────────────────────

class ListMacrosInput(BaseInput):
    limit: int = Field(default=100, ge=1, le=500, description="Max macros to return.")


@mcp.tool(
    name="gorgias_list_macros",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Gorgias Macros",
    },
)
async def gorgias_list_macros(params: ListMacrosInput) -> str:
    """
    List all macros (pre-defined response templates) in the Gorgias account.
    Returns macro IDs, names, and action descriptions.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    macros, total = await _fetch_all_cursor(
        "/macros", domain, auth_email, api_key, max_items=params.limit
    )

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "returned": len(macros),
            "has_more": len(macros) < total,
            "macros": macros,
        }, indent=2)

    if not macros:
        return f"[{acct_name}] No macros found."

    lines = [f"## [{acct_name}] Macros ({len(macros)} of {total})\n"]
    for m in macros:
        actions = m.get("actions") or []
        action_types = ", ".join({a.get("type", "?") for a in actions}) or "?"
        lines.append(
            f"**#{m.get('id')}** — {m.get('name', '?')} "
            f"[{action_types}]"
        )
    return "\n".join(lines)


# ─── Tool: List Custom Fields ─────────────────────────────────────────────────

class ListCustomFieldsInput(BaseInput):
    limit: int = Field(default=200, ge=1, le=500, description="Max fields to return.")


@mcp.tool(
    name="gorgias_list_custom_fields",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Gorgias Custom Fields",
    },
)
async def gorgias_list_custom_fields(params: ListCustomFieldsInput) -> str:
    """
    List all custom ticket fields defined in the Gorgias account.
    Returns field IDs, names, types, and required status.
    Custom fields extend tickets with account-specific data like order IDs.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    fields, total = await _fetch_all_cursor(
        "/custom-fields", domain, auth_email, api_key, max_items=params.limit
    )

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "returned": len(fields),
            "fields": fields,
        }, indent=2)

    if not fields:
        return f"[{acct_name}] No custom fields found."

    lines = [f"## [{acct_name}] Custom Fields ({len(fields)} of {total})\n"]
    for f in fields:
        required_str = " (required)" if f.get("required") else ""
        lines.append(
            f"**#{f.get('id')}** — {f.get('name', '?')} "
            f"[{f.get('field_type', '?')}]{required_str}"
        )
    return "\n".join(lines)


# ─── Tool: List Customers ─────────────────────────────────────────────────────

class ListCustomersInput(BaseInput):
    email: Optional[str] = Field(
        default=None, description="Filter by exact customer email address."
    )
    query: Optional[str] = Field(
        default=None, description="Free-text search across customer name and email."
    )
    limit: int = Field(default=50, ge=1, le=500, description="Max customers to return.")


@mcp.tool(
    name="gorgias_list_customers",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List or Search Gorgias Customers",
    },
)
async def gorgias_list_customers(params: ListCustomersInput) -> str:
    """
    List or search customers in the Gorgias account.
    Returns customer ID, name, email, channels, and creation date.
    Uses cursor pagination for complete results.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    base_params: Dict[str, Any] = {}
    if params.email:
        base_params["email"] = params.email
    if params.query:
        base_params["q"] = params.query

    customers, total = await _fetch_all_cursor(
        "/customers", domain, auth_email, api_key,
        base_params=base_params,
        max_items=params.limit,
    )

    has_more = len(customers) < total

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": total,
            "returned": len(customers),
            "has_more": has_more,
            "customers": customers,
        }, indent=2)

    if not customers:
        return f"[{acct_name}] No customers found."

    lines = [f"## [{acct_name}] Customers ({len(customers)} of {total})\n"]
    for c in customers:
        channels = [ch.get("address", "") for ch in (c.get("channels") or [])]
        lines.append(
            f"**#{c['id']}** — {c.get('firstname', '')} {c.get('lastname', '')} "
            f"<{c.get('email', '?')}> | Channels: {', '.join(channels) or 'none'}"
        )
    return "\n".join(lines)


# ─── Tool: List Customer Tickets ──────────────────────────────────────────────

class CustomerTicketsInput(BaseInput):
    customer_id: Optional[int] = Field(
        default=None,
        description="Gorgias customer ID (use gorgias_list_customers to find it).",
    )
    customer_email: Optional[str] = Field(
        default=None,
        description="Customer email address — will look up the customer ID automatically.",
    )
    limit: int = Field(default=50, ge=1, le=200, description="Max tickets to return.")


@mcp.tool(
    name="gorgias_list_customer_tickets",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Tickets for a Customer",
    },
)
async def gorgias_list_customer_tickets(params: CustomerTicketsInput) -> str:
    """
    Get all tickets for a specific customer, by ID or email address.
    Useful for looking up a customer's full support history.
    """
    # Use auth_email to avoid shadowing the customer_email concept
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    customer_id = params.customer_id

    # Resolve email to customer ID if needed
    if customer_id is None and params.customer_email:
        data = await _api_request(
            "/customers", domain, auth_email, api_key,
            params={"email": params.customer_email, "limit": 1},
        )
        customers = data.get("data", [])
        if not customers:
            raise ToolError(
                f"No customer found with email '{params.customer_email}'."
            )
        customer_id = customers[0]["id"]

    if customer_id is None:
        raise ToolError("Provide either customer_id or customer_email.")

    tickets, total = await _fetch_all_cursor(
        "/tickets", domain, auth_email, api_key,
        base_params={"customer_id": customer_id},
        max_items=params.limit,
    )

    identifier = params.customer_email or f"ID {customer_id}"
    has_more = len(tickets) < total

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "customer_id": customer_id,
            "total": total,
            "returned": len(tickets),
            "has_more": has_more,
            "tickets": tickets,
        }, indent=2)

    if not tickets:
        return f"[{acct_name}] No tickets found for customer {identifier}."

    lines = [
        f"## [{acct_name}] Tickets for {identifier} ({len(tickets)} of {total})\n"
    ]
    for t in tickets:
        csat = t.get("satisfaction_survey") or {}
        csat_str = f" | CSAT: {csat['score']}/5" if csat.get("score") else ""
        lines.append(
            f"**#{t['id']}** — {t.get('subject', '(no subject)')} "
            f"[{t.get('status')}] [{t.get('channel')}]{csat_str} — {t.get('created_datetime', '?')}"
        )
    return "\n".join(lines)


# ─── Tool: List Views ─────────────────────────────────────────────────────────

class ListViewsInput(BaseInput):
    pass


@mcp.tool(
    name="gorgias_list_views",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
        "idempotentHint": True,
        "title": "List Gorgias Ticket Views",
    },
)
async def gorgias_list_views(params: ListViewsInput) -> str:
    """
    List all ticket views (saved filters/queues) in the Gorgias account.
    Views define which tickets agents see in their queue.
    """
    acct_name, domain, auth_email, api_key = _resolve_account(params.account)

    data = await _api_request("/views", domain, auth_email, api_key)

    # Robustly handle both {data: [...]} and direct list responses
    if isinstance(data, dict):
        view_list = data.get("data")
        if view_list is None:
            view_list = []
        elif not isinstance(view_list, list):
            raise ToolError(
                f"Unexpected response shape from /views: data field is {type(view_list).__name__}"
            )
    elif isinstance(data, list):
        view_list = data
    else:
        raise ToolError(f"Unexpected response type from /views: {type(data).__name__}")

    if params.response_format == "json":
        return json.dumps({
            "account": acct_name,
            "total": len(view_list),
            "views": view_list,
        }, indent=2)

    if not view_list:
        return f"[{acct_name}] No views found."

    lines = [f"## [{acct_name}] Views ({len(view_list)})\n"]
    for v in view_list:
        lines.append(f"- **#{v.get('id')}** — {v.get('name', '?')}")
    return "\n".join(lines)


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio")
