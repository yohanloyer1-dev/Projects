# Gorgias MCP Server — v3

Connect Claude directly to one or more Gorgias helpdesk accounts via the Gorgias REST API.
No Zapier, no third-party services — just your API key(s) and Python.

---

## What's New in v3

- **All errors properly signalled** — tools raise `ToolError` so Claude correctly flags failures
- **Rate-limit safe** — 0.55s inter-page delay on paginated calls (respects 2 req/s limit)
- **Analytics timeout fix** — ticket stats tools capped at 500 items (was 5000 → guaranteed timeout)
- **Newest-first by default** — `gorgias_list_tickets` now sorts by `id desc` (newest tickets first)
- **Sorting control** — `order_by` and `order_dir` params on `gorgias_list_tickets`
- **Three new tools** — `gorgias_list_teams`, `gorgias_list_macros`, `gorgias_list_custom_fields`
- **Hot-reload** — `gorgias_reload_accounts` refreshes credentials without server restart
- **Persistent HTTP client** — connection pooling instead of a new client per request
- **Complete pagination** — search, messages, tags, and customers all use cursor pagination
- **Strict input validation** — typos in param names are caught; `response_format` is validated
- **JSON responses include `has_more`** — so you know when more data exists

---

## Requirements

- Python 3.10+
- `mcp[cli] >= 1.0.0`
- `httpx >= 0.27.0`
- `pydantic >= 2.0.0`
- A Gorgias account with API access

Install dependencies:
```bash
pip install mcp[cli] httpx pydantic
```

---

## Setup

### 1 — Create your accounts config

Create `gorgias_accounts.json` in the same folder as `gorgias_mcp_server.py`:

```json
{
  "accounts": {
    "ClientA": {
      "domain": "clienta",
      "email": "you@yourcompany.com",
      "api_key": "YOUR_API_KEY_HERE"
    },
    "ClientB": {
      "domain": "clientb",
      "email": "you@yourcompany.com",
      "api_key": "YOUR_API_KEY_HERE"
    }
  }
}
```

**Where to find your API key:**
Gorgias → Settings → You → REST API → Generate a token

**Single-account alternative (env vars):**
```bash
export GORGIAS_DOMAIN="yourstore"
export GORGIAS_EMAIL="you@example.com"
export GORGIAS_API_KEY="your_api_key"
```

### 2 — Register with Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "gorgias": {
      "command": "python3",
      "args": ["/full/path/to/gorgias_mcp_server.py"]
    }
  }
}
```

> Replace `/full/path/to/` with the actual path to the folder.

### 3 — Restart Claude Desktop

Quit and reopen Claude Desktop. You should see the Gorgias tools available.

---

## Tools Reference (21 tools)

### Account Management

| Tool | Description |
|------|-------------|
| `gorgias_list_accounts` | Show all configured accounts and their domains |
| `gorgias_reload_accounts` | Hot-reload credentials from `gorgias_accounts.json` |
| `gorgias_account_info` | Verify connectivity and show authenticated user details |

### Tickets

| Tool | Description |
|------|-------------|
| `gorgias_list_tickets` | List tickets with filters (status, channel, assignee, date, tags) + sorting |
| `gorgias_get_ticket` | Get full details for a single ticket by ID |
| `gorgias_list_ticket_messages` | Get the full conversation thread for a ticket |
| `gorgias_search_tickets` | Full-text search across all ticket subjects and messages |
| `gorgias_list_customer_tickets` | All tickets for a customer (by ID or email) |

### Analytics & Stats

| Tool | Description |
|------|-------------|
| `gorgias_get_stats` | Pre-computed KPIs via the stats engine (fast, official) — **use this first** |
| `gorgias_get_csat_stats` | CSAT summary: avg score, positive/negative rate, distribution, comments |
| `gorgias_list_satisfaction_surveys` | Raw CSAT survey responses with scores and comments |
| `gorgias_ticket_stats` | Ticket volume breakdown by status, channel, and tag (sampled) |
| `gorgias_agent_performance` | Per-agent ticket counts and CSAT averages (sampled) |

### People & Configuration

| Tool | Description |
|------|-------------|
| `gorgias_list_users` | All agents and their roles, email, and active status |
| `gorgias_get_user` | Full profile for a specific user by ID |
| `gorgias_list_customers` | Search or list customers by name/email |
| `gorgias_list_teams` | All teams with IDs (use team IDs in ticket filters) |
| `gorgias_list_tags` | All ticket tags with IDs |
| `gorgias_list_macros` | All macros (response templates) |
| `gorgias_list_custom_fields` | All custom ticket field definitions |
| `gorgias_list_views` | All saved ticket views / queues |

---

## `gorgias_get_stats` — Stat Names Reference

This is the fastest and most accurate way to get KPIs. Always prefer it over `gorgias_ticket_stats`.

| `stat_name` | What it returns |
|-------------|-----------------|
| `overview` | Overall support summary |
| `first-response-time` | Average and median first response time |
| `resolution-time` | Average time to close tickets |
| `created-tickets` | Ticket creation volume by period |
| `closed-tickets` | Closed ticket count by period |
| `replied-tickets` | Tickets that received at least one agent reply |
| `one-touch-tickets` | Tickets resolved with a single response |
| `messages-statistics` | Message volume and breakdown |
| `agent-overview` | Per-agent performance table (response time, resolution, CSAT) |
| `satisfaction-surveys` | CSAT score distribution and summary |
| `support-performance` | Comprehensive KPI dashboard data |

---

## Example Questions for Claude

**Tickets**
- "Show me the last 20 open tickets from ClientA"
- "List all tickets tagged 'billing' opened this month for ClientB"
- "Search for tickets about 'refund' across all channels"
- "What's the full conversation history for ticket #12345?"

**CSAT & Analytics**
- "What was our average CSAT score in Q1 2025 for ClientA?"
- "Show me the first-response-time stats for January 2026"
- "Which agents handled the most tickets last month?"
- "How many tickets did we get per channel in Q4?"

**Account & Team Setup**
- "List all teams and their IDs"
- "What macros do we have configured?"
- "Show me all custom fields on tickets"
- "Who are the active agents and what roles do they have?"

---

## Common Parameters

All tools accept two shared parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `account` | `string` (optional) | Account name from `gorgias_accounts.json`. Required only when multiple accounts are configured. |
| `response_format` | `"markdown"` \| `"json"` | Output format. Markdown (default) is human-readable. JSON is better for data processing. |

---

## Troubleshooting

**"No Gorgias accounts configured"**
→ Check that `gorgias_accounts.json` is in the same folder as `gorgias_mcp_server.py`.

**"Authentication failed (401)"**
→ Verify your email and API key. Generate a new token at Gorgias → Settings → You → REST API.

**"Forbidden (403)"**
→ Your API key lacks the needed scopes. Try generating a new key with full access.

**"Rate limited — retry after N seconds"**
→ The server automatically throttles paginated calls to 2 req/s. If this occurs on a single-page call, you are hitting the burst limit. Wait and retry.

**Changes to gorgias_accounts.json not picked up**
→ Run `gorgias_reload_accounts` in Claude, or restart Claude Desktop.

**Results seem too old (not the most recent tickets)**
→ `gorgias_list_tickets` defaults to `order_by=id, order_dir=desc` (newest first). If you're getting old tickets, check your date filters.

---

## API Notes

- **Rate limit:** 2 requests/second per account (burst of 40). The v3 server adds automatic 0.55s delays between paginated pages.
- **Legacy Stats API** (`gorgias_get_stats`) is being sunset **December 31, 2026**. It works today and is the most reliable stats source. A migration to Gorgias's new Statistics API (launched Dec 2025) is planned for a future version.
- **Pagination:** Gorgias removed offset/page-based pagination in February 2024. This server uses cursor-based pagination throughout.
- **Auth:** HTTP Basic Auth with your email as username and the API token as password.
