# 🎯 [Success] AI Agent Optimization Playbook ✨

**Source:** https://www.notion.so/1d81ae2178f5809b89efd4eebebaaaf0  
**Last Updated (Notion):** February 10, 2026  
**Version:** v1_LATEST (Extracted February 24, 2026)

---

## 🎯 Context

The goal of this playbook is to create a comprehensive and standardized workflow of bringing merchants to a 10% uplift in global automation rate using AI Agent (Support Agent + Shopping Assistant), supplemented by other Automation Features.

---

## 🚀 Methodology

### Resources & Tools

When using these resources, keep in mind:

- **Calendly:** Always share links with UTM included
- **Macros:** Edit the macro and make it merchant-specific before sharing
- **Vitally:** Document all key notes and discovery items
- **Templates:** Use the pre-built merchant-facing templates provided

### Key Tools Referenced

- Vitally notes and timeline tracking
- Calendly booking links
- Merchant-facing templates
- Performance metrics and dashboards

---

## Step 1: Kick-off (45 minutes)

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Understand merchant context

Check meeting notes and prior interactions to align with their goals:

- What do they want to optimize?
- What limitations might they have?
- Any apprehensions with using AI to automate their CX?
- Previous automation or AI experience

#### 🔎 [Research] Identify the primary Shopify store

If not explicitly specified, determine which store has the highest ticket volume:

- Use the Audit Periscope dashboard
- Look for the email integration with the most volume
- Identify which store it's associated with
- This will be the default store to start implementation

#### 🔎 [Research] Check Shopify permissions

Ensure merchant has updated their Shopify permissions:

- If not done yet, include this as part of the first call
- Guide them through updating permissions
- Confirm they can complete Shopify auth flow

#### 👷 [Setup] Check and configure Channels

Ensure merchant has proper channel setup:

- **Email integration** connected to the correct Shopify store
- **Chat** set up and visible on all pages + checkout
  - If not yet set up, create chat integration before the call
  - Enable Order Management on chat by default
  - Brief introduction on first call: "This allows shoppers to track orders directly"
- **Contact Form** available on their website
  - If not using Gorgias contact form, try to convince them to start
  - Enables automation of contact form requests via AI Agent

#### 👷 [Setup] Configure AI Agent basic settings

- Select the correct Email integration for the store
- Select the correct Chat integration for the store
- Set up AI Agent name and signature
  - Find something relevant to the brand
  - For younger audiences: lean into "AI" terminology
  - For older audiences: use softer terms like "Virtual Assistant"

#### 👷 [Setup] Sync Shopify + Knowledge Sources

- Start the store sync process (website scraping)
- Select the correct Help Center
  - If merchant doesn't have prepared Help Center, create one
  - Migrate 15+ articles from their website
  - Focus on: FAQ, Returns & Shipping policies, Warranty
- Add relevant public URLs (optional - not advised by default)
  - Only if merchant has info not covered by store sync
  - Example: External knowledge sources not in sitemap
- Upload files (PDFs, docs) if received prior to the call

#### 👷 [Setup] Build 5 core Guidances

⚠️ **Critical:** Ensure no overlap between Guidances and other Knowledge sources (Help Center, Store Sync)

Create or adapt at least 5 high-volume support Guidances:

- Find highest volume intents using Audit Periscope or merchant in-product stats
- **Most common high-volume topics:**
  - Order status
  - Shipping costs
  - Discount requests
  - Return requests (cover with actions if possible)
  - Cancellation requests (cover with actions if possible)
  - Subscription management (cover with actions if possible)

#### 👷 [Setup] Define Tone of Voice

- Choose: Friendly, Professional, Sophisticated, or Custom (recommended)
- For custom tone: Write 2–3 sentence definition
- Align with merchant's branding
- Guide how AI Agent should communicate

#### 👷 [Setup] Configure Shopping Assistant (If USD-6)

If merchant has USD-6 access with Shopping Assistant:

**Sliders (Persuasiveness + Discount Strategy)**

- **Persuasiveness:**
  - "Balanced" is good starting point
  - Rule of thumb:
    - "Promotional" for low AOV items (clothing, accessories, consumables)
    - "Educational" for high AOV items (electronics, jewelry, luxury)
- **Discount Strategy:** Set to second-highest position with 10% discount
  - Adjust with merchant during discovery call

**Customer Engagement Features**

- Turn all on before the call
- Easily disable any merchant objects to during call (concession tactic)

**Product Recommendations**

- Use Product Recommendations tab to add weight to certain products
- Use "exclude" section to prevent recommending specific products

#### 👷 [Setup] Create Actions (If USD-5)

If merchant does NOT have Shopping Assistant (USD-5):

- Create 2 basic AI Agent Actions:
  - Cancel Order
  - Edit Order Shipping Address
  - Cancel Subscription
  - Skip Subscription

If merchant HAS Shopping Assistant: Leave Actions for the second call

#### 📝 [Admin] Finalize merchant-facing slide deck

Prepare slides with:

- Intro to AI Agent
- Overview of setup components
- Implementation success timeline
- Optional Shopping Assistant section (if relevant)

---

### ☎️ [Call] During the Call (45 minutes)

#### 📞 [0–3 min] Introductions (Slides)

- Quick intros and roles
- Confirm agenda:
  - Intro to AI Agent
  - Overview of setup and impact
  - Review what's prepared in Gorgias
  - Test experience
  - Enable AI Agent
  - Book the next step

#### 📞 [3–8 min] Discovery (Slides)

- "What kind of questions are you hoping AI Agent can help with?"
- "What's your team's current pain point in support volume?"
- "Any CX areas you'd like to automate but are hesitant about?"

#### 📞 [8–15 min] AI Agent Presentation

- Present how AI Agent works:
  - Channels (Email, Chat)
  - Knowledge sources
  - Eligibility logic
- Emphasize safeguards:
  - Handover topics for escalation
  - Unhappy customer detection
  - QA processes
- If merchant has Shopping Assistant: Include overview

#### 📞 [15–25 min] Review Implementation Setup (Helpdesk)

Walk through what's been prepared:

- **[If Shopify Permissions not updated]** Guide through updating permissions
- **Basic settings**
  - Skip Handover topics and Ignore rule
- **Base Knowledge** (Store sync, HC, Public URLs, Documents)
  - Note: Avoid recommending Public URLs unless merchant brings them up
  - URLs often cause confusion when things change
  - Rely on connected website as single source of truth
- **Guidances**
  - Review custom guidance items together
  - Ask if they'd make adjustments
  - When merchants start editing, they feel ownership
  - Increases likelihood to enable AI Agent
- **Tone of voice**
- **[If applicable] Shopping Assistant** - Go over sliders
  - Explain how to leverage guidance for Shopping Assistant
  - Tailor product recommendation and discount behavior
  - Use SA-specific guidance items
- **[If applicable] Actions** - Go over standard action setup
  - Mention option to include actions in guidance
  - Detail expected outcomes and use cases
  - Shopping Assistant pitch for USD-5 merchants: "The Shopping Assistant helps you engage shoppers in real time through personalized interactions, by answering their questions, recommending products, and offering smart discounts that lift AOV and conversion while enhancing the overall shopping experience."
- **Show Helpdesk views** (All / Closed / Handover / Snooze)
- **Walk through tag settings**

#### 📞 [25–35 min] Test AI Agent Live (Helpdesk)

Instead of defaulting to live testing, focus on enabling AI Agent.

- Explain it's best trained gradually through real interactions
- Only do quick testing (5 min) if necessary
- Avoid impression everything must be perfect before enabling
- Build confidence in "train as you go" approach

Test 2–3 ticket scenarios:

- General inquiry (e.g., international shipping)
- Shopify-linked (test AI Action or WISMO)
- If applicable: Try one Shopping Assistant test

Encourage live feedback and iteration

#### 📞 [35–43 min] Enable AI Agent + Objection Handling (Helpdesk)

**Main goal:** Enable AI Agent on Email + Chat if possible

**Default to enabling AI Agent:**

- Explain best way to train is 'as you go' on real-life tickets
- Refine over time through use

**If objections arise, handle by:**

- Making Guidance edits
- Disabling Actions or refining conditions
- Creating "Ignore Rule" to limit intents
- Offering Preview Mode as fallback option
- Adding handover topics (last resort if possible)

#### 📞 [43–45 min] Book next call + Next steps (Slides)

- Book Call #2 directly on the call
- Ask merchant to review tickets in "To review" section before next session
- Encourage them to start providing feedback
- Have them pick 2–3 tickets to revisit on second call
- Will walk through AI Agent training live on second call

**Recap action items:**

- What you'll do async (add/edit Guidance, setup Chat, etc.)
- What merchant should prepare (FAQs, Shopify checks, ticket examples, etc.)

---

## Step 2: Follow-up (60 minutes)

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Review AI Agent performance

Go to AI Agent > Performance tab and review:

- Overall automation rate
- Handover vs Closed tickets
- Support Skills & Shopping Assistant metrics (if applicable)
- Improvements in FRT and RT metrics
- Changes in customer satisfaction
- If major CSAT gap: Focus on improvements to match human agent CSAT

#### 🔎 [Research] Identify knowledge gaps

Use the AI Agent Audit Periscope dashboard:

- Review handover tickets for missing Guidance or Help Center content
- QA unsuccessful tickets for opportunities
- Prepare Guidance improvements or new ones
- Aim to increase coverage, success rate, and quality

#### 🔎 [Research] Prepare Knowledge Assessment Sheet

- Fill out the Knowledge Assessment sheet
- Identify weak articles
- Suggest new ones
- Show merchants gaps they can close to improve automation

#### 👷 [Setup] Actions setup and refinement

- Create and refine existing out-of-the-box actions:
  - If no Actions added in Call #1: Set up at least 2 core Actions (Cancel Order, Edit Address)
  - If Actions were added: Refine conditions, customize instructions
- Set up multi-step Actions (e.g., Cancel Order + Cancel Subscription)
- Custom Actions for Commercial GMV merchants
  - Collect detailed specifications and requirements
  - Document use case and developer/API information
  - Create request in #cx-technical-solutions-help

#### 👷 [Setup] Quality and CSAT improvements

- Delay satisfaction survey to 24+ hours after ticket close
- Create handovers for most sensitive topics generating 1-star ratings
- Adjust tone of voice, AI Agent name, signature for target audience
- Add disclaimer in signature: "This reply was created by our AI Agent in training; you can always get further assistance from our team by replying 'speak to human'"

#### 👷 [Setup] Refine Shopping Assistant settings (if applicable)

Adjust Shopping Assistant sliders:

- **Persuasiveness:** Is the AI too promotional or not persuasive enough?
- **Discount strategy:** Are discount codes being generated? Are they used?
- **Customer engagement features:** Enable any not yet enabled

#### 👷 [Setup] Prepare Flows & Order Management

- Identify top 3–5 common issues suitable for Flows
- Focus on minimum two-step, high-value flows
- Keep transparency about automation effect (avoid one-step flows)
- Refine existing Flows with >80% success rate
- Prefer "End interaction" for boosting automation rate (if merchant open)
- Set up or polish Order Management:
  - Set up or refine Track Order
  - Set up or refine Return Order
  - Review Order Management visibility in different channels

#### 📝 [Admin] Prepare merchant-facing slides

- Recap performance from AI Agent
- Highlight action items from last call
- Present new automations (Flows + OM)
- Include expansion potential if nearing plan limits

---

### ☎️ [Call] During the Call (60 minutes)

#### 📞 [0–3 min] Welcome & Agenda (Slides)

Confirm today's focus:

- AI Agent performance & improvements
- Actions, Flows, Order Management
- Final tune-ups to boost results
- Expansion if applicable
- Book next call or wrap-up

#### 📞 [3–10 min] AI Agent Performance Overview (Helpdesk)

Present AI Agent results:

- Automation rate, handovers, closed tickets
- FRT, RT, CSAT if available
- Talk through Helpdesk stats and views
- Compare to kickoff goals

#### 📞 [10–25 min] Deep Dive: Improvements & Coaching (Helpdesk)

- Show "Optimize" tab and how to use it
- Live edits to:
  - Update Guidance
  - Add/remove handover topics
  - Adjust tone of voice
- Show how to leave in-ticket feedback and train AI Agent:
  - Focus on tickets merchant wants to review most
  - Walk through training process live
  - Check the AI Feedback tab
  - Update resources
  - Retest tickets until responses improve
  - Helps merchants see how training works
  - Gives confidence to manage on their own
- Point out:
  - What's working well
  - What's underperforming

#### 📞 [25–38 min] Review & Add AI Agent Actions (Slides and Helpdesk)

- Walk through any existing Actions
- Suggest enabling additional Actions:
  - Out-of-the-box Actions
  - Multi-step or Custom if relevant
- Refine trigger conditions with merchant input
- If merchant can't enable yet:
  - Discuss additional conditions
  - Timeline for activation

#### 📞 [38–45 min] Present Automations: Flows & OM (Slides)

Explain benefits of:

- Single-step or multi-step Flows for FAQs
  - Maintain transparency about automation plan impact
  - See if merchant is open to this setup
  - Recommend flow with at least 2-3 steps
- Self-serve Track and Return Order
- Self-serve returns/subscription
- Emphasize deflection and CX value

#### 📞 [45–53 min] Activate features in Helpdesk (Helpdesk)

- Enable Flows (Chat + Help Center + Contact Form)
- Enable Order Management (Track Order, Loop Returns if integrated)
- Confirm visibility settings + preferences

#### 📞 [53–57 min] Expansion Talk if applicable (Slides)

- Use expansion calculator insights
- "Based on your automation volume, you may be outgrowing your current plan"
- Offer to bring in AM or CSM if too many objections
- Reference savings + CS rep cost comparison if needed

#### 📞 [57–60 min] Book Next Step + Recap

- **If Commercial merchant:** Book Call #3 – Wrap-up during this call
- **If SMB merchant:** Say this is the final call, guide them to:
  - Academy course on writing good AI Agent Guidance
  - Help Center articles on optimizing AI Agent
  - Shopping Assistant optimization for sales
- Recap changes made today
- Outline any remaining async work (both sides)

---

## Step 3: Wrap-up (30 minutes)

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Review AI Agent performance

Use the Audit dashboard, Optimize tab, and AI Agent statistics:

- Evaluate performance of Support Agent and Shopping Assistant
- Identify weak contact reasons (handover rate, failed actions)
- Pull examples of successful + failed automation
- Check FRT, RT, CSAT (Support Performance > Agents)

#### 👷 [Setup] Finish previous action items

Complete any open tasks from Call #2:

- Enable Actions if not done
- Finalize Flows/OM rollout
- Complete Guidance edits or article suggestions

#### 📝 [Admin] Prepare merchant-facing slides

- Recap AI Agent + Automation performance
- Highlight any last refinements
- Include feedback section + prompt for next steps

---

### ☎️ [Call] During the Call (30 minutes)

#### 📞 [0–3 min] Welcome & Agenda

Recap where we left off and confirm focus:

- Review AI Agent performance
- Final tweaks & wrap-up
- Feedback + education

#### 📞 [3–10 min] Review AI Agent Results (Slides or Helpdesk)

- Show automation rate improvements since kickoff
- Share metrics by channel (Chat, Email)
- Share Support and Sales metrics
- Highlight top handover vs closed intents
- Discuss Guidance coverage
- Share CSAT, FRT, RT if available

#### 📞 [10–20 min] Final Improvements (Helpdesk)

Go into ticket views:

- QA examples of successful + missed replies
- Review tag logic or topics excluded
- Refine 1–2 remaining Guidances
- Check on Actions, Flows, OM coverage
- If Shopping Assistant is live:
  - Reassess slider settings
  - Look at performance on pre-sale topics

#### 📞 [20–27 min] Feedback + Resources (Slides)

Ask:

- "What have you liked most about AI Agent so far?"
- "What felt unclear or needed more support?"
- "What would make AI Agent even more effective for you?"

Share educational resources to support merchant autonomy:

- Academy course on writing good AI Agent Guidance
- Help Center articles on optimizing AI Agent
- Shopping Assistant optimization for sales
- Guidance Generator GPT

#### 📞 [27–30 min] Final Recap + Exit Plan

- Confirm AI Agent is enabled and stable on all channels
- Note any long-term tasks for the merchant:
  - Continue building Guidance/Articles
  - Coach AI Agent through in-ticket feedback
  - Expand Actions
- Confirm Support/CSM availability for long-term support

---

## 📊 Auditing Accounts

### Key Questions to Ask During Audit

1. What's their current automation rate?
2. What are the top handover intents?
3. How is CSAT comparing to human agents?
4. Are they using all available features?
5. What's missing from their Guidance?

### Metrics to Track

- Automation rate trend
- Handover rate by intent
- CSAT by channel
- Actions usage
- Flows activation

---

**For questions about this playbook, refer to the README.md in NOTION_SOURCES/ folder.**

