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

---

## Session 2026-05-01 — Competitive Intelligence + Architecture Decision

### Competitive Map [VERIFIED — live sources, 2026-05-01]

**Who covers ManoMano → Gorgias today:** Nobody. Clear gap confirmed.

| Competitor | ManoMano | Cdiscount | Amazon FR | Veepee | Gorgias native |
|---|---|---|---|---|---|
| Juble.io | ❌ | ❌ | ✅ | ❌ | ✅ |
| ChannelReply | ❌ | ❌ | ✅ | ❌ | ✅ |
| eDesk | ✅ | ✅ | ✅ | ✅ | ❌ (replaces Gorgias) |
| Our integration | ✅ (Phase 1) | Phase 3 | low priority | Phase 3 | ✅ |

**Juble.io:** $30/$60/$150/mo, message-based pricing, covers Mirakl/Amazon/eBay → Gorgias. Does NOT cover ManoMano or Veepee. Already has Gorgias integration.

**ChannelReply:** US-focused (Amazon, eBay, Walmart, Back Market, Etsy, Mirakl beta). No French marketplace coverage.

**eDesk:** Full helpdesk (requires merchants to abandon Gorgias). Native ManoMano, Cdiscount, Veepee, Fnac. Uses ChannelEngine for order enrichment (NOT for message routing).

### ADR-001: Do Not Build on ChannelEngine [DECIDED]

ChannelEngine (950+ marketplaces) was considered as "Option 2" — build once, cover all. **Ruled out.**

**Evidence:** Live OpenAPI scrape (api.channelengine.net/api/swagger/) confirmed zero message/conversation endpoints across all 107 endpoints (83 Merchant + 24 Channel). Only `/v2/orders/comment` exists — internal merchant note, not buyer-seller messaging.

**How eDesk actually uses it:** Order context enrichment AFTER their own direct connectors have routed messages. ChannelEngine is an OMS layer, not a messaging layer.

Full decision record: `decisions/architecture-decision-channelengine-2026-05-01.md`

### Revised Build Architecture

**Phase 1 (NOW):** ManoMano direct → Gorgias. No competitor. 24h SLA urgency for merchants. ~4–6 weeks.

**Phase 2 (after Phase 1 validation):** Mirakl API → Gorgias. One integration covers Fnac, Darty, Decathlon, Boulanger, Leroy Merlin, La Redoute, 400+ others. **GATE: must verify Mirakl exposes buyer-seller messaging endpoints (T-021).**

**Phase 3 (demand-driven):** Cdiscount via Octopia, Veepee direct. Both require API messaging verification first (T-022).

### Open Research Gates Before Phase 2 Commit
- **T-021** — Mirakl API messaging verification (CRITICAL — gates Phase 2)
- **T-022** — Octopia API messaging verification (HIGH — gates Cdiscount/Phase 3)

