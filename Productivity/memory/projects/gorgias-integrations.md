# Project Memory: Gorgias Integrations Venture
**Last updated:** 2026-04-30 | **Status:** Active — validation phase

---

## What This Is
A paid integration layer between Gorgias and tools with no native connection.
Two delivery architectures: (1) HTTP widget for display integrations, (2) polling/push service for channel integrations.
Revenue: usage-based (per ticket routed) for channels, fixed monthly for display.
GTM: direct to merchants + Gorgias agencies as resellers.

**Strategic fit:** Active cash pillar. Core, not sandbox. Leverage (build once, sell many). No employment conflict.
**Locked goal:** €2K–5K MRR within 12 months, ≤20h/week to operate.

---

## Wedge Product: ManoMano → Gorgias Channel Integration
ManoMano is France's #2 marketplace (DIY/home improvement). No native Gorgias connector exists.
French merchants selling on ManoMano currently manage support in a separate seller portal — outside Gorgias.
Integration routes ManoMano buyer messages → Gorgias tickets automatically via polling/push service.

**GO decision made:** 2026-04-30. All 4 criteria met. Full rationale: `decisions/go-decision-2026-04-30.md`

---

## GitHub Location
All files under: `https://github.com/yohanloyer1-dev/Projects/tree/main/Gorgias-Integrations/`

| Folder | Contents |
|--------|----------|
| `research/` | step1-challenge, step2-opportunity-map |
| `decisions/` | go-decision, venture-decisions |
| `architecture/` | intelligence-layer design |
| `roadmap/` | 90-day-roadmap |
| `validation/` | validation scripts (merchant + agency) |
| `parking-lot/` | pre-launch-checklist (9 legal/compliance gates) |
| `AGENT-TASKS.md` | T-001 through T-018, full dependency chain |

---

## Current Status: Phase 1 — Validate the Wedge (Days 1–14)

### Completed (T-001 → T-007)
- Folder structure initialized
- Co-founder stress test passed
- Opportunity map: ManoMano ranked #1 of 3
- GO decision made
- Intelligence layer designed (Reddit + G2/Capterra monitors in n8n)
- 90-day roadmap built (4 phases)
- Validation scripts written (Script A: merchant, Script B: agency)

### Blocked on Yohan (T-008, T-009, T-010, T-018)
- **T-010** — Run 5 validation conversations (scripts ready). Pass threshold: ≥3/5 confirm pain + WTP ≥€50/mo
- **T-008** — Confirm ManoMano API access tier from seller portal (manomano.pro or manomano.dev)
- **T-009** — Confirm Gorgias ticket creation endpoint (browser/Postman)
- **T-018** — Contact employment lawyer: IP/non-compete review (non-blocking for validation, blocking for launch)

### Dependency Chain
T-008 + T-009 + T-010 → T-011 (feasibility, Claude Code) → T-012 (build) → T-014 (ops cockpit)

---

## Key Decisions Made
- Channel integration over display as wedge: higher switching cost, usage-based revenue, no native competitor
- ManoMano over Cdiscount: larger merchant base, worse support tooling, more accessible API
- Revenue model: usage-based per ticket routed (not flat monthly)
- Architecture: polling/push service (not HTTP widget)
- Next session type: Cowork (validation synthesis) once T-010 done; Claude Code (feasibility) once T-008+T-009 done

---

## Infrastructure Setup (2026-04-30)
- GitHub PAT stored at `~/Projects/.github-token` (token: "Cowork auto-push", repo+gist scope)
- Same token in dashboard localStorage as `yl_gist_token`
- Cowork can now push to GitHub autonomously via GitHub API

---

## Parking Lot / Legal Gates
9 gates tracked in `parking-lot/pre-launch-checklist.md`. All open. Key ones:
- IP assignment + non-compete review (French employment lawyer)
- GDPR/DPA template
- Gorgias trademark use clearance
- ManoMano ToS review (reselling API access)
- Tech partner program terms (no application until post-employment or explicit clearance)
