# LOVABLE SAAS SPEC — D12
# Phase 2 product. Build only after D13 GO/NO-GO criteria pass.
# Last updated: 2026-05-04

> **Phase gate**: Do not start Lovable build until 3 DFY clients are live AND 6 weeks of stable operation per client AND €1,500/mo retainer MRR. See D13.

---

## a) SCREEN LIST + USER FLOW

### Auth & onboarding (5 screens)
1. **Login** — email magic link, no password. "Send me a sign-in link."
2. **Magic link sent** — confirmation screen with retry button.
3. **Onboarding wizard step 1** — niche, target audience, tone guide
4. **Onboarding wizard step 2** — CTA keyword, free resource URL, brand terms to avoid
5. **Onboarding wizard step 3** — connect Higgsfield (OAuth), connect Metricool (OAuth), connect Kit (API key paste)

### Core dashboard (4 screens)
6. **Home dashboard** — this week's pipeline (research → scripts → videos → posts), key metrics tiles, action items
7. **Scripts** — current week's 5 scripts with approve/reject/edit buttons (mirrors Telegram approval flow)
8. **Posts** — calendar view of scheduled and posted videos, performance per post
9. **Pattern library** — read-only view of pattern-library.md rendered as cards (Validated / Emerging / Retired sections)

### Settings (3 screens)
10. **Account settings** — billing, subscription tier, usage meter, team members
11. **Channel settings** — niche, tone, CTA, persona, schedules, integrations
12. **API & webhooks** — generate Lovable→n8n API tokens, view webhook logs

### Admin console (1 screen, owner role only)
13. **Admin** — tenant list, usage per tenant, manual workflow trigger, error log

**Total**: 13 screens.

### Primary user flow
1. New user lands on marketing site → "Start free trial"
2. Magic link login → onboarding wizard (5 min)
3. First Monday: system generates first 5 scripts → user gets email + dashboard notification
4. User reviews scripts in `Scripts` screen → approves → videos generate → posts ship
5. User checks `Posts` screen for performance, `Pattern library` for what's working
6. Weekly: 15 minutes total time in app

---

## b) AUTH + RBAC

### Magic link auth
- Email-only. No password.
- Powered by Supabase Auth (built-in passwordless).
- Magic link expires in 30 minutes.
- Session: 30-day refresh, 1-hour access token.

### RBAC matrix

| Permission | Owner | Admin | Editor | Viewer |
|------------|-------|-------|--------|--------|
| View dashboard | ✅ | ✅ | ✅ | ✅ |
| Approve/reject scripts | ✅ | ✅ | ✅ | ❌ |
| Edit scripts manually | ✅ | ✅ | ✅ | ❌ |
| View pattern library | ✅ | ✅ | ✅ | ✅ |
| Edit channel settings | ✅ | ✅ | ❌ | ❌ |
| Manage integrations | ✅ | ✅ | ❌ | ❌ |
| Manage billing | ✅ | ❌ | ❌ | ❌ |
| Invite team members | ✅ | ✅ | ❌ | ❌ |
| Delete account | ✅ | ❌ | ❌ | ❌ |

Default: first signup = owner. Invitees default to editor unless owner specifies.

---

## c) STRIPE + PRICING TIERS

### Tiers

| Tier | Price/mo | Videos/mo | Personas | Channels | Team seats | Analytics |
|------|----------|-----------|----------|----------|------------|-----------|
| Starter | €99 | 20 | 1 | 1 | 1 | Basic |
| Growth | €199 | 60 | 2 (A/B) | 1 | 3 | Advanced |
| Pro | €299 | 160 | Unlimited | 3 | Unlimited | Advanced + API access |

Annual discount: -20% (equivalent to 2 free months).

### Stripe webhook events to handle

| Event | Action |
|-------|--------|
| `customer.subscription.created` | INSERT into Supabase tenants + clients (active=true) |
| `customer.subscription.updated` | UPDATE tier, usage limits |
| `customer.subscription.deleted` | UPDATE clients.status=paused |
| `invoice.payment_failed` | Send dunning email + 7-day grace; after 7d UPDATE clients.status=paused |
| `invoice.paid` | UPDATE last_paid_at, reset usage counter for new billing cycle |

### Enforcement
- Usage counters incremented per workflow run (research, script_generation, video_generation, posts).
- When approaching limit (90%): email warning + dashboard banner.
- When hitting limit: pause future workflows for the cycle, dashboard prompt to upgrade.
- Override: owner can request 1 emergency video pack (1-click upgrade or one-off €25 for 5 videos).

### Subscription lifecycle hooks (clients.status)
- `active` — paid, in good standing, workflows running
- `paused` — payment failed or user-paused; workflows skip
- `churned` — cancelled, retained for 90 days for reactivation, then GDPR-deleted

---

## d) API ENDPOINTS (Lovable → n8n)

All endpoints require HMAC auth: `X-Hub-Signature-256: sha256={hex_hmac(N8N_SHARED_SECRET, body)}`.

| Method | Path | Payload | Response | Purpose |
|--------|------|---------|----------|---------|
| POST | `/webhook/typeform/onboard` | full client config | `{success: true, client_id}` | Initial provisioning |
| POST | `/webhook/research/start` | `{client_id, week_start}` | `{success: true, research_run_id}` | Trigger research run |
| POST | `/webhook/content/start` | `{client_id, week_start, research_run_id}` | `{success: true, script_batch_id}` | Trigger content generation |
| POST | `/webhook/approval/approve` | `{script_id}` or `{batch_id, action: "approve_all"}` | `{success: true}` | Approve scripts |
| POST | `/webhook/approval/reject` | `{batch_id, feedback}` | `{success: true, attempt: N}` | Reject and regenerate |
| POST | `/webhook/production/start` | `{client_id, week_start, script_ids}` | `{success: true}` | Trigger video generation |
| POST | `/webhook/distribution/start` | `{client_id, week_start}` | `{success: true}` | Trigger posting |
| POST | `/webhook/manychat/lead` | `{client_id, email, keyword, ...}` | ManyChat v2 response format | Lead capture |
| POST | `/webhook/gdpr/delete` | `{client_id, email}` | `{success: true, deleted_at}` | GDPR deletion |
| GET | `/webhook/health` | none | `{healthy: true, timestamp}` | Health check |

### Lovable-side reads (Supabase direct)
Lovable reads Supabase directly via Supabase JS client (RLS enforced):
- Scripts, posts, pattern_library entries, performance data, events log
- Tenant-scoped via RLS policy: `auth.uid() IN (SELECT user_id FROM users WHERE client_id = scripts.client_id)`

---

## e) DATA MODEL ADDITIONS FOR SAAS

Add these tables on top of existing schema (preserve all existing tables):

```sql
create table tenants (
  tenant_id text primary key,
  legal_name text not null,
  primary_owner_email text not null,
  stripe_customer_id text unique,
  stripe_subscription_id text unique,
  tier text not null default 'starter' check (tier in ('starter','growth','pro')),
  status text not null default 'active' check (status in ('active','paused','churned','trial')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table users (
  user_id uuid primary key references auth.users(id) on delete cascade,
  tenant_id text not null references tenants(tenant_id) on delete cascade,
  email text not null,
  role text not null default 'editor' check (role in ('owner','admin','editor','viewer')),
  created_at timestamptz not null default now()
);

create table integrations (
  integration_id bigserial primary key,
  tenant_id text not null references tenants(tenant_id) on delete cascade,
  client_id text references clients(client_id) on delete cascade,
  service text not null check (service in ('higgsfield','metricool','manychat','convertkit','beehiiv','tiktok')),
  encrypted_credentials text not null, -- AES-256 encrypted JSON, key stored in vault
  status text not null default 'active' check (status in ('active','expired','revoked')),
  last_validated_at timestamptz,
  created_at timestamptz not null default now()
);

create table usage_counters (
  counter_id bigserial primary key,
  tenant_id text not null references tenants(tenant_id) on delete cascade,
  client_id text not null references clients(client_id) on delete cascade,
  billing_cycle_start date not null,
  videos_generated int not null default 0,
  research_runs int not null default 0,
  posts_published int not null default 0,
  api_calls int not null default 0,
  unique (tenant_id, client_id, billing_cycle_start)
);

-- Add tenant_id to existing tables (nullable in DFY, NOT NULL after migration)
alter table clients add column tenant_id text references tenants(tenant_id);
```

### RLS policies for SaaS

```sql
-- Tenant-scoped read policies
create policy "tenant members can read their clients"
  on clients for select
  using (tenant_id in (select tenant_id from users where user_id = auth.uid()));

create policy "tenant members can read their scripts"
  on scripts for select
  using (client_id in (select client_id from clients where tenant_id in (select tenant_id from users where user_id = auth.uid())));

-- Repeat similar policies for: posts, content_insights, pattern_library entries, dm_leads, events, video_jobs

-- Write policies
create policy "owners and admins can update clients"
  on clients for update
  using (tenant_id in (select tenant_id from users where user_id = auth.uid() and role in ('owner','admin')));

-- ... etc
```

### Encryption for integrations.encrypted_credentials
- Use Supabase's `pgsodium` extension for column-level encryption, OR
- Use Infisical/Vault for centralized secrets and store only `vault_path` in this column (recommended for SaaS scale)

---

## f) ADMIN CONSOLE (Yohan-only, role=owner of master tenant)

### Tenant list view
- Table: tenant_id, legal_name, tier, status, MRR, users, last activity, error count
- Filters: status=active|paused, tier, error_count>0

### Tenant detail view
- All clients under tenant
- Usage metrics (current cycle): videos generated, research runs, posts, API calls
- Recent error log (events table filtered by tenant_id)
- Action buttons: pause workflows, manually trigger workflow, force script regeneration, send Telegram alert
- Webhook logs: last 100 webhook calls with response status

### Workflow override controls
- Manual "Run research now" button per client
- Manual "Re-generate scripts" button per week
- Manual "Re-queue stuck video" button
- Each override action: logs to events table with admin user_id

### Error log view
- All events with level=error|critical across all tenants
- Filters: workflow, client, time range, resolved status
- Bulk action: mark resolved

---

## g) DFY → SAAS MIGRATION STRATEGY

When SaaS launches, existing DFY clients migrate to SaaS accounts without disruption.

### Migration steps
1. Create a `tenants` row for each DFY client (1 tenant = 1 client initially)
2. Create a `users` row for the operator email with role=owner
3. Update `clients.tenant_id` to point to the new tenant
4. Send magic link to client email so they can claim the account
5. n8n workflows continue to run unchanged (they reference clients.client_id, not tenant_id)
6. Operator can decide: hand over the tenant fully (they take over via Lovable) OR continue managing as DFY service (operator logs in as admin to that tenant)

### Pricing migration
- DFY clients on €300-500/mo retainer get grandfathered to Growth tier (€199/mo) for 6 months as a thank-you
- After 6 months, they upgrade or cancel

### Risks during migration
- RLS policies must be tested with simulated multi-tenant load BEFORE migration (D13 GO/NO-GO criterion)
- TikTok OAuth tokens need to be re-validated under tenant context (per-integration check)
- ManyChat workspace IDs must be confirmed still active per client

---

## h) LOVABLE BUILD ORDER (when D13 passes)

Build in this order to keep complexity manageable:

1. **Auth + tenant model** (1 week) — magic link, RBAC, tenants/users tables
2. **Read-only dashboard** (1 week) — Home, Scripts, Posts, Pattern library — read from Supabase, no actions
3. **Approve/reject flow** (1 week) — wire approve/reject buttons to n8n webhooks
4. **Onboarding wizard** (1 week) — replace Typeform with in-app wizard
5. **Stripe billing** (1 week) — checkout + webhook handlers + tier enforcement
6. **Admin console** (1 week) — owner-only views and override actions
7. **Polish + bug fixes** (1 week)

**Total**: 7 weeks for one developer working full-time. Realistic with Lovable assist + Yohan reviewing daily.

---

## i) LOVABLE LIMITATIONS TO PLAN AROUND

- **Fix-break loops**: Decompose components to single-responsibility. Never ask Lovable to build a component that talks to >1 API endpoint.
- **Complex backend logic**: Keep all logic in n8n/Supabase. Lovable does UI + auth + Stripe only.
- **Real-time updates**: Use Supabase Realtime subscriptions for dashboard tiles. Lovable handles the subscription, not custom WebSocket.
- **File uploads**: For persona reference images during onboarding, upload directly from browser to Cloudflare R2 with presigned URLs (Lovable component).
