# Gorgias REST API — Complete Reference

**Last updated:** March 2026 (post-audit update)
**API Version:** v1 (current)
**Base URL:** `https://{your-domain}.gorgias.com/api`
**Official docs:** https://developers.gorgias.com/reference/introduction
**Postman workspace:** https://www.postman.com/core-gorgias/public-workspace/documentation/0d3dyeo/gorgias-public-api

---

## Authentication

Gorgias uses **HTTP Basic Authentication** on every request.

```
Authorization: Basic base64(email:api_key)
```

With httpx/requests, pass `auth=(email, api_key)` — the library handles base64 encoding automatically.

**Getting your API key:**
1. Log in to Gorgias
2. Go to **Settings → You → REST API**
3. Generate or copy your API key

**Key scopes:** API keys can have restricted scopes. If you get 403 errors, the key may lack permission for that endpoint. Regenerate with broader scopes or check your key configuration.

---

## Pagination — CRITICAL UPDATE (Feb 2024)

Gorgias **removed offset/page-based pagination in February 2024**. All listing endpoints now use cursor-based pagination exclusively.

### How cursor-based pagination works

**First request:**
```
GET /api/tickets?limit=100
```

**Response:**
```json
{
  "data": [...],
  "meta": {
    "total_count": 3421,
    "next_cursor": "eyJpZCI6MTIzNDV9",
    "prev_cursor": null
  }
}
```

**Subsequent pages:**
```
GET /api/tickets?limit=100&cursor=eyJpZCI6MTIzNDV9
```

**Stop paginating when:** `next_cursor` is `null` or empty, OR the batch returned fewer items than `limit`.

**Important notes:**
- Cursors are opaque and short-lived — do not store them long-term
- The `total_count` in meta gives the overall total (useful for pagination UI)
- You cannot jump to a specific page — you must iterate sequentially

### Sorting (affects cursor ordering)

Many list endpoints support `order_by` and `order_dir`:
- `order_by`: `created_datetime`, `updated_datetime`, `closed_datetime`, `id`
- `order_dir`: `desc` (default, newest first), `asc` (oldest first)

Always set these before starting pagination — changing sort mid-cursor is undefined.

---

## Rate Limits

- Gorgias enforces per-key rate limits
- On limit, API returns **HTTP 429** with `Retry-After` header (seconds to wait)
- Typical limits are generous for normal usage; bulk fetches (5000+ items) risk hitting limits

---

## Common HTTP Response Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | — |
| 400 | Bad request | Check query parameters and body format |
| 401 | Invalid credentials | Wrong email or API key — regenerate |
| 403 | Forbidden | API key lacks required scope |
| 404 | Not found | Check the resource ID or path |
| 429 | Rate limited | Wait `Retry-After` seconds, then retry |
| 500 | Server error | Retry after brief wait |

---

## Complete Endpoint Reference

### Tickets

#### List Tickets
```
GET /api/tickets
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `limit` | int | Items per page (max 100) |
| `cursor` | string | Pagination cursor from previous response |
| `order_by` | string | Sort field: `created_datetime`, `updated_datetime`, `closed_datetime`, `id` |
| `order_dir` | string | `desc` (default) or `asc` |
| `status` | string | `open`, `closed`, `spam`, `snoozed` |
| `channel` | string | `email`, `chat`, `phone`, `instagram`, `facebook`, `twitter`, `whatsapp`, `sms`, `helpcenter`, `api` |
| `assignee_user_id` | int | Filter by agent user ID |
| `assignee_team_id` | int | Filter by team ID |
| `customer_id` | int | Filter by customer ID |
| `created_datetime[gte]` | ISO 8601 | Created on or after |
| `created_datetime[lte]` | ISO 8601 | Created on or before |
| `updated_datetime[gte]` | ISO 8601 | Updated on or after |
| `q` | string | Full-text search across subject and messages |

#### Get Single Ticket
```
GET /api/tickets/{id}
```

#### Update Ticket
```
PUT /api/tickets/{id}
```
Updatable fields: `status`, `subject`, `assignee_user_id`, `assignee_team_id`, `tags`, `snooze_datetime`

#### Create Ticket
```
POST /api/tickets
```

#### Ticket Object — Key Fields

```json
{
  "id": 12345,
  "subject": "My order hasn't arrived",
  "status": "open",
  "channel": "email",
  "is_unread": false,
  "messages_count": 3,
  "excerpt": "Hi, I placed order #5678...",
  "created_datetime": "2025-01-15T10:30:00Z",
  "updated_datetime": "2025-01-15T11:00:00Z",
  "closed_datetime": null,
  "snooze_datetime": null,
  "spam_reason": null,
  "meta": {
    "priority": "normal"
  },
  "customer": {
    "id": 789,
    "firstname": "Jane",
    "lastname": "Doe",
    "email": "jane@example.com"
  },
  "assignee_user": {
    "id": 42,
    "firstname": "Alice",
    "lastname": "Smith",
    "email": "alice@company.com"
  },
  "assignee_team": {
    "id": 5,
    "name": "Support Team"
  },
  "tags": [
    {"id": 1, "name": "shipping"},
    {"id": 2, "name": "urgent"}
  ],
  "satisfaction_survey": {
    "score": 4,
    "body_text": "Great support, thank you!"
  }
}
```

**Note on `satisfaction_survey`:** This field is `null` if no CSAT survey was sent or responded to. Check for existence before accessing `score`.

---

### Ticket Messages

#### List Messages for a Ticket
```
GET /api/tickets/{id}/messages
```

#### Create Message (reply)
```
POST /api/tickets/{id}/messages
```

#### Message Object — Key Fields

```json
{
  "id": 99001,
  "ticket_id": 12345,
  "from_agent": false,
  "public": true,
  "channel": "email",
  "created_datetime": "2025-01-15T10:30:00Z",
  "sender": {
    "id": 789,
    "firstname": "Jane",
    "lastname": "Doe",
    "email": "jane@example.com"
  },
  "stripped_text": "Hi, I placed order #5678 last week...",
  "body_text": "Hi, I placed order #5678 last week...",
  "body_html": "<p>Hi, I placed order #5678...</p>",
  "attachments": []
}
```

`from_agent: true` = agent or automation message
`from_agent: false` = customer message
`public: false` = internal note (not visible to customer)

---

### Statistics — Legacy API (`POST /api/stats/{name}`)

> **⚠️ Deprecation Warning:** This API will be sunset on **December 31, 2026**. New integrations should use the New Statistics API (see below). Use this for now but plan migration.

#### Endpoint
```
POST /api/stats/{stat_name}
```

#### Request Body
```json
{
  "start_datetime": "2025-01-01T00:00:00",
  "end_datetime": "2025-03-31T23:59:59",
  "filters": {
    "channel": "email"
  }
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `start_datetime` | Yes | ISO 8601 start of period |
| `end_datetime` | Yes | ISO 8601 end of period (max range: 365 days) |
| `filters` | No | Optional filters to narrow scope |

#### Available Stat Names (Legacy API)

| Stat name | Description |
|-----------|-------------|
| `overview` | High-level support summary |
| `first-response-time` | Average and median first response time |
| `resolution-time` | Average time from first customer message to close |
| `created-tickets` | Ticket creation volume over time |
| `closed-tickets` | Closed ticket count over time |
| `replied-tickets` | Tickets that received at least one agent reply |
| `one-touch-tickets` | Tickets resolved with a single response |
| `messages-statistics` | Message volume and breakdown |
| `agent-overview` | Per-agent performance table |
| `satisfaction-surveys` | CSAT score distribution and summary |
| `support-performance` | Comprehensive KPI dashboard data |

**Removed stat names:**
- `self-service-overview` — removed January 1, 2025 (old Automate data source deprecated)

#### Filter Examples
```json
{ "channel": "email" }
{ "assignee_user": { "id": 42 } }
{ "assignee_team": { "id": 5 } }
{ "tags": ["billing", "refund"] }
```

#### Download as CSV
```
POST /api/stats/{stat_name}/download
```
Same request body — returns a CSV file.

#### Notes
- Max date range: **365 days**
- Deleted (merged), trash, and spam tickets are excluded
- Times are in seconds for FRT/resolution metrics
- Stat names use hyphens, not underscores

---

### Statistics — New API (December 2025)

> **This is the future of Gorgias analytics.** Launched December 18, 2025. All new integrations and dashboards should use this.

#### Key improvements over legacy API:
- Multi-dimensional queries — combine multiple breakdown dimensions in one call
- Cross-reference Ticket Custom Fields as dimensions
- Faster and more reliable (dedicated analytics engine)
- Aligned with Gorgias Helpdesk reporting UI
- Where all future metric additions will happen

#### Migration timeline:
- Legacy API (`/api/stats/{name}`) deprecated: **December 31, 2026**
- New API coverage target: **100% by end of 2026**

#### Endpoint format (verify against official docs):
The exact endpoint for the new API needs confirmation from `developers.gorgias.com`. Based on available information, it uses multi-dimensional query parameters including dimensions like `store`, `integration`, `channel`, and custom `ticket_fields`.

**Action:** Check Gorgias developer docs or changelog for the exact endpoint URL and request format before implementing.

---

### CSAT / Satisfaction Surveys

#### List Surveys
```
GET /api/satisfaction-surveys
```

**Query parameters:**

| Parameter | Description |
|-----------|-------------|
| `limit` | Items per page |
| `cursor` | Pagination cursor |
| `created_datetime[gte]` | Filter by submission date start |
| `created_datetime[lte]` | Filter by submission date end |

#### Survey Object — Key Fields

```json
{
  "id": 5001,
  "ticket_id": 12345,
  "score": 4,
  "body_text": "Very helpful team!",
  "created_datetime": "2025-01-16T09:00:00Z",
  "customer": {
    "id": 789,
    "email": "jane@example.com"
  }
}
```

**Score scale:**
- 5 = Very satisfied
- 4 = Satisfied
- 3 = Neutral
- 2 = Dissatisfied
- 1 = Very dissatisfied

**Important:** `score` can be null if the customer opened the survey link but did not submit a rating.

---

### Users (Agents)

#### List Users
```
GET /api/users
```

#### Get User
```
GET /api/users/{id}
```
Use `id = 0` to get the currently authenticated user.

#### User Object — Key Fields

```json
{
  "id": 42,
  "firstname": "Alice",
  "lastname": "Smith",
  "email": "alice@company.com",
  "active": true,
  "timezone": "Europe/Paris",
  "bio": "Senior Support Agent",
  "role": {
    "id": 1,
    "name": "agent"
  },
  "created_datetime": "2024-06-01T00:00:00Z"
}
```

**Role names:** `owner`, `admin`, `lead-agent`, `agent`, `read-only`

---

### Teams

#### List Teams
```
GET /api/teams
```

Returns team objects with `id`, `name`, `description`, and member list. Use team IDs for `assignee_team_id` filtering in ticket queries.

**Note:** Team membership affects routing rules and ticket visibility in views.

---

### Customers

#### List / Search Customers
```
GET /api/customers
```

**Query parameters:**

| Parameter | Description |
|-----------|-------------|
| `limit` | Items per page |
| `cursor` | Pagination cursor |
| `email` | Filter by exact email address |
| `q` | Full-text search by name or email |

#### Get Customer
```
GET /api/customers/{id}
```

#### Customer Object — Key Fields

```json
{
  "id": 789,
  "firstname": "Jane",
  "lastname": "Doe",
  "email": "jane@example.com",
  "channels": [
    { "type": "email", "address": "jane@example.com" },
    { "type": "phone", "address": "+1-555-0100" }
  ],
  "notes": "VIP customer, handle with priority",
  "created_datetime": "2024-09-01T00:00:00Z"
}
```

---

### Tags

#### List Tags
```
GET /api/tags?limit=200
```

Simple list of `{id, name}` objects. Tags can be used as filters in ticket queries.

---

### Views (Ticket Queues)

#### List Views
```
GET /api/views
```

Views are saved filter configurations. The View object includes:
- `id`, `name`, `description`
- `order_by`, `order_dir` — default sort for this view
- `conditions` — filter rules that define which tickets appear

---

### Macros (Response Templates)

#### List Macros
```
GET /api/macros
```

#### Get Macro
```
GET /api/macros/{id}
```

Macros are pre-written responses that agents apply to tickets. The macro object includes:
- `id`, `name`
- `actions` — array of actions to perform (send message, set tags, assign user, etc.)
- `created_by_user` — who created it
- `is_shared` — whether it's visible to all agents or just the creator

**Common use case:** Audit available macros to understand standard responses, check if macros exist for common topics, or analyze macro usage patterns.

---

### Custom Fields

#### List Custom Fields
```
GET /api/custom-fields
```

Custom (ticket) fields are user-defined properties shown on tickets. The object includes:
- `id`, `name`, `type` (`text`, `select`, `boolean`, `integer`, `datetime`, `list`)
- `options` — for `select` type, the available choices
- `required` — whether agents must fill this before closing

**Why this matters:** Raw ticket responses include custom field data by ID only. You need the field definitions to map IDs to human-readable labels.

---

### Events (Activity Log)

#### List Events
```
GET /api/events
```

Events are an audit log of every action on every ticket. Supports cursor-based pagination (added Feb 2024).

**Query parameters:**

| Parameter | Description |
|-----------|-------------|
| `object_type` | `Ticket`, `Message`, `Customer`, etc. |
| `event_type` | `created`, `updated`, `deleted`, `assigned`, etc. |
| `created_datetime[gte]` | Start date |

**Note:** Events can be very high-volume. Always filter by date range and/or object type.

---

### Integrations

#### List Integrations
```
GET /api/integrations
```

Returns active channel integrations (email addresses, Instagram accounts, live chat widgets, etc.).

---

## Gotchas and Known Issues

### 1. Cursor validity
Cursors expire after a short time (minutes to hours). Do not cache cursors for later use. If a cursor expires, start pagination from the beginning.

### 2. `satisfaction_survey` in ticket list vs. survey endpoint
The `satisfaction_survey` object embedded in ticket responses only includes `score` and basic fields. The full survey response with customer details and `body_text` requires the dedicated `/api/satisfaction-surveys` endpoint.

### 3. `total_count` may be approximate
On very large result sets, `total_count` in pagination meta may be an estimate, not an exact count. Don't rely on it for precise counting in critical applications.

### 4. Ticket `status` values
Valid statuses: `open`, `closed`, `spam`, `snoozed`. Note that `snoozed` tickets appear as neither open nor closed and have a non-null `snooze_datetime`.

### 5. `from_agent: true` includes automation
Messages with `from_agent: true` include both human agent replies AND automated responses from Gorgias Rules. If you need to distinguish human vs. automated, check the `source.type` field on the message.

### 6. Channel name casing
Channel names are always lowercase in API responses and query parameters (`email`, not `Email`).

### 7. Date filtering format
Gorgias date filters accept ISO 8601 format. Include timezone `Z` suffix for UTC, or omit for account timezone. For stats API, use the exact format `"2025-01-01T00:00:00"` (no Z).

### 8. Large account performance
For accounts with 100k+ tickets:
- Never paginate through all tickets for aggregate stats — use the Stats API instead
- Date-range filter all ticket queries
- Use `gorgias_get_stats` for KPIs, not raw ticket aggregation

---

## Useful Query Patterns

### Latest open tickets (sorted most-recent first)
```
GET /api/tickets?status=open&order_by=updated_datetime&order_dir=desc&limit=50
```

### All tickets for a customer by email
```
GET /api/customers?email=jane@example.com&limit=1
# Then use customer ID:
GET /api/tickets?customer_id=789&order_by=created_datetime&order_dir=desc
```

### Tickets with a specific tag (concept)
```
GET /api/tickets?tags[]=billing&order_by=created_datetime&order_dir=desc
```
(Verify exact param format against Gorgias docs)

### Official first response time for Q1 2025
```
POST /api/stats/first-response-time
{
  "start_datetime": "2025-01-01T00:00:00",
  "end_datetime": "2025-03-31T23:59:59"
}
```

### Agent performance for a specific team
```
POST /api/stats/agent-overview
{
  "start_datetime": "2025-01-01T00:00:00",
  "end_datetime": "2025-01-31T23:59:59",
  "filters": { "assignee_team": { "id": 5 } }
}
```

### CSAT breakdown for email channel only
```
POST /api/stats/satisfaction-surveys
{
  "start_datetime": "2025-01-01T00:00:00",
  "end_datetime": "2025-03-31T23:59:59",
  "filters": { "channel": "email" }
}
```

---

## What's NOT Available via REST API

| Feature | Status | Notes |
|---------|--------|-------|
| Macros (list/get) | ✅ Available | `GET /api/macros` |
| Rules (automations) | ❌ No public API | Configure in UI only |
| Live/real-time stats | ❌ Not available | Stats API is historical |
| Ticket merge history | ❌ Not exposed | Merged tickets appear deleted |
| Agent online/offline status | ❌ Not available | No real-time presence API |
| Helpdesk settings | ❌ Limited | Some settings endpoints exist but incomplete |
