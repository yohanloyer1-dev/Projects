# Gorgias MCP Server — Expert Audit Report v2
**Date:** 2026-03-08
**Scope:** `gorgias_mcp_server.py` (v2) — full line-by-line deep-dive
**Auditor role:** Senior MCP/API integration engineer with Gorgias, FastMCP, and httpx expertise
**Status:** Pre-deployment — do NOT deploy v2; v3 with all fixes is the deployable version

---

## Executive Summary

The v2 server is a solid structural foundation: multi-account design is correct, cursor-based pagination is implemented, and the stats endpoint integration is functional. However, the deep-dive audit uncovered **5 critical bugs, 10 high-priority issues, 11 medium issues, and 7 low-priority issues** that would cause runtime failures, silent data loss, API rate-limit violations, and poor Claude experience in production. All have been fixed in v3.

**Severity counts:**
| Severity | Count | v2 Status |
|----------|-------|-----------|
| Critical | 5 | All fixed in v3 |
| High | 10 | All fixed in v3 |
| Medium | 11 | All fixed in v3 |
| Low | 7 | All fixed in v3 |

---

## CRITICAL Issues

### C1 — Errors returned as plain text, not `ToolError`

**Location:** Every tool function (~17 occurrences)
**Pattern found:**
```python
except ValueError as e:
    return f"Error: {e}"     # WRONG
except Exception as e:
    return f"[{acct_name}] Error: {e}"   # WRONG
```

**Problem:** In MCP, a tool returning a string is a _successful_ result. Claude will happily display "Error: Account not found" as if it were valid data, then potentially continue reasoning on that phantom response. Tool errors must be signalled with `isError: true` by raising `ToolError`. The `ToolError` class is available from `mcp.server.fastmcp` but was never imported.

**Also in `_api_request`:** All `raise RuntimeError(...)` calls are wrong — `RuntimeError` inside an async FastMCP tool propagates as an unhandled exception with no useful detail reaching Claude.

**Fix:** Import `ToolError`, replace every `return f"Error: ..."` with `raise ToolError(...)`, replace every `raise RuntimeError(...)` with `raise ToolError(...)`.

---

### C2 — `Content-Type: application/json` sent on every request including GETs

**Location:** `_api_request`, line 123
**Code:**
```python
headers={"Content-Type": "application/json", "Accept": "application/json"},
```

**Problem:** `Content-Type` describes the _body_ of a request. Sending it on GET requests (which have no body) is technically incorrect per RFC 7231 and is known to cause 400/415 errors on strict API servers. Gorgias may be lenient today but this is a latent bug.

**Fix:** Only send `Content-Type` when `method` is `POST`, `PUT`, or `PATCH`.

---

### C3 — No inter-page rate limiting in `_fetch_all_cursor`

**Location:** `_fetch_all_cursor`, lines 164–181
**Problem:** The pagination loop calls `_api_request` in a tight while-loop with no delay between pages. Gorgias enforces **2 calls/second per account** (leaky bucket, burst of 40). Fetching 1000 items = 10 consecutive API calls fired as fast as Python can execute — easily triggering rate limiting. When rate-limited (HTTP 429), `_api_request` raises immediately, giving a partial result with no indication of how much data was retrieved before failure.

**Fix:** Add `asyncio.sleep(0.55)` between pages. Also honour the `Retry-After` header on 429 by retrying once.

---

### C4 — Analytics tools cap at `max_items=5000` — guaranteed timeout

**Location:** `gorgias_ticket_stats` and `gorgias_agent_performance`
**Code:**
```python
tickets, total = await _fetch_all_cursor(
    "/tickets", domain, email, api_key,
    base_params=query_params,
    max_items=5000,
)
```

**Problem:** 5000 items = 50 paginated API calls × 0.55s minimum delay = **27+ seconds**. Claude Desktop MCP requests time out at 30s. On any busy account this will routinely fail. Even if it completes, 5000 ticket objects is ~10–25 MB of data processed in Python.

**Fix:** Cap analytics tools at `max_items=500`. For volumetric statistics, use the Stats API (`gorgias_get_stats`) instead of downloading raw tickets.

---

### C5 — Missing `order_by`/`order_dir` on `gorgias_list_tickets`

**Location:** `ListTicketsInput`, `gorgias_list_tickets`
**Problem:** Gorgias supports sorting by `created_datetime`, `updated_datetime`, `closed_datetime`, and `id` in `asc`/`desc` order. Without these, results return in Gorgias's default order (id ascending) — so "show me the last 50 tickets" actually returns the 50 oldest tickets.

**Fix:** Add `order_by: Optional[str]` and `order_dir: Optional[str]` to `ListTicketsInput`, defaulting to `order_by="id"` and `order_dir="desc"`.

---

## HIGH Issues

### H1 — New Statistics API (December 2025) not implemented

The legacy Stats API (`POST /api/stats/{name}`) is being **sunset on December 31, 2026**. The new multi-dimensional Statistics API (launched December 2025) is the forward-compatible replacement. All new integrations should target it. Currently `gorgias_get_stats` calls the legacy endpoint, and there is no `gorgias_get_statistics` tool for the new API.

**Fix:** Add `gorgias_get_statistics` tool for the new API. Keep the legacy tool marked as deprecated.

---

### H2 — Missing `/api/teams` endpoint

Teams are essential for multi-agent setups. The `assignee_team_id` filter in `gorgias_list_tickets` is useless if users can't discover team IDs. A `gorgias_list_teams` tool was in the original design but never implemented.

---

### H3 — Missing `/api/macros` endpoint

Macros are pre-defined response templates widely used in Gorgias. Without `gorgias_list_macros`, Claude cannot help users understand what automations are configured or audit macro usage.

---

### H4 — Missing `/api/custom-fields` endpoint

Many Gorgias customers use custom ticket fields (order IDs, product categories, etc.). Without `gorgias_list_custom_fields`, Claude cannot see or reference these fields when summarizing tickets.

---

### H5 — `_load_accounts()` called on every tool invocation

**Location:** `_resolve_account`, line 70 (called by every tool)
**Problem:** Every tool call opens, reads, and parses `gorgias_accounts.json` from disk. Unnecessary I/O on every invocation. If the file is temporarily unreadable (OS lock, write in progress), the tool fails.

**Fix:** Cache the accounts dict at module load time. Expose a `gorgias_reload_accounts` tool for hot-reloading without server restart.

---

### H6 — New `httpx.AsyncClient` created per API request

**Location:** `_api_request`, line 116
**Problem:** Creating a new HTTP client per request means no TCP connection reuse, no keep-alive, and no connection pooling. Each API call pays the full TLS handshake + TCP connection overhead. For paginated fetches with 10–50 calls, this is significant added latency.

**Fix:** Use FastMCP's lifespan feature to create one shared `httpx.AsyncClient` at server startup and close it cleanly on shutdown.

---

### H7 — No pagination exposure to caller

**Location:** All list tools
**Problem:** JSON responses include `total` but no `has_more: bool` or `next_cursor: str`. It's impossible for programmatic callers to know whether more data exists or how to page through it.

**Fix:** Add `has_more` and `next_cursor` fields to all JSON responses from list tools.

---

### H8 — Falsy check on integer IDs silently drops filters

**Location:** `gorgias_list_tickets`, lines 292–297
**Code:**
```python
if params.assignee_user_id:      # BUG: evaluates False when ID = 0
    query_params["assignee_user_id"] = params.assignee_user_id
```

**Problem:** In Gorgias, `user_id=0` means "the authenticated user." Specifying `assignee_user_id=0` evaluates to `False` and the filter is silently dropped, returning all tickets regardless of assignee. Same bug on `assignee_team_id` and `customer_id`.

**Fix:** Replace with `if params.assignee_user_id is not None:` throughout.

---

### H9 — `gorgias_search_tickets` fetches only the first page

**Location:** `gorgias_search_tickets`, line 491
**Problem:** Calls `_api_request` directly (one page). If the search matches more tickets than `params.limit` (max 100), remaining matches are silently lost. The `total` in the response shows the real count, revealing the discrepancy.

**Fix:** Replace with `_fetch_all_cursor` using the query params.

---

### H10 — `gorgias_list_ticket_messages` fetches only the first page

**Location:** `gorgias_list_ticket_messages`, line 428
**Problem:** Tickets with more than 100 messages (long-running email threads) silently return only the first page. The user gets a truncated conversation with no indication that messages are missing.

**Fix:** Replace with `_fetch_all_cursor` for the messages endpoint.

---

## MEDIUM Issues

### M1 — `response_format` is unvalidated raw string

**Location:** `BaseInput`, line 198
**Problem:** `response_format: str` accepts any string. Passing `"JSON"` (uppercase) or `"json5"` silently falls through to markdown with no validation error.

**Fix:** `response_format: Literal["markdown", "json"] = Field(default="markdown", ...)`.

---

### M2 — `BaseInput` missing `extra='forbid'`

**Problem:** Typos in parameter names (e.g. `status_filter` instead of `status`) are silently ignored. The filter is never applied with no error raised.

**Fix:** Add `extra='forbid'` to `ConfigDict`.

---

### M3 — `_render_value` defined as nested function inside `gorgias_get_stats`

**Problem:** The `_render_value` helper is defined inside the tool function — Python recreates the function object on every tool invocation. It's also impossible to unit-test in isolation.

**Fix:** Move to module level.

---

### M4 — `gorgias_list_accounts` is inconsistent (no `BaseInput`)

**Problem:** Unlike every other tool, `gorgias_list_accounts` takes no parameters — no `response_format`, no JSON output. Can't be extended without breaking the signature.

**Fix:** Add `ListAccountsInput(BaseInput)` and implement JSON output mode.

---

### M5 — `gorgias_list_tags` uses single-page fetch with hard limit

**Location:** Line 1115
**Problem:** Gorgias accounts can have hundreds of tags. With `limit=200` (max configured), tags beyond 200 are silently omitted with no truncation notice.

**Fix:** Use `_fetch_all_cursor` for tags.

---

### M6 — `gorgias_list_customers` uses single-page fetch

**Location:** Line 1166
**Problem:** Customer lists can be very large; only the first page is returned without warning.

**Fix:** Use `_fetch_all_cursor` for customers (with the search/email filter passed through).

---

### M7 — `gorgias_list_views` has fragile response handling

**Location:** Line 1290
**Code:**
```python
views = data.get("data", data) if isinstance(data, dict) else data
```

**Problem:** If the API returns an unexpected shape, this defensive code silently accepts it. Any structural change in the Gorgias API response would cause silent misbehaviour.

**Fix:** Explicitly handle the expected dict shape; raise `ToolError` for unexpected shapes.

---

### M8 — All tool annotations missing `idempotentHint`

Every read-only tool should have `"idempotentHint": True` — calling them multiple times with the same parameters gives the same result.

---

### M9 — All tool annotations missing `title`

MCP tool annotations support a human-readable `title`. Without it, clients fall back to the raw tool name (`gorgias_list_tickets`), which is less user-friendly.

---

### M10 — `gorgias_list_customer_tickets` — credential variable shadows concept

**Location:** Line 1155 vs 1197
**Problem:** The resolved API credential is named `email` in scope. The input parameter is `customer_email`. These names are in the same function scope, creating a maintainability hazard where `email` could be confused for the customer's email address.

**Fix:** Rename the credential tuple variable to `auth_email` inside this function.

---

### M11 — No explicit `transport="stdio"` in `mcp.run()`

**Location:** Line 1346
**Problem:** `mcp.run()` without arguments relies on FastMCP auto-detecting the transport. For Claude Desktop (stdio), this works, but if the server is accidentally started in a different context it may hang silently.

**Fix:** `mcp.run(transport="stdio")` makes the intent explicit.

---

## LOW Issues

### L1 — Missing `gorgias_reload_accounts` tool

Without hot-reloading, credential changes to `gorgias_accounts.json` require restarting Claude Desktop.

---

### L2 — `gorgias_list_ticket_messages` may expose raw HTML

**Location:** Line 451
**Problem:** `body_text` fallback can contain raw HTML from email messages. `stripped_text` is preferred but may be absent. The 500-char preview mitigates but doesn't eliminate noise.

**Recommendation:** Add a note in the output if only HTML body was available.

---

### L3 — `gorgias_agent_performance` CSAT average has no sample size indicator

An agent with 100 tickets and 2 CSAT responses will show an average from only 2 data points, which is statistically misleading.

**Recommendation:** Show `(N responses)` alongside the CSAT average.

---

### L4 — `gorgias_get_csat_stats` filters surveys in Python, not via API

**Problem:** Fetches up to 1000 surveys then filters by date in Python. On large accounts with >1000 surveys, surveys outside the fetched window are missed.

**Fix:** Pass date filters as API query parameters (`created_datetime[gte]`, `created_datetime[lte]`).

---

### L5 — `BaseInput` missing `validate_assignment=True`

Post-construction field modification won't be validated. Defensive best practice.

---

### L6 — No input validation for date format

`created_after`, `created_before`, etc. accept any string. Passing `"January 1, 2025"` results in a cryptic API 400 error.

**Fix:** Add a `@field_validator` checking the string matches ISO 8601 format.

---

### L7 — `gorgias_account_info` doesn't verify API scopes

`GET /users/0` verifies credentials but not scope permissions. A read-only key missing `tickets` scope passes the connectivity check but fails on `gorgias_list_tickets`.

---

## What's Correct (Positive Findings)

These areas were reviewed and found to be correctly implemented:

- **Cursor-based pagination** — `_fetch_all_cursor` correctly uses `meta.next_cursor`. The early-exit condition (`len(batch) < limit_per_page`) is correct.
- **Multi-account resolution** — `_resolve_account` correctly handles exact match, case-insensitive fallback, single-account auto-select, and multi-account disambiguation.
- **Stats API integration** — `gorgias_get_stats` correctly uses `POST /api/stats/{name}` with date range and filters in the request body.
- **`gorgias_list_customer_tickets` email lookup** — Correctly uses `GET /customers?email=...&limit=1` then extracts the ID for the tickets query.
- **Auth pattern** — HTTP Basic Auth with `auth=(email, api_key)` is correct for Gorgias REST API.
- **Timeout handling** — 30-second timeout on `httpx.AsyncClient` is appropriate.
- **ENV variable fallback** — Single-account users who prefer env vars are supported.

---

## Priority Fix Matrix

| Priority | Issue | Effort | Risk if skipped |
|----------|-------|--------|-----------------|
| 🔴 Deploy-blocker | C1 — `ToolError` | Medium | Claude silently ignores all errors |
| 🔴 Deploy-blocker | C2 — Content-Type on GET | Low | Possible API 400/415 errors |
| 🔴 Deploy-blocker | C3 — Rate limiting in pagination | Medium | 429 failures on any bulk fetch |
| 🔴 Deploy-blocker | C4 — Analytics timeout | Low | Guaranteed timeout on large accounts |
| 🔴 Deploy-blocker | C5 — Sort order | Low | Results in wrong order (oldest first) |
| 🟠 Pre-prod | H8 — Falsy ID check | Low | Silent filter drops |
| 🟠 Pre-prod | H9/H10 — Single-page pagination | Medium | Missing data on large tickets/searches |
| 🟠 Pre-prod | M1 — `response_format` validation | Low | Silent fallback to markdown |
| 🟠 Pre-prod | M2 — `extra='forbid'` | Low | Typos silently ignored |
| 🟡 Sprint 1 | H1 — New Stats API | High | Legacy API sunset Dec 2026 |
| 🟡 Sprint 1 | H2/H3/H4 — Missing tools | Medium | Incomplete feature set |
| 🟡 Sprint 1 | H5 — Account caching | Low | Unnecessary disk I/O |
| 🟡 Sprint 1 | H6 — Persistent httpx client | Medium | Latency on paginated calls |
| 🟡 Sprint 1 | L4 — CSAT date filter via API | Low | Incorrect date ranges on large accounts |
| 🟡 Sprint 1 | L6 — Date validation | Low | Confusing API errors |

---

*All issues above have been addressed in `gorgias_mcp_server.py` v3.*
