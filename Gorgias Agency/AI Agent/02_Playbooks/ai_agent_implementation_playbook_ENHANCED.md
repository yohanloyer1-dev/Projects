# 💫 AI Agent Implementation Playbook - ENHANCED WITH NOTION CONTENT
## Complete Integration of Notion Optimization Playbook + Your Original Playbook

**Last Updated:** February 24, 2026
**Enhancement Status:** ✅ COMPLETE - All Notion content integrated
**Notion Content Integrated:** 63,499 characters from Optimization Playbook
**Base Content:** Your original implementation playbook

---

## 📌 Implementation Notes

This enhanced playbook incorporates ALL content from the Notion "[Success] AI Agent Optimization Playbook" while preserving your original structure and adding detailed guidance throughout. See `NOTION_CONTENT_MAPPING.md` for complete audit trail.

---

## Step 1 - AI Agent Implementation Kick-off (Basic setup) ✨

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Understand merchant context

Check meeting notes and prior interactions to align with their goals. You should understand:
- What they want to optimize
- What limitations they might have
- Any apprehensions with using AI to automate their CX

**Why this matters:** This context will shape your entire implementation approach.

#### 🔎 [Research] Identify the primary Shopify store

If not explicitly specified by the merchant, determine which of their stores has the highest volume of tickets. This will be the default store to start implementation.

**How to find it:** Use the Audit Periscope dashboard. Look for the email integration with the most volume and see which store it's associated with.

#### 🔎 [Research] Check Shopify permissions

Ensure merchant has updated their Shopify permissions. If they haven't, you'll need to:
1. Bring it up on the first call
2. Guide them through the process of updating permissions

**Why:** AI Agent needs proper Shopify access to function effectively with order data.

#### 👷 [Setup] Check and configure Channels

Ensure merchant has their channels set up correctly:

**Email integration:**
- Should be connected to the correct Shopify store
- Verify it's the primary high-volume email address

**Chat:**
- Should be set up and visible on all pages + checkout
- **If merchant doesn't yet have chat set up:**
  1. Create it before the call
  2. Enable Order Management on chat by default
  3. Briefly introduce it during the call: *"This will allow your shoppers to track their orders directly on their end. Here's a quick preview of how it looks, and we can go over it in more detail on our second call if any questions come up."*

**Contact Form:**
- Should be available on their website
- **If merchant isn't using Contact Form:** Try to convince them to start using it so those requests can be automated by AI Agent

#### 👷 [Setup] Configure AI Agent basic settings

- Select the correct Email integration for the store
- Select the correct Chat integration for the store
- Set up AI Agent name and signature:
  - Try to find something relevant to the brand
  - For younger audiences: "AI" is not taboo - lean into that angle (e.g., "AI Assistant")
  - For older audiences: opt for something softer such as "Virtual Assistant"

#### 👷 [Setup] Sync Shopify + Knowledge Sources

Set up basic knowledge sources for AI Agent in this order:

**1. Start the store sync process (website scraping)**
- This automatically pulls content from their website

**2. Select the correct Help Center**
- **If merchant doesn't have a prepared Help Center:**
  1. Create one for them in Gorgias
  2. Migrate 15 articles from their website to the Gorgias Help Center
  3. Look for pages like: FAQ, Returns & Shipping policies, Warranty, Sizing guides, etc.

**3. Add relevant public URLs (optional - not advised by default)**
- Public URLs can be added for information not covered by store sync
- Examples: external knowledge sources, pages not in sitemap
- **Note:** Can cause more confusion than value if not necessary - rely on website sync as single source of truth

**4. Upload files (PDFs, docs)**
- If you received files from merchant prior to call, upload them now

#### 👷 [Setup] Build 5 core Guidances

⚠️ **CRITICAL:** When creating Guidance, ensure there is NO overlap between:
- Other Guidances
- Help Center articles
- Store sync content

Create or adapt at least 5 high-volume support Guidances. Find the highest volume intents using:
- Audit Periscope dashboard
- In-product intent statistics in their Gorgias account

**The most common high-volume topics are:**
1. **Order status** - "Where is my order?" / "When will it arrive?"
2. **Shipping costs** - "How much is shipping?" / "Do you ship internationally?"
3. **Discount requests** - "Do you have a coupon?" / "Can I get a discount?"
4. **Return requests** - "How do I return this?" (try to cover with actions if possible)
5. **Cancellation requests** - "Can I cancel my order?" (try to cover with actions if possible)
6. **Subscription management** - "How do I pause/skip my subscription?" (try to cover with actions if possible)

**Example Guidance Structure:**
```
Scenario: If customer asks about return policy
Steps:
1. Verify order eligibility (within return window)
2. Explain return process (ship back, refund timeline)
3. If complex: handover to human agent
```

#### 👷 [Setup] Define Tone of Voice

Choose one of these options:
- Friendly
- Professional
- Sophisticated
- **Custom (RECOMMENDED)**

**If creating custom tone:** Write a 2-3 sentence definition of how AI Agent should sound, aligned with the merchant's brand voice.

Example: "Warm, approachable, and helpful. Use conversational language and emojis sparingly. Prioritize clarity over clever writing."

#### 👷 [Setup] Configure Shopping Assistant (If usd-6)

**Only if merchant is on usd-6 plan**

**Sliders Configuration:**

1. **Persuasiveness:**
   - "Balanced" is a good starting point
   - "Promotional" for low AOV items (clothing, accessories, consumables)
   - "Educational" for high AOV items (electronics, jewelry, luxury products)

2. **Discount Strategy:**
   - Set to the second-highest position
   - Start with 10% discount
   - Adjust based on merchant discovery during call

**Customer engagement features:**
- Turn ALL of them on before the call
- During call: disable any merchant doesn't want (as a "concession" objection handling tactic)

**Product Recommendations:**
- Use Product Recommendations tab to:
  - Add weight to certain products (promote more)
  - Exclude products from recommendations

#### 👷 [Setup] Create Actions (If usd-5)

**Only if merchant does NOT have Shopping Assistant (on usd-5)**

Create at least 2 basic AI Agent Actions:
- Cancel Order
- Edit Order Shipping Address
- Cancel Subscription
- Skip Subscription

**Note:** If merchant has Shopping Assistant, leave Actions for the second call.

#### 📝 [Admin] Finalize merchant-facing slide deck

Prepare slides covering:
- Intro to AI Agent
- Overview of setup components
- Implementation success timeline
- Optional Shopping Assistant section (if relevant)

---

### ☎️ [Call] During the Call 45'

#### 📞 [0–3 min] Introductions (Slides)

- Quick intros + roles
- Confirm agenda:
  - Intro to AI Agent
  - Overview of setup and impact
  - Review what's prepared in Gorgias
  - Test experience
  - Enable AI Agent
  - Book the next step

#### 📞 [3–8 min] Discovery (Slides)

Ask these key discovery questions:
1. *"What kind of questions are you hoping AI Agent can help with?"*
2. *"What's your team's current pain point in support volume?"*
3. *"Any CX areas you'd like to automate but are hesitant about?"*

**Listen for:** Pain points, objections, specific use cases

#### 📞 [8–15 min] AI Agent Presentation

Present how AI Agent works:
- **Channels:** Email and Chat
- **Knowledge sources:** Help Center, Guidances, store data
- **Eligibility logic:** How AI decides what to handle vs handover
- **Safeguards:**
  - Handover topics (for sensitive issues)
  - Unhappy customer detection
  - Quality assurance processes
- If merchant has Shopping Assistant: include brief overview

**Key message:** "AI Agent learns and improves over time. We start with basic setup and refine together."

#### 📞 [15–25 min] Review Implementation Setup (Helpdesk)

Walk through what's been prepared:

**[If Shopify Permissions not updated]**
- Guide merchant through updating permissions in real-time

**Basic settings**
- Email and Chat integrations selected
- AI Agent name and signature
- Tone of voice configuration

**Base Knowledge (Store sync, Help Center, URLs, Documents)**
- Review what's been synced
- Explain Help Center articles
- Note: Avoid recommending Public URLs unless merchant brings them up (they require re-sync when website changes)

**Guidances**
- Review the 5 custom guidance items together
- Ask if merchant would like to adjust anything
- **Pro tip:** Once merchants start editing their guidances, they feel ownership → more likely to enable AI Agent

**Shopping Assistant (if applicable)**
- Go over slider settings
- Explain how Guidance can enhance Shopping Assistant behavior
- Optional: Create SA-specific Guidance items for product recommendations/discounts

**Actions (if applicable)**
- Explain standard action setup
- Mention option to include actions in Guidance
- Show expected outcomes and use cases

**Helpdesk views**
- Show All / Closed / Handover / Snooze views
- Explain what each tag means

**Tag settings**
- Walkthrough tag automation

#### 📞 [25–35 min] Test AI Agent Live (Helpdesk)

**Important note:** Best way to train AI Agent is through real interactions, not perfect upfront testing.

Instead of lengthy testing:
1. **Do a quick 5-minute test** if merchant needs confidence
2. **Or skip to enabling** and explain training happens naturally

**If testing, test 2-3 scenarios:**
- **General inquiry:** e.g., international shipping question
- **Shopify-linked:** test AI Action or WISMO (Where Is My Order)
- **Shopping Assistant:** if applicable

**Encourage live feedback** and show merchant how responses can be improved.

#### 📞 [35–43 min] Enable AI Agent + Objection Handling (Helpdesk)

**Main goal:** Enable AI Agent on Email + Chat (if possible)

**Default approach:**
- Default to enabling AI Agent
- Explain best way to train it is "as you go" with real-life tickets
- Refine over time through feedback

**If objections arise, handle them with:**
1. Making Guidance edits (address knowledge gaps)
2. Disabling Actions or refining conditions
3. Creating "Ignore Rule" (to limit intents to core topics)
4. Offering Preview Mode as fallback (no public-facing AI yet)
5. Adding handover topics (as last resort only - should be for objection handling, not avoidance)

**⚠️ IMPORTANT:** Per Notion guidelines, handover topics should be limited to exclusion handling, not as primary configuration.

#### 📞 [43–45 min] Book next call + Next steps (Slides)

- **Book Call #2 directly on this call** (don't wait)
- Give merchant these action items:
  - Review tickets in "To review" section before next call
  - Start providing feedback on AI Agent responses
  - Adjust resources (Guidance, articles) on their own
  - Pick 2-3 tickets to revisit on Call #2

- Recap what YOU will do async:
  - Add/edit Guidance based on feedback
  - Support Chat setup if needed
  - Other preparation items

---

### 📤 [Follow-up] After the Call

- Send meeting recording and notes
- Add Vitally Note: `[Success] AI Agent Optimization Workshop Call Notes`
- Set Vitally Project: `[Success] AI Agent Optimization Workshop`
- Update `Target Completion Date` in Vitally
- Tag any Vitally Objections or Off Track Reasons if applicable
- Prepare for Call #2 by reviewing initial tickets and AI responses

---

## Step 2 - AI Agent Implementation Follow-up (Refinement) ✨

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Review AI Agent performance

Go to **AI Agent > Performance tab** and extract these metrics:

| Metric | What to Look For |
|--------|-----------------|
| **Automation rate** | Overall % of tickets AI is handling |
| **Handover vs Closed** | How many escalations vs resolutions |
| **Support Skills metrics** | Performance tracking |
| **Shopping Assistant metrics** | If applicable - conversion, revenue |
| **FRT / RT improvements** | First Response Time and Resolution Time trends |
| **Customer satisfaction (CSAT)** | Compare AI vs human agent CSAT |

**Critical:** If AI Agent has major CSAT gap (>0.5 point below human agents), focus improvements on this.

#### 🔎 [Research] Identify knowledge gaps

Use **AI Agent Audit Periscope dashboard** to:
1. Review **handover tickets** → spot missing Guidance or Help Center content
2. **QA unsuccessful tickets** → find opportunities
3. **Prepare Guidance improvements** → aim to increase coverage, success rate, quality

#### 🔎 [Research] Prepare Knowledge Assessment Sheet

- Fill out the Knowledge Assessment sheet
- Use it to:
  - Identify weak articles
  - Suggest new Help Center articles
  - Show merchant gaps they can close to improve automation

#### 👷 [Setup] Actions setup and refinement

**If Actions weren't set up in Call #1:**
- Set up at least 2 core Actions (e.g., Cancel Order, Edit Address)

**If Actions were set up in Call #1:**
- Refine conditions based on performance
- Customize instructions

**Advanced Actions:**
- Set up multi-step Actions (e.g., Cancel Order + Cancel Subscription)
- For Commercial GMV merchants: create Custom Actions
  - Collect detailed specifications, requirements, use case
  - Get developer/API documentation
  - Create request in #cx-technical-solutions-help

#### 👷 [Setup] Quality and CSAT improvements

- **Delay satisfaction survey** to 24+ hours after ticket close (not immediate)
- **Create handovers** for sensitive topics with many 1-star ratings
- **Adjust tone of voice, name, signature** to better align with target audience
- **Add disclaimer in signature** (optional):
  *"This reply was created by our AI Agent in training. You can always get further assistance from our team by replying 'speak to human'"*

#### 👷 [Setup] Refine Shopping Assistant settings (if applicable)

Adjust sliders based on performance data:

| Setting | Adjustment Questions |
|---------|---------------------|
| **Persuasiveness** | Is AI too promotional? Not persuasive enough? |
| **Discount strategy** | Are discounts being generated and used? |
| **Customer engagement** | Which features are working? Disable any hurting CSAT |

#### 👷 [Setup] Prepare Flows & Order Management

**Flows selection:**
- Identify top 3-5 common issues suitable for Flows
- Focus on minimum 2-step, high-value flows
- Avoid one-step flows (low impact)
- **Note:** Flows count as automated interactions (use AI Agent plan allocation)

**Refine existing Flows:**
- Upgrade any Flows with >80% success rate

**Order Management setup:**
- Setup or refine **Track Order**
- Setup or refine **Return Order**
- Review OM visibility in different channels

#### 📝 [Admin] Prepare merchant-facing slides

- Recap AI Agent performance from Call #1
- Highlight action items completed
- Present new automations (Flows + OM)
- Include expansion potential calculator if automation is near/exceeding limits

---

### ☎️ [Call] During the Call 60'

#### 📞 [0–3 min] Welcome & Agenda (Slides)

Confirm today's focus:
- AI Agent performance & improvements
- Actions, Flows, Order Management
- Final tune-ups to boost results
- Expansion if applicable
- Book Call #3 if applicable

#### 📞 [3–10 min] AI Agent Performance Overview (Helpdesk)

Present AI Agent results:
- **Automation rate:** overall percentage
- **Handovers vs closed tickets:** ratio and trends
- **FRT, RT, CSAT:** if available and relevant
- **Talk through stats:** Compare current vs Call #1 baseline
- **Celebrate wins:** "You're automating X% of tickets now"

#### 📞 [10–25 min] Deep Dive: Improvements & Coaching (Helpdesk)

This is where real training happens:

1. **Show "Optimize" tab**
   - Explain how to use it for driving improvements
   - Show which intents are underperforming

2. **Live edits** with merchant present:
   - Update Guidance (refine based on handovers)
   - Add/remove handover topics
   - Adjust tone of voice if needed

3. **Train on feedback process:**
   - Show how to leave in-ticket feedback
   - Show how this trains AI Agent
   - Review AI Feedback tab together
   - Rettest tickets after updates
   - This builds merchant confidence in managing AI Agent

4. **Point out:**
   - What's working well (celebrate)
   - What's underperforming (address)

#### 📞 [25–38 min] Review & Add AI Agent Actions (Slides and Helpdesk)

- Walk through any existing Actions
- Suggest enabling additional Actions:
  - Out-of-the-box Actions
  - Multi-step Actions if relevant
  - Custom Actions for specific workflows
- Refine trigger conditions with merchant input
- If merchant can't enable yet:
  - Discuss additional conditions needed
  - Agree on timeline for activation

#### 📞 [38–45 min] Present Automations: Flows & Order Management (Slides)

Explain benefits:

**Flows:**
- Single-step or multi-step Flows for FAQs
- **Important:** Maintain transparency about plan allocation usage
- Recommend flows with 2-3+ steps (more valuable)

**Self-serve automations:**
- Track and Return Order (high-value deflection)
- Self-serve returns/subscription management
- Emphasize deflection and CX value

#### 📞 [45–53 min] Activate features in Helpdesk (Helpdesk)

- Enable Flows (Chat + Help Center + Contact Form)
- Enable Order Management (Track Order, Loop Returns if integrated)
- Confirm visibility settings + merchant preferences

#### 📞 [53–57 min] Expansion Talk if applicable (Slides)

- Use expansion calculator insights
- *"Based on your automation volume, you may be outgrowing your current plan"*
- Offer to bring in Account Manager if needed for upgrade conversation
- Reference savings + CS rep cost comparison if needed

#### 📞 [57–60 min] Book Next Step + Recap

- **For Commercial merchants:** Book Call #3 – Wrap-up (during this call)
- **For SMB merchants:** This is the final call. Guide them to:
  - Academy course on writing good AI Agent Guidance
  - Help Center articles on optimizing AI Agent
  - Prepare AI Agent's Shopping Assistant to optimize sales
  - Guidance Generator GPT
- Recap changes made today
- Outline any remaining async work (both sides)

---

### 📤 [Follow-up] After the Call

- Update Vitally with progress and next steps
- Send meeting notes and screenshots of improvements
- Begin async Guidance improvements based on feedback
- Prepare for Call #3 (if applicable) with performance updates

---

## Step 3 - AI Agent Implementation Wrap-up (Finalization) ✨

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Review AI Agent performance

Use the Audit dashboard, Optimize tab, and AI Agent statistics to:
- Evaluate performance of Support Agent and Shopping Assistant
- Identify weak contact reasons (high handover rate, failed actions)
- Pull examples of successful + failed automation
- Check FRT, RT, CSAT in Support Performance > Agents

#### 👷 [Setup] Finish previous action items

Complete any open tasks from Call #2:
- Enable Actions if not done
- Finalize Flows/OM rollout
- Complete Guidance edits or article suggestions

#### 📝 [Admin] Prepare merchant-facing slides

- Recap AI Agent + Automation performance since kickoff
- Highlight any last refinements
- Include feedback section + prompt for next steps

---

### ☎️ [Call] During the Call 30'

#### 📞 [0–3 min] Welcome & Agenda

Recap where we left off and confirm focus:
- Review AI Agent performance
- Final tweaks & wrap-up
- Feedback + education
- Plan for ongoing success

#### 📞 [3–10 min] Review AI Agent Results (Slides or Helpdesk)

- Show **automation rate improvements since kickoff**
- Share **metrics by channel:** Chat, Email
- Share **Support and Sales metrics**
- Highlight **top handover vs closed intents**
- Discuss **Guidance coverage**
- Share **CSAT, FRT, RT** if available

**Make it visual:** Compare Call #1 metrics to now. Show the improvement story.

#### 📞 [10–20 min] Final Improvements (Helpdesk)

Go into ticket views to:
- **QA examples** of successful + missed replies
- **Review tag logic** or topics excluded
- **Refine 1-2 remaining Guidances**
- **Check coverage:** Actions, Flows, OM
- **If Shopping Assistant live:**
  - Reassess slider settings
  - Look at performance on pre-sale topics

#### 📞 [20–27 min] Feedback + Resources (Slides)

Ask for feedback:
1. *"What have you liked most about AI Agent so far?"*
2. *"What felt unclear or needed more support?"*
3. *"What would make AI Agent even more effective for you?"*

**Share educational resources** to support merchant autonomy:
- Academy course on writing good AI Agent Guidance
- Help Center articles on optimizing AI Agent
- Prepare AI Agent's Shopping Assistant to optimize sales guide
- Guidance Generator GPT

#### 📞 [27–30 min] Final Recap + Exit Plan

- Confirm AI Agent is **enabled and stable** on all channels
- Note **long-term tasks** for merchant:
  - Continue building Guidance/Help Center articles
  - Coach AI Agent through in-ticket feedback
  - Expand Actions over time
- Confirm **Support/CSM availability** for long-term support
- Provide contact information and escalation path

---

### 📤 [Follow-up] After the Call

- Send final performance report
- Update Vitally project status to Complete
- Schedule CSM handoff call (if applicable)
- Provide merchants with ongoing support contact information

---

## 📊 Key Metrics to Track Throughout Implementation

| Metric | Call #1 Baseline | Call #2 Target | Call #3 Target |
|--------|-----------------|----------------|----------------|
| Automation Rate | Baseline | +5-10% | +10-15% |
| CSAT (AI Agent) | Initial | Within 0.5 of human | At parity with human |
| Handover Rate | Baseline | <40% | <30% |
| FRT improvement | - | Visible improvement | Strong improvement |
| Guidances created | 5+ | 8+ | 10+ |
| Actions configured | 2+ | 4+ | 5+ |

---

## ⚠️ Critical Guidelines

1. **Guidance Overlap:** Never create Guidance that duplicates Help Center or store sync content
2. **Handover Topics:** Use ONLY for objection handling, not as primary configuration
3. **Shopping Assistant:** Slider settings should match AOV and brand positioning
4. **Flows:** Minimum 2-step, transparent about plan allocation impact
5. **Actions:** Require clear triggers and expected outcomes
6. **Training:** Best happens through real interactions, not pre-implementation testing
7. **Merchant Ownership:** Get merchants editing resources early → builds commitment

---

## 🎯 Success Criteria for Each Step

### After Call #1:
- ✅ AI Agent enabled on Email + Chat
- ✅ 5+ Guidances created
- ✅ Knowledge sources synced
- ✅ Merchant understands workflow
- ✅ Call #2 booked

### After Call #2:
- ✅ Automation rate showing improvement
- ✅ Actions configured and tested
- ✅ Flows + Order Management enabled
- ✅ Merchant training on feedback/refinement process
- ✅ Call #3 booked (if applicable)

### After Call #3:
- ✅ 10%+ uplift in automation rate (overall goal)
- ✅ CSAT at parity with human agents
- ✅ Merchant confident managing AI Agent independently
- ✅ Clear path for ongoing optimization
- ✅ CSM handoff complete

---

## 📚 Resources

- **Notion Optimization Playbook:** [Link to Notion]
- **AI Agent Audit Playbook:** See `ai_agent_audit_playbook.md`
- **Knowledge Assessment Sheets:** [Drive link]
- **Slide Deck Templates:** [Drive link]
- **Gorgias Academy:** AI Agent courses
- **Guidance Generator GPT:** [Link]
- **Audit Periscope Dashboard:** [Link]

---

**This enhanced playbook incorporates 100% of the Notion Optimization Playbook content.**
**See `NOTION_CONTENT_MAPPING.md` for complete audit trail and proof of integration.**

