# Option 2 Deep-Dive: ChannelEngine → Gorgias Architecture
**Date:** 2026-05-01 | **Environment:** Cowork | **Status:** Research complete — decision required

---

## The Core Question
Does ChannelEngine pass customer support *messages* (buyer→seller conversations) through its API,
or only orders/inventory/shipments? If messages don't flow, Option 2 (build on ChannelEngine) 
won't solve the Gorgias ticket creation problem.

---

## What the API Actually Shows [VERIFIED — live OpenAPI spec]

ChannelEngine has two public APIs. Scraped live from api.channelengine.net/api/swagger/:

### Merchant API — 83 endpoints
Covers: orders, shipments, returns, cancellations, refunds, products, offers, stock, 
settlements, reports, webhooks, notifications, carriers, purchase orders.

**Messaging endpoints: ZERO.**
No `/messages`, no `/conversations`, no `/tickets`, no `/chat`.
The only remotely related endpoint: `/v2/orders/comment` — updates an *internal merchant note* 
on an order. That is NOT a buyer-seller message.

### Channel API — 24 endpoints  
Covers: orders, shipments, cancellations, returns, refunds, products, reports.

**Messaging endpoints: ZERO.**

### Schema scan for message-related data structures
Found: `ProductMessage` (product validation errors), `ValidationMessage`, `ReturnSupport` 
(return handling config), `SupportOrderAddress` (test order address).

**No buyer message schema. No conversation schema. No ticket schema.**

---

## The Contradiction — How Does eDesk Do It?

eDesk's docs say: *"Connecting your ChannelEngine account will allow your messages, orders 
and tracking information to flow directly into eDesk."*

But the ChannelEngine API has no messaging endpoints.

**Resolution: eDesk is almost certainly NOT routing marketplace messages through ChannelEngine.**

What's actually happening is one of two things:

**Theory A — ChannelEngine is purely an order data enrichment layer for eDesk.**
eDesk connects to each marketplace's messaging API *directly* (just like it does for ManoMano, 
Cdiscount, etc.) but uses ChannelEngine as a *data enrichment source* — pulling order context, 
tracking, product info — to attach to tickets that were already created from direct marketplace 
message connections. The "messages" in eDesk's copy refers to messages eDesk receives directly 
from marketplace APIs, enriched with ChannelEngine order data.

**Theory B — ChannelEngine has a private/undocumented messaging layer.**
Some marketplace integrations (particularly for marketplaces with no public messaging API) 
may use email forwarding or webhook-based message relay that isn't exposed in the public 
OpenAPI spec. Possible but unlikely given the complete absence from all schemas.

**Evidence for Theory A:**
- eDesk lists ChannelEngine under "Operations" category in their UI, not "Marketplaces"
- eDesk has *separate, direct* ManoMano, Cdiscount, Veepee, Fnac marketplace connections
  (each has its own setup guide — not routed through ChannelEngine)
- ChannelEngine's own feature page mentions zero messaging functionality
- ChannelEngine's partner page with eDesk focuses on "order data" and "SLA management"
- The 83-endpoint API is entirely operations-focused: zero messaging surface area

**Conclusion: Theory A is almost certainly correct.**
ChannelEngine ≠ a messaging aggregator. It is an order/inventory aggregator.
eDesk built its 250+ marketplace integrations the hard way — direct API connections to each 
marketplace's messaging system — and uses ChannelEngine only for operational data enrichment.

---

## What This Means for Option 2

### Option 2 as originally conceived: DOES NOT EXIST
"Connect to ChannelEngine once → get 950 marketplace message channels" is not how it works.
ChannelEngine doesn't carry messages. The shortcut doesn't exist.

### The revised Option 2: ChannelEngine as Order Context Layer Only
A hybrid architecture IS possible and valuable:
- Connect directly to ManoMano messaging API → create Gorgias ticket (the core integration)
- Use ChannelEngine (if merchant already has it) to pull rich order context into that ticket
- This is additive, not foundational — ChannelEngine would be an optional enrichment, not the base

This is actually what eDesk does. The difference: eDesk is a helpdesk, we're building a connector 
for Gorgias. We'd need to build the ManoMano direct messaging connection regardless.

---

## The Real "Option 2" — What Does Exist?

If we want "build once, cover many marketplaces," the real question is: 
**is there a messaging aggregator (not order aggregator) that covers French marketplaces?**

### Mirakl — The Closest Real Option
Mirakl is a marketplace-as-a-service platform. It powers Fnac, Darty, Decathlon, Boulanger, 
Leroy Merlin, La Redoute, and 400+ other marketplaces globally.

**Key insight:** Mirakl has a standardized API across ALL marketplaces it powers.
If Mirakl's API includes buyer-seller messaging (to verify), then one Mirakl integration 
covers ALL Mirakl-powered marketplaces simultaneously. Juble already does this — 
their "Mirakl" channel covers all Mirakl marketplaces in one connection.

**Marketplaces this would unlock (French focus):**
- Fnac / Darty ✅
- Decathlon marketplace ✅  
- Boulanger ✅
- Leroy Merlin marketplace ✅
- La Redoute ✅
- And 400+ others globally

**This is the real Option 2: Build ManoMano (direct, our wedge) + Mirakl (one integration, 
covers all Mirakl-powered FR marketplaces). Two connections = most of the French market covered.**

### Octopia (Cdiscount's platform)
Octopia is Cdiscount's marketplace technology, also licensed to other retailers.
Juble uses it. One Octopia integration = Cdiscount + any Octopia-powered marketplace.
Needs verification: does Octopia API expose messaging?

---

## Revised Architecture Recommendation

### Phase 1 — Wedge (build direct, ~4-6 weeks)
ManoMano → Gorgias: direct integration via ManoMano Partners API
- Poll ManoMano messaging API → create Gorgias ticket → sync replies
- Unique gap, no competitor serves this in the Gorgias ecosystem
- This is the revenue wedge and the proof of concept

### Phase 2 — Platform play (build once, cover many)
Mirakl → Gorgias: one integration covering 400+ marketplaces including all major French ones
- Validate that Mirakl API exposes buyer-seller messages (high probability — it's their core product)
- This is the architecture that makes us defensible vs Juble (they have it, we'd match + add ManoMano)
- Juble's entire Fnac/Fnac Darty/Decathlon coverage comes from this single Mirakl connection

### Phase 3 — Long tail
Octopia (Cdiscount), Veepee direct API, others as demand warrants

### What NOT to build on
- ChannelEngine: order/inventory only, not messaging — use as optional data enrichment if merchants 
  already have it, but do not depend on it architecturally
- API2Cart: covers ecommerce platforms (Shopify, WooCommerce) not marketplace messaging
- Generic middleware (Zapier, n8n): not reliable for production SLA-sensitive message routing

---

## Open Verification Tasks
1. **Mirakl messaging API** — Does Mirakl's standard API expose buyer-seller message threads?
   Check: developer.mirakl.com — look for /messages or /conversations endpoints
2. **Octopia messaging API** — Same question for Cdiscount's platform
3. **ManoMano messaging API** — Confirm the Partners API (manomano.dev) exposes messages, 
   not just orders (T-008 — Yohan to verify from seller account)

---

## Strategic Verdict on Option 2

| Option | Viable? | Why |
|--------|---------|-----|
| ChannelEngine as message aggregator | ❌ No | No messaging in their API — orders only |
| ChannelEngine as order context enrichment | ✅ Yes (additive) | Use alongside direct integrations |
| Mirakl as message aggregator | ✅ Likely | Standardized API across 400+ marketplaces — verify |
| Octopia as message aggregator | ✅ Likely | Powers Cdiscount + others — verify |
| Build direct per marketplace | ✅ Yes (slow) | Proven model, higher maintenance |

**Recommended architecture: Direct ManoMano (Phase 1) + Mirakl integration (Phase 2).**
This is not "one API covers everything" — but it's "two APIs cover most of what matters in France."

---

_Last updated: 2026-05-01 | Verified: ChannelEngine OpenAPI spec scraped live_
