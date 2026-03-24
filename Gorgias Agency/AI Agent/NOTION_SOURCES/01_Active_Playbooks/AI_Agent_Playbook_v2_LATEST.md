# 📖 AI Agent Playbook

**Source:** https://www.notion.so/2461ae2178f5804fae7fe627d2355ed0  
**Last Updated (Notion):** October 16, 2025  
**Version:** v2_LATEST (Completely Re-extracted February 24, 2026)

---

## Purpose

This playbook is designed to help you understand, operate, and optimize Gorgias AI Agent. Whether you're just launching your AI Agent, refining its performance, or scaling to new use cases, this guide outlines the **why**, **what**, and **how** behind an intelligent, brand-aligned, and revenue-generating customer experience.

---

## Objective

- Resolve high volumes of repetitive tickets automatically.
- Provide accurate, instant answers through both email and chat
- Reduce handle time and improve response consistency on email.
- Scale your support team's productivity without adding headcount.
- Deliver delightful experiences through accurate, personalized replies.

---

## Setup & Configuration ⚙️

### 1. Requirements ✅

Before you begin:

- [ ] You have an active **AI Agent subscription** (`on usd-6`)
- [ ] Your **Shopify store** is connected to Gorgias
- [ ] You have **Lead, Admin, or Account Owner** permissions in Gorgias
- [ ] You are **Admin in Shopify** (to update permissions)
- [ ] Go to **Settings → My Apps → Shopify**
- [ ] Select your store, then click **Update App Permissions**
- [ ] Sign into Shopify to confirm permissions

⚠️ **Note:** AI Agent can only access the last 10 orders per customer.

---

### 2. [Train] Onboard AI Agent with Knowledge ✅

AI Agent needs at least one knowledge source before it can go live.

- [ ] Go to **AI Agent → Knowledge**
- [ ] Select your store
- [ ] Add these resources:
  - Sync your Shopify store ⭐
  - **Guidance** ⭐
  - Help Center ⭐
  - Public URLs
  - Uploaded documents (e.g., PDFs, FAQs)

---

### 3. [Train] Customize AI Agent ✅

Tailor how AI Agent communicates to reflect your brand.

- [ ] Choose a tone of voice
- [ ] Add an email signature (max 250 characters)
- [ ] Instruct when to handover tickets to human agents
- [ ] Enable auto-tagging
- [ ] Adjust selling style and discounts (if using Shopping Assistant)

---

### 4. [Test] Test AI Agent Responses ✅

Use the testing environment to preview AI behavior on Email and Chat.

- [ ] Go to **AI Agent → Test**
- [ ] Choose a channel (Email or Chat)
- [ ] Run sample conversations
- [ ] Identify and fix gaps in knowledge or behavior

💡 **Tip:** Tests do not impact customers, reporting, or integrations.

---

### 5. [Deploy] Connect Channels & Go Live ✅

AI Agent must be connected to **at least one** support channel to operate.

#### ✉️ Enable on Email

- [ ] Go to **AI Agent → Settings → Channels**
- [ ] Under **Email**, select one or more addresses
- [ ] Add a unique **Email signature**
- [ ] Toggle **Enable AI Agent on Email**
- [ ] Click **Save Changes**

💡 **Tip:** Agent also handles tickets from Order Management, Flows, and contact forms linked to the email.

#### 💬 Enable on Chat

- [ ] Go to **AI Agent → Settings → Channels**
- [ ] Under **Chat**, select one or more chats (site, Help Center, checkout)
- [ ] Configure **handover instructions** for escalation
- [ ] Toggle **Enable AI Agent on Chat**
- [ ] Click **Save Changes**

---

### 6. [Analyze] Monitor AI Agent Views in Inbox ✅

Track what the AI is doing using default Views in the Tickets menu:

| View Name | Tag | Description |
|-----------|-----|-------------|
| **All** | — | All AI Agent-processed tickets |
| **Processing** | `ai_processing` | Tickets being handled now |
| **Close** | `ai_close` | Tickets closed by AI |
| **Handover** | `ai_handover` | Tickets escalated to human team |
| **Ignore** | `ai_ignore` | Ignored by AI (optional rule) |
| **Snooze** | `ai_snooze` | Waiting for shopper response (3-day timer before auto-close) |

🔎 **Access:** Tickets → AI Agent in the sidebar.

---

## Knowledge Sources

AI Agent needs at least one knowledge source before it can go live.

### Configuring Knowledge Sources

**Shopify Sync** ⭐
- Enabled automatically when you activate AI Agent
- Provides: Product descriptions, order details, inventory status
- Requires: Valid Shopify app permissions

**Guidance** ⭐ (Most Important)
- Custom instructions you write specifically for AI Agent
- Best for: Company policies, edge cases, tone customization

**Help Center** ⭐
- Articles published in your Gorgias Help Center
- Best for: Public-facing information (FAQs, shipping, returns, etc.)

**Public URLs**
- External webpages AI Agent can reference
- Best for: When information is not in Help Center or docs

**Uploaded Documents**
- PDFs, Word docs, or plain text files
- Best for: Internal policies, detailed procedures, compatibility charts

---

## Guidance Best Practices

### When to use Guidance

Use Guidance to:
- Handle **internal policies** not published in your Help Center
- Navigate **gray area** scenarios like feedback, thank-you notes, or press inquiries
- Clarify **ambiguous topics**
- Replace **missing Help Center articles** during setup
- Customize how AI responds when using **Actions**

### How to write Guidance

#### Structure & Format

Follow this consistent format:

1. **Scenario Label** (e.g., "Scenario 1")
2. **Title** that starts with "If the shopper…" or "When the shopper…"
3. **Step-by-step resolution**
   - Use numbered steps
   - Sub-bullets for clarification

#### Use the Right Variables

**Shopify:**
- `order number`, `order name`, `shipping address`, `tracking link`
- `order date`, `package status`, `item list`, etc.

**Ticket data:**
- `ticket subject`, `ticket creation date`
- `shopper says: [x]`, `agent says: [x]`

Avoid vague conditions — be explicit.

#### Vocabulary & Tone Tips

- Do not use negative phrasing (e.g., *"don't answer X"*)
- Do use situational prompts (e.g., *"When shopper asks X, do Y"*)
- Let the tone of voice be handled via Configuration, not in Guidance

### Example of Good Guidance

#### Scenario 1: If the shopper requests a refund for their order

**Steps to Resolve the Scenario:**

1. **Verify the Order and Refund Eligibility**
   - Check if the `order number` is included in the message
   - Confirm the order date against the refund window
   - Review order tags for non-refundable conditions

2. **Determine the Refund Reason**
   - Ask the shopper why they are requesting a refund
   - Common reasons: damaged, changed mind, not arrived, wrong item
   - If reason is clear, proceed

3. **Request Supporting Information (if needed)**
   - If damage/defect: Request clear photos
   - If not arrived: Check tracking; ask about neighbors
   - If delays: Proceed to escalate if needed

4. **Determine Refund Path Based on Policy**
   - Without return: Issue refund with timeframe
   - With return required: Share return instructions
   - Non-refundable: Explain gently; offer alternatives

5. **Escalate if Manual Review Needed**
   - Shopper refuses return but demands refund
   - Request is outside policy but may warrant exception
   - Shopper is upset or disputing previous decision

6. **Close the Loop**
   - Summarize what happens next
   - Thank them for patience

---

## Monitoring for Performance: Audit Checklist

### Performance Metrics Review

| Metric | Goal | ✔️ Check |
|--------|------|---------|
| **Automation Rate** (chat & email) | ↑ week-over-week growth | ☐ |
| **Escalation Rate** | < 20% (target) | ☐ |
| **AI CSAT vs Human CSAT** | ±5% or better | ☐ |
| **Avg Resolution Time** | ↓ from pre-AI baseline | ☐ |

**Tip:** Flag any drops >10% for deeper investigation.

### Ticket Review (Quality & Accuracy)

| Task | Details | ✔️ Check |
|------|---------|---------|
| Review **10–15 AI-resolved tickets** | Ensure accuracy, tone, and relevance | ☐ |
| Identify **low-CSAT or negative feedback** tickets | Add to feedback backlog | ☐ |
| Flag handed over tickets | Investigate knowledge gaps | ☐ |

### Knowledge & Macro Update

| Task | Details | ✔️ Check |
|------|---------|---------|
| Review top **used macros** | Are they still accurate and helpful? | ☐ |
| Check for **missing macros** | Create or revise as needed | ☐ |
| Confirm **Help Center content** is up-to-date | Especially for shipping, returns, promos | ☐ |
| Submit **macro or article updates** | Ensure prompt fixes | ☐ |

**Tip:** Keep a changelog of macro/HC updates impacting AI.

---

## Resources

### Help Center
- [Setting up AI Agent](https://docs.gorgias.com/en-US/set-up-and-go-live-with-ai-agent-500219)

### Blogs
- [Guidance Playbook](https://www.gorgias.com/playbooks/chapters/automate-5)

---

**For questions or updates to this playbook, contact:** matilda.lee@gorgias.com

**This is the complete, faithfully extracted version from Notion. All sections have been preserved.**

