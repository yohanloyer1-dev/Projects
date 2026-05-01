# Competitive Intelligence — ManoMano → Gorgias Integration Space
**Date:** 2026-05-01 | **Session:** Validation research | **Environment:** Cowork
**Status:** VERIFIED (all findings from live sources, scraped or search-confirmed)

---

## TL;DR

ManoMano → Gorgias gap is **real and unserved** by every Gorgias-compatible tool.
The closest competitor (eDesk) covers ManoMano but **requires leaving Gorgias entirely**.
Juble.io is the most structurally similar competitor — covers Gorgias + many marketplaces — but **does NOT support ManoMano**.
Speed to first customer is the only real moat. Juble could add ManoMano at any time.

---

## 1. Tools That Connect Marketplaces to Gorgias

### Juble.io [PRIMARY COMPETITOR]
- **What it is:** Middleware connecting marketplaces → any helpdesk (Gorgias, Zendesk, Freshdesk, Kustomer, etc.)
- **Gorgias support:** ✅ Native, listed on Gorgias app store
- **Pricing:** $30/mo (3 marketplaces, 200 msgs) · $60/mo (unlimited, 1,000 msgs) · $150/mo (4,000 msgs) — message-based
- **Supported marketplaces:** Amazon · eBay · Fnac/Darty · Mirakl · Miravia · Newegg · Octopia/Cdiscount · TikTok · Walmart
- **ManoMano:** ❌ NOT listed. Confirmed absent from channels page, FAQ, and homepage (live scrape 2026-05-01)
- **Veepee:** ❌ Not listed
- **Risk:** Already has Gorgias infrastructure. Could add ManoMano at any time.
- Source: https://juble.io/channels/ (live scrape)

### ChannelReply
- **What it is:** Marketplace → helpdesk connector (older, US-focused)
- **Gorgias support:** ✅ Native
- **Supported marketplaces:** Amazon · eBay · Walmart · Back Market · Etsy · Newegg · Mirakl (beta)
- **ManoMano:** ❌ Not supported
- **Cdiscount:** ❌ Not supported
- **Veepee:** ❌ Not supported
- **French marketplaces:** Blind spot. Explicitly noted they "don't support all marketplaces yet."
- Source: https://www.channelreply.com/integrations/gorgias

### eDesk [DIFFERENT BUYER — replaces Gorgias]
- **What it is:** Full helpdesk (NOT a connector — replaces Gorgias entirely)
- **Gorgias support:** ❌ Competes with Gorgias, does not integrate with it
- **Pricing:** $39–$119/agent/month
- **ManoMano:** ✅ Native
- **Cdiscount:** ✅ Native
- **Veepee:** ✅ Native
- **Fnac/Darty:** ✅ Native
- **200+ integrations total**
- **Our positioning vs eDesk:** "Stay on Gorgias. Don't migrate." Zero switching cost.
- Source: https://www.edesk.com/appstore/manomano/

---

## 2. Marketplace Coverage Matrix

| Connector | ManoMano | Cdiscount | Amazon FR | Veepee | Fnac/Darty | Works w/ Gorgias? |
|---|---|---|---|---|---|---|
| Juble.io | ❌ | ✅ (Octopia) | ✅ | ❌ | ✅ | ✅ Native |
| ChannelReply | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ Native |
| eDesk | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ Replaces Gorgias |
| **Our integration** | ✅ Target | ✅ Expansion | — | ✅ Possible | — | ✅ Built for it |

---

## 3. Marketplace Analysis

### Amazon France — ❌ SKIP
Gap doesn't exist. ChannelReply + Juble both cover it natively with Gorgias. No opportunity.

### Cdiscount — ⚠️ WEAKENED
Juble supports it via Octopia at $60/mo. Gorgias merchants wanting Cdiscount already have a solution.
Could compete on price, French-language support, or SLA tracking — but not a clean gap.

### ManoMano — ✅ PRIMARY WEDGE (confirmed)
No Juble, no ChannelReply, no native Gorgias connector. Only eDesk — which requires migrating helpdesks.
Gap is precise, real, and unserved. Validated by eDesk's own SEO content targeting this query.

### Veepee — ✅ SECONDARY OPPORTUNITY
No Gorgias-compatible connector exists. eDesk covers it but requires full migration.
Different seller profile (fashion/lifestyle, flash sales = volume spikes). Architecture question: 
per-message pricing painful for Veepee spikes — flat monthly may be better here.

---

## 4. Strategic Implications

### The real question before building:
Do we build a standalone connector (competing with Juble head-on on ManoMano),
OR become a **Juble reseller/agency partner** focused on French marketplaces — 
charging setup fees for configuration, letting Juble maintain the tech?

**Build:** Full moat if we get to market first. Risk: Juble adds ManoMano and gap closes.
**Partner:** Zero build time, immediate revenue, lower ceiling. But no proprietary asset.
**Hybrid:** Build ManoMano (Juble's gap), use Juble for all others (Cdiscount, Fnac, etc.)
→ This is likely the right answer. Gives us a unique connector + broad coverage via Juble.

### Speed is the only moat
Juble already has the Gorgias integration infrastructure. The barrier to them adding ManoMano
is low — it's just another API adapter on their existing platform. First-mover + agency relationships
are the defensible position, not the technology itself.

---

## 5. Open Research Questions [UNVERIFIED]
- How does eDesk achieve 200+ integrations? Built in-house or via aggregator/middleware layer?
- Is there a marketplace API aggregator (like a "Plaid for marketplaces") we could license?
- Juble's ManoMano roadmap — is it planned? (check their changelog/Twitter/ProductHunt)
- Cdiscount API accessibility vs ManoMano (T-008 equivalent needed)

---

_Last updated: 2026-05-01 | Source: Live web research, Cowork session_
