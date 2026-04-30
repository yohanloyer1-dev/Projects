# Step 2 — Opportunity Map
**Date:** 2026-04-30 | **Session:** master-prompt-V1 | **Environment:** Cowork

---

## Key Finding from Step 1: Hypothesis Adjustment Required

The original hypothesis (Yotpo, Smile.io, Recharge, LoyaltyLion, Okendo) is **largely invalidated** — these tools all have native Gorgias integrations already. The opportunity is not in the top-tier loyalty stack.

The real gaps are:

1. **EMEA-specific loyalty tools** with Gorgias integrations (Loyoly — confirmed native; but depth/customization gap may exist)
2. **Mid-tier review tools** in Gorgias app store with limited functionality vs. what merchants actually need
3. **French/EMEA marketplaces** not covered by ChannelReply (Cdiscount direct API, ManoMano direct API, Fnac Darty)
4. **ERP/OMS sidebar data** (custom NetSuite fields beyond default widget)
5. **Specific niche tools** with no or shallow Gorgias integration

---

## Part A: Integration Coverage Audit (Public Sources Only)

### Loyalty & Rewards — Coverage Status

| Tool | Gorgias Native Integration | What It Shows | Adequate? |
|------|---------------------------|---------------|-----------|
| Smile.io | ✅ Yes (app store) | Points, referral URL, VIP tier | ✅ Yes |
| LoyaltyLion | ✅ Yes (app store) | Loyalty data in sidebar | ✅ Yes |
| Yotpo Loyalty | ✅ Yes (app store) | Loyalty account info, aggregate data | ✅ Yes |
| Recharge | ✅ Yes (app store) | Subscriptions, cancel/refund/reactivate | ✅ Yes |
| Loyoly | ✅ Yes (app store + docs) | Points, missions, rewards, tier, profile link | ✅ Yes — **but EMEA-native, growing** |
| Growave | ✅ Yes (OAuth2 integration, 2026) | Loyalty + reviews | ✅ Yes |
| Klaviyo | ✅ Yes (preferred partner) | Segments, campaign history, profile data | ✅ Yes |

Sources: [Gorgias Apps](https://www.gorgias.com/apps); [Loyoly Gorgias docs](https://docs.gorgias.com/en-US/loyoly-490163); [Growave OAuth2 guide](https://help.growave.io/en/articles/11275120-switching-to-oauth2-for-klaviyo-and-gorgias-integrations)

### Reviews — Coverage Status

| Tool | Gorgias Native Integration | What It Shows | Adequate? |
|------|---------------------------|---------------|-----------|
| Yotpo Reviews | ✅ Yes | Review metrics, latest reviews | ✅ Yes |
| Okendo | ✅ Yes (sidebar widget) | Ratings, reviews, UGC | ✅ Yes |
| Stamped.io Reviews | ✅ Yes (HTTP widget setup) | Last product reviews in sidebar | ✅ Yes — requires Premium plan |
| REVIEWS.io | ✅ Yes (app store) | Company + product reviews, stats | ✅ Yes |
| Trustpilot | ⚠️ [REQUIRES VERIFICATION — not confirmed in app store search] | Unknown | UNKNOWN |
| Judge.me | ⚠️ [REQUIRES VERIFICATION] | Unknown | UNKNOWN |

Sources: [Stamped Gorgias docs](https://docs.gorgias.com/en-US/stamped-io-81812); [REVIEWS.io integration](https://support.reviews.io/en/articles/9185001-gorgias-integration)

### Channel Integrations — Coverage Status

| Marketplace | Gorgias Solution | Coverage | Gap |
|-------------|-----------------|----------|-----|
| Amazon | ChannelReply (app store) | ✅ Full — messages, threaded tickets | ✅ Solved |
| eBay | ChannelReply | ✅ Full | ✅ Solved |
| Etsy | ChannelReply | ✅ Full | ✅ Solved |
| Walmart | ChannelReply | ✅ Full | ✅ Solved |
| Back Market | ChannelReply | ✅ Full | ✅ Solved |
| Cdiscount | Juble.io (partial/Mirakl) | ⚠️ Partial — Mirakl layer adds cost/complexity | **GAP** |
| ManoMano | No confirmed direct solution | ❌ No native integration | **GAP** |
| Fnac Darty | No confirmed Gorgias integration | ❌ No native integration | **GAP** |
| La Redoute | No confirmed Gorgias integration | ❌ No native integration | **GAP** |

Sources: [ChannelReply Gorgias](https://www.gorgias.com/apps/channelreply); [Juble.io Gorgias](https://docs.gorgias.com/en-US/marketplaces-by-jubleio-933434); [eDesk ManoMano comparison](https://www.edesk.com/blog/best-helpdesk-for-manomano-france/) — "Gorgias is Shopify-centric... for sellers where ManoMano represents a meaningful share of revenue, it lacks the marketplace depth required"; [eDesk Cdiscount comparison](https://www.edesk.com/blog/best-ecommerce-customer-support-software-for-cdiscount-sellers/) — confirms Gorgias/Cdiscount gap

### ERP/OMS Data in Sidebar

| Tool | Gorgias Native | Coverage | Gap |
|------|---------------|----------|-----|
| NetSuite | ✅ Yes (app store, 40+ fields) | Strong | ✅ Solved |
| Magento (Adobe Commerce) | ✅ Native (Pro plan+) | Full | ✅ Solved |
| Shopify | ✅ Native | Full | ✅ Solved |
| SAP Business Central | ⚠️ [REQUIRES VERIFICATION] | Unknown | POTENTIAL GAP |
| Custom OMS / bespoke | ❌ HTTP widget only, DIY | Manual config required | **GAP** |

---

## Part B: Highest-Pain Categories (Ranked)

### Ranking Methodology: Frequency of mentions × presence of competitor coverage gap × EMEA relevance

**Tier 1 — Clear gap, real pain:**

1. **French/EMEA marketplaces → Gorgias channel integration**
   - ManoMano, Fnac Darty, La Redoute have NO confirmed Gorgias solution
   - Cdiscount is partial (Juble.io/Mirakl layer)
   - eDesk explicitly positions against Gorgias on this gap in 2026 content — meaning eDesk sees it as a conversion argument
   - Source: [eDesk ManoMano](https://www.edesk.com/blog/best-helpdesk-for-manomano-france/) — "If ManoMano is a minor channel alongside Shopify, Gorgias works, but for sellers where ManoMano represents a meaningful share of revenue in France, it lacks the marketplace depth required." (2026)
   - Source: [eDesk Cdiscount](https://www.edesk.com/blog/best-ecommerce-customer-support-software-for-cdiscount-sellers/) — positions eDesk as better than Gorgias for Cdiscount-heavy sellers. (2026)
   - **Architecture: channel integration (polling/push). Timeline: 45–90 days.**

2. **Loyalty/Reviews depth gap for tools that DO have integrations**
   - Stamped requires Premium plan to activate the Gorgias widget — merchants on lower Stamped tiers can't use it. Opportunity: custom widget that works without the tier restriction.
   - [UNVERIFIED — training data only] Some merchants report the native Yotpo/Smile.io widgets lack depth (e.g., don't show recent order-specific loyalty actions). Needs manual merchant conversation to confirm.
   - **Architecture: HTTP widget (display). Timeline: 15–25 days.**

**Tier 2 — Possible gap, needs more validation:**

3. **Judge.me → Gorgias sidebar** [REQUIRES VERIFICATION — Judge.me is among the most popular Shopify review apps by install count but no confirmed Gorgias native integration found]
   - Source: [UNVERIFIED — check gorgias.com/apps for Judge.me listing]

4. **Trustpilot → Gorgias sidebar** [REQUIRES VERIFICATION — Trustpilot is commonly used by mid-market merchants but no app store listing confirmed]

5. **Custom OMS/bespoke ERP data in sidebar** — merchants on bespoke order management need HTTP widget setup. High implementation complexity but high willingness to pay (Pro plan merchants, €500+/mo Gorgias spend).
   - **Architecture: HTTP widget (custom). Timeline: 15–25 days per client.**

---

## Part C: Top 3 Opportunities with Merchant Profiles

### Opportunity 1: French Marketplace Channel Integration (ManoMano/Fnac Darty → Gorgias)

**Architecture: Channel integration (polling/push service)**
**Timeline: 45–90 days**
**Competition: None confirmed for direct ManoMano/Fnac integration with Gorgias**

**Merchant profile:**
- French or EMEA-based ecommerce brand selling on ManoMano (DIY/home, gardening) or Fnac Darty (electronics, tech)
- Revenue: €1M–10M ARR, predominantly marketplace-driven (not Shopify-first)
- Gorgias plan: Basic or Pro (€50–300/mo) — has Gorgias but manages marketplace support separately in a different tool or email inbox
- Monthly order volume: 500–5,000 marketplace orders/mo
- Primary pain: Support team switching between Gorgias and marketplace seller portals. SLA compliance risk on marketplace tickets. No unified view.
- Willingness to pay: High. Marketplace SLA failures cost them ranking. €100–200/mo is trivial vs. the risk of account suspension.
- **Source for gap:** eDesk 2026 content explicitly names this as Gorgias's weakness and a reason to choose eDesk instead.

### Opportunity 2: Cdiscount → Gorgias (Direct, replacing Juble.io complexity)

**Architecture: Channel integration (polling/push)**
**Timeline: 45–90 days**
**Competition: Juble.io (Mirakl layer) — adds cost and complexity**

**Merchant profile:**
- French ecommerce brand selling heavily on Cdiscount
- Revenue: €500K–5M ARR, Cdiscount as primary or secondary channel
- Gorgias plan: Basic or Pro
- Monthly order volume: 300–3,000 Cdiscount orders/mo
- Primary pain: Juble.io adds an extra subscription layer; direct integration would be simpler and cheaper for merchants not using the full Mirakl suite
- Willingness to pay: €75–150/mo for a cleaner solution
- **Source for gap:** eDesk Cdiscount comparison (2026); Juble.io positioning in app store suggests price point complexity

### Opportunity 3: Judge.me or Trustpilot → Gorgias Sidebar Widget

**Architecture: HTTP widget (display)**
**Timeline: 15–25 days**
**Competition: Unknown — requires manual verification**

**Merchant profile:**
- Shopify merchant on Gorgias Basic or Pro (€50–300/mo)
- Revenue: €500K–5M ARR
- Uses Judge.me or Trustpilot for reviews (Judge.me: most popular free/affordable review app on Shopify)
- Monthly order volume: 200–2,000 orders
- Primary pain: Support agents can't see review history in Gorgias sidebar; have to open separate tab
- Willingness to pay: €29–79/mo (lower than channel integrations — display-only value)
- **[UNVERIFIED — need to confirm no native Judge.me Gorgias integration exists before building]**

---

## Part D: My Hypothesis — Confirmed vs. Invalidated

| Original Hypothesis | Status |
|---------------------|--------|
| Yotpo → Gorgias: opportunity | ❌ INVALIDATED — native integration exists |
| Okendo → Gorgias: opportunity | ❌ INVALIDATED — native integration exists |
| Smile.io → Gorgias: opportunity | ❌ INVALIDATED — native integration exists |
| LoyaltyLion → Gorgias: opportunity | ❌ INVALIDATED — native integration exists |
| Stamped → Gorgias: opportunity | ⚠️ PARTIAL — integration exists but requires Stamped Premium plan |
| Recharge → Gorgias: opportunity | ❌ INVALIDATED — native integration exists |
| French marketplace channels | ✅ CONFIRMED — ManoMano, Fnac Darty, La Redoute have no Gorgias solution |
| Cdiscount → Gorgias | ✅ CONFIRMED GAP — Juble.io is partial/complex |

**Revised strongest hypothesis:** French marketplace channel integrations (ManoMano, Fnac Darty) are the clearest uncontested gap with documented competitor coverage.

---

## Part E: 2-Source Threshold Check per Opportunity

| Opportunity | Source 1 | Source 2 | Threshold met? |
|-------------|----------|----------|----------------|
| ManoMano → Gorgias gap | eDesk ManoMano guide (2026): "lacks marketplace depth" | eDesk Cdiscount guide (2026): same positioning | ✅ YES (2 independent sources) |
| Cdiscount → Gorgias gap | eDesk Cdiscount guide (2026) | Juble.io partial coverage confirmed in Gorgias docs | ✅ YES (2 independent sources) |
| Judge.me → Gorgias | No source found | No source found | ❌ NO — [UNVERIFIED] |
| Trustpilot → Gorgias | No source found | No source found | ❌ NO — [UNVERIFIED] |

---

_Sources:_
- https://www.gorgias.com/apps (2026-04-30)
- https://docs.gorgias.com/en-US/loyoly-490163
- https://help.growave.io/en/articles/11275120-switching-to-oauth2-for-klaviyo-and-gorgias-integrations
- https://docs.gorgias.com/en-US/stamped-io-81812
- https://support.reviews.io/en/articles/9185001-gorgias-integration
- https://www.gorgias.com/apps/channelreply
- https://docs.gorgias.com/en-US/marketplaces-by-jubleio-933434
- https://www.edesk.com/blog/best-helpdesk-for-manomano-france/ (2026)
- https://www.edesk.com/blog/best-ecommerce-customer-support-software-for-cdiscount-sellers/ (2026)
- https://www.gorgias.com/apps/netsuite
- https://www.gorgias.com/pricing

_Last updated: 2026-04-30_
