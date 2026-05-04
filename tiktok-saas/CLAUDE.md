# CLAUDE.md
# TikTok SaaS — System Overview & Session Protocol

> **Every agent reads this file at session start. Every agent writes to GitHub at session end.**

---

## SYSTEM IDENTITY

A productized done-for-you TikTok content automation system. Multi-agent Claude + n8n. Validated on one niche, sold as DFY service, scaled to SaaS.

**Current phase**: Phase 1 — DFY validation  
**Active niche**: Quiet health optimization for busy professionals  
**Active clients**: See Supabase `clients` table (status=active)  
**Stack**: Claude Sonnet 4.6 · n8n (self-hosted, Railway.app) · Supabase · ScrapeCreators · Supadata · Higgsfield Seedance 2.0 · Metricool (posting Phase 1) · Chatfuel (DM/comment automation — replaces ManyChat, EU-compatible) · Kit (ConvertKit) · Cloudflare R2 · GitHub  

---

## SESSION PROTOCOL

Every Claude Code session acting as an agent MUST:

1. **Read at session start**:
   - This file (CLAUDE.md)
   - ARCHITECTURE.md (decisions, gaps, stack choices)
   - `clients/{CLIENT_ID}/memory.md` (client-specific context)
   - Agent-specific instruction file from `/agents/{agent_name}.md`

2. **Write at session end**:
   - Commit any updated files to GitHub with a descriptive one-line message
   - Update relevant Supabase status rows to `completed` or `failed`
   - Append to `clients/{CLIENT_ID}/performance-log.md` if running Intelligence Agent

3. **Never**:
   - Overwrite existing prompt template versions — create v2, v3, etc.
   - Assume Supabase row state without reading it first
   - Write secrets or tokens to any GitHub file
   - Skip the GitHub write step even if session output is small

---

## AGENT COLONY OVERVIEW

| Agent | When | Purpose |
|-------|------|---------|
| Orchestrator | Mon 05:00 | Reads weekly state, delegates, collects signals |
| Research | Mon 06:00 | Scrapes top content, extracts transcripts, updates pattern library |
| Content | Mon 07:00 | Writes 5 scripts, sends Telegram approval checkpoint |
| Production | Post-approval | Generates videos via Higgsfield MCP or REST fallback |
| Distribution | Post-production | Schedules and posts via Metricool, polls TikTok for performance |
| Intelligence | Sat 08:00 | Analyzes what worked, updates pattern library rankings |
| Monitor | Daily 08:00 + errors | Silent when healthy, one Telegram message when not |
| A/B Persona | Post 30 days | Tests persona variant on 1 video/week |

---

## CRITICAL ARCHITECTURE DECISIONS (see ARCHITECTURE.md for full reasoning)

- **Posting**: Metricool primary (Phase 1, Weeks 1-3). TikTok Direct Post API audit submitted Week 4. Switch when approved (5-10 business days typical).
- **DM/Comment automation**: Chatfuel (replaces ManyChat — ManyChat doesn't work in EU at all). CTAs can be **comment-first OR DM-first** — Chatfuel handles both. Default: comment-first (lower friction).
- **Orchestration**: n8n for scheduling/triggers/data-movement. Claude for all reasoning/generation.
- **State**: GitHub = knowledge. Supabase = operational. Local files = temporary only.
- **Webhook security**: All n8n webhooks require HMAC validation (X-Hub-Signature-256).
- **LLM**: Claude Sonnet 4.6 for all agent API calls.
- **Character video**: Higgsfield Seedance 2.0, $0.35/generation. MCP in Claude sessions, REST fallback in automated n8n runs.

---

## PARAMETERIZED ENVIRONMENT

All secrets live in n8n credential store (global) or Supabase encrypted column (per-client). Never in code.

Key variables available to agents via Supabase `client_config` table:
- `niche`, `target_audience`, `tone_guide`, `cta_keyword`
- `brand_terms_to_avoid[]`, `disclaimer_rules` (jsonb)
- `free_resource_url`, `tiktok_scheduler` (default: metricool)
- `higgsfield_character_id`, `persona_ref_image_url`
- `convertkit_form_id`, `convertkit_tag_id`, `chatfuel_bot_id`

Key environment variables (n8n credential store):
- `SCRAPECREATORS_API_KEY`, `SUPADATA_API_KEY`, `HIGGSFIELD_API_KEY`
- `CLAUDE_API_KEY`, `METRICOOL_API_KEY`, `CHATFUEL_API_KEY`
- `SUPABASE_URL`, `SUPABASE_SERVICE_KEY`
- `CLOUDFLARE_R2_BUCKET`, `CLOUDFLARE_R2_ACCESS_KEY`, `CLOUDFLARE_R2_SECRET_KEY`
- `GITHUB_TOKEN`, `GITHUB_REPO` (yohanloyer1-dev/tiktok-saas), `GITHUB_OWNER`
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
- `N8N_SHARED_SECRET` (HMAC webhook validation)

---

## COMPLIANCE RULES (apply in every prompt)

1. No medical claims, diagnoses, treatment promises, or efficacy guarantees
2. No brand_terms_to_avoid (read from client_config)
3. Every script must include a compliance disclaimer_line
4. Health-safe framing only: "may support," "some people find," "research suggests" — never "will," "cures," "treats"
5. CTA can be comment-first OR DM-first (Chatfuel handles both). Default: comment-first.
6. GDPR: no personal data in GitHub. Email/contact data only in Supabase dm_leads with consent=true

---

## REPOSITORY STRUCTURE

```
/tiktok-saas/
  CLAUDE.md                         ← This file
  ARCHITECTURE.md                   ← Stack decisions, gap analysis, colony design
  /clients/
    {CLIENT_ID}/
      memory.md                     ← Client context, compliance rules, lessons
      persona.md                    ← Character spec, Higgsfield IDs, reference URLs
      pattern-library.md            ← Hook patterns ranked by performance
      performance-log.md            ← Weekly results, newest first
  /prompts/
    research-summary-v1.md          ← Template 1
    script-generator-v1.md          ← Template 2
    compliance-rewrite-v1.md        ← Template 3
    orchestrator-v1.md              ← Orchestrator instructions
  /workflows/
    supabase-schema.sql             ← Full DB schema
    onboarding-provisioning.json    ← n8n importable
    weekly-research.json
    script-generation.json
    video-generation-fallback.json
    scheduling-posting.json
    chatfuel-leadcapture.json
    observability.json
  /agents/
    orchestrator.md
    research.md
    content.md
    production.md
    distribution.md
    intelligence.md
    monitor.md
    ab-persona.md
```

---

## CURRENT WEEK STATUS

*Updated by Orchestrator Agent each Monday. Manual update format below.*

**Week of**: 2026-05-04  
**Phase**: D1–D14 initial build  
**Clients active**: 0 (c_001 being provisioned for self-validation)  
**Last Orchestrator run**: N/A  
**System health**: Initializing  
