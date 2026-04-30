---
last_updated: 2026-04-30
session_type: cowork
status: active
---

# Venture Decisions — Gorgias Integrations

> This file captures decisions already made. Update as new decisions are locked in.
> Do not remove decisions — append with date and rationale.

---

## Architecture

**Decision: Dual delivery architecture**
- Display integrations (loyalty, reviews, subscriptions in Gorgias sidebar) → delivered as **Gorgias HTTP widget**: Gorgias calls the endpoint when an agent opens a ticket, endpoint returns data, renders in sidebar. No separate app install. Configured via Gorgias Settings. Target build time: 15–25 days.
- Channel integrations (marketplace messages → Gorgias tickets) → delivered as **polling/push service**: n8n or lightweight server polls marketplace API on schedule, creates Gorgias tickets via REST API. NOT an HTTP widget. Target build time: 45–90 days.
- The CTO Agent (Claude Code) must specify which architecture applies before any build begins.

**Decision: Revenue model**
- Display integrations: fixed monthly fee per merchant.
- Channel integrations: usage/ticket-based pricing.

---

## Go-To-Market

**Decision: Dual GTM channel**
1. Direct to merchants: monthly subscription, self-serve or agency-assisted onboarding.
2. Through Gorgias agencies: agencies charge clients a one-time implementation fee + earn recurring revenue by recommending/reselling — making building in-house economically irrational.
- Agency pricing placeholder (to validate): €500–2,000 one-time setup + €20–50/mo per merchant managed.

**Decision: Agency moat as primary distribution**
- Yohan's existing EMEA agency relationships are the primary GTM advantage.
- Agencies get revenue share / reseller margin to lock in referral behavior.

---

## Operations

**Decision: Notion as operational layer**
- Notion: pipeline, agency CRM, ideas in flight.
- GitHub: technical memory, all build outputs, research, architecture.
- Nothing lives only in a conversation.

**Decision: GitHub as source of truth**
- Repo: yohanloyer1-dev/Projects
- All outputs under /Gorgias-Integrations/ with subfolders: research/, architecture/, roadmap/, validation/, decisions/, parking-lot/, integrations/, agents/
- Date-prefixed filenames throughout.

**Decision: Ops cockpit scope**
- Static HTML dashboard at /Gorgias-Integrations/ops/cockpit.html, deployed via GitHub Pages.
- Shows: MRR by channel, active integrations, agency pipeline, weekly research output.
- Built by Claude Code. Enables ≤20h/week at scale.

---

## Constraints (non-negotiable)

- €2K–5K/mo MRR within 12 months
- ≤15–20h/week to operate once built
- Lean — no full team, automated wherever possible
- No internal Gorgias system access
- No tech partner program application until after employment ends or explicit written clearance
- Every output to GitHub immediately

---

## Open Questions (as of 2026-04-30)

- Go/no-go decision pending Step 3 of master prompt
- First integration not yet selected
- Agency partner pricing not validated
- Legal gates (IP, non-compete, GDPR, trademark) not yet cleared

---

_Init commit: 2026-04-30 | Session: master-prompt-V1 kickoff_
