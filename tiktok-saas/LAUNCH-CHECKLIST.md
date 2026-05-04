# LAUNCH CHECKLIST — D14
# Every action to go live with the first DFY client (Yohan as c_001 for self-validation)
# Last updated: 2026-05-04

> Sort: dependency order. Each item: owner / estimated time / acceptance criteria / blocked by.

---

## PHASE 0 — INFRASTRUCTURE SETUP (Days 1-3)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 1 | Create GitHub repo `yohanloyer1-dev/tiktok-saas` (private) | You | 5 min | Repo exists, can push | — |
| 2 | Push initial scaffold (CLAUDE.md, ARCHITECTURE.md, all stubs) | Claude | 1 min | Repo has all D1-D14 files | #1 |
| 3 | Create Supabase project (Pro tier, EU region) | You | 10 min | Project URL + keys obtained | — |
| 4 | Run `workflows/supabase-schema.sql` in Supabase SQL Editor | You | 5 min | All tables exist, RLS enabled, test insert works | #3 |
| 5 | Verify Supabase service role key bypasses RLS | You | 5 min | `select * from clients` works with service key | #4 |
| 6 | Create Cloudflare R2 bucket `tiktok-saas-prod` | You | 10 min | Bucket created, S3-compatible credentials issued | — |
| 7 | Sign up for Railway.app, deploy n8n container | You | 15 min | n8n UI accessible at custom URL | — |
| 8 | Set n8n environment variables (see ENV section below) | You | 15 min | `$env.SUPABASE_URL` etc. resolves in n8n | #3, #6, #7 |
| 9 | Configure n8n Supabase credential (service key) | You | 5 min | Test query runs successfully | #5, #8 |
| 10 | Sign up for Telegram bot (BotFather) + create channel | You | 10 min | Bot token + chat ID stored in n8n env | #7 |

---

## PHASE 1 — EXTERNAL ACCOUNTS (Days 2-4, can parallelize with Phase 0)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 11 | Sign up for ScrapeCreators ($10/mo plan) | You | 5 min | API key in n8n env | — |
| 12 | Sign up for Supadata (100 free credits + paid plan if needed) | You | 5 min | API key in n8n env | — |
| 13 | Sign up for Higgsfield AI (paid plan with MCP + REST API) | You | 10 min | API key + MCP endpoint accessible | — |
| 14 | Get Anthropic API key (Claude API) | You | 5 min | Key in n8n env, test API call works | — |
| 15 | Sign up for Metricool (with TikTok integration) | You | 10 min | Account active, API key issued | — |
| 16 | Create TikTok Business account (or upgrade personal to Business) | You | 5 min | Account is Business tier | — |
| 17 | Create Chatfuel account, connect TikTok account | You | 15 min | TikTok channel connected in Chatfuel | #16 |
| 18 | Sign up for Kit (ConvertKit) Creator plan | You | 10 min | Account active, API key issued | — |
| 19 | Create Kit form for the niche + tag for `tiktok_lead` | You | 10 min | Form ID + tag ID stored | #18 |
| 20 | Configure Kit form for double opt-in (GDPR) | You | 5 min | Confirmation email triggers on signup | #19 |
| 21 | Create Typeform account, build onboarding form per CLIENT-ONBOARDING.md | You | 30 min | Form live with all fields, webhook configured | — |

---

## PHASE 2 — n8n WORKFLOW IMPORT (Day 4)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 22 | Import `workflows/onboarding-provisioning.json` into n8n | You | 5 min | Workflow visible, no validation errors | #9 |
| 23 | Import `workflows/weekly-research.json` | You | 5 min | Workflow visible | #9 |
| 24 | Import `workflows/script-generation.json` | You | 5 min | Workflow visible | #9 |
| 25 | Import `workflows/video-generation-fallback.json` | You | 5 min | Workflow visible | #9 |
| 26 | Import `workflows/scheduling-posting.json` | You | 5 min | Workflow visible | #9 |
| 27 | Import `workflows/manychat-dm-leadcapture.json` | You | 5 min | Workflow visible | #9 |
| 28 | Import `workflows/observability.json` | You | 5 min | Workflow visible, Error Trigger connected to other workflows | #9 |
| 29 | Activate all 7 workflows | You | 5 min | All show "Active" status | #22-#28 |
| 30 | Test webhook reachability: `curl POST {N8N_URL}/webhook/health` | You | 2 min | 200 response | #29 |

---

## PHASE 3 — HIGGSFIELD CHARACTER (Day 5)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 31 | Generate 3 reference photos in Midjourney for c_001 persona | You | 30 min | 3 photos saved, 9:16, character consistent across all 3 | — |
| 32 | Upload 3 reference photos to Cloudflare R2 | You | 10 min | URLs accessible publicly | #6, #31 |
| 33 | Run HIGGSFIELD-SETUP.md MCP session in Claude Code | You + Claude | 30 min | character_id obtained, 3 test videos generated | #13, #32 |
| 34 | Manual consistency review of 3 test videos | You | 15 min | All checks pass per HIGGSFIELD-SETUP.md section b step 4 | #33 |
| 35 | Write `clients/c_001/persona.md` per template | Claude | 10 min | File committed to GitHub with character ID + ref URLs | #33 |
| 36 | Update Supabase client_config with higgsfield_character_id + persona_ref_image_url | You | 5 min | Row updated, query returns the IDs | #33 |

---

## PHASE 4 — FIRST CLIENT PROVISIONING (Day 6) — c_001 (yourself)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 37 | Submit Typeform onboarding for c_001 | You | 10 min | All Phase 0-3 complete, fields filled | #21, #29 |
| 38 | Verify n8n executes onboarding-provisioning workflow successfully | You | 5 min | Supabase has clients + client_config + 5 schedules + 1 research_run row | #37 |
| 39 | Verify Telegram welcome message arrives | You | 1 min | Message in Telegram channel | #38 |
| 40 | Configure Chatfuel keyword flow for c_001 (CTA_KEYWORD) | You | 20 min | Test DM with keyword triggers flow | #17 |
| 41 | Configure Chatfuel External Request to n8n webhook | You | 10 min | URL + body match D9 spec | #29, #40 |
| 42 | Configure Kit (ConvertKit) automation: subscribe → send Day 0 email | You | 15 min | Test subscribe via API → email arrives | #19 |
| 43 | Connect Metricool to TikTok account for c_001 | You | 10 min | Metricool can see your TikTok profile | #15, #16 |
| 44 | Store metricool_user_id in Supabase client_config | You | 2 min | Field updated | #43 |

---

## PHASE 5 — TEST RUN (Day 7)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 45 | Manually trigger weekly-research workflow for c_001 | You | 1 min | n8n execution starts | #38 |
| 46 | Verify research run completes within 10 min | You | 10 min | Supabase: ≥20 content_insights rows + research_runs.status=completed | #45 |
| 47 | Verify pattern-library.md updated in GitHub | You | 2 min | New entry prepended | #46 |
| 48 | Verify content-generation triggered automatically | You | 1 min | n8n execution log shows webhook fired | #46 |
| 49 | Verify 5 scripts generated, status=pending_approval in Supabase | You | 5 min | 5 rows in scripts table | #48 |
| 50 | Verify Telegram approval message arrives with all 5 scripts | You | 2 min | Message visible with inline keyboard | #49 |
| 51 | Tap "Approve All" in Telegram | You | 1 min | scripts.status=approved, video-generation triggered | #50 |
| 52 | Verify first video generates successfully (MCP path) | You | 10 min | video_jobs[1].status=completed, R2 has the file | #36, #51 |
| 53 | Wait for all 5 videos to complete | You | 50 min | All 5 video_jobs.status=completed | #52 |
| 54 | Verify Distribution agent triggered, posts created in Metricool | You | 5 min | 5 posts visible in Metricool scheduled queue | #53, #43 |
| 55 | Wait for first scheduled post to publish (Tuesday 08:30) | n8n | varies | posts[1].platform_status=posted, video on TikTok | #54 |
| 56 | Test Chatfuel: DM the channel with CTA_KEYWORD from a separate account | You | 5 min | dm_leads row appears in Supabase within 30s | #41 |
| 57 | Verify Kit subscriber created from the DM test | You | 2 min | Subscriber visible in Kit dashboard | #56, #42 |
| 58 | Verify confirmation email arrives (Day 0 email) | You | 5 min | Email in test inbox | #57 |
| 59 | Wait 24h after first post → verify perf_24h captured | You | n/a | posts.perf_24h is populated | #55 |
| 60 | Wait 72h after first post → verify perf_72h captured | You | n/a | posts.perf_72h is populated | #59 |

---

## PHASE 6 — INTELLIGENCE CYCLE (Day 14, Saturday)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 61 | Verify Intelligence Agent runs Saturday 08:00 | n8n cron | n/a | Performance-log entry committed to GitHub | All Phase 5 |
| 62 | Manually review Intelligence output: top performer, pattern updates, recommendations | You | 15 min | Insights are accurate vs. real performance data | #61 |
| 63 | Verify pattern-library.md has new ✅ Validated entries based on top performer | You | 5 min | File updated, newest at top | #61 |

---

## PHASE 7 — SECOND WEEK STABILIZATION (Days 15-21)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 64 | Monday 06:00: Research workflow runs automatically | n8n | n/a | New research_runs row, 30 insights | All Phase 5+6 |
| 65 | Verify Content Agent uses pattern library from Week 1 | You | 5 min | Generated scripts reference validated patterns | #64 |
| 66 | Approve Week 2 scripts in Telegram | You | 5 min | All 5 approved | #65 |
| 67 | Monitor for any errors during Week 2 generation | You | n/a | Events table shows <2 warnings, 0 critical | #66 |
| 68 | Week 2 posts publish on schedule | n8n cron | n/a | 5 posts published Tuesday-Friday | #66 |

---

## PHASE 8 — FIRST DFY CLIENT (Days 30-45, after self-validation working)

| # | Action | Owner | Time | Acceptance criteria | Blocked by |
|---|--------|-------|------|---------------------|------------|
| 69 | Post first LinkedIn reveal post (Post 1 in SALES-FUNNEL.md) | You | 30 min | Posted on LinkedIn | All Phase 5+6+7 |
| 70 | Build Lovable landing page per SALES-FUNNEL.md spec | You | 4 hours | Page live, mobile-responsive | — |
| 71 | Build Typeform application form | You | 1 hour | Form live, webhook to email notifier | #70 |
| 72 | Wait for inbound applications | n/a | days | ≥3 qualified applicants | #69, #71 |
| 73 | Run qualification calls | You | 30 min × N | ≥1 qualified buyer | #72 |
| 74 | Onboard first DFY client (c_002) following CLIENT-ONBOARDING.md | You | 90 min | All Phase 4 steps repeated for new client | #73 |
| 75 | Document any onboarding friction → update CLIENT-ONBOARDING.md | You | 30 min | Doc updated, committed | #74 |

---

## ENV VARIABLES SUMMARY (configure in n8n)

```
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_SERVICE_KEY=eyJhbGc...
SUPABASE_ANON_KEY=eyJhbGc...
SCRAPECREATORS_API_KEY=sc_xxxxx
SUPADATA_API_KEY=sd_xxxxx
HIGGSFIELD_API_KEY=hf_xxxxx
CLAUDE_API_KEY=sk-ant-xxxxx
METRICOOL_API_KEY=mc_xxxxx
TIKTOK_ACCESS_TOKEN=  # populated via Metricool initially, after audit: TikTok OAuth
TIKTOK_REFRESH_TOKEN=
TIKTOK_OPEN_ID=
CHATFUEL_BOT_ID=
CHATFUEL_API_KEY=
EMAIL_PROVIDER_API_KEY=  # Kit API key
CLOUDFLARE_R2_BUCKET=tiktok-saas-prod
CLOUDFLARE_R2_ACCOUNT_ID=
CLOUDFLARE_R2_ACCESS_KEY=
CLOUDFLARE_R2_SECRET_KEY=
GITHUB_TOKEN=  # repo+gist scope
GITHUB_OWNER=yohanloyer1-dev
GITHUB_REPO=tiktok-saas
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
N8N_SHARED_SECRET=  # generate random 32-byte hex
N8N_URL=https://your-n8n.up.railway.app
```

---

## RISK TIMING NOTES

- **Higgsfield character setup (Phase 3)** is the critical-path blocker. If reference photos aren't right, character drift forces re-do. Budget 4 hours instead of 1 the first time.
- **TikTok Business account upgrade** can take 24h for approval. Start Phase 1 task #16 on Day 2 latest.
- **Kit double opt-in DNS configuration** (SPF/DKIM) takes 24-48h to propagate. Don't block Phase 4 on this; just plan for it.
- **First TikTok post via Metricool** may sit in "processing" state for up to 30 min. Don't panic; check Metricool dashboard.
- **TikTok Direct Post API audit** (post-MVP path) takes 2-8 weeks. Keep using Metricool until audit passes; don't switch on launch day.

---

## TOTAL TIME TO LAUNCH

- Solo operator (Yohan working part-time, ~3h/day): **7-10 calendar days** to first c_001 self-validation post
- After self-validation: **6-8 weeks of stable operation** before opening DFY waitlist
- First DFY client live: **~10 weeks** from Day 0
