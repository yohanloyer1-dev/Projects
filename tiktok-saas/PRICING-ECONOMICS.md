# PRICING + UNIT ECONOMICS + GO/NO-GO — D13
# Last updated: 2026-05-04

---

## a) DFY PRICING TABLE

Three pricing tiers based on scope, not feature gates.

| Tier | Setup | Monthly retainer | Best for |
|------|-------|------------------|----------|
| Starter | €1,500 | €300 | Single niche, single CTA, validation phase |
| Standard | €2,500 | €400 | Refined niche, A/B persona testing, monthly performance call |
| Premium | €3,000 | €500 | Multi-CTA / multi-resource funnel, weekly call, priority support |

### What's included at each tier

#### Starter (€1,500 setup + €300/mo)
- 1 AI character (1 persona)
- 1 niche, 1 CTA keyword, 1 free resource
- 5 videos per week (Mon-Fri)
- Pattern library + Intelligence agent active from week 1
- Telegram approval flow
- Monthly 30-min performance review call
- Email support: <48h response

#### Standard (€2,500 setup + €400/mo)
- Everything in Starter
- A/B persona testing (Persona A vs Persona B from week 4)
- 2 free resources (different CTAs)
- Bi-weekly 30-min performance call
- Weekly Slack/email check-in summary
- Email support: <24h response

#### Premium (€3,000 setup + €500/mo)
- Everything in Standard
- Up to 3 free resources / lead magnets
- Multi-CTA orchestration (different keywords for different angles)
- Weekly 30-min strategy call
- Priority hotline (WhatsApp): <4h response during business hours
- Custom n8n workflow modifications (reasonable scope, ≤4h/mo)
- Quarterly system audit + optimization recommendations

### What's ALWAYS excluded (regardless of tier)
- Filming or editing the client's real face/voice
- Niches requiring medical, financial, legal, or gambling claims
- TikTok account growth via paid ads (organic only)
- Multi-platform expansion in Phase 1 (TikTok-first)
- Custom Higgsfield character beyond initial setup (re-creation = €500 add-on)
- Same-day response time SLAs

### Overage policy for retainer
- Each tier includes a base scope
- Additional video packs: €25 / 5 videos (one-off purchase)
- Additional persona: €500 setup + €100/mo
- Multi-channel expansion (Instagram, YouTube): +€200/mo per channel from Phase 2

---

## b) SAAS GROSS MARGIN TABLE

Per-unit cost assumptions (2026 pricing):

### Cost components (per client per month, Starter equivalent: 20 videos/mo)

| Component | Unit cost | Volume/mo | Cost/mo |
|-----------|-----------|-----------|---------|
| ScrapeCreators API | $0.10/100 calls | 4 weekly runs × 6 endpoints = 24 calls | $0.024 |
| Supadata API | $0.02/transcript | 4 weekly × 10 transcripts = 40 | $0.80 |
| Claude Sonnet 4.6 — research summary | $3/$15 per 1M in/out | ~3K in, ~2K out per week × 4 | $0.16 |
| Claude Sonnet 4.6 — script generator | $3/$15 per 1M in/out | ~5K in, ~5K out per week × 4 | $0.36 |
| Claude Sonnet 4.6 — compliance rewrite | $3/$15 per 1M in/out | ~2K in, ~2K out per week × 4 (avg 30% scripts flagged) | $0.04 |
| Claude Sonnet 4.6 — intelligence | $3/$15 per 1M in/out | ~5K in, ~3K out per week × 4 | $0.24 |
| Higgsfield Seedance 2.0 (MCP) | $0.35/video | 20 videos | $7.00 |
| Cloudflare R2 storage | $0.015/GB/mo | ~2GB videos retained | $0.03 |
| Cloudflare R2 egress | $0.00 (free egress) | — | $0.00 |
| Supabase | $0.025/100K rows | shared $25/mo plan ÷ 50 clients | $0.50 |
| n8n self-hosted (Railway) | $20/mo for instance | shared ÷ 50 clients | $0.40 |
| Metricool API (counted in client's own Metricool sub) | client pays direct | n/a | $0.00 |
| Telegram bot | free | — | $0.00 |
| **Total COGS** | | | **$9.55/mo** |

**Convert USD → EUR (2026 ~1.08): COGS ≈ €8.85/client/mo at Starter volume**

### Gross margin per tier

| Tier | Price | COGS | Gross profit | Margin |
|------|-------|------|--------------|--------|
| Starter (20 vid/mo) | €99 | €8.85 | €90.15 | 91.1% |
| Growth (60 vid/mo) | €199 | €23.55 | €175.45 | 88.2% |
| Pro (160 vid/mo) | €299 | €58.85 | €240.15 | 80.3% |

### COGS sensitivity
- Higgsfield is the dominant variable cost. At 160 videos/mo for Pro tier, video cost = $56 → if Higgsfield raises to $0.50/video, Pro tier margin drops from 80% to 73%. Still healthy.
- Claude API token cost is minimal (~$0.80/client/mo). Could increase 10x and still be <€10/client.

### Economic GO/NO-GO threshold for SaaS
- Starter @ 91% margin → break-even on customer acquisition cost (CAC) at €100 CAC requires 1.1 months retention. Realistic.
- 100 paying customers = €9,900 MRR, €9,015/mo gross profit. Sustainable.

---

## c) UPSELLS (DFY and SaaS)

### One-time upsells (DFY)
- **Extra video pack**: €100 / 10 videos (€10/video) — for launches or events
- **TikTok audit-ready package**: €1,500 — prepares the channel + n8n app for TikTok's official API audit (so they can graduate from Metricool to Direct Post). Includes documentation, sample data, audit submission, follow-up.
- **Custom persona design**: €500 — additional persona (A/B test variant or alt character for different niche angle)
- **Multi-niche expansion**: €1,500 — 2nd niche on the same channel or 2nd channel for the same client

### Monthly add-ons
- **LinkedIn content add-on**: €400/mo — Yohan repurposes top TikTok scripts into LinkedIn posts, 2/week
- **Email sequence copywriting add-on**: €300/mo — custom 7-email sequence per quarter (replaces template Day 0-14 with niche-specific content)
- **Performance dashboard (custom)**: €200/mo — bespoke BI dashboard built in Metabase or similar for clients who want deeper analytics than Lovable provides

### Strategic upsells
- **Sponsorship deal pipeline**: €1,000 + 15% commission on first sponsorship value — Yohan brokers the first brand deal once channel reaches 10K followers. Massive value-add.
- **Annual retainer discount**: -15% off monthly when paid annually (€3,060 → €2,601/yr for Starter)

---

## d) HARD GO/NO-GO CRITERIA FOR SAAS BUILD

**ALL** of these must be true before touching Lovable:

```
[ ] 3 DFY clients fully onboarded and running
[ ] 6 consecutive weeks of stable operation per client (<5% error rate per week in Supabase events table)
[ ] €1,500/mo total retainer MRR (not one-time setup revenue)
[ ] Onboarding flow documented and completable in <90 min without Yohan's involvement (someone else can do it from CLIENT-ONBOARDING.md)
[ ] 1 documented case study: channel age, follower count, leads captured, weeks of fully automated operation
[ ] Supabase RLS policies tested with simulated multi-tenant load (run a script that creates 10 tenants, attempts cross-tenant reads, verifies all blocked)
[ ] Lovable builder capacity confirmed (Yohan has 7+ weeks of build time without pausing DFY operations OR has hired help)
```

### Verification protocol (run at end of each month)

| Criterion | Check command/tool |
|-----------|-------------------|
| 3 DFY clients running | `SELECT count(*) FROM clients WHERE status='active'` ≥ 3 |
| 6 weeks stable per client | `SELECT client_id, count(*) FROM events WHERE level IN ('error','critical') AND created_at >= now()-interval '7 days' GROUP BY client_id` — all should be <5% of weekly run count |
| €1,500 MRR | Manual: sum of retainers > €1,500 |
| Onboarding <90 min documented | Yohan times one onboarding from scratch following only CLIENT-ONBOARDING.md |
| Case study documented | `clients/{CLIENT_ID}/case-study.md` exists with metrics, screenshots, narrative |
| RLS load tested | Test script run in Supabase staging — see Lovable spec section e |
| Build capacity | Calendar review: 7 consecutive weeks with ≥10h/week available, OR signed contract with builder |

### What if criteria are NOT met after 6 months?
- DO NOT build Lovable.
- Reassess: is the DFY channel itself the product? Many high-margin businesses stay at DFY level forever.
- Consider: license the system as a one-time install with documentation (€5,000 one-time) instead of SaaS.
- Worst case: shut down SaaS plans, double down on DFY at premium pricing.

---

## e) PHASE 1 (DFY) FINANCIAL TARGETS

### 90-day targets (from Day 0)
- 5 paying DFY clients (mix of tiers, average €2,000 setup + €400/mo retainer)
- Setup revenue: €10,000
- Monthly retainer MRR: €2,000
- 90-day total: €10,000 + 3 × €2,000 = €16,000

### Year 1 targets (Phase 1 only, no SaaS)
- 15 DFY clients total (5 churn assumed, 20 acquired)
- Avg setup: €2,000 → €40,000 setup revenue
- Avg retainer: €400/mo × 15 active clients = €6,000 MRR
- Year 1 ARR: €40,000 + €72,000 retainer = **€112,000 from DFY alone**

### Year 1 with SaaS launch (if GO/NO-GO passes month 6)
- DFY: €112,000 (as above)
- SaaS: 50 customers by year-end (avg €150/mo) = €7,500 MRR by Dec, ~€30,000 from SaaS in year 1
- **Total Year 1: ~€142,000 ARR**

---

## f) WHEN TO RAISE PRICES (signals)

- Setup converts >50% of qualified calls → raise setup price by €500
- Waitlist >10 qualified applicants → raise both setup and retainer by 20%
- 3 unsolicited "I'd pay more" mentions → raise immediately
- Year 1 Q4 retention >90% → raise retainer for new customers (grandfather existing)

---

## g) WHEN TO LOWER OR DISCOUNT (signals to RESIST)

- "I'd buy if it was cheaper" — DO NOT lower. Wrong fit.
- "Can you do a 3-month trial?" — DO NOT. Hurts revenue, creates churn risk.
- Acceptable discount situations:
  - Annual prepay: -15% (cash flow benefit)
  - Friend/portfolio client willing to be a public case study: -50% setup, full retainer
  - Founder's referral (someone Yohan already trusts): -€500 setup
