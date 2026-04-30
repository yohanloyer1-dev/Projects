# AGENT-TASKS.md — Gorgias Integrations Venture

> Schema: Task ID | Task | Owner | Status | Blocked by | GitHub output path | Success metric | Last updated
> Owner: Cowork / Code / n8n / Yohan
> Status: todo / in-progress / blocked / done
> Blocked by: Task ID or blank

---

| Task ID | Task | Owner | Status | Blocked by | GitHub output path | Success metric | Last updated |
|---------|------|-------|--------|------------|-------------------|----------------|--------------|
| T-001 | [one-time] Initialize folder structure + base files | Cowork | done | — | Gorgias-Integrations/ (all subfolders) | All subfolders + checklist + decisions file in GitHub | 2026-04-30 |
| T-002 | [one-time] Step 1: Co-founder stress test | Cowork | done | T-001 | research/step1-challenge-2026-04-30.md | All 10 dimensions answered with cited sources | 2026-04-30 |
| T-003 | [one-time] Step 2: Opportunity map | Cowork | done | T-002 | research/step2-opportunity-map-2026-04-30.md | Top 3 opportunities ranked, 2-source threshold checked | 2026-04-30 |
| T-004 | [one-time] Step 3: Wedge + go/no-go decision | Cowork | done | T-003 | decisions/go-decision-2026-04-30.md | GO decision reached; all 4 criteria met | 2026-04-30 |
| T-005 | [one-time] Step 4: Intelligence layer design | Cowork | done | T-004 | architecture/intelligence-layer-2026-04-30.md | Reddit + G2/Capterra + API monitors designed | 2026-04-30 |
| T-006 | [one-time] Step 5: 90-day roadmap | Cowork | done | T-004 | roadmap/90-day-roadmap-2026-04-30.md | All 4 phases defined with environments, outputs, metrics | 2026-04-30 |
| T-007 | [one-time] Validation scripts (merchant + agency) | Cowork | done | T-004 | validation/validation-script-2026-04-30.md | 2 scripts (4–5 questions each) ready to use | 2026-04-30 |
| T-008 | [one-time] Confirm ManoMano API access + rate limits | Yohan | todo | — | — (paste into session for CTO Agent) | API access tier confirmed, rate limits known, ToS reviewed | 2026-04-30 |
| T-009 | [one-time] Confirm Gorgias ticket creation endpoint spec | Yohan | todo | — | — (paste into session for CTO Agent) | Endpoint spec confirmed from browser/Postman | 2026-04-30 |
| T-010 | [one-time] Run 5 validation conversations | Yohan | todo | T-007 | validation/validation-script-2026-04-30.md (update tracking table) | ≥3/5 confirm pain + WTP ≥€50/mo or agency fee ≥€500 | 2026-04-30 |
| T-011 | [one-time] ManoMano integration feasibility assessment | Code | blocked | T-008, T-009, T-010 | architecture/manomano-gorgias-feasibility-[date].md | Architecture confirmed, API endpoints mapped, build estimate validated | 2026-04-30 |
| T-012 | [one-time] Build ManoMano → Gorgias v1 | Code | blocked | T-011 | integrations/manomano-gorgias/ | 3 test merchants, ≥100 msg/mo, <30 min latency, 0 missed msgs over 7 days | 2026-04-30 |
| T-013 | [one-time] Agency agreement template | Cowork | blocked | T-010 | roadmap/agency-agreement-template-[date].md | Template covers: referral terms, margin structure, DPA obligations | 2026-04-30 |
| T-014 | [one-time] Ops cockpit v1 | Code | blocked | T-012 | Gorgias-Integrations/ops/cockpit.html | Live on GitHub Pages; shows MRR, active integrations, agency pipeline, research feed | 2026-04-30 |
| T-015 | [recurring] Weekly research signal scan | n8n + Cowork | todo | — | research/signals-[date].md | ≥1 actionable demand signal or competitor move per month | 2026-04-30 |
| T-016 | [one-time] Set up Reddit OAuth2 in n8n | Yohan | todo | — | — (n8n credentials setup) | Reddit node authenticated, test poll returning results | 2026-04-30 |
| T-017 | [one-time] Set up Firecrawl API key in n8n | Yohan | todo | — | — (n8n credentials setup) | G2/Capterra scrape returning review text in n8n | 2026-04-30 |
| T-018 | [one-time] Legal gates review | Yohan | in-progress | — | parking-lot/pre-launch-checklist.md (update) | All 5 legal gates in checklist marked done | 2026-04-30 |

---

**Blocked dependency chain:**
T-008 + T-009 + T-010 → T-011 → T-012 → T-014

**Immediate next actions for Yohan:**
1. T-010: Schedule 5 validation conversations (use scripts in validation/validation-script-2026-04-30.md)
2. T-008: Check ManoMano seller API access tier from your seller portal or manomano.dev
3. T-018: Contact employment lawyer re: IP/non-compete review

---

_Last updated: 2026-04-30 | Session: master-prompt-V1 kickoff_
