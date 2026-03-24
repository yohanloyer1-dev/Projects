# ⚙️ Post-Audit Implementation Checklist
## From Report to 50% Automation

**Purpose:** Step-by-step execution plan after audit report delivery
**Duration:** 4-12 weeks depending on complexity and client priority
**Owner:** Project manager + Gorgias consultant
**Output:** Measurable progress toward automation target (typically 30-50%)

---

## Phase 1: Report Delivery & Planning (Week 1)

### ✓ Deliver Audit Report
- [ ] Present report to client stakeholder group
- [ ] Walk through findings and recommendations
- [ ] Address questions and concerns
- [ ] Get buy-in on proposed roadmap
- [ ] Schedule follow-up implementation kickoff

### ✓ Create Implementation Roadmap
Based on the audit findings, prioritize improvements in this order:

**Priority 1 (Quick Wins):** 1-2 weeks, high impact
- Feature enablement with no content creation needed
- Fixing broken configurations
- Example: Enable Order Management, fix handover topics

**Priority 2 (Content Creation):** 2-4 weeks, medium effort
- Create/optimize 5-10 high-volume guidances
- Reuse templates to save time
- Example: Order Status, Returns, Shipping

**Priority 3 (Advanced Features):** 4-8 weeks, high effort
- Implement Flows for proactive support
- Set up Actions for order operations
- Deploy Chat on website
- Example: Pre-purchase chat flows, auto-refund actions

### ✓ Assign Resources & Timeline
- [ ] Who owns implementation? (internal client team vs. your team)
- [ ] Weekly check-in cadence established
- [ ] Milestones mapped to calendar dates
- [ ] Success metrics defined and tracking set up

---

## Phase 2: Quick Wins (Week 1-2)
### Enable Missing Features with Minimal Work

#### 2.1 Order Management Features
**Impact:** +5-10% automation, immediate ROI

- [ ] **Activate Track Order** (if not already)
  - Test: Can customer view order status from link?
  - Test: Does response appear in French (if applicable)?
  - Document: "How to get order tracking" for knowledge base

- [ ] **Activate Return Order** (if not already)
  - Test: Can customer initiate return from link?
  - Configure: Return reasons match your policy
  - Test: Does return portal work end-to-end?

- [ ] **Activate Cancel Order** (if not already)
  - Test: What happens for orders already shipped? (should show message)
  - Clarify: What's your policy on cancellations after X hours?
  - Test: Cancellation workflows

#### 2.2 Fix Broken Configurations
**Impact:** +2-5% automation, zero effort

- [ ] **Handover Topics Review**
  - Identify overly broad topics (e.g., "refund" catches too much)
  - Split into: "Refund Status" (WISMO) vs. "Refund Request" (human approval)
  - Remove topics blocking legitimate automatable requests

- [ ] **Ignore Rules Audit**
  - Check: Are any ignore rules too aggressive?
  - Example: Ignore rule blocking "order status" is too broad
  - Tighten to: Only ignore if customer expresses anger + "cancel" keyword

- [ ] **Deploy Settings Check**
  - Email: Enabled? Correct inbox?
  - Chat: Should it be enabled? (high opportunity on pre-purchase)
  - Other channels: Instagram, SMS, etc.?

- [ ] **Action Review**
  - Which actions are created but inactive? (toggle ON)
  - Example: "Get Order Info", "Update Shipping Address"
  - Test each action end-to-end

#### 2.3 Knowledge Base Audit
**Impact:** Ensures guidances aren't duplicated by Help Center

- [ ] **Check for overlap** between Help Center and Guidances
  - Problem: If Help Center has "How to track order", guidance isn't needed
  - Solution: Link Help Center article instead of creating guidance
  - Save time by avoiding duplication

- [ ] **Identify missing content**
  - Are key topics in Help Center? (returns, shipping, warranty, etc.)
  - If not, add them OR create guidances

**Output:** Quick wins list done, immediate metrics improvement measurable

---

## Phase 3: Guidance Creation & Optimization (Week 2-4)

### 3.1 Prioritize Guidances to Create
Use audit findings to prioritize by volume × improvement opportunity:

```
Priority = Ticket Volume × (100% - Current Success Rate)

Example:
- Order Status: 780 tickets × (100% - 33%) = 521 opportunity tickets
- Return Status: 535 tickets × (100% - 3%) = 519 opportunity tickets
- Warranty: 1,455 tickets × (100% - 4%) = 1,396 opportunity tickets ⭐ TOP PRIORITY
```

### 3.2 Create Top 5 Guidances
**Use 12_ECOMMERCE_GUIDANCE_TEMPLATES.md as starting point**

For each guidance, follow this workflow:

#### Step 1: Define Trigger
```
"When a customer asks about [topic]"
Example: "When a customer asks about tracking their order"
```

#### Step 2: Map Scenarios
```
Scenario 1: Order shipped (in transit)
Scenario 2: Order not yet shipped
Scenario 3: Order delivered
Scenario 4: Order lost/delayed
```

#### Step 3: Define Conclusions
For each scenario:
- 🟢 **End Flow** = AI provides answer + closes ticket
- 🟡 **Handover** = AI provides info + transfers (if truly needed)

Example for "Order Status" guidance:
```
Scenario 1: Order shipped
→ Confirm order number
→ Share tracking link [TRACKING_URL]
→ Provide estimated delivery
→ ✓ End flow (customer has what they need)

Scenario 2: Order not shipped
→ Confirm order number
→ Explain processing timeline
→ Offer to check logistics
→ → Handover (if customer demands to speak to someone)

Scenario 3: Order delivered
→ Confirm delivery date
→ Link to returns policy
→ ✓ End flow
```

#### Step 4: Review with Client
- [ ] Does guidance align with your brand voice?
- [ ] Are actions/links accurate and working?
- [ ] Are policies correctly reflected?
- [ ] Any scenarios missing?

#### Step 5: Test in Gorgias
- [ ] Test trigger activates correctly
- [ ] Each scenario flows as expected
- [ ] Variables ([ORDER_STATUS], etc.) populate correctly
- [ ] Links are clickable and correct

#### Step 6: Track Results
- [ ] Record baseline metrics before publishing
- [ ] Publish guidance
- [ ] Monitor for 1 week, measure impact

### 3.3 Typical Top 5 Guidances (for e-commerce)
Adapt based on your audit findings:

1. **Order Status (WISMO)**
   - Volume: Usually #1-2 intent
   - Current success: Often 30-60%
   - Improvement: Focus on "not shipped" scenario

2. **Returns/Refund Status**
   - Volume: Usually #3-5 intent
   - Current success: Often 0-10%
   - Improvement: Add "return received" → "refund processing" flow

3. **Shipping/Delivery**
   - Volume: Usually #3-5 intent
   - Current success: Often 20-40%
   - Improvement: Add logistics escalation path

4. **Warranty/Claim**
   - Volume: Often high (surprise to clients!)
   - Current success: Often 0-10%
   - Improvement: Add eligibility check + claim form link

5. **Product Availability/Restock**
   - Volume: Varies by business
   - Current success: Often 20-50%
   - Improvement: Link to waitlist or similar products

### 3.4 Measure & Optimize
After 1 week of each guidance:

- [ ] **Coverage:** How many tickets trigger this guidance?
- [ ] **Success Rate:** Of those triggered, what % resolved without handover?
- [ ] **CSAT:** What feedback are customers leaving?
- [ ] **Handover Reasons:** If transferring, why? (fix in next iteration)

**Iteration template:**
```
Guidance: Order Status
Initial: 164 tickets, 54.9% success
After optimization: 164 tickets, 68% success (+13%)

What changed:
- Separated "not shipped" into distinct scenario
- Added "check with logistics" as explicit step
- Changed from "I'll transfer you" to "They'll respond within 2h"
```

**Output:** 5 high-impact guidances live and showing measurable improvement

---

## Phase 4: Advanced Features (Week 4-8)

### 4.1 Implement Flows (Proactive Support)
**Impact:** Intercept common requests before ticket creation

**Example Flow:** Pre-purchase shipping question
```
Trigger: Customer on product page + leaves mouse for 3 seconds
Action: Show chat prompt: "Questions about shipping? I can help!"
Flow: → Shipping cost? → Destination? → Tracking options?
Result: Customer gets instant answer, never creates ticket
```

**Steps:**
- [ ] Identify top "wasted" conversations (customers asking same thing repeatedly)
- [ ] Design flow to address that topic
- [ ] Build flow in Gorgias (use templates)
- [ ] Test on staging environment
- [ ] Deploy to specific product pages
- [ ] Monitor trigger rate and completion rate

### 4.2 Implement Actions (Operational Automation)
**Impact:** Allow AI to actually DO things, not just transfer

**Example Action:** Auto-initiate return
```
When: Customer asks about returning an item
AI: "I can start your return right now. Here's the prepaid label."
Action: Email prepaid return label from ShipStation
Result: No human involvement needed
```

**Common Actions by Business Type:**

**E-commerce Jewelry (like Nébuleuse):**
- [ ] Email return label (via Shippo/ShipStation integration)
- [ ] Create support ticket (for manual review)
- [ ] Send proactive care instructions

**E-commerce Fashion:**
- [ ] Process size exchange (via Shopify API)
- [ ] Email prepaid label
- [ ] Send loyalty points (for retention)

**SaaS:**
- [ ] Create support ticket (for engineering team)
- [ ] Reset user password
- [ ] Upgrade trial to paid

**Steps:**
- [ ] Audit what integrations you have (Shopify, ShipStation, etc.)
- [ ] List what actions are possible (technical team can confirm)
- [ ] Prioritize by impact (volume × importance)
- [ ] Build 2-3 key actions
- [ ] Reference in relevant guidances

### 4.3 Deploy Chat (if not already)
**Impact:** +20-30% automation (chat has higher resolution rates than email)

**Steps:**
- [ ] Enable Chat in Gorgias admin
- [ ] Add chat widget to website (homepage + key pages)
- [ ] Configure message routing (office hours?)
- [ ] Enable Order Management features on chat
- [ ] Deploy same guidances to chat
- [ ] Set customer expectations ("Response within 2 hours")
- [ ] Monitor chat volume vs. email (should see shift)

**Output:** Advanced features live, approaching target automation rate

---

## Phase 5: Ongoing Optimization (Week 8+)

### 5.1 Weekly Performance Monitoring
Every Monday, review:

- [ ] **Automation Rate:** Is it trending toward 50%?
- [ ] **Coverage Rate:** Are we attempting the right % of tickets?
- [ ] **Success Rate:** Are we resolving the ones we attempt?
- [ ] **CSAT:** Are customers happy?
- [ ] **Handover Reasons:** What's causing transfers? (fix it)
- [ ] **New Patterns:** Are new issues emerging?

**Dashboard you should track:**
| Metric | Week 1 | Week 2 | Week 4 | Target |
|--------|--------|--------|--------|--------|
| Coverage Rate | 41% | 45% | 52% | 65% |
| Success Rate | 24% | 28% | 35% | 45% |
| Automation Rate | 8% | 13% | 18% | 50% |
| CSAT | 3.7 | 3.8 | 3.9 | 4.0+ |

### 5.2 Monthly Optimization Sprints
Every month, pick 1-2 areas to improve:

**Month 1:** Fix top 5 handover reasons
- Example: "Returns guidance" not covering "exchange" scenario
- Fix: Add scenario + test
- Result: +2-3% improvement

**Month 2:** Launch proactive Flows
- Example: Pre-purchase chat on product pages
- Result: +5-10% reduction in incoming tickets (if chat implemented)

**Month 3:** Implement Actions
- Example: Auto-send return labels via integration
- Result: +10-15% improvement in return process efficiency

### 5.3 Quarterly Business Review
Every 3 months (or at 50% automation achievement):

- [ ] Compare current vs. baseline metrics
- [ ] Calculate actual cost savings
- [ ] Present ROI to client stakeholder group
- [ ] Plan next phase (additional channels, new products, etc.)
- [ ] Update guidances based on 90-day learnings

**Example QBR Results:**
```
BASELINE (Day 1):
- Automation rate: 8.1%
- Monthly outsourcing cost: €12,000

3-MONTH RESULTS:
- Automation rate: 31% (+23 points!)
- Monthly outsourcing cost: €7,200
- Savings: €4,800/month
- Cost of implementation: €8,000
- Payback period: <2 months
```

---

## Success Metrics & Tracking

### Metrics to Monitor

| Metric | Baseline (from audit) | 1-Month Target | 3-Month Target |
|--------|----------------------|-----------------|------------------|
| **Automation Rate** | 8.1% | 15% | 30%+ |
| **Coverage Rate** | 41% | 50% | 60%+ |
| **Success Rate** | 24% | 30% | 40%+ |
| **CSAT** | 3.7/5 | 3.8/5 | 3.9/5+ |
| **Monthly Cost** | €12,000 | €11,000 | €8,000 |
| **Cost per ticket** | €2.05 | €1.85 | €1.50 |

### How to Measure

**Weekly (Monday morning):**
- Gorgias > Statistics > AI Agent > Overview Report
- Record: Automation rate, coverage, success, CSAT
- Note: Any new handover patterns

**Monthly (end of month):**
- Compare to baseline
- Calculate improvement %
- Identify what caused improvement (new guidance? feature?)
- Plan next month's optimization

**Quarterly (every 3 months):**
- Full business review
- ROI calculation
- Stakeholder presentation
- Updated implementation plan

---

## Common Challenges & Solutions

### Challenge 1: Slow Progress
**Symptom:** 2 weeks in, still at 10% automation
**Causes:**
- Guidances not well-designed (too many handovers)
- Handover topics too broad (blocking automatable requests)
- Missing key guidance (top intent not covered)

**Solutions:**
- Review handover reasons daily (identify patterns)
- Optimize guidance scenarios (reduce handovers)
- Create missing guidance for top intents
- Enable Order Management features

### Challenge 2: Low CSAT on Automated Responses
**Symptom:** Customers complaining "I need to talk to a human"
**Causes:**
- Tone mismatch (AI sounds too corporate)
- Guidance concludes without offering human escalation
- Guidance gives info but doesn't answer their actual question

**Solutions:**
- Adjust tone to match brand (friendly, helpful, empathetic)
- Add: "If you need to speak to someone, let me know"
- Map guidance scenarios to actual customer questions (use real tickets)
- Add more context/empathy before solution

### Challenge 3: Client Wants Too Much Too Fast
**Symptom:** "We want 80% automation in 2 weeks"
**Causes:**
- Unrealistic expectations
- Underestimating complexity

**Solutions:**
- Share realistic timeline (use examples: Nébuleuse took 12 weeks to hit 40%)
- Show weekly progress (momentum is motivating)
- Celebrate milestones (30% → 35% → 40%)
- Show ROI already achieved (even at 20%, this saves money)

---

## Handoff Checklist

When implementation is complete (client reaches 50% or chooses to stop):

- [ ] Document final configuration (guidances, features, workflows)
- [ ] Create runbook for client team (how to maintain/update)
- [ ] Transfer admin/editor access (if needed)
- [ ] Schedule quarterly business reviews (ongoing optimization)
- [ ] Get testimonial/case study (with permission)
- [ ] Archive project files (for reference with future clients)

---

## Ongoing Support (Post-Launch)

### Maintenance Tasks (Client Responsibility)
- **Monthly:** Review handover reasons, update guidances
- **Quarterly:** Business review, optimization planning
- **As needed:** Update for policy changes, seasonal adjustments

### Optional Premium Support (Your Service)
- [ ] Offer retainer: X hours/month for ongoing optimization
- [ ] Offer new feature implementation: Flows, new Actions, integrations
- [ ] Offer scaling: Chat deployment, new channels, new products

---

## Template: Weekly Implementation Status

**Week X Implementation Update**

**Completed This Week:**
- ✅ Enabled Order Management
- ✅ Created "Order Status" guidance
- ✅ Fixed handover topics

**Metrics Movement:**
- Automation: 8% → 12% (+4 points)
- Coverage: 41% → 44%
- Success: 24% → 28%

**This Week's Wins:**
- Order status guidance showing 65% success rate (vs. 54% baseline)
- Customers no longer need to email about shipping status

**Next Week:**
- Create "Returns" guidance
- Test "Not Shipped" scenario
- Deploy Chat on homepage

**Blockers:** None currently

---

**Remember:** Consistent, incremental improvements add up. 2% per week = 50% in 25 weeks. Stay the course!
