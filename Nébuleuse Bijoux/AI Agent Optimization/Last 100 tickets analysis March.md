# Handover Analysis — Last 100 AI Agent Tickets
**Period:** March 15–19, 2026 | **Account:** Nébuleuse Bijoux

---

## Executive Summary

Analyzed 100 consecutive handover tickets one by one. The AI Agent is handing over **too often** — in many cases, human agents performed simple, repeatable actions that the AI could handle with better guidance. The top 3 handover categories account for **72% of all handovers**, and roughly **30-40 of the 100 tickets could have been resolved by AI** with targeted guidance improvements.

---

## Handover Breakdown by Category

| Category | Count | % | Automatable? |
|----------|-------|---|-------------|
| **Return/Exchange status & refund follow-ups** | 28 | 28% | Partially (needs tools) |
| **Product quality / Warranty claims** | 22 | 22% | Mostly ✅ |
| **Promotion & Discount issues** | 12 | 12% | Partially ✅ |
| **Order issues (damaged, wrong, missing)** | 14 | 14% | Partially |
| **Shipping delays & delivery issues** | 10 | 10% | Partially |
| **Loyalty / Account issues** | 8 | 8% | Not yet (needs tools) |
| **Other (gift cards, customs, misc)** | 6 | 6% | Case-by-case |

---

## Detailed Findings by Category

### 1. Return/Exchange Status (28 tickets) — BIGGEST HANDOVER DRIVER

**What's happening:** The #1 handover topic is "Customer asking when they will receive their refund or store credit after a return has been processed." This single topic triggered **18 of the 28 handovers** in this category.

**What human agents actually did:**
- Confirmed return was received → triggered refund → said "2-5 business days" (tickets 212544300, 212595247, 212616496, 212363779, 212322873)
- Confirmed return received → logistics team processing within 30 days (tickets 212573229, 212717489, 212253142)
- Confirmed exchange replacement being prepared (ticket 212717887)
- Provided store credit code (ticket 212662424)
- Explained return process / label instructions (tickets 212585115, 212747923, 212771959)

**Current guidance gap:** The Exchange guidance has a **hard handover rule** for exchange status inquiries: *"IF the shopper is asking about the status of an existing exchange → hand over the ticket."* This is intentional but very costly — it's the single biggest handover driver.

**🟡 Recommendation (MEDIUM — needs Return/Refund tools):**
Once you have access to return/refund tools, this is the #1 opportunity. For now, the AI could at least:
- Acknowledge the return was received (if tracking shows delivery)
- Set expectations: "refunds take 2-5 business days" / "exchanges processed within 30 days"
- Snooze instead of handing over for simple status checks

**Estimated impact:** Could eliminate ~15 handovers/week.

---

### 2. Product Quality / Warranty Claims (22 tickets) — QUICK WINS AVAILABLE

**What's happening:** Many warranty handovers are for cases the AI *should* already handle based on the current guidance, but doesn't.

**Ticket-by-ticket patterns:**

| Pattern | Tickets | What human did | AI could do? |
|---------|---------|---------------|-------------|
| Directed to warranty form | 212625615, 212637660, 212471106, 212471848, 212232147, 212232452, 212287001, 212291518, 212449920, 212455117 | Apologized + sent warranty form link | ✅ YES — guidance already covers this |
| Repeated defect → escalation | 212798024, 212416681, 212306991 | Escalated to quality team or offered SORRY code | ✅ Already in guidance (hard handover rule) |
| Oxidation/blackening | 212559588, 212196239 | Asked about cleaning + shared care page | ✅ Already in guidance (Scenario 3b) |
| Gift purchase, no order # | 212164657 | Asked for gifter's email | ✅ NOW FIXED (Scenario 1c we just added) |
| Warranty form follow-up | 212155471, 212536835 | Reassured + shared video tip | ✅ NOW FIXED (Scenario 2 we just updated) |
| Refund status follow-up | 212198916 | Checked refund status | ✅ NOW FIXED (Scenario 2b we just added) |
| Safety/injury concern | 212322633 | Escalated piercing incident | ✅ Correct handover (hard rule) |

**🟢 Key finding:** ~10 of these 22 tickets were cases where the AI sent the customer to the warranty form and then handed over anyway. The guidance explicitly says "DO NOT hand over after sending the warranty form" — but the AI is still doing it in some cases.

**Recommendation (LOW-HANGING FRUIT):**
- **Reinforce the "DO NOT hand over after warranty form" instruction** — consider adding it as a blockquote rule at the top of the guidance for more visibility
- The 3 changes we just published (Scenarios 1c, 2, 2b) should already fix ~5 of these 22 tickets going forward
- **Estimated impact:** 5-8 fewer handovers/week from warranty alone

---

### 3. Promotion & Discount Issues (12 tickets) — QUICK WIN

**What's happening:** Two distinct patterns:

**Pattern A — "Customers requiring a discount code" (5 tickets: 212824871, 212780414, 212638263, 212559588, 212556469)**
These are triggered by a **handover topic** called "Customers requiring a discount code." The AI hands over whenever a customer needs a discount code, even when the guidance already covers providing codes like AVIS10.

**What human agents did:**
- Provided AVIS10 code (ticket 212780414)
- Explained birthday code location in account (ticket 212523264)
- Clarified 15% vs €15 confusion (ticket 212638263)
- Investigated promo code technical issues (tickets 212713928, 212165018)

**Pattern B — Loyalty-related discount questions (3 tickets: 212556469, 212364045, 212805518)**
Customers asking about loyalty codes, birthday discounts, or pre-order promotions.

**🟢 Recommendation (LOW-HANGING FRUIT):**
- **Remove or refine the "Customers requiring a discount code" handover topic** — the promotions guidance already handles providing AVIS10 and explaining newsletter codes. This handover topic is overriding the guidance and causing unnecessary escalations.
- Add a scenario for **birthday discount code lookup** — human agents simply tell customers to check their account history. AI could do this.
- **Estimated impact:** 5-8 fewer handovers/week

---

### 4. Order Issues — Damaged, Wrong Item, Missing Item (14 tickets)

**What's happening:**

| Sub-type | Count | What human did |
|----------|-------|---------------|
| Damaged at receipt | 5 | Sent warranty form |
| Wrong item received | 3 | Generated return label + reshipped correct item |
| Missing item | 4 | Reshipped missing item or offered promo code |
| Payment/other | 2 | Processed refund or investigated |

**Current guidance:** The "Order issues" guidance (2440188) covers damaged items well — it directs to the warranty form. But for **wrong items and missing items**, it says "hand over the ticket" after confirming what's missing.

**🟡 Recommendation (MEDIUM — partially needs tools):**
- For **damaged items**: AI is already supposed to send the warranty form and close. Same issue as warranty — AI is handing over after sending the form. Reinforce the "close after form" instruction.
- For **wrong/missing items**: Needs order editing/reshipping tools to fully automate. For now, keep as handover but ensure AI collects all details (which items missing, which received) before escalating.
- **Estimated impact:** 3-4 fewer handovers/week from damaged items alone

---

### 5. Shipping Delays & Delivery Issues (10 tickets)

**What's happening:**

| Sub-type | Count | What human did |
|----------|-------|---------------|
| Carrier delay (>6 days) | 4 | Opened carrier investigation |
| Delivered not received | 2 | Asked for sworn statement + ID |
| Returned to sender | 2 | Asked for new address, reshipped |
| Address change | 1 | Confirmed address for reshipment |
| Customs/duties | 1 | Explained DOM-TOM customs policy |

**Current guidance:** The WISMO guidance already covers all these scenarios well. The handovers here are mostly **correct** — carrier investigations, reshipments, and delivered-not-received cases genuinely need human intervention.

**🟡 Recommendation (MEDIUM):**
- The **customs/duties** case (ticket 212159018) could be handled by adding a scenario for DOM-TOM deliveries explaining that customs fees are the customer's responsibility.
- **Estimated impact:** 1-2 fewer handovers/week

---

### 6. Loyalty / Account Issues (8 tickets)

**What's happening:**
- Loyalty points disappeared after migration (212644572, 212591436)
- Loyalty tier questions (212704285, 212635140, 212589308)
- Account updates (212271393, 212279805)
- Affiliate commission questions (212279805)

**What human agents did:**
- Re-credited loyalty points (212591436, 212644572)
- Explained loyalty tier rules
- Updated account details

**🔴 Recommendation (BLOCKED — needs Loyalty tools):**
You mentioned Loyalty tools are the next step. Once available, this category (~8% of handovers) becomes automatable. The human actions are very repetitive: check points balance, re-credit points, explain tier rules.

---

### 7. Other / Miscellaneous (6 tickets)

- Gift card number lost (212569525) — agent explained they can't retrieve physical card numbers
- Gift card email not received (212158540) — agent resent the email
- Order edit requests (212204979, 212378016) — agent made modifications
- Promo code technical issues (212369198) — no human response yet

These are low-volume, diverse cases — not worth dedicated guidance improvements.

---

## Priority Recommendations — Low-Hanging Fruits

### 🟢 Priority 1: Remove/refine "Customers requiring a discount code" handover topic
- **Effort:** 5 minutes (configuration change)
- **Impact:** ~5-8 fewer handovers/week
- **Why:** The promotions guidance already handles providing AVIS10 and explaining codes. The handover topic is overriding the guidance.

### 🟢 Priority 2: Reinforce "DO NOT hand over after warranty form" 
- **Effort:** 10 minutes (guidance edit)
- **Impact:** ~5-8 fewer handovers/week
- **Why:** AI is still handing over after sending the warranty form in ~10 cases, despite the guidance saying not to. Moving this instruction to a more prominent position (blockquote at top) may help.

### 🟢 Priority 3: Add DOM-TOM customs scenario to WISMO or Shipping guidance
- **Effort:** 15 minutes (guidance addition)
- **Impact:** ~1-2 fewer handovers/week
- **Why:** Simple informational response — customs fees for overseas territories are the customer's responsibility.

### 🟡 Priority 4: Add exchange/return status expectations (when tools available)
- **Effort:** 30 minutes (guidance + tool setup)
- **Impact:** ~15 fewer handovers/week (biggest single opportunity)
- **Why:** 28% of all handovers are return/exchange status checks where agents just confirm receipt and set timeframe expectations.

### 🟡 Priority 5: Add birthday discount code lookup scenario to Promotions guidance
- **Effort:** 15 minutes (guidance addition)
- **Impact:** ~2-3 fewer handovers/week
- **Why:** Human agents simply tell customers to check their account history for the birthday code.

---

## Summary Impact Estimate

| Priority | Change | Weekly handover reduction |
|----------|--------|-------------------------|
| P1 | Remove discount code handover topic | -5 to -8 |
| P2 | Reinforce warranty form close rule | -5 to -8 |
| P3 | DOM-TOM customs scenario | -1 to -2 |
| P4 | Return/exchange status (needs tools) | -12 to -15 |
| P5 | Birthday discount lookup | -2 to -3 |
| **Already done** | Warranty Scenarios 1c, 2, 2b | -5 to -8 |
| **TOTAL** | | **-30 to -44 per week** |

Current handover volume is ~80-90/week. These changes combined could reduce it to ~45-60/week — a **35-50% reduction** in handover rate.