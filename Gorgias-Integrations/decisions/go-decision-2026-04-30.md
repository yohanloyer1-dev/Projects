# Step 3 — Wedge Definition + Go/No-Go Decision
**Date:** 2026-04-30 | **Session:** master-prompt-V1 | **Environment:** Cowork

---

## Recommended First Integration: ManoMano → Gorgias Channel Integration

**Single best first integration:** ManoMano seller messages → Gorgias tickets (polling/push service)
**Architecture:** Channel integration (n8n polling ManoMano Partners API → Gorgias ticket creation via REST API)
**Timeline:** 45–90 days to v1

### Why ManoMano over Cdiscount or Fnac Darty

| Factor | ManoMano | Cdiscount | Fnac Darty |
|--------|----------|-----------|------------|
| API quality | ✅ Public REST API, documented (manomano.dev) | ⚠️ Mirakl layer — indirect | ✅ Mirakl-based API (documented) |
| Gap clarity | ✅ No Gorgias solution confirmed | ⚠️ Juble.io partial | ⚠️ No Gorgias solution but Mirakl/Juble may cover |
| Market size | ✅ Largest FR DIY marketplace | ✅ Broad GMV | ✅ Strong in electronics |
| eDesk positioning | ✅ Explicitly names Gorgias gap | ✅ Same | ✅ Same |
| Yohan's EMEA network relevance | ✅ EMEA agencies serve FR brands | ✅ | ✅ |
| Build risk | Lower — own API | Moderate | Moderate (Mirakl dependency) |

**Decision rationale:** ManoMano has its own documented REST API (not a Mirakl wrapper), making it the lowest-risk build. The gap is unambiguous. eDesk treats it as a conversion argument against Gorgias in 2026 content — meaning the pain is real and actively being sold against. France is Yohan's home market and EMEA network stronghold.

---

## Go Decision — 4 Criteria Checklist

### Criterion 1: Demand signal from ≥2 independent public sources ✅

**Source 1:** eDesk (2026) — "Which Helpdesk Is Best for ManoMano Sellers in France?" explicitly states: *"If ManoMano is a minor channel alongside Shopify, Gorgias works, but for sellers where ManoMano represents a meaningful share of revenue in France, it lacks the marketplace depth required."*
URL: https://www.edesk.com/blog/best-helpdesk-for-manomano-france/ (2026)

**Source 2:** eDesk (2026) — "Best Customer Service Platform for eCommerce in France" positions Gorgias as weak for multi-marketplace French sellers and positions eDesk's native ManoMano integration as a differentiator.
URL: https://www.edesk.com/blog/best-customer-service-platform-ecommerce-france/ (2026)

**Additional supporting signal:** ManoMano deprecated their XML Orders API in March 2025, requiring all sellers to migrate to the new REST API — indicating active platform investment and a growing seller base that now needs updated tooling.
URL: https://help.lengow.com/hc/en-us/articles/8697042853660 (Dec 2024)

→ **CRITERION 1: PASS**

---

### Criterion 2: No existing solution adequately solves this for Gorgias merchants ✅

- ChannelReply: covers Amazon, eBay, Etsy, Walmart, Back Market — **not ManoMano**
- Juble.io: Mirakl connector — covers Cdiscount via Mirakl but **ManoMano runs its own API (not Mirakl)**, so Juble.io does not cover ManoMano
- No other app found in the Gorgias app store for ManoMano specifically
- Source: Gorgias app store (verified 2026-04-30) — no ManoMano listing found

→ **CRITERION 2: PASS**

---

### Criterion 3: Technical feasibility within 45–90 days ✅

**ManoMano Partners API:**
- Public REST API at manomano.dev — documented, accessible
- Supports: orders, messages, order status updates
- Architecture: n8n polls ManoMano Messages API on a schedule (e.g., every 5 min) → for each new message, creates a Gorgias ticket via POST /tickets → subsequent seller replies update the same ticket thread
- Source: https://www.manomano.dev/ (public); https://www.postman.com/security-operator-73995327/xsellco/documentation/zrf5k2n/manomano-partners-api (Postman docs)

**Risk:** API access tier and rate limits not confirmed — **[Gate: Yohan must confirm ManoMano seller API access level before build begins — T-008 equivalent]**

**Gorgias ticket creation:** Well-documented REST API. No blocker. Source: https://developers.gorgias.com/docs

**Build estimate:** 45–60 days for v1 (n8n workflow + Gorgias ticket creation + basic message threading). 90 days for production-ready with error handling, retry logic, and a simple merchant config UI.

→ **CRITERION 3: PASS** (conditional on API access confirmation)

---

### Criterion 4: Realistic path to €2,000 MRR within 12 months ✅

**Pricing model:** Usage-based — €0.08–0.12 per ManoMano ticket created in Gorgias. Minimum fee: €49/mo.

**Direct channel math:**
- Average French mid-market ManoMano seller: ~500–2,000 messages/mo
- At €0.10/ticket × 1,000 tickets/mo = €100/mo per merchant
- To reach €2,000 MRR: **20 direct merchants**
- Timeline: 3 merchants in months 1–3 (validation), 10 by month 6 (agency activation), 20 by month 10

**Agency channel math (separate):**
- 3 Gorgias agencies in EMEA, each managing 5 French merchant clients on ManoMano
- Setup fee: €800/agency × 3 = €2,400 one-time
- Recurring: 15 merchants × €80/mo = €1,200/mo MRR from agency channel alone
- Combined direct + agency at month 10: 8 direct + 15 agency-managed = 23 merchants → **€2,070–2,760 MRR** depending on volume

**€2K MRR path: viable by month 10 with 3 agency activations + 8 direct merchants.**

→ **CRITERION 4: PASS**

---

## ✅ GO DECISION: All 4 criteria met. Proceed to build.

**Caveat:** One conditional gate — ManoMano API access level must be confirmed before Claude Code begins build (T-008).

---

## First 3 Merchant Customer Types

### Merchant Type 1: French Mid-Market DIY/Home Brand (Highest WTP)
- **Gorgias plan:** Pro (€300/mo) — high ticket volume, needs automation
- **Monthly order volume:** 1,000–5,000 ManoMano orders/mo
- **Platform:** Shopify (primary DTC) + ManoMano (secondary, 20–40% of revenue)
- **Why highest WTP:** Marketplace SLA compliance is existential — late responses risk ranking drops or account suspension. €100–200/mo is a rounding error vs. the risk.

### Merchant Type 2: Multi-Channel EMEA Brand (ManoMano + Amazon)
- **Gorgias plan:** Pro or Advanced (€300–750/mo)
- **Monthly order volume:** 3,000–10,000 orders total across channels
- **Platform:** Shopify + ManoMano + Amazon (using ChannelReply for Amazon)
- **Why high WTP:** Already paying for ChannelReply; understand integration value; will pay for ManoMano parity. €100/mo is obvious spend.

### Merchant Type 3: French Niche Specialist (ManoMano-Primary)
- **Gorgias plan:** Basic (€50/mo) — smaller but price-sensitive
- **Monthly order volume:** 200–800 ManoMano orders/mo
- **Platform:** WooCommerce or Shopify + ManoMano as primary channel
- **Why still valuable:** There are hundreds of these. €49/mo minimum is affordable; low support burden per merchant for you.

---

## First 2 Agency Partner Profiles

### Agency Profile 1: Gorgias-Specialist Implementation Agency (Primary Target)
- **Typical client size:** 10–50 merchants per agency, mostly SMB/mid-market French brands
- **Implementation vs. strategy:** 70% implementation (Gorgias onboarding, automations, integrations), 30% ongoing advisory
- **What makes them more money recommending you than building themselves:**
  - They do 2–4 Gorgias implementations per month. Adding your ManoMano integration to every French client is a €800–1,200 upsell with zero build work on their side.
  - At 4 implementations/mo × €1,000 setup = €4,000/mo in added revenue from your product alone.
  - Building themselves: €15,000+ dev cost, ongoing maintenance, support burden. Never rational at their scale.
  - Arrangement: agency earns 30% of first-year MRR per merchant they bring + one-time setup margin.

### Agency Profile 2: eCommerce Growth Agency (Broader Scope)
- **Typical client size:** 5–20 merchants, mid-market focus (€2M–20M ARR brands)
- **Implementation vs. strategy:** 40% implementation, 60% strategic advisory (CX, automation, retention)
- **What makes them more money recommending you:**
  - They advise clients on tech stack, not just build. Recommending your integration = they look current + competent on EMEA marketplace tooling.
  - Revenue arrangement: finder's fee (€200–500 per activated merchant) or ongoing revenue share (€15–25/mo per merchant they manage).
  - At 10 managed merchants: €150–250/mo passive income from their existing clients. Pure margin.

---

## Pivot Notes (if validation fails)

If 5 validation conversations (3 merchants + 2 agencies) reveal:
- Low WTP (merchants won't pay >€29/mo) → pivot to display widget (Judge.me or Trustpilot sidebar) with lower price/lower build cost
- ManoMano API access restricted → pivot to Cdiscount via direct Cdiscount API or La Redoute API
- Agency resistance → pivot to pure direct merchant, skip agency channel for v1

---

_Sources:_
- https://www.edesk.com/blog/best-helpdesk-for-manomano-france/ (2026)
- https://www.edesk.com/blog/best-customer-service-platform-ecommerce-france/ (2026)
- https://help.lengow.com/hc/en-us/articles/8697042853660 (Dec 2024)
- https://www.manomano.dev/ (public API documentation)
- https://www.postman.com/security-operator-73995327/xsellco/documentation/zrf5k2n/manomano-partners-api
- https://developers.gorgias.com/docs
- https://www.gorgias.com/apps (app store verification, 2026-04-30)

_Last updated: 2026-04-30_
