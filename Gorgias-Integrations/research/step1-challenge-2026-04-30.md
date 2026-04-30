# Step 1 — Co-Founder Stress Test
**Date:** 2026-04-30 | **Session:** master-prompt-V1 | **Environment:** Cowork

---

## 1. MOAT: Could Gorgias build this natively?

**Short answer: Yes, for the highest-demand tools. No, for the long tail. Window: 12–24 months.**

**Evidence:**
- Gorgias already has native sidebar integrations with Yotpo (Reviews + Loyalty), Smile.io, LoyaltyLion, Recharge, Okendo, and Klaviyo — the most-requested loyalty/reviews/subscription tools by volume.
  - Source: [Gorgias App Store](https://www.gorgias.com/apps) (verified 2026-04-30); [Yotpo Gorgias integration guide](https://support.yotpo.com/docs/gorgias-integration-guide-for-reviews-and-loyalty-referrals); [Okendo sidebar widget setup](https://support.okendo.io/en/articles/5899793-setting-up-the-okendo-sidebar-widget-in-gorgias)
- For channel integrations: ChannelReply already handles Amazon, eBay, Etsy, Walmart, Back Market, Newegg via the Gorgias app store. Source: [ChannelReply × Gorgias](https://www.gorgias.com/apps/channelreply) (verified 2026-04-30)
- French marketplaces (Cdiscount, ManoMano, Fnac Darty) are **partially** addressed via Juble.io (Mirakl connector in Gorgias app store) but competitors like eDesk are actively targeting this gap. Source: [Marketplaces by Juble.io](https://docs.gorgias.com/en-US/marketplaces-by-jubleio-933434); [eDesk ManoMano comparison](https://www.edesk.com/blog/best-helpdesk-for-manomano-france/) (2026)
- Gorgias has a tech partner team of 6 people managing 75+ integrations. They do build natively for high-volume tools but rely on the app marketplace for the long tail.
  - Source: [Crossbeam case study on Gorgias tech partner program](https://www.crossbeam.com/case-study/how-to-increase-your-tech-partner-programs-revenue-by-30-and-be-a-joy-to-work-with)

**Conclusion:** The top 10–15 tools already have native solutions. The moat lives in: (a) tools with smaller TAMs that Gorgias won't prioritize, (b) tools that haven't invested in partnership, (c) French/EMEA-specific tools outside Shopify-first coverage, (d) any tool category where merchants need a *customized* widget beyond what the native integration shows.

**Window:** If you target an uncovered tool today, Gorgias could build it within 6–18 months if it gets enough merchant requests. The business model must not depend on being first forever — it must create switching costs before Gorgias catches up.

---

## 2. COMPETITION: Does anything already adequately solve this?

### What exists today:

| Solution | Coverage | Gap |
|----------|----------|-----|
| **Gorgias App Store native** | Yotpo, Smile.io, LoyaltyLion, Recharge, Okendo, Klaviyo | Already solved for these tools |
| **ChannelReply** | Amazon, eBay, Etsy, Walmart, Back Market, Newegg → Gorgias tickets | Already solved for English-language marketplaces |
| **Juble.io** | Mirakl + Cdiscount (partial) → Gorgias | Exists but narrow; ManoMano/Fnac incomplete |
| **Alloy Automation** | Broad ecommerce automation | Developer/builder tool, not merchant-facing sidebar widget |
| **Zapier** | Generic workflow automation | No Gorgias sidebar widget delivery; workflow-only |
| **Truto / Merge.dev** | Unified API layer | B2B SaaS developer tools; not Gorgias-specific widget delivery |
| **Composio (Gorgias MCP)** | MCP connector for Gorgias API | Agent/developer tooling; not display widgets |

**Key finding:** The "adequately solved" bar is already HIGH for the main loyalty/reviews/subscription tools. The real opportunity is the **second and third tier**: tools like Stamped, Loyoly (EMEA), Okendo (depth beyond basic widget), custom ERP/OMS data, and EMEA-specific marketplaces not covered by ChannelReply.

**Stamped:** No confirmed native Gorgias integration found in search results. [REQUIRES MANUAL VERIFICATION — check gorgias.com/apps directly]

**Cdiscount/ManoMano direct API → Gorgias (without Juble.io middleware):** No dedicated solution found. Source: [eDesk Cdiscount analysis](https://www.edesk.com/blog/best-ecommerce-customer-support-software-for-cdiscount-sellers/); [eDesk ManoMano analysis](https://www.edesk.com/blog/best-helpdesk-for-manomano-france/) — both confirm Gorgias lacks native depth for these.

---

## 3. TAM: The Math

### Direct merchant channel

Gorgias has 15,000+ merchants as of 2024 (source: [Sacra Gorgias profile](https://sacra.com/c/gorgias/)). Realistically addressable = merchants on Starter/Basic/Pro plans who use at least one tool you support AND don't already have a native integration. Rough estimate: 2,000–4,000 merchants in your first 2 integration categories.

| Price/mo | Merchants to hit €2K MRR | Merchants to hit €5K MRR |
|----------|--------------------------|--------------------------|
| €50/mo | 40 | 100 |
| €100/mo | 20 | 50 |
| €200/mo | 10 | 25 |

**Verdict:** At €50/mo, 40 merchants is achievable but hard solo without automation. At €100–200/mo, 10–25 merchants is very achievable — especially via agency channel where each agency manages multiple merchants.

### Agency channel math (separate)

If 5 agencies each manage 10 merchants on your integration:
- Setup fees: 5 agencies × €1,000 one-time = €5,000 one-time
- Recurring: 50 merchants × €50/mo = €2,500/mo MRR from day one at scale

If 3 agencies at 5 merchants each, you hit €750/mo recurring — still a foundation. The setup fee recovers build cost fast.

**Verdict:** Agency channel is the faster path to €2K MRR with fewer direct relationships to manage.

---

## 4. REVENUE MODEL: Should you charge merchants, agencies, or both?

**Comparable tools:**
- Alloy Automation, Truto, Merge.dev — charge **developers/builders** (SaaS companies embedding integrations), not end merchants.
- ChannelReply — charges **merchants directly** ($49–$149/mo tiers). Source: [ChannelReply × Gorgias page](https://www.channelreply.com/integrations/gorgias)
- Juble.io — charges merchants directly (Gorgias app store listing).

**Channel conflict risk:** If you charge both agencies AND merchants, agencies will resent the direct sales motion once they've sent you 10 merchants. Structure clearly from the start: agency pricing = wholesale rate + implementation fee they pocket. Direct merchant pricing = standard rate. Never compete with agencies on price.

**Recommendation:** Primary = agency-assisted merchant subscription (agencies white-label or co-sell, merchants pay you directly, agencies earn implementation margin). Secondary = pure direct for merchants who discover you via search or Gorgias community.

---

## 5. AGENCY MOAT: What stops an agency from building this themselves?

**At what size does in-house become rational?**
- A Gorgias agency managing 50+ merchants on a single integration type could justify a €10K–20K one-time build (amortized = ~€20–40/mo/merchant over 24 months).
- At 20 merchants: buying from you at €50/mo = €1,000/mo = €12,000/yr. Build cost €15,000. Break-even at ~15 months. Marginal to build.
- At 10 merchants: buying at €50/mo = €500/mo. Building never makes sense.

**How to stay ahead of the threshold:**
1. Continuous improvement (version updates, new tool support, bug fixes) — agencies don't want ops overhead.
2. Multi-integration value: once you cover 3+ tools in one dashboard, build cost multiplies; your subscription is cheap by comparison.
3. Support + SLA: agencies can't provide 24/7 support for custom integrations they built. You can.
4. Network effects: your widget improves for all merchants; their build only improves if they invest.

**The real moat:** Not technical. It's the combination of (a) being already live with no friction, (b) covering enough tools that replacing you requires replacing multiple integrations, and (c) agencies earning more money recommending you than building themselves.

---

## 6. EMPLOYMENT + IP RISK: What a lawyer must verify

**Specific items for legal review (France / international employment law):**
1. Does Yohan's Gorgias employment contract contain an IP assignment clause covering side projects in adjacent domains? (Many French CDI contracts include this for "activités connexes.")
2. Does the non-compete (if any) cover SaaS/integration tooling for ecommerce helpdesks specifically, or only direct Gorgias competitors?
3. Is building a Gorgias integration layer "direct competition" under French law — even if Gorgias doesn't have this specific product today?
4. Does the Gorgias tech partner program terms, if signed, create a conflicting obligation? (E.g., exclusivity clauses, revenue sharing terms that assign rights to Gorgias.)
5. Timing: can this be structured as a "projet de création d'entreprise" under French law (allowing preparation during employment with notice)?

**Tech partner program as a second conflict:** The program requires a formal application and agreement with Gorgias. Even reading and signing those terms while employed could create obligations. Do not apply, do not engage formally with Gorgias BD on this venture, until employment ends or explicit written clearance is obtained. [HARD GATE — in pre-launch-checklist.md]

---

## 7. TECHNICAL FORM RISK

### Risk A: Gorgias deprecates the HTTP integration layer
- **Evidence against:** HTTP integrations have been actively invested in — OAuth2 support added in early 2026 (source: [Gorgias Updates - Integrations REST API](https://updates.gorgias.com/publications/integrations-rest-api-documentation)). The layer is being expanded, not wound down.
- **Fallback architecture:** If HTTP widgets are deprecated, rebuild as Gorgias app store listing (requires tech partner membership) or migrate to a browser extension that injects data into the Gorgias UI (technical fallback, not preferred).
- **Verdict:** Low risk in the next 24 months. Flag in pre-launch-checklist.md for annual review.

### Risk B: Marketplace API restricts access (channel integrations)
- Amazon SP-API requires seller approval; rate limits exist. ManoMano API is less documented.
- Mitigation: Confirm API access tier before committing to build. [Already in pre-launch-checklist.md as T-008 gate]
- Verdict: Real risk for channel integrations. Lower risk for display integrations (you only read loyalty/review APIs, not write marketplace data).

---

## 8. GDPR: What the privacy-first architecture must include

**Even a pass-through integration processes personal data under GDPR Art. 4(2).**

Required before any merchant data flows:
a. **DPA clause in every merchant contract** — Yohan acts as a data processor; the merchant is the controller. DPA must specify: data categories processed, retention periods, sub-processors, deletion rights.
b. **Server log retention policy** — No PII in logs beyond 30 days maximum. Prefer: log ticket IDs and event types only, never customer names/emails/order data.
c. **Data processor registration in France** — Not always mandatory but recommended (CNIL guidance). Lawyer must confirm.
d. **Privacy-first architecture:** The widget must not store customer data on your servers. The architecture should be: Gorgias calls your endpoint → your endpoint calls the third-party API → data returned in real-time → nothing persisted on your side. This is both the fastest build and the most defensible GDPR posture.
e. **Sub-processor agreements** — If you use n8n Cloud, Vercel, Netlify, Railway, or any hosting provider, they become sub-processors. Each needs a DPA.

**Verdict:** Architect as pure pass-through from day one. This costs nothing extra and removes the hardest GDPR obligations.

---

## 9. TECH PARTNER PROGRAM AS ASSET

**What the program offers (sourced from public pages):**
- App marketplace listing (75+ integrations as of the Crossbeam case study) — direct distribution to 15,000+ Gorgias merchants browsing the app store.
- Co-marketing: Gorgias promotes listed apps in newsletters, webinars, and "new apps" announcements.
- Lead sharing: Gorgias surfaces relevant apps to merchants who need them.
- Revenue share: "Industry leading" (exact % not public).
- Dedicated partner manager + Slack channel.
- Source: [Gorgias Tech Partner page](https://www.gorgias.com/tech-partner); [PartnerStack Gorgias program](https://market.partnerstack.com/page/gorgias); [Crossbeam case study](https://www.crossbeam.com/case-study/how-to-increase-your-tech-partner-programs-revenue-by-30-and-be-a-joy-to-work-with)

**What a marketplace listing is worth:**
- Gorgias drives 50% of company revenue through partnerships (PartnerStack case study, source: [PartnerStack](https://partnerstack.com/customers/gorgias)). A listing in a marketplace this active has compounding distribution value.
- Conservative estimate: if a marketplace listing converts 0.1% of 15,000 merchants per month to a trial = 15 trials/mo. At 10% trial-to-paid = 1.5 new merchants/mo from passive distribution alone.
- At €100/mo, that's €1,800 ARR added per month from one channel — just from the listing.
- Over 12 months: €21,600 ARR from zero active sales effort.

**Path to membership post-employment:**
- The program appears open to any tech company that builds a Gorgias integration. No confirmed exclusivity or headcount requirement.
- Path: build the integration, validate with 5 paying merchants, apply to the tech partner program after employment ends (or with written clearance). This is a 6–12 month timeline from today.
- **This is the highest-leverage growth lever available once the employment gate is cleared.** Priority 1 after legal clearance.

---

## 10. FALLBACK DIRECTIONS (if idea fails validation)

If Step 3 produces a NO-GO:

**Fallback A: Gorgias agency services — implementation only, no product**
- Use the same insider knowledge + agency relationships to offer implementation-only services: Gorgias onboarding, HTTP widget configuration for existing app store tools, AI Agent setup.
- No IP risk. No GDPR complexity. Revenue: €2,000–5,000/project. Scalable via subcontracting.
- Same Ohtani Matrix fit. Lower upside (no recurring revenue), lower risk.

**Fallback B: Gorgias-specialist AI Agent config and prompt library**
- Build a library of tested Gorgias AI Agent automation templates (intents, rules, macros) sold as a productized service or subscription to agencies.
- No custom integration required. Recurring via updates. Gorgias AI Agent is actively growing (AI Agent 2.0 launched mid-2025, source: Sacra).
- Revenue model: €200–500/mo per agency for maintained templates + config support.

---

## STRESS TEST VERDICT

| Dimension | Status |
|-----------|--------|
| Moat | ⚠️ Conditional — real gap exists but narrower than initial hypothesis |
| Competition | ⚠️ Top tools already covered; opportunity in tier-2 tools + EMEA marketplaces |
| TAM math | ✅ Viable at €100–200/mo direct; strong agency channel leverage |
| Revenue model | ✅ Merchant subscription + agency implementation margin |
| Agency moat | ✅ Holds below 20-merchant threshold; needs multi-integration strategy to hold longer |
| Employment/IP risk | 🔴 Real — needs lawyer before public launch |
| Technical form risk | ✅ Low for display; moderate for channel integrations |
| GDPR | ⚠️ Manageable with pass-through architecture + DPA template |
| Tech partner program | ✅ High-value asset post-employment — prioritize after legal clearance |
| Fallback | ✅ Two solid alternatives identified |

**Proceed to Step 2? Conditionally yes — with the constraint that the hypothesis must be re-tested against tier-2 tools (not Yotpo/Smile.io/Recharge which are already solved). Focus: (a) Stamped, (b) EMEA-specific loyalty tools not yet in Gorgias app store, (c) French marketplaces not covered by ChannelReply/Juble.io.**

---

_Sources consulted:_
- https://www.gorgias.com/apps (2026-04-30)
- https://support.yotpo.com/docs/gorgias-integration-guide-for-reviews-and-loyalty-referrals
- https://support.okendo.io/en/articles/5899793-setting-up-the-okendo-sidebar-widget-in-gorgias
- https://www.gorgias.com/apps/channelreply
- https://docs.gorgias.com/en-US/marketplaces-by-jubleio-933434
- https://www.edesk.com/blog/best-helpdesk-for-manomano-france/
- https://www.edesk.com/blog/best-ecommerce-customer-support-software-for-cdiscount-sellers/
- https://updates.gorgias.com/publications/integrations-rest-api-documentation
- https://www.gorgias.com/tech-partner
- https://partnerstack.com/customers/gorgias
- https://www.crossbeam.com/case-study/how-to-increase-your-tech-partner-programs-revenue-by-30-and-be-a-joy-to-work-with
- https://sacra.com/c/gorgias/
- https://www.channelreply.com/integrations/gorgias

_Last updated: 2026-04-30_
