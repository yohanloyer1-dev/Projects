# Nébuleuse Bijoux — Client Project File

**Last updated:** 2026-03-21
**Status:** Active — Phase 1 in progress, target April 30, 2026

---

## Client Overview

**Company:** Nébuleuse Bijoux
**Industry:** French jewelry e-commerce
**Platform:** Shopify
**Support tool:** Gorgias
**Human support:** Outsourced to One Pilot

**AI Agent name:** "L'assistant cosmique Nébuleux"

---

## Baseline Metrics (Audit)

| Metric | Value |
|--------|-------|
| Overall automation rate | 8.1% |
| Email automation rate | 18.1% |
| Coverage rate | ~44% |
| Tickets ignored by AI | 36.7% of email tickets |
| Unsuccessful → handover | 91% |
| **Target automation rate** | **50% by April 30, 2026** |

---

## Root Problem

AI Agent engages and responds well but **hands over instead of concluding**. The issue is not AI quality — it's configuration. The AI lacks the tools and instructions to close tickets independently.

---

## 3-Phase Optimization Plan

### Phase 1 — Quick Wins (Current)
1.1 Set up ignored tickets rules (prevent AI from touching tickets it can't handle)
1.2 Refine handover topics (reduce unnecessary transfers)
1.3 New guidances: Return/Status + Exchange/Status
1.4 WISMO fix (improve order tracking responses)
1.5 Deploy AI Agent to Chat

### Phase 2 — Structural (Next)
2.1 Baback integration (returns/refunds) — **#1 unlock: +45-52% automation**
2.2 Loyoly integration (loyalty points API)
2.3 Gorgias Flows deployment
2.4 Order Management activation

### Phase 3 — Optimization (Later)
- Performance analysis + iteration
- CSAT tracking
- Advanced personalization

---

## Key Integrations

| Integration | Purpose | Status |
|------------|---------|--------|
| **Baback** | Returns + refunds portal | Ready — checklist prepared, awaiting client |
| **Loyoly** | Loyalty program (points, tier, history) | Planned |
| **Shopify** | Order data | Connected |
| **One Pilot** | Human agent handover KB | Connected |

---

## Key URLs / Assets

- Return portal: nebuleusebijoux.com/a/return
- Warranty form: https://icvk1xljokz.typeform.com/to/ssHc7vn6
- Notion optimization page: (monitored Mon + Fri via scheduled task)

---

## Live Progress (from Notion, March 20, 2026)

- WISMO guidance: 79.1% resolution rate
- Baback integration checklist: ready to share with client
- Warranty guidance: improved
- Returns guidance: rewritten

---

## Project Files

All files at: `/Users/yohanloyer/Projects/Nébuleuse Bijoux/`

Key files:
- `nebuleuse_bijoux_ai_agent_audit.md` — full audit
- `OPTIMIZATION_EXECUTION_PLAN.md` — 3-phase plan detail
- `HANDOFF_BRIEF_nebuleuse.md` — handoff context
- `nebuleuse-ai-agent-report.v2.html` — visual report
- `rapport_nebuleuse_v6.md` — full French report
