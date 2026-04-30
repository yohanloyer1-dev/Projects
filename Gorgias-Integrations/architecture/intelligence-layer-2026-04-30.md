# Step 4 — Intelligence Layer Design
**Date:** 2026-04-30 | **Session:** master-prompt-V1 | **Environment:** Cowork (design) → Code (build)

---

## Overview

A lightweight research radar that surfaces demand signals, competitor moves, and API changes without requiring manual monitoring. Runs weekly, outputs to GitHub, resumes without conversation history.

**Design principle:** n8n handles scheduling and HTTP calls only. Claude (Cowork or Code) handles analysis and synthesis. Never assign LLM reasoning to n8n.

---

## Component 1: Reddit Monitoring

**Environment:** n8n (scheduling + retrieval) → Cowork (synthesis)
**Trigger:** Weekly, Mondays 08:00 CET

**n8n workflow:**
- Node type: n8n native Reddit node (OAuth2 — not scraping)
- Subreddits to monitor: r/ecommerce, r/shopify, r/FranceEcommerce, r/customerservice, r/smallbusiness
- Search terms: "Gorgias", "ManoMano support", "helpdesk marketplace France", "Cdiscount integration", "Gorgias integration missing"
- Output: raw post list (title, URL, upvotes, date, subreddit, comment count) saved to a temp JSON

**Claude synthesis step (Cowork session, triggered manually or by n8n webhook):**
- Claude reads the JSON, extracts posts with demand signal relevance (pain points, tool requests, competitor mentions)
- Writes summary to: `research/signals-[YYYY-MM-DD].md`

**GitHub output path:** `Gorgias-Integrations/research/signals-[date].md`
**How next session resumes:** Read the latest `research/signals-*.md` file — full context without conversation history.
**Success metric:** ≥1 actionable demand signal or competitor move captured per month.

**Gate:** Reddit OAuth2 credentials required. Set up in n8n credentials manager before activating. [Add to pre-launch-checklist.md]

---

## Component 2: G2/Capterra Review Monitoring

**Environment:** n8n (HTTP node + Firecrawl) → Cowork (synthesis)
**Trigger:** Bi-weekly, every other Monday

**n8n workflow:**
- Node type: HTTP Request node calling Firecrawl API (`/scrape` endpoint)
- URLs to monitor:
  - https://www.g2.com/products/gorgias/reviews (filter: most recent)
  - https://www.capterra.com/p/155357/Gorgias/reviews/
  - https://www.g2.com/products/channelreply/reviews (competitor)
  - https://www.g2.com/products/edesk/reviews (competitor)
- Firecrawl API key: store in n8n credentials (not in workflow JSON)
- Output: raw text of recent reviews (last 10 per platform) saved to JSON

**Claude synthesis step:**
- Extract: complaints about missing integrations, praise for specific integrations, competitor comparisons
- Writes to: `research/signals-[date].md` (appended to weekly signal file)

**GitHub output path:** `Gorgias-Integrations/research/signals-[date].md`
**Success metric:** Competitor weaknesses or merchant pain points identified from reviews monthly.

**Note:** Do NOT use n8n for this if Firecrawl API is unavailable. Fall back to: Yohan manually pastes recent G2/Capterra reviews into a Cowork session for synthesis.

---

## Component 3: API Doc Parsing (Gorgias + ManoMano)

**Environment:** Claude Code only (Firecrawl or Chrome MCP) — NOT n8n
**Trigger:** On-demand — run when Gorgias or ManoMano publish changelog updates

**Claude Code process:**
1. Fetch Gorgias developer changelog: https://developers.gorgias.com/changelog
2. Fetch ManoMano API docs: https://www.manomano.dev/
3. Diff against last-saved version in `architecture/api-snapshots/`
4. Flag: breaking changes, new endpoints, deprecations
5. Output: `architecture/api-snapshot-gorgias-[date].md` and `architecture/api-snapshot-manomano-[date].md`

**GitHub output path:** `Gorgias-Integrations/architecture/api-snapshots/`
**How next session resumes:** Read latest snapshot file — no conversation history needed.
**Success metric:** Breaking change detected within 7 days of publication.

---

## AGENT-TASKS.md Schema (Canonical Definition)

File location: `/Gorgias-Integrations/AGENT-TASKS.md`

**Columns:**

| Column | Type | Rules |
|--------|------|-------|
| Task ID | String (T-NNN) | Sequential, never reused |
| Task | String | Imperative verb, specific outcome |
| Owner | Enum: Cowork / Code / n8n / Yohan | Required |
| Status | Enum: todo / in-progress / blocked / done | Update immediately on change |
| Blocked by | Task ID or blank | Blocked tasks MUST name the blocking Task ID |
| GitHub output path | File path relative to repo root | Every task must produce a file |
| Success metric | String | Measurable, not vague |
| Last updated | YYYY-MM-DD | Update on every status change |

**Rules:**
- Every task has a success metric. "Done" is not a metric.
- Blocked tasks name the blocking Task ID explicitly.
- n8n tasks are scheduling/routing only — no LLM reasoning assigned to n8n.
- One-time tasks marked with `[one-time]` in task name. Recurring tasks marked with `[recurring]`.

---

_Last updated: 2026-04-30_
