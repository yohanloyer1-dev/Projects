# 🎯 Nébuleuse Bijoux — AI Agent Optimization Execution Plan

**Project Owner:** Yohan
**Client:** Nébuleuse Bijoux (nebuleusebijoux.com)
**Platform:** Gorgias AI Agent
**Status:** Ready for Execution
**Last Updated:** February 24, 2026
**Target Completion:** April 30, 2026 (9 weeks)

---

## 📊 Executive Summary

Based on a comprehensive 60-day audit of 41,419 messages across 12,024 tickets, we have identified a clear path to increase AI Agent automation from **8.1% to 50%** through strategic optimization of guidances, actions, and feature enablement.

### Key Insight
The AI Agent performs well at identification and response — the issue is **unnecessarily transferring tickets to human agents** rather than concluding them. This is fixable through:
- Guidance optimization (remove handover at conclusion)
- Feature enablement (Order Management, Actions)
- Channel expansion (Chat, WhatsApp, Instagram)

### Economic Impact
| Metric | Current | Target (50%) | Improvement |
|--------|---------|--------------|-------------|
| Automation Rate | 8.1% | 50% | +41.9% |
| Tickets/month resolved | 488 | 1,414 | +928 |
| Monthly outsourcing cost | €1,000 | €2,900 | -€1,900 |
| AI Agent cost | €589 | €1,035 | +€446 |
| **Net monthly savings** | **€411** | **€1,865** | **+€1,454** |
| **Annual net savings** | **~€4,900** | **~€22,400** | **+€17,500** |

---

## 📋 Current Baseline (60-day audit)

### Performance Metrics
| Metric | Current | Target |
|--------|---------|--------|
| Automation Rate | 8.1% | 50% |
| Coverage Rate | 38.9% | 65% |
| Success Rate | 25.3% | 45% |
| CSAT | 3.5/5 | 4.0/5 |
| First Response Time | 23min 20s | <30min |
| Handover Rate | 33.6% | <15% |

### Problem Areas Identified

**Systematic Handovers (1,744 tickets)**
- 91% of unsuccessful tickets follow this pattern: AI Agent gives complete response → transfers unnecessarily
- Root cause: Missing conclusion instructions in guidances, not AI capability issues

**Ignored Tickets (1,933 emails, 36.7%)**
- Email tickets never attempted by AI Agent due to broad ignore rules
- Includes easy wins: Return/Status (300), Order/Status (265), Warranty (218)

**Missing Guidances**
- Return/Status: 2.6% success (535 tickets) — No guidance for status inquiries
- Exchange/Status: 5.8% success (327 tickets) — No guidance for tracking

**Broad Handover Topics**
- "Enquiries about reimbursements" captures 189 tickets, many are just status checks
- Rule is too wide, needs to exclude simple followup questions

**Unused Features**
- Order Management (Track Order, Return Order): Activated but incomplete
- Actions (Baback, Loyoly, Shopify): Not integrated
- Flows: Zero deployed
- Chat channel: Not yet enabled for AI Agent

### What Works Well (Success >70%)
- Jewelry care/maintenance: 92%
- Shipping costs: 86%
- Oxidation/discoloration: 82%
- Restocking information: 74%
- Lost jewelry/clasp: 72%

**Pattern:** When AI Agent has complete guidance with clear conclusion paths, it resolves consistently. We replicate this pattern across all intents.

---

## 🎬 Phase 1 — Quick Wins (Weeks 1-2)

**Objective:** Fast, high-impact improvements to automation rate
**Target Impact:** +15% to +25% automation
**Effort Level:** Low (configuration changes, no complex integrations)

### Task 1.1: Reduce Ignored Tickets
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 3 days
**Impact:** +3% to +5% automation

**What to do:**
- Review ai_ignore (Prevent AI from answering) rules in Gorgias
- Identify overly broad rules blocking legitimate requests
- Remove rules for: Return/Status, Order/Status, Warranty inquiry
- Consider contextual ignore rules (only for non-standard requests)

**Tickets recovered:** ~338 tickets
**Success metric:** Monitor next 7 days to confirm AI now attempts previously ignored email types

---

### Task 1.2: Affine Handover Topics
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 3 days
**Impact:** +5% to +7% automation

**What to do:**
- Review "Enquiries about reimbursements" topic (189 tickets captured)
- Separate into two categories:
  - "Status inquiry about existing refund" → Keep with AI Agent
  - "Request for new refund" → Keep with handover
- Update filtering rules to be more specific
- Test with 20 sample tickets before full deployment

**Tickets recovered:** ~95 tickets
**Success metric:** Handover topic acceptance rate drops, more status inquiries resolved

---

### Task 1.3: Optimize WISMO Guidance (Order Tracking)
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 4 days
**Impact:** +4% to +6% automation

**What to do:**
- Current WISMO has 91% handover rate (23 tickets, 21 transferred)
- Issue: Commandes "Unfulfilled" and "Tracking inactive" automatically trigger handover
- Changes:
  1. **Unfulfilled orders without "duplicate name" tag** → New response: "Your order is being prepared and will ship in 2-4 business days"
  2. **Tracking inactive but delivery confirmed** → Conclude ticket instead of handover
  3. **Complete Track Order** → Add response for "Unfulfilled" status in Order Management feature

**Tickets recovered:** ~15 tickets
**Success metric:** WISMO handover rate drops from 91% to <30%

---

### Task 1.4: Optimize Warranty Guidance
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 4 days
**Impact:** +2% to +3% automation

**Current issue:** Warranty guidance sends Typeform but then handovers on scenarios 3 & 4 (online purchase <30 days, 31-364 days)

**What to do:**
- **Scenarios 3 & 4:** Replace handover with conclusion message: "We've received your claim. Our team will review and respond within X days."
- **Scenario 2 (in-store purchase):** Conclude after redirect instead of handover
- **Keep handovers for:** Warranty expired, specialty cases, damage assessment needed

**Tickets recovered:** ~20 tickets
**Success metric:** Warranty guidance goes from ~50% handover to <20%

---

### Task 1.5: Create Return/Status Guidance
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 5 days
**Impact:** +3% to +4% automation

**Current state:** 535 tickets (Return/Status), 2.6% resolution, no guidance

**New guidance structure:**
```
Intent: Return Status Inquiry
├─ Return in transit
│  └─ "Your return is in transit. Standard processing is 30 days from arrival."
├─ Return received, processing
│  └─ "We've received your return. Processing typically takes X days."
├─ Return processed, refund issued
│  └─ "Your refund has been issued. It should appear in 2-5 business days."
└─ Return delayed (>10 days)
   └─ Handover to agent for investigation
```

**Tickets recovered:** ~125 tickets
**Success metric:** Return/Status success rate jumps from 2.6% to 20%+

---

### Task 1.6: Create Exchange/Status Guidance
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 5 days
**Impact:** +3% to +4% automation

**Current state:** 327 tickets (Exchange/Status), 5.8% resolution, no guidance

**New guidance structure:**
```
Intent: Exchange Status Inquiry
├─ Return in transit
│  └─ "Your return is in transit. Once received, we'll process your exchange within 30 days."
├─ Return received, exchange processing
│  └─ "We've received your return. Your replacement is being prepared."
├─ Exchange shipped
│  └─ "Your replacement has been shipped! Here's your tracking: [link]"
└─ Exchange delayed (>30 days)
   └─ Handover for priority handling
```

**Tickets recovered:** ~95 tickets
**Success metric:** Exchange/Status success rate jumps from 5.8% to 20%+

---

### Task 1.7: Deploy AI Agent to Chat
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 3 days
**Impact:** +3% to +5% automation

**Current state:** 841 chat conversations/60 days, zero AI Agent automation, 100% relies on One Pilot

**What to do:**
- Enable AI Agent on Chat channel (already configured from initial setup)
- Test with sample messages across guidance topics
- Monitor CSAT and response times (should improve significantly)
- Note: Weekend activation especially valuable (16.5-17.5% conversion rate)

**Tickets recovered:** ~210 tickets/60 days
**Success metric:** Chat response time <2min, CSAT maintains 3.5+

---

## 📊 Phase 1 Summary

| Task | Timeline | Impact | Total Recovered |
|------|----------|--------|-----------------|
| 1.1 Reduce ignored tickets | 3d | +3-5% | +338 |
| 1.2 Affine handover topics | 3d | +5-7% | +95 |
| 1.3 Optimize WISMO | 4d | +4-6% | +15 |
| 1.4 Optimize Warranty | 4d | +2-3% | +20 |
| 1.5 Return/Status guidance | 5d | +3-4% | +125 |
| 1.6 Exchange/Status guidance | 5d | +3-4% | +95 |
| 1.7 Deploy Chat | 3d | +3-5% | +210 |
| **TOTAL** | **~2 weeks** | **+23-34%** | **+893 tickets** |

**Expected new automation rate:** 8.1% → ~30-35%

---

## 🔧 Phase 2 — Structural Improvements (Weeks 3-4)

**Objective:** Enable new capabilities through feature activation and integrations
**Target Impact:** +8% to +15% additional automation
**Effort Level:** Medium (feature configuration, basic API integration)

### Task 2.1: Complete Order Management Setup
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 4 days
**Impact:** +2% to +3% automation

**What to do:**
- **Track Order:** Add "No response configured" for Unfulfilled orders
  - Response template: "Your order is being prepared. Expected ship date: [calculated from shop settings]"
- **Return Order:** Activate if not already (link to portal: nebuleusebijoux.com/a/return)
- **Cancel Order:** Evaluate and enable if policy allows
- **Test flow:** Mock customer scenarios for each order status

**Success metric:** Order Management handles 20%+ of Order intent tickets

---

### Task 2.2: Activate Baback Actions (Returns & Refunds)
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 6 days
**Impact:** +3% to +5% automation

**Current issue:** 43.8% of handovers (764 tickets) are refund/reimbursement actions

**What to do:**
- Integrate Baback API with Gorgias
- Create actions:
  - Check return status (real-time from Baback)
  - Check refund status
  - Initiate refund process (if policy allows)
  - Generate return label
- Update Return/Status and Exchange/Status guidances to use actions
- Test with One Pilot review first

**Success metric:** Refund-related handovers drop from 43.8% to <15%

---

### Task 2.3: Activate Loyoly Actions (Loyalty)
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 5 days
**Impact:** +1% to +2% automation

**Current issue:** Loyalty guidance (3 scenarios) handovers for point transfers, point discrepancies, rank loss

**What to do:**
- Integrate Loyoly API with Gorgias
- Create actions:
  - Check point balance
  - Check loyalty tier/rank
  - Check point transaction history
  - Initiate point transfer (if applicable)
- Update Loyalty guidances to resolve common inquiries
- Test with small cohort

**Success metric:** Loyalty inquiries resolved without handover for simple balance/tier checks

---

### Task 2.4: Deploy Flows for FAQ Interception
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 6 days
**Impact:** +2% to +3% automation

**What to do:**
Create guided flows for high-volume simple inquiries:

1. **"Shipping & Returns"** (volume: 862)
   - Explain return policy → Link to portal → Confirm receipt

2. **"Order Tracking"** (volume: 780)
   - Request order number → Show status → Offer help

3. **"Warranty & Guarantees"** (volume: 1,455)
   - Explain warranty → Link to claim form → Confirm submission

4. **"Shipping Problems"** (volume: 355)
   - Identify problem type → Provide solution → Escalate if needed

**Success metric:** Flows intercept 5-10% of chat interactions, reducing ticket creation

---

### Task 2.5: Optimize Order Issues Guidance
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 4 days
**Impact:** +2% automation

**Current issue:** "Order issues or shipping issues" guidance mostly handovers for damage/missing items

**What to do:**
- Scenario: Product damaged with clear photo → Direct to Warranty form instead of manual reship
- Scenario: Article missing → Request photo evidence, submit claim form, conclude
- Keep handovers only for: Livré non reçu (sworn statement required), modification requests

**Success metric:** Damage/missing item tickets resolved via form instead of handover

---

### Task 2.6: Add Report Order Issue Scenarios
**Status:** Not Started
**Owner:** Yohan
**Timeline:** 3 days
**Impact:** +1% to +2% automation

**Jewelry-specific additions to Order Issue reporting:**
- Bracelet/Ring size non-conforming
- Oxidation/discoloration at receipt
- Clasp/fastening defective
- Gravure error (personalization)
- Incomplete colis delivery

**Success metric:** New scenarios capture 15-20 additional tickets from open-ended "issues"

---

## 📊 Phase 2 Summary

| Task | Timeline | Impact | Cumulative |
|------|----------|--------|-----------|
| 2.1 Complete Order Management | 4d | +2-3% | +31-38% |
| 2.2 Activate Baback | 6d | +3-5% | +34-43% |
| 2.3 Activate Loyoly | 5d | +1-2% | +35-45% |
| 2.4 Deploy Flows | 6d | +2-3% | +37-48% |
| 2.5 Optimize Order Issues | 4d | +2% | +39-50% |
| 2.6 Add Issue Scenarios | 3d | +1-2% | +40-52% |
| **TOTAL** | **~2 weeks** | **+11-17%** | **+34-52%** |

**Expected cumulative automation rate:** ~35% → **41-52%** (target: 50%)

---

## 🚀 Phase 3 — Advanced Optimizations (Week 5+)

**Objective:** Reach and exceed 50% automation target through advanced API integrations and channel expansion
**Target Impact:** +5% to +10% additional automation
**Timeline:** Ongoing through Month 2

### Task 3.1: Advanced Shopify API Actions
- Custom cancel order action (non-fulfilled only)
- Expedited processing for VIP customers
- Inventory queries for pre-order status

**Impact:** +1-2% automation

---

### Task 3.2: Prepare WhatsApp & Instagram Deployment
- Gorgias extending AI Agent support to these channels (Q2/Q3 2026)
- NB Instagram DM: 1,358 tickets/60 days (11.3% of volume)
- NB Instagram Comments: 2,883 tickets/60 days (24% of volume)
- These channels will add significant automation opportunity

**Impact:** +3-5% automation (projected for later deployment)

---

### Task 3.3: Advanced Optimization Opportunities
- A/B test different guidance conclusion messages
- Implement dynamic response variations based on customer tier
- Create merchant-facing analytics dashboard
- Ongoing metric refinement and optimization

**Impact:** +1-2% ongoing improvements

---

## 📈 Success Metrics & Tracking

### Weekly Metrics to Monitor

| Metric | Baseline | Week 2 Target | Week 4 Target | Goal |
|--------|----------|---------------|---------------|------|
| Automation Rate | 8.1% | 20-25% | 40-45% | 50% |
| Coverage Rate | 38.9% | 50-55% | 60-65% | 65% |
| Success Rate | 25.3% | 35-40% | 45-50% | 45% |
| Avg Response Time | 23min | <20min | <15min | <15min |
| CSAT | 3.5/5 | 3.6/5 | 3.8/5 | 4.0/5 |
| Handover Rate | 33.6% | 25-28% | 12-15% | <15% |
| Tickets/month | 488 | 800-1000 | 1200-1350 | 1,414 |

### Economic Tracking

| Metric | Baseline | Phase 1 | Phase 2 | Goal |
|--------|----------|---------|---------|------|
| Monthly outsourcing cost | €1,000 | €750 | €500 | €375 |
| Monthly AI Agent cost | €589 | €700 | €850 | €1,035 |
| **Net monthly cost** | **€1,589** | **€1,450** | **€1,350** | **€1,410** |
| **Monthly savings** | **€0** | **€139** | **€239** | **€179** |

---

## 🎯 Critical Success Factors

### Prerequisites
- ✅ Access to Gorgias admin settings (confirm with One Pilot contact)
- ✅ Shopify API permissions current (verified in audit)
- ✅ One Pilot collaboration for KB/handover alignment
- ✅ Typeform guidance links active (warranty form verified)

### Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|-----------|
| Guidances too broad, catch edge cases | Medium | Quality drop | Test with sample tickets first |
| API integrations fail | Low | Phase 2 delays | Test in sandbox, One Pilot review |
| Customer complaints on automation | Low | CSAT drop | Monitor CSAT closely, conservative guidance |
| One Pilot resistance to changes | Medium | Adoption delay | Present ROI, involve early in planning |

---

## 📅 Timeline & Milestones

```
Week 1
├─ Mon-Tue: Tasks 1.1, 1.2 (Ignore rules, handover topics)
├─ Wed-Fri: Tasks 1.3, 1.4 (WISMO, Warranty)
└─ Status: First metrics snapshot

Week 2
├─ Mon-Tue: Tasks 1.5, 1.6 (Return/Status, Exchange/Status)
├─ Wed-Fri: Task 1.7 (Deploy Chat)
└─ Milestone: Phase 1 complete — expect 20-25% automation rate

Week 3
├─ Mon-Wed: Task 2.1 (Order Management)
├─ Thu-Fri: Task 2.2 (Baback integration begins)
└─ Status: Phase 1 performance validated, Phase 2 in progress

Week 4
├─ Mon-Tue: Task 2.2 cont., Task 2.3 (Loyoly)
├─ Wed-Fri: Tasks 2.4, 2.5, 2.6 (Flows, optimizations)
└─ Milestone: Phase 2 complete — expect 40-50% automation rate

Week 5+
├─ Phase 3: Advanced optimizations, channel expansion
├─ Ongoing: Weekly metrics review, customer communication
└─ Milestone: Reach 50%+ automation target by end of April
```

---

## 📞 Communication Plan

### Weekly Updates (Every Monday)
- Automation rate update
- Tickets recovered this week
- Blockers and resolutions
- Next week priorities

### Stakeholder Updates
- **One Pilot:** Monthly check-ins on handover trends, KB alignment
- **NB Leadership:** Monthly ROI/savings reports
- **Internal:** Keep documentation current as changes deploy

### Success Celebration
- Reach 30% automation → Announce 3x improvement
- Reach 50% automation → Full ROI realized, potential expansion discussion

---

## 📄 Appendix: Implementation Checklists

### Phase 1.1 Checklist (Reduce Ignored Tickets)
- [ ] List all current ai_ignore rules
- [ ] Identify rules capturing Return/Status, Order/Status, Warranty
- [ ] Draft new rules or removals
- [ ] Test with 50 sample tickets
- [ ] Deploy and monitor

### Phase 1.2 Checklist (Handover Topics)
- [ ] Export all handover topics with matching rules
- [ ] Analyze "reimbursements" topic (189 tickets)
- [ ] Create separate "new refund request" topic
- [ ] Test rule specificity with edge cases
- [ ] Deploy with monitoring

### Phase 2.2 Checklist (Baback Integration)
- [ ] Confirm Baback API access credentials
- [ ] Build test integration in Gorgias sandbox
- [ ] Create return status check action
- [ ] Create refund status check action
- [ ] Test with One Pilot team
- [ ] Deploy to production

---

**Document Status:** Ready for Implementation
**Next Step:** Begin Phase 1 Week 1 tasks
**Review Date:** March 3, 2026 (mid-point assessment)
