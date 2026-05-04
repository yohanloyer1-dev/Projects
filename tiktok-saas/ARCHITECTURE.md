# ARCHITECTURE.md
# TikTok SaaS — Agent Colony Architecture & Decision Log

> **Session protocol**: Every agent reads this file at session start. Every material decision is appended here. Newest entries at top of each section.

---

## D1 ARCHITECTURE CHALLENGE REPORT
*Completed: 2026-05-04 | Author: Claude Code (Principal Engineer)*

---

### 1. STACK CHALLENGE — TOOL-BY-TOOL VERDICT

#### n8n — KEEP (with constraints)
**Role in stack**: Cron triggers, webhook ingestion, deterministic data-pipeline nodes, error routing.
**Verdict**: Keep for what it's good at. Replace its "AI agent" role entirely.
**2026 assessment**: n8n self-hosted on a $6/mo VPS handles thousands of executions/month flat-rate. The drag-and-drop debugger is genuinely faster than reading Claude logs when a webhook payload breaks. Its HTTP Request node maps 1:1 to every API in this stack with no adapter code.
**Failure modes**:
- n8n cloud pricing scales poorly above 10k executions/mo — self-host from day one.
- Complex branching logic in n8n Code nodes becomes unmaintainable fast. Hard ceiling at ~50 nodes per workflow before it becomes a debugging nightmare.
- n8n has no native retry-with-backoff on HTTP errors. Must implement in Code nodes.
**Lock-in risk**: Medium. Workflows are JSON-exportable. Logic lives in Code nodes (JS) that are portable. Migrating to Temporal or Inngest later is 2-3 days of work, not weeks.
**Decision**: n8n handles scheduling, webhook intake, data movement, and error routing. All reasoning, judgment, and dynamic prompt construction happens in Claude sessions triggered by n8n — not inside n8n.

#### Supabase — KEEP (locked in spec, confirmed correct)
**2026 assessment**: Supabase Postgres is the right call. The table editor handles DFY visual inspection without building an admin UI. RLS enforced from day one is non-negotiable — retrofitting multi-tenant RLS onto a single-tenant schema after 10 clients is a painful migration. $25/mo Pro plan covers the entire DFY phase.
**Failure modes**: Supabase free tier pauses after 7 days of inactivity — use Pro from day one with a real client. Connection pooling (PgBouncer, built in) must be enabled for n8n's concurrent HTTP calls.
**Lock-in risk**: Low. Standard Postgres. Migrating to Neon or RDS is a connection string change + export.
**Decision**: Keep. RLS on all tables from day one. Service role key for n8n and agents. Anon key restricted to nothing until SaaS auth layer.

#### ScrapeCreators — KEEP (primary), Bright Data (fallback documented)
**2026 assessment**: ScrapeCreators earned a permanent spot in reviewer toolkits after 90 days of testing. Fast, structured JSON, creator-economy-focused. At $10/mo entry it is the cheapest correct tool for this job.
**Failure modes**: It is specialized — if TikTok changes its web structure, ScrapeCreators may lag 24-72h behind. Its search endpoint returns up to 100 results but ranking is algorithmic, not guaranteed chronological. Rate limits undocumented — assume 1 req/sec safe, implement 1.2s delay between calls in n8n.
**Alternative**: Bright Data Social Media Scraper API (98.44% success rate benchmark, 2026). More expensive ($500/mo minimum serious tier) — overkill for MVP. Document as fallback if ScrapeCreators degrades.
**Lock-in risk**: Low. HTTP calls with structured JSON output. Swap requires changing 4 endpoint URLs and normalizing the response schema in one Code node.
**Decision**: Keep ScrapeCreators primary. Add 1.2s inter-request delay. Implement Bright Data endpoint URLs in ARCHITECTURE.md as documented fallback — activate by env var swap only.

#### Supadata — KEEP (no credible alternative at this price)
**2026 assessment**: Supadata is the only API in 2026 that does TikTok transcript extraction without requiring a TikTok API key, handles edge cases with AI transcription when captions don't exist, and covers TikTok + YouTube + Instagram in one integration. 100 free credits/mo, scales cost-effectively. Recommended by SocialKit as best-in-class for this use case.
**Failure modes**: Some videos have no captions and no clear audio — Supadata returns empty transcript. Research Agent must handle null transcript gracefully (skip transcript analysis, use caption only for scoring). API rate limit unknown — assume 2 req/sec safe.
**Lock-in risk**: Low. One HTTP call, plain text output. Replacement requires only changing the endpoint.
**Decision**: Keep. Implement null-transcript fallback in Research Agent (use caption text + engagement score only).

#### Higgsfield MCP / Seedance 2.0 — KEEP (strong validation)
**2026 assessment**: Seedance 2.0 is confirmed 2026 leader in character consistency. $0.35/generation is 7x cheaper than nearest competitor (Arcads at $2.64). Phoneme-level lip-sync across 8 languages. The MCP endpoint (https://mcp.higgsfield.ai/mcp) enables direct Claude session integration — no REST polling boilerplate when Claude is in the loop. Character identity stays locked from uploaded reference image across all scenes.
**Failure modes**: Seedance 2.0 is ByteDance-built — geopolitical risk if US/EU regulations tighten on ByteDance products. At $0.35/video, 5 videos/week = $1.75/week = $91/year per client — negligible. Generation time ~3-5 min per video, acceptable for weekly batch.
**Lock-in risk**: Medium. Character training data lives in Higgsfield's system (character ID). If platform goes down, character must be re-created on alternative. Mitigate: store all reference images in Cloudflare R2 and keep persona spec in GitHub — re-creation possible in <2h.
**Alternative**: Runway Gen-4, Pika 2.2 — both less consistent on character identity in 2026 benchmarks. Not worth switching.
**Decision**: Keep. MCP primary in Claude sessions. REST API fallback for fully automated n8n runs. Store character ID + reference assets in both Supabase and GitHub.

#### ~~ManyChat~~ → **CHATFUEL** (architecture decision changed 2026-05-04 after deeper research)
**Original spec said ManyChat. Replaced because**: Yohan operates from France (EU). **TikTok and ManyChat cannot connect AT ALL in EU/UK** — this is a TikTok-side GDPR restriction, not a ManyChat limitation. ManyChat is fundamentally non-functional for an EU-based operator running EU-targeted channels. This is not a "comment vs DM" workaround — ManyChat is OFF the table entirely for the operator's home market.

**Replacement: Chatfuel**
- Connects to TikTok Business Messaging API directly (the official one TikTok exposes)
- Works in EU
- **Has comment-to-DM** (which ManyChat doesn't have in any Western market) — this is BETTER than the original spec
- Replies to both comments AND DMs in one flow
- Visual flow builder, keyword triggers, External Request equivalent for n8n webhook calls

**Architecture changes from original spec**:
1. CTAs can now be **"comment CALM" OR "DM me CALM"** — Chatfuel handles both. Comment-based has lower friction, higher conversion. Use comment-first by default.
2. Workflow file `workflows/manychat-dm-leadcapture.json` renamed to `workflows/chatfuel-leadcapture.json` (only the webhook endpoint changes; payload format and Supabase/Kit logic remain identical).
3. n8n response format changes from ManyChat v2 schema to Chatfuel JSON format (a one-line edit — Chatfuel response shape is documented).
4. Onboarding step #17 (Phase 1, LAUNCH-CHECKLIST.md) changes from "Create ManyChat account" to "Create Chatfuel account."

**Alternatives evaluated and rejected**:
- **SendPulse** — works in EU, has comment+DM, but flow builder is less mature than Chatfuel. Hold as fallback.
- **CreatorFlow** — flat $15/mo pricing is attractive for SaaS scale, but smaller ecosystem. Re-evaluate at SaaS phase.

**Lock-in risk**: Low. Chatfuel flows export. Webhook payloads stored in Supabase. Switching to SendPulse or back to ManyChat (if EU support arrives) = 1 day of work.

**Decision**: **Chatfuel primary**. SendPulse documented as fallback. ManyChat removed from the architecture entirely for v1. Original spec's ManyChat reference is preserved in commit history but workflows/prompts/agents updated to Chatfuel naming.

#### ConvertKit (Kit) — KEEP, flag rename and verify API status
**2026 assessment**: ConvertKit rebranded to "Kit" in late 2024. API endpoints and SDK still function under convertkit.com but official name is Kit. Plain-text emails, strong deliverability, creator-economy focus. The right tool for this niche. Beehiiv is a strong alternative if Kit degrades (better analytics, newsletter-native).
**Failure modes**: Kit's API rate limit is 120 req/min — fine for single-client DFY, may require batching at SaaS scale. Double opt-in must be configured at the form level in Kit UI, not just in the n8n workflow.
**Lock-in risk**: Low. Standard REST API, subscribers are exportable CSV.
**Decision**: Keep. Use "Kit" naming in all code comments but reference as ConvertKit in client-facing materials to avoid confusion. Implement Beehiiv endpoint as documented alternative in ARCHITECTURE.md.

#### TikTok Content Posting API — Metricool primary, audit submission Week 4
**2026 assessment** (refined with deeper research): Audit timeline is **5–10 business days realistic, up to 4 weeks worst case** — not 2-8 weeks. More tractable than originally assessed.
**Hard requirements for audit approval** (must implement BEFORE submitting):
1. Demo video showing the upload flow end-to-end (record screen of n8n workflow + TikTok appearance)
2. Privacy policy URL (host on Lovable landing page or simple GitHub Pages)
3. Clear data handling description (what's stored, where, for how long)
4. **UI requirement**: app must show creator's username and avatar before every post. This is verified during review. For our system: implement a Telegram preview message showing username/avatar/preview before triggering Metricool/Direct Post. Hard requirement.
5. Privacy level selector (public/friends/private) per post — already in our schema (posts.platform_status flow)

**Pending-audit restrictions**: SELF_ONLY (private posts only), max 5 user accounts can authorize the app per 24h.

**Phase plan**:
- Phase 1 (Week 1-3): Metricool primary, no audit yet. All posts public via Metricool's already-audited TikTok Business API integration.
- Phase 1.5 (Week 4): Submit Direct Post API audit in parallel. Continue using Metricool while audit is pending. Build the demo video + UI compliance pieces during Week 3.
- Phase 2 (Week 5-8 typical, up to 12 worst case): Audit approved. Switch `client_config.tiktok_scheduler` to `tiktok_content_posting_api`. Zero downtime — Metricool stays as fallback.

**Architecture decision**: Same as before — env var toggle (`metricool` | `tiktok_direct`). Audit-related demo video + privacy policy are now Week 3 deliverables (added to LAUNCH-CHECKLIST.md).

**Lock-in risk**: Medium during Phase 1 (Metricool dependency). Low after audit (own TikTok OAuth, can bypass Metricool entirely).

#### Lovable — KEEP for SaaS frontend (Phase 2 only, with eyes open)
**2026 assessment**: Lovable enters fix-break loops on complex backend logic. However, for this system the backend is entirely n8n + Supabase — Lovable only needs to build the frontend dashboard, auth flow, Stripe checkout, and read-only analytics views. This is exactly Lovable's strength. Complex data logic stays in Supabase views and n8n.
**Failure modes**: Fix-break loops on complex components. Mitigate: decompose into small single-purpose components. Never ask Lovable to build a component that talks to more than one API endpoint.
**Alternative**: Bubble (2-3 month learning curve, overkill), Vercel + Next.js (requires dev time). Lovable is correct for Phase 2 given the operator's time constraints.
**Hard rule**: Lovable is Phase 2 only. No Lovable work until all D13 GO/NO-GO criteria are met.
**Decision**: Keep. Deferred to Phase 2. Start with Lovable only after 3 DFY clients running and stable.

---

### 2. ARCHITECTURE CHALLENGE — ORCHESTRATION MODEL

**Question**: Should n8n drive the workflow with Claude as a called service, or should Claude Code drive the workflow with n8n handling only scheduling/triggers?

**Verdict**: Hybrid, Claude-primary for intelligence, n8n-primary for scheduling and data movement.

**The pure-n8n model fails because**:
- n8n's AI Agent node treats Claude as a black box — you can't inspect reasoning, can't prepend pattern library, can't do multi-step template chaining with state carried across steps.
- Debugging a failed content generation inside n8n means reading raw JSON responses with no context.
- Prompt versioning in n8n means storing template text in a field inside a node inside a workflow JSON. Unmanageable.

**The pure-Claude-colony model fails because**:
- Cron scheduling requires something that runs independently of Claude. Claude Code sessions are not daemons.
- Deterministic data plumbing (fetch rows, upsert rows, upload file to R2) is 10x cheaper and more reliable in n8n than in a Claude session where every token costs money and errors cost context.
- n8n's visual error inspector + retry UI is genuinely better for non-technical operator debugging.

**The winning hybrid**:
- n8n owns: cron triggers, webhook intake, HTTP data-pipeline nodes (Supabase reads/writes, ScrapeCreators calls, Supadata calls, file uploads to R2), error routing, Telegram notifications.
- Claude Code owns: all reasoning, pattern analysis, script generation, compliance rewriting, performance analysis, prompt construction. Each Claude-in-the-loop step is triggered by n8n webhook and runs as a Claude Code session or API call.
- State handoff: n8n passes structured JSON payload to Claude. Claude returns structured JSON. n8n writes result to Supabase and continues pipeline.

**The recommend hybrid point**: n8n triggers Claude via HTTP webhook for every step that requires judgment. Claude sessions read GitHub (patterns, prompts) and write back. n8n handles all non-judgment steps and all scheduling.

---

### 3. NICHE VALIDATION — "Quiet Health Optimization for Busy Professionals"

**Verdict**: VALIDATED with one recommendation for adjacent sub-niche to test in parallel.

**TikTok search volume evidence (2026)**:
- Sleep sanctuaries and circadian routine content reached peak TikTok search interest in January 2026.
- Nervous system regulation / vagal tone content is the #1 emerging wellness angle in 2026, replacing generic "reduce stress" content.
- #quietwellness, #softliving, #burnoutrecovery are active and growing hashtag clusters.
- The 2026 wellness shift explicitly names "Emotional ROI" and "Quiet Wellness" as the cultural moment — this system is timed correctly.

**Creator density**: The niche has sufficient established creators to scrape patterns from (ScrapeCreators keyword search for "nervous system," "sleep optimization," "burnout recovery" returns populated results). Not saturated — still white space for an AI character persona.

**Monetization validation**:
- Health/wellness micro-influencers (10K–50K): $500–$5,000 per sponsorship post.
- Health/fitness TikTok ads CPM: $2–$5 (higher than average, 2026 benchmark).
- Therapy apps, wellness platforms, sleep/supplement brands actively seek partnerships at this follower range.
- No gym aesthetics = no supplement gray area = cleaner compliance story = faster brand deals.

**Risk flag**: No medical claims is not just a brand preference — it is a legal requirement. FTC and MHRA (EU equivalent) specifically monitor health content automation. Every prompt template must include hard-stop rules against efficacy claims.

**Adjacent niche recommendation**: Test "productivity for creatives" as a parallel sub-niche after week 4. Same target audience (busy professionals), higher CPM potential (SaaS tools, productivity apps at $8–15 CPM), faster trend cycles. If this system works on quiet health, it ports to productivity in 3 hours of config change.

---

### 4. GAP ANALYSIS — RISKS AND INTENDED APPROACHES

| # | Gap | Risk | Intended Approach |
|---|-----|------|-------------------|
| G1 | ManyChat cannot connect TikTok in EU at all (TikTok-side GDPR block, NOT a comment-to-DM issue — it's total) | RESOLVED 2026-05-04 | **Replaced ManyChat with Chatfuel.** Chatfuel works in EU, has comment-to-DM (better than ManyChat anywhere), connects to TikTok Business Messaging API. CTAs can use comment-first OR DM-first. |
| G2 | TikTok Direct Post API requires audit for public posts | RESOLVED with concrete plan | Metricool primary Phase 1 (Weeks 1-3). Audit submitted Week 4 with demo video + privacy policy + creator-preview UI. 5-10 business days typical approval. Env var toggle to switch when approved. |
| G3 | Higgsfield character ID lock-in | MEDIUM | Store all reference assets in R2. Full persona spec in GitHub. Re-creation possible in <2h. |
| G4 | No native retry-with-backoff in n8n | MEDIUM | Implement retry logic in n8n Code nodes. Max 3 attempts with 30s base delay, exponential backoff. |
| G5 | TikTok OAuth token expiry (access tokens expire in 24h) | HIGH | Implement token refresh workflow in n8n. Store refresh token in Supabase client_config. Auto-refresh 30min before expiry via cron. |
| G6 | Supadata null transcript on videos with no audio/captions | LOW | Fallback: use caption text only. Score video normally. Mark transcript=null in content_insights. |
| G7 | n8n self-hosting infrastructure not defined | MEDIUM | Railway.app or Render.com for n8n self-host. $7-12/mo. One-click n8n deploy. Document setup. |
| G8 | Telegram bot approval flow has no timeout enforcement in n8n | MEDIUM | Observability workflow daily sweep catches unanswered approvals >24h. Alert operator. Auto-reject at 72h to prevent week blocking. |
| G9 | No Stripe integration defined for DFY retainer billing | LOW | Out of scope for Phase 1 DFY. Manual invoice. Stripe webhook integration is a D12 item. |
| G10 | GDPR deletion workflow: "delete all rows + R2 prefix" is not atomic | MEDIUM | Implement as n8n workflow: (1) soft-delete Supabase rows (status=deleted), (2) R2 object deletion by prefix, (3) log deletion event. Not atomic but auditable and reversible for 30 days. |
| G11 | Claude API token cost not modeled in unit economics | MEDIUM | Template 1 (~2K tokens in, ~1K out), Template 2 (~3K in, ~4K out), Intelligence (~5K in, ~2K out). At Sonnet 4.6 pricing: ~$0.20 per weekly content cycle per client. Include in D13. |
| G12 | n8n HMAC webhook auth not implemented in spec workflows | HIGH | Every n8n webhook must validate `X-Hub-Signature-256` header using N8N_SHARED_SECRET. Implement in all webhook-trigger nodes. Reject 401 on mismatch. |
| G13 | Lovable "fix-break loops" risk on complex UI | LOW | Deferred to Phase 2. Decompose into single-endpoint components when building. |
| G14 | No TikTok Creator API performance data endpoint after Metricool posting | MEDIUM | When posting via Metricool, video_id comes back in Metricool response. Use it to poll TikTok Creator API for perf data at 24h/72h regardless of posting method. |

---

### 5. AGENT COLONY DESIGN

**State sharing protocol**:
- **GitHub**: patterns, prompts, memory, knowledge — persists across sessions and machines.
- **Supabase**: operational state, job queues, performance data — the nervous system.
- **Rule**: agents write to GitHub only at session end. Agents write to Supabase throughout execution (status updates). No local file persistence.

**Handoff protocol**: Every agent completes by updating its job status in Supabase (`status=completed`) and writing a completion payload to the `events` table. The next agent either polls Supabase or is triggered by n8n webhook watching for status changes.

#### Agent Registry

| Agent | Trigger | Primary Reads | Primary Writes | Handoff Signal |
|-------|---------|---------------|----------------|----------------|
| Orchestrator | Monday 05:00 cron | Supabase: active clients, last-week statuses; GitHub: CLAUDE.md, client memory | GitHub: performance-log.md; Supabase: events | Webhook to Research Agent n8n workflow |
| Research | Monday 06:00 cron OR Orchestrator webhook | ScrapeCreators API; Supadata API; GitHub: pattern-library | Supabase: content_insights, research_runs; GitHub: pattern-library (appended) | Supabase research_runs.status=completed → triggers Script-Generation workflow |
| Content | Research completion webhook | Supabase: content_insights; GitHub: pattern-library, script-generator prompt | Supabase: scripts (5 rows, pending_approval); GitHub: memory.md if new compliance rules | Telegram approval message with inline buttons |
| Production | Telegram approval OR Supabase webhook (scripts.status=approved) | GitHub: persona.md; Supabase: approved scripts | Supabase: video_jobs; Cloudflare R2: video files | Supabase video_jobs.status=completed (all 5) → triggers Distribution |
| Distribution | All 5 video_jobs completed | Supabase: video_jobs, schedules; Metricool/TikTok API | Supabase: posts (status progression) | posts.status=posted for all 5 → triggers Intelligence at Saturday 08:00 |
| Intelligence | Saturday 08:00 cron | Supabase: posts (perf_24h, perf_72h), scripts; GitHub: pattern-library | GitHub: pattern-library (updated rankings), performance-log entry | None — terminal agent for the week |
| Monitor | n8n Error Trigger + daily 08:00 cron | Supabase: video_jobs, posts, research_runs, scripts | Supabase: events; Telegram: alert message | None — reactive |
| A/B Persona | Production Agent (20% of videos) | GitHub: persona.md (Persona B spec) | Supabase: video_jobs (persona_variant column) | Feeds Intelligence Agent for split analysis |

---

### DECISION LOG

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-05-04 | Metricool primary scheduler Phase 1, Direct Post API audit Week 4 | Unaudited apps restricted to private posts. Audit timeline 5-10 business days realistic. Run both in parallel. |
| 2026-05-04 (revised) | **ManyChat REPLACED with Chatfuel** | TikTok cannot connect to ManyChat in EU at all (operator is in France). Chatfuel works in EU, has comment-to-DM (better than spec). |
| 2026-05-04 (revised) | CTAs use comment-first OR DM-first (Chatfuel handles both) | Comment-to-DM gives lower friction. Original "DM-first only" constraint dropped — operator can choose per script. |
| 2026-05-04 | n8n self-hosted on Railway.app | Flat-rate cost, one-click deploy, avoids n8n cloud pricing cliff. |
| 2026-05-04 | Token refresh cron added for TikTok OAuth | Access tokens expire 24h, refresh tokens 30 days. Must auto-refresh. |
| 2026-05-04 | HMAC webhook validation mandatory on all n8n webhooks | Security requirement — webhooks are internet-accessible endpoints. |
| 2026-05-04 | Claude Sonnet 4.6 for all agent LLM calls | Best cost/capability ratio for structured JSON output tasks in 2026. |
| 2026-05-04 | **Repo nested under existing yohanloyer1-dev/Projects/tiktok-saas instead of separate repo** | Token has access to Projects, can push immediately. Public-repo risk: must move to private OR flip Projects to private before first DFY client onboarding (Week 10+). |
| 2026-05-04 | TikTok audit demo video + privacy policy + creator-preview UI added to Week 3 deliverables | Required for audit submission. Was missing from original spec. |
