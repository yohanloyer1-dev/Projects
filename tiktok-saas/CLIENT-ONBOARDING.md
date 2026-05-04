# CLIENT ONBOARDING — D10
# Typeform → n8n → Supabase auto-provisioning + 12-step checklist + test protocol
# Last updated: 2026-05-04

---

## a) TYPEFORM FIELD SPEC

Build this Typeform at typeform.com → "New form." Use **hidden fields** (`?CLIENT_ID=c_001`) for system-generated IDs and **visible fields** for client input.

| # | Field name | Type | Validation | Required | Field ref (for n8n) |
|---|-----------|------|------------|----------|---------------------|
| 1 | CLIENT_ID | Hidden field | Regex `^c_[a-z0-9_]{2,20}$` | Yes | `client_id` |
| 2 | CLIENT_NAME | Short text | 2-50 chars | Yes | `client_name` |
| 3 | NICHE | Long text | 5-200 chars | Yes | `niche` |
| 4 | TARGET_AUDIENCE | Long text | 5-200 chars | Yes | `target_audience` |
| 5 | TONE_GUIDE | Long text | 5-300 chars | Yes | `tone_guide` |
| 6 | CTA_KEYWORD | Short text | 2-15 chars, alphanumeric | Yes | `cta_keyword` |
| 7 | TIMEZONE | Dropdown | One of: Europe/Paris, Europe/London, America/New_York, America/Los_Angeles, Asia/Singapore | Yes (default Europe/Paris) | `timezone` |
| 8 | FREE_RESOURCE_URL | Website | Valid HTTPS URL | Yes | `free_resource_url` |
| 9 | BRAND_TERMS_TO_AVOID | Long text | comma-separated list | No | `brand_terms` |
| 10 | DISCLAIMER_RULES | Long text | optional JSON | No | `disclaimer_rules` |
| 11 | TIKTOK_HANDLE | Short text | starts with @ | Yes | `tiktok_handle` |
| 12 | EMAIL_PROVIDER | Dropdown | ConvertKit, Beehiiv, Mailchimp | Yes (default ConvertKit) | `email_provider` |
| 13 | OPERATOR_EMAIL | Email | Valid email | Yes | `operator_email` |
| 14 | TELEGRAM_CHAT_ID | Short text | numeric | Yes | `telegram_chat_id` |
| 15 | METRICOOL_USER_ID | Short text | numeric | No | `metricool_user_id` |
| 16 | NOTES | Long text | optional | No | `notes` |

### Webhook configuration
Settings → Connect → Webhooks → Add webhook
- URL: `{N8N_URL}/webhook/typeform/onboard`
- Method: POST
- Send all fields

---

## b) FIELD MAPPING TABLE (Typeform → n8n → Supabase)

| Typeform field ref | n8n variable | Supabase column | Table |
|--------------------|--------------|-----------------|-------|
| `client_id` | `CLIENT_ID` | `client_id` | clients, client_config, schedules |
| `client_name` | `CLIENT_NAME` | `client_name` | clients |
| `niche` | `NICHE` | `niche` | client_config |
| `target_audience` | `TARGET_AUDIENCE` | `target_audience` | client_config |
| `tone_guide` | `TONE_GUIDE` | `tone_guide` | client_config |
| `cta_keyword` | `CTA_KEYWORD` | `cta_keyword` | client_config |
| `timezone` | `TIMEZONE` | `timezone` | clients, schedules |
| `free_resource_url` | `FREE_RESOURCE_URL` | `free_resource_url` | client_config |
| `brand_terms` | `BRAND_TERMS_TO_AVOID` (split on comma) | `brand_terms_to_avoid` | client_config |
| `disclaimer_rules` | `DISCLAIMER_RULES` (parsed JSON) | `disclaimer_rules` | client_config |
| `email_provider` | `EMAIL_PROVIDER` | `email_provider` | client_config |
| `metricool_user_id` | `METRICOOL_USER_ID` | `metricool_user_id` | client_config |
| `telegram_chat_id` | (env var per-client) | (operator-side, not stored) | n8n credential |

---

## c) 12-STEP AUTO-PROVISIONING CHECKLIST

After Typeform submission, the n8n `5a. Onboarding Provisioning` workflow runs. Each step has acceptance criteria.

| # | Step | Owner | Acceptance criteria |
|---|------|-------|---------------------|
| 1 | Typeform submission received | n8n | Webhook 200 returned, payload valid |
| 2 | Validate payload (CLIENT_ID regex, URL format, CTA_KEYWORD length) | n8n | All required fields pass; if not, events row + Telegram alert + 400 response |
| 3 | Upsert `clients` row | n8n | Row exists with status=active, timezone set |
| 4 | Upsert `client_config` row | n8n | Row exists with all niche/tone fields |
| 5 | Insert 5 `schedules` rows (Mon–Fri 08:30 local) | n8n | 5 rows in schedules table for this client |
| 6 | Insert `research_runs` row (status=queued, week_start = next Monday) | n8n | Row exists; first weekly run will pick it up |
| 7 | Send Telegram welcome message to operator | n8n | Message delivered confirming onboarding success |
| 8 | Operator manually creates Higgsfield character (per HIGGSFIELD-SETUP.md) | Operator | Character ID stored in client_config.higgsfield_character_id |
| 9 | Operator connects Chatfuel TikTok channel + configures keyword flow | Operator | Chatfuel workspace ID + flow live for CTA_KEYWORD |
| 10 | Operator sets up Kit (ConvertKit) form + tag + email sequence | Operator | Form ID + tag ID stored in client_config |
| 11 | Operator authenticates Metricool with TikTok account | Operator | Metricool user_id stored in client_config; test post succeeds |
| 12 | First test research run + script generation + Telegram approval | n8n + Operator | Approval message received within 90 minutes of Monday 06:00 cron |

**Estimated total time** (auto + manual): **75–90 minutes** to fully provision a new client end-to-end.

---

## d) TEST RUN PROTOCOL

After provisioning, run a manual test before the first scheduled cron. Use these checks:

### Pre-test
- [ ] Supabase: `clients`, `client_config`, `schedules`, `research_runs` rows exist for CLIENT_ID
- [ ] GitHub: `clients/{CLIENT_ID}/persona.md` written (post-Higgsfield setup)
- [ ] Higgsfield: `higgsfield_character_id` in client_config is non-null
- [ ] Chatfuel: keyword flow is live, External Request configured to n8n
- [ ] Kit: form ID and tag ID stored in client_config

### Trigger test research run
```bash
curl -X POST "{N8N_URL}/webhook/research/start" \
  -H "Content-Type: application/json" \
  -H "X-Hub-Signature-256: sha256=$(echo -n '{"client_id":"c_001","week_start":"2026-05-04"}' | openssl dgst -sha256 -hmac "$N8N_SHARED_SECRET" -hex | cut -d' ' -f2)" \
  -d '{"client_id":"c_001","week_start":"2026-05-04"}'
```

### Acceptance criteria
- [ ] Research run completes within 10 minutes
- [ ] Supabase: ≥20 `content_insights` rows inserted with score>0
- [ ] Supabase: ≥5 of those rows have `transcript IS NOT NULL` (Supadata worked)
- [ ] GitHub: `clients/{CLIENT_ID}/pattern-library.md` updated with new entry
- [ ] Content Agent triggered automatically: 5 `scripts` rows inserted with status=pending_approval
- [ ] Telegram approval message received (with all 5 scripts and inline buttons)
- [ ] Tap "Approve All" → 5 video_jobs created, status=in_progress
- [ ] First video completes within 8 minutes (MCP) or 12 minutes (REST fallback)
- [ ] R2: video file uploaded at `clients/{CLIENT_ID}/videos/{WEEK}/script_1/v1.mp4`
- [ ] Distribution Agent triggered: 5 `posts` rows inserted with planned_publish_at correct
- [ ] Metricool: post visible in scheduled queue
- [ ] Chatfuel webhook test: send DM with CTA_KEYWORD from a test TikTok account → check Supabase `dm_leads` row appears within 30s
- [ ] Kit: test subscriber appears in Kit form, double opt-in email sent

### If any check fails
- Insert events row level=critical, message=failed step
- Telegram alert with action item
- Block onboarding completion until resolved

---

## e) CLIENT WELCOME EMAIL TEMPLATE (plain text, sent by operator after onboarding)

```
Subject: welcome to your TikTok system

Hey {CLIENT_NAME},

Your TikTok content system is set up. Here's what to expect, what's already done, and what I need from you.

WHAT'S DONE
- Your channel persona is created (Higgsfield character ID locked).
- Research workflow is scheduled for every Monday at 06:00 local.
- Script generation runs Monday morning. You get a Telegram message with 5 scripts to approve.
- Once approved, videos generate by Tuesday morning. Posting starts Tuesday-Friday at 08:30.

WHAT YOU DO
1. Connect TikTok OAuth in Metricool (5 min, link: {METRICOOL_AUTH_LINK})
2. Confirm your Chatfuel channel is connected (5 min, link: {MANYCHAT_LINK})
3. Reply to me with your Telegram username so I can add you to the approval channel

TIMELINE
- Today: setup complete
- This Monday: first research run
- This Monday afternoon: I send you 5 scripts to review in Telegram
- Tuesday-Friday: 5 videos posted, leads start flowing
- Weekly: I review performance with you every Monday in a 30-min call

WHAT YOU DON'T NEED TO DO
- You don't write scripts.
- You don't appear in videos.
- You don't post manually.
- You don't manage DMs.

You review 5 scripts in Telegram once a week, that's it.

Reply with your Telegram username and any questions.

— Yohan
```

---

## f) TROUBLESHOOTING ONBOARDING

| Issue | Fix |
|-------|-----|
| Typeform webhook returns 400 | Check n8n executions log → validation error message → fix the failing field in Typeform |
| Supabase row insert fails | Check service key in n8n credentials; check RLS — service role should bypass |
| First research run returns <10 insights | Niche keywords may be too narrow; add 2-3 alternative search terms in client_config |
| Higgsfield character ID empty | Operator hasn't run HIGGSFIELD-SETUP.md yet — block onboarding completion until done |
| Chatfuel keyword doesn't fire | Check Chatfuel → Automation → Flow status = live; check keyword exact match settings |
| Telegram approval message doesn't arrive | Verify TELEGRAM_CHAT_ID in env vars; bot may not be in chat — `/start` in chat once |
