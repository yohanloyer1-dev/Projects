# ADR-001: Do Not Build on ChannelEngine for Messaging — Phase Architecture Decision

**Date:** 2026-05-01  
**Status:** DECIDED  
**Decider:** Yohan Loyer  
**Environment:** Cowork (research) → to be implemented in Claude Code  

---

## Context

The original "Option 2" for the Gorgias Integrations venture was to build a single integration
on top of ChannelEngine (950+ marketplace connections) rather than integrating each marketplace
directly. The hypothesis: if ChannelEngine aggregates all marketplace data including support
messages, one Claude Code build covers the entire European marketplace universe.

Before committing engineering time, we ran a live API verification session.

---

## Decision

**We are NOT building on ChannelEngine for message routing.**

**Rationale:** ChannelEngine has zero messaging endpoints. This was verified by scraping the live
OpenAPI specification from `api.channelengine.net/api/swagger/` on 2026-05-01.

### Evidence [VERIFIED — live API, not documentation claims]

**Merchant API (83 endpoints):** Orders, shipments, returns, cancellations, refunds, products,
offers, stock, settlements, reports, webhooks, notifications, carriers, purchase orders.
No message/conversation/thread endpoints.

**Channel API (24 endpoints):** Price/stock submissions, order acknowledgment, shipping updates,
returns processing. No message/conversation/thread endpoints.

**The one apparent exception:** `/v2/orders/comment` — creates an internal merchant note on an
order. This is NOT a buyer-seller message. It does not send anything to the marketplace buyer.
It is a private operational annotation.

### How eDesk Actually Uses ChannelEngine

eDesk's help center lists ChannelEngine under its "Operations" category, not "Channels." eDesk
uses ChannelEngine to enrich tickets with order context (shipment status, product details) AFTER
messages have already been routed through eDesk's own direct marketplace connectors. ChannelEngine
is their OMS layer, not their messaging layer.

This debunks the hypothesis that eDesk's "250+ marketplace integrations" are powered by
ChannelEngine.

---

## Revised Architecture — Three-Phase Build

### Phase 1: ManoMano Direct (WEDGE — build now)
- **Scope:** ManoMano Partners API → Gorgias HTTP widget + channel integration
- **Why first:** Only competitor with native ManoMano support is eDesk (requires full helpdesk
  migration). Juble and ChannelReply both absent. Clear market gap with 24h SLA urgency.
- **API:** REST, public, documented on manomano.dev Postman workspace. Orders, offers, messaging.
- **Timeline:** ~4–6 weeks to MVP
- **Revenue model:** €149–299/mo per merchant (channel integration, usage-based)

### Phase 2: Mirakl API (PLATFORM PLAY — after Phase 1 validation)
- **Scope:** One Mirakl integration covers all Mirakl-powered marketplaces
- **Mirakl powers:** Fnac, Darty, Decathlon, Boulanger, Leroy Merlin, La Redoute, Cdiscount
  marketplace (separate from Cdiscount direct), 400+ marketplaces globally
- **Why Phase 2:** Juble already covers Mirakl — need to confirm their coverage gaps and whether
  Mirakl messaging API is sufficiently exposed. This is a platform play but NOT a clear gap yet.
- **GATE:** Must verify Mirakl API exposes buyer-seller messaging endpoints before committing
  (see Open Questions below)
- **Timeline:** 6–10 weeks after Phase 1 launch

### Phase 3: Direct integrations as demand warrants
- **Candidates:** Cdiscount direct (via Octopia API), Veepee (flash sales, different model),
  Amazon FR (existing ChannelReply coverage — lower priority)
- **Trigger:** Inbound merchant requests from Phase 1/2 users
- **Note:** Octopia messaging capability also unverified — same gate applies

---

## Open Questions (must resolve before Phase 2 commit)

| Question | Source to check | Priority |
|---|---|---|
| Does Mirakl API expose buyer-seller message threads? | developer.mirakl.com | CRITICAL |
| Does Octopia API expose buyer-seller message threads? | Octopia developer docs | HIGH |
| Does Veepee have a partner API at all? | veepee.fr/pro or partner portal | MEDIUM |
| What is Juble's actual Mirakl coverage depth? | juble.io feature list + test account | MEDIUM |

---

## What We Ruled Out

| Option | Verdict | Reason |
|---|---|---|
| Build on ChannelEngine | ❌ RULED OUT | Zero messaging endpoints, verified live |
| Build a full helpdesk (compete with eDesk) | ❌ OUT OF SCOPE | Violates ≤20h/week constraint |
| Buy/white-label Juble | ⚠️ EXPLORE IF PHASE 2 STALLS | Would need pricing negotiation |
| ChannelReply partnership | ❌ LOW VALUE | US-focused, no French marketplaces |

---

## Files Updated This Session

- `research/competitive-intelligence-2026-05-01.md` — Full competitor map
- `research/option2-channelengine-analysis-2026-05-01.md` — Live API verification detail
- `decisions/architecture-decision-channelengine-2026-05-01.md` — This file

---

*Decision verified by: live OpenAPI scrape 2026-05-01. Not based on marketing materials or
documentation claims — based on actual endpoint enumeration.*
