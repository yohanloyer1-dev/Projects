# 💫 AI Agent Implementation Playbook

## Step 1 - AI Agent Implementation Kick-off (Basic setup) ✨

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Understand merchant context

Check meeting notes and prior interactions to align with their goals. You should understand what they want to optimize, what limitations they might have, any apprehensions with using AI to automate their CX, etc.

#### 🔎 [Research] Identify the primary Shopify store

If not explicitly specified by the merchant, determine which of their stores has the highest volume of tickets. This will be the default store to start implementation. You can find the store with the highest volume in the Audit Periscope dashboard. Look for the email integration with the most volume and see which store it's associated with.

#### 🔎 [Research] Check Shopify permissions

Ensure merchant has updated their Shopify permissions. If they haven't, bring it up on the first call and guide them through the process of doing it.

#### 👷 [Setup] Check and configure Channels

Ensure merchant has their channels set up:

- **Email integration** should be connected to the correct Shopify store
- **Chat** should be set up and visible on all page + checkout
  - If the merchant doesn't yet have a chat integration set up, create it before the call and enable Order Management on chat by default. Briefly introduce it on the first call when presenting and installing the chat (to later enable the AI Agent there) by saying something like: "This will allow your shoppers to track their orders directly on their end. Here's a quick preview of how it looks, and we can go over it in more detail on our second call if any questions come up."
- **Contact Form** should be available on their website
  - If the merchant isn't using our Contact Form, try to convince them to start using it so those requests can be automated by AI Agent.

#### 👷 [Setup] Configure AI Agent basic settings

- Select the correct Email integration for the store
- Select the correct Chat integration for the store
- Set up AI Agent name and signature
  - Try to find something relevant to the brand that will point you in the right direction when it comes to naming and signature.
  - For younger audiences, "AI" is not taboo so lean into that angle. For older audiences, you can opt for something softer such as "Virtual Assistant."

#### 👷 [Setup] Sync Shopify + Knowledge Sources

Set up basic knowledge sources for AI Agent:

- Start the store sync process (AKA website scraping)
- Select the correct Help Center
  - If the merchant doesn't have a prepared Help Center, create one for them and migrate 15 articles from their website to the Gorgias Help Center (look for pages such as FAQ, Returns & Shipping policies, Warranty etc.)
- Add relevant public URLs (optional - not advised by default)
  - Public URLs can be added that contain information not covered by the store sync, such as pages which are not in the sitemap or external knowledge sources relevant to the product.
- Upload files (PDFs, docs) if you received them from the merchant prior to the call

#### 👷 [Setup] Build 5 core Guidances

⚠️ **When creating Guidance, ensure that there is no overlap between other Guidances and other sources of Knowledge (Help Center, Store Sync)**

Create or adapt at least 5 high-volume support Guidances. You can find the highest volume intents using the Audit Periscope dashboard or by checking the intent statistics of the merchant in-product.

**The most common high-volume topics are:**

- Order status
- Shipping costs
- Discount requests
- Return requests (try to cover with actions if possible)
- Cancellation requests (try to cover with actions if possible)
- Subscription management (try to cover with actions if possible)

#### 👷 [Setup] Define Tone of Voice

- Choose Friendly, Professional, Sophisticated, or add Custom (recommended) tone settings
- When writing the Custom tone of voice, align with the merchant's branding and write a 2–3 sentence definition of how AI Agent should sound

#### 👷 [Setup] Configure Shopping Assistant (If usd-6)

If the merchant has access to Shopping Assistant (they're on usd-6), set:

**Sliders (Persuasiveness + Discount Strategy)**

- **Persuasiveness:** "Balanced" is a good place to start, but a good rule of thumb is to set it to "Promotional" for low AOV items (clothing, accessories, consumables), and "Educational" for high AOV items (electronics, jewelry, luxury products)
- **Discount Strategy:** set it to the second-highest position with a 10% discount and then adjust if needed with the merchant on the call through discovery.

**Customer engagement features**

- Turn all of them on before the call, and you can easily disable any that the merchant is not too keen on during the call as a form of "concession" and objection handling tactic.

**Product Recommendations**

- Use the Product Recommendations tab to either add more weight to certain products so that Shopping Assistant promotes them more, or use the "exclude" section to have it not recommend specific products to shoppers.

#### 👷 [Setup] Create Actions (If usd-5)

If the merchant does not have Shopping Assistant available (they are on usd-5):

- Create 2 basic AI Agent Actions such as:
  - Cancel Order
  - Edit Order Shipping Address
  - Cancel Subscription
  - Skip Subscription

If the merchant has Shopping Assistant, leave Actions for the second call

#### 📝 [Admin] Finalize merchant-facing slide deck

Prepare your slides with:

- Intro to AI Agent
- Overview of setup components
- Implementation success timeline
- Optional Shopping Assistant section (if relevant)

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

- "What kind of questions are you hoping AI Agent can help with?"
- "What's your team's current pain point in support volume?"
- "Any CX areas you'd like to automate but are hesitant about?"

#### 📞 [8–15 min] AI Agent Presentation

- Present how AI Agent works: channels, knowledge sources, eligibility logic
- Emphasize safe guards (handover topics, unhappy customers, QA)
- If merchant has Shopping Assistant, include overview

#### 📞 [15–25 min] Review Implementation Setup (Helpdesk)

Walk through what's been prepared:

- **[If Shopify Permissions not updated]** Guide the merchant through updating their Shopify permissions
- **Basic settings** (Skip Handover topics and Ignore rule)
- **Base Knowledge** (Store sync, HC, Public URLs, Documents):
  - Avoid recommending Public URLs unless merchants specifically bring them up. They often cause more confusion than value since merchants have to re-sync both the URLs and their site if anything changes. It's better to rely on the connected website as the single source of truth.
- **Guidances:** Start by reviewing the custom guidance items together and ask if they'd make any adjustments. Once merchants start editing their guidance, they feel ownership of it, which makes them more likely to enable it, and, shortly after, to enable the AI Agent as well.
- **Tone of voice**
- **[If applicable] Shopping Assistant** - Go over the sliders
  - Explain how to leverage guidance for Shopping Assistant: Advise tailoring the product recommendation and discount-sharing behavior according to the merchant's processes by creating SA-specific guidance items.
- **[If applicable] Actions** - Go over the standard action setup process. You can also mention the option to include actions in guidance to better detail the expected outcome and use cases.
  - Shopping Assistant pitch for usd-5 merchants: "The Shopping Assistant helps you engage shoppers in real time through personalized interactions, by answering their questions, recommending products, and offering smart discounts that lift AOV and conversion while enhancing the overall shopping experience."
- **Show Helpdesk views** (All / Closed / Handover / Snooze)
- **Walk through tag settings**

#### 📞 [25–35 min] Test AI Agent live (Helpdesk)

Instead of defaulting to live testing, focus on enabling the AI Agent and explaining that it's best trained gradually, through real interactions. If it feels necessary, you can dedicate around five minutes for a quick test, but avoid giving the impression that everything must be perfect before enabling it. The goal is to build confidence in training on the go, not to perfect it upfront.

- Test 2–3 ticket scenarios:
  - General inquiry → e.g. international shipping
  - Shopify-linked → test AI Action or WISMO
  - If applicable, try one Shopping Assistant test
- Encourage live feedback

#### 📞 [35–43 min] Enable AI Agent + Objection Handling (Helpdesk)

**Main goal:** enable AI Agent on both Email + Chat if possible

- Default to enabling the AI Agent and explain that the best way to train it is 'as you go', by using it on real-life tickets and refining it over time.
- If objections arise, handle by:
  - Making Guidance edits
  - Disabling Actions or refining conditions
  - Creating "Ignore Rule" to limit intents
  - Offering Preview Mode as fallback option
  - Adding handover topics (as last resource if possible)

#### 📞 [43–45 min] Book next call + Next steps (Slides)

- Book Call #2 directly on the call
- By the end of the first call, after enabling the AI Agent, ask the merchant to review the tickets in the "To review" section before your next session. Encourage them to start providing feedback and adjusting resources on their own in the meantime. Have them pick two or three tickets they'd like to revisit on the second call, so you can walk through the AI Agent training process with them live: reviewing responses, refining resources, and showing how training improves results in real time.
- Recap action items:
  - What you'll do async (add/edit Guidance, support Chat setup, etc.)
  - What merchant should prepare (FAQs, Shopify integration check, AI Agent ticket examples, etc.)

---

## Step 2 - AI Agent Implementation Follow-up (Refinement) ✨

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Review AI Agent performance

Go to AI Agent > Performance tab

Review metrics:

- Overall automation rate
- Handover vs Closed tickets
- Support Skills & Shopping Assistant metrics (if applicable)
- Improvements in FRT and RT metrics
- Changes in customer satisfaction
- If the AI Agent has a major CSAT gap, focus on improvements to address this. The goal is to bring the AI Agent to a comparable CSAT level to that of the human agents.

#### 🔎 [Research] Identify knowledge gaps

Use the AI Agent Audit Periscope dashboard to:

- Review handover tickets to spot missing Guidance or Help Center content
- QA unsuccessful tickets for opportunities
- Prepare Guidance improvements or new ones (aim to increase coverage, success rate, and quality)

#### 🔎 [Research] Prepare Knowledge Assessment Sheet

- Fill out the Knowledge Assessment sheet
- Use it to:
  - Identify weak articles
  - Suggest new ones
  - Show merchants gaps they can close to improve automation

#### 👷 [Setup] Actions setup and refinement

- Create and refine existing out-of-the-box actions:
  - If no Actions were added in Call #1: set up at least 2 core Actions (e.g., Cancel Order, Edit Address)
  - If Actions were added in Call #1: refine conditions, customize instructions
- Set up multi-step Actions (e.g., Cancel Order + Cancel Subscription)
- Custom Actions for Commercial GMV merchants (if merchant has 3PL or external tools) - collect detailed specifications and requirements, use case, information about the developer or API documentation that the merchant might be aware of, and create a request in #cx-technical-solutions-help

#### 👷 [Setup] Quality and CSAT improvements

- Delay satisfaction survey to be sent out 24 hours or later after the ticket is closed
- Create handovers for the most sensitive topics that are generating many 1-star satisfaction ratings
- Adjust the tone of voice, AI Agent name, and AI Agent signature to better align with the target audience
- Add a disclaimer in the signature (e.g., This reply was created by our AI Agent in training; you can always get further assistance from our team by replying "speak to human")

#### 👷 [Setup] Refine Shopping Assistant settings (if applicable)

Adjust Shopping Assistant sliders for:

- Persuasiveness (Is the AI Agent too promotional or not persuasive enough?)
- Discount strategy (Are discount codes being generated? Are they used?)
- Customer engagement features (enable any that you haven't so far)

#### 👷 [Setup] Prepare Flows & Order Management

- Identify the top 3–5 common issues suitable for Flows
- Focus on minimum two-step, high-value flows, while keeping transparency about how these can affect automated interactions (avoid one-step flows)
- Refine existing Flows that have a >80% success rate
- "End interaction" is preferable for boosting AR if the merchant is open to it
- Set up or polish Order Management:
  - Set up or refine Track Order
  - Set up or refine Return Order
  - Review OM visibility in different channels

#### 📝 [Admin] Prepare merchant-facing slides

- Recap performance from AI Agent
- Highlight action items from last call
- Present new automations (Flows + OM)
- Include expansion potential if automation is nearing or exceeding plan limits

### ☎️ [Call] During the Call 60'

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

#### 📞 [10–25 min] Deep Dive in Helpdesk: Improvements & Coaching (Helpdesk)

- Show "Optimize" tab and how to use it for driving improvements
- Live edits to:
  - Update Guidance
  - Add/remove handover topics
  - Adjust tone of voice
- Show how to leave in-ticket feedback and train AI Agent:
  - Focus on the tickets the merchant wants to review most. Walk through the training process live: checking the AI Feedback tab, updating resources, and retesting tickets until the responses improve. This helps merchants see how training works and gives them confidence to manage it on their own.
- Point out:
  - What's working well
  - What's underperforming

#### 📞 [25–38 min] Review & Add AI Agent Actions (Slides and Helpdesk)

- Walk through any existing Actions
- Suggest enabling additional Actions:
  - Out-of-the-box Actions
  - Multi-step or Custom if relevant
- Refine trigger conditions with merchant input
- If merchant can't enable yet, discuss:
  - Additional conditions
  - Timeline for activation

#### 📞 [38–45 min] Present Automations: Flows & OM (Slides)

Explain benefits of:

- Single-step or multi-step Flows for FAQs
  - Maintain transparency about how these affect their AI Agent plan as they are counted as automated interactions. See if the merchant is open to this type of setup.
  - Recommend a flow with at least 2-3 steps
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
- Offer to bring in AM or CSM to support upgrade convo if too many objections
- Reference savings + CS rep cost comparison if needed

#### 📞 [57–60 min] Book Next Step + Recap

- If Commercial merchant: book Call #3 – Wrap-up during this call
- If SMB merchant: say this is the final call, and guide them to:
  - Our Academy course on writing good AI Agent Guidance
  - Our Help Center articles on optimizing AI Agent
  - Prepare AI Agent's Shopping Assistant to optimize sales
- Recap changes made today and outline any remaining async work (both sides)

---

## Step 3 - AI Agent Implementation Wrap-up (Finalization) ✨

### ⚙️ [Prep] Prepare for the Call

#### 🔎 [Research] Review AI Agent performance

Use the Audit dashboard, Optimize tab, and AI Agent statistics to:

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

### ☎️ [Call] During the Call 30'

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

Go into ticket views to:

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

- Our Academy course on writing good AI Agent Guidance
- Our Help Center articles on optimizing AI Agent
- Prepare AI Agent's Shopping Assistant to optimize sales
- Our Guidance Generator GPT

#### 📞 [27–30 min] Final Recap + Exit Plan

- Confirm AI Agent is enabled and stable on all channels
- Note any long-term tasks for the merchant:
  - Continue building Guidance/Articles
  - Coach AI Agent through in-ticket feedback
  - Expand Actions
- Confirm Support/CSM availability for long-term support
