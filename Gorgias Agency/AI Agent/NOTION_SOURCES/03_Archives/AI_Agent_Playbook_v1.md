# 📖 AI Agent Playbook

**Source:** https://www.notion.so/2461ae2178f5804fae7fe627d2355ed0  
**Last Updated (Notion):** October 16, 2025  
**Version:** v1_LATEST (Extracted February 24, 2026)

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

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Requirements](#1-requirements)
  - [Train: Onboard AI Agent with Knowledge](#2-train-onboard-ai-agent-with-knowledge)
  - [Train: Customize AI Agent](#3-train-customize-ai-agent)
  - [Test: Test AI Agent Responses](#4-test-test-ai-agent-responses)
  - [Deploy: Connect Channels & Go Live](#5-deploy-connect-channels--go-live)
  - [Analyze: Monitor AI Agent Views](#6-analyze-monitor-ai-agent-views-in-inbox)
- [Knowledge Sources](#knowledge-sources)
- [Guidance Best Practices](#guidance-best-practices)
- [Monitoring for Performance](#monitoring-for-performance-audit-checklist)
- [Resources](#resources)

---

## Setup & Configuration ⚙️

### 1. Requirements ✅

Before you begin:

- ☐ You have an active **AI Agent subscription** (`on usd-6`)
- ☐ Your **Shopify store** is connected to Gorgias
- ☐ You have **Lead, Admin, or Account Owner** permissions in Gorgias
- ☐ You are **Admin in Shopify** (to update permissions)
- ☐ Go to **Settings → My Apps → Shopify**
- ☐ Select your store, then click **Update App Permissions**
- ☐ Sign into Shopify to confirm permissions

⚠️ **Note:** AI Agent can only access the last 10 orders per customer.

---

### 2. [Train] Onboard AI Agent with Knowledge ✅

AI Agent needs at least one knowledge source before it can go live.

- ☐ Go to **AI Agent → Knowledge**
- ☐ Select your store
- ☐ Add these resources:
  - Sync your Shopify store ⭐
  - **Guidance** ⭐
  - Help Center ⭐
  - Public URLs
  - Uploaded documents (e.g., PDFs, FAQs)

---

### 3. [Train] Customize AI Agent ✅

Tailor how AI Agent communicates to reflect your brand.

- ☐ Choose a tone of voice
- ☐ Add an email signature (max 250 characters)
- ☐ Instruct when to handover tickets to human agents
- ☐ Enable auto-tagging
- ☐ Adjust selling style and discounts (if using Shopping Assistant)

---

### 4. [Test] Test AI Agent Responses ✅

Use the testing environment to preview AI behavior on Email and Chat.

- ☐ Go to **AI Agent → Test**
- ☐ Choose a channel (Email or Chat)
- ☐ Run sample conversations
- ☐ Identify and fix gaps in knowledge or behavior

💡 **Tip:** Tests do not impact customers, reporting, or integrations.

---

### 5. [Deploy] Connect Channels & Go Live ✅

AI Agent must be connected to **at least one** support channel to operate.

#### ✉️ Enable on Email

- ☐ Go to **AI Agent → Settings → Channels**
- ☐ Under **Email**, select one or more addresses
- ☐ Add a unique **Email signature**
- ☐ Toggle **Enable AI Agent on Email**
- ☐ Click **Save Changes**

💡 **Tip:** Agent also handles tickets from Order Management, Flows, and contact forms linked to the email.

#### 💬 Enable on Chat

- ☐ Go to **AI Agent → Settings → Channels**
- ☐ Under **Chat**, select one or more chats (site, Help Center, checkout)
- ☐ Configure **handover instructions** for escalation
- ☐ Toggle **Enable AI Agent on Chat**
- ☐ Click **Save Changes**

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

### What are Knowledge Sources?

Knowledge sources are the information AI Agent uses to answer customer questions. Without them, AI Agent cannot operate effectively.

**Five types of knowledge sources:**

1. **Shopify Sync** - Automatic product, order, and inventory data
2. **Guidance** - Custom instructions for specific scenarios
3. **Help Center** - Published articles for customers
4. **Public URLs** - External pages with relevant information
5. **Uploaded Documents** - PDFs, files, or other text documents

### Configuring Knowledge Sources

**Shopify Sync** ⭐

- Enabled automatically when you activate AI Agent
- Provides: Product descriptions, order details, inventory status
- Requires: Valid Shopify app permissions (updated in requirements step)

**Guidance** ⭐ (Most Important)

- Custom instructions you write specifically for AI Agent
- Best for: Company policies, edge cases, tone customization
- See **Guidance Best Practices** section below

**Help Center** ⭐

- Articles published in your Gorgias Help Center
- Best for: Public-facing information (FAQs, shipping, returns, etc.)
- How to: Create/import articles in Help Center, then add to AI Agent knowledge

**Public URLs**

- External webpages AI Agent can reference
- Best for: When information is not in Help Center or docs
- ⚠️ Warning: Use sparingly—URLs can change or become outdated

**Uploaded Documents**

- PDFs, Word docs, or plain text files
- Best for: Internal policies, detailed procedures, compatibility charts
- How to: Upload in AI Agent → Knowledge → Documents

---

## Guidance Best Practices

Guidance is the most powerful tool for controlling AI Agent behavior. It covers policies, edge cases, and specific scenarios that don't fit in your Help Center.

### When to Use Guidance

Use Guidance to:

- Handle **internal policies** not published in your Help Center (e.g., warranty eligibility, VIP handling).
- Navigate **gray area** scenarios like feedback, thank-you notes, or press inquiries.
- Clarify **ambiguous topics** (e.g., refunds vs. store credit rules).
- Replace **missing Help Center articles** during setup.
- Customize how AI responds when using **Actions** (like refunds, discounts, or returns).

### How to Write Guidance

#### Structure & Format

Follow this consistent format:

1. **Scenario Label** (e.g., "Scenario 1")
2. **Title** that starts with "If the shopper…" or "When the shopper…"
3. **Step-by-step resolution**
   - Use numbered steps
   - Sub-bullets for clarification

**Example:**

> 📝 **Scenario 1: If the shopper shares they did not receive all items in their order:**
> 1. Confirm details (ask for photo, packing slip, order #)
> 2. Inform customer the issue will be escalated
> 3. Clarify that reshipment is not guaranteed

#### Use the Right Variables

To make your Guidance "readable" to the AI Agent, use structured variables from:

**Shopify:**
- `order number`, `order name`, `shipping address`, `tracking link`
- `order date`, `package status`, `item list`, etc.

**Ticket data:**
- `ticket subject`, `ticket creation date`
- `shopper says: [x]`, `agent says: [x]`

Avoid vague conditions like "recent orders" — be explicit.

#### 📣 Vocabulary & Tone Tips

- Do not use negative phrasing (e.g., *"don't answer X"*)
- Do use situational prompts (e.g., *"When shopper asks X, do Y"*)
- Let the tone of voice be handled via Configuration, not in the Guidance text

### Example of Good Guidance

#### Scenario 1: If the shopper requests a refund for their order

**Steps to Resolve the Scenario:**

1. **Verify the Order and Refund Eligibility**
   - Check if the `order number` is included in the message. If not, ask the shopper to provide it.
   - Confirm the order date and determine if the request falls within the merchant's refund window (refer to internal refund policy if one is provided).
   - Review order tags or order notes to check for any non-refundable conditions (e.g., "final sale," "custom item," etc.).

2. **Determine the Refund Reason**
   - Ask the shopper why they are requesting a refund, if not already stated.
   - Common refund reasons include:
     - Item arrived damaged or defective.
     - Shopper changed their mind.
     - Item did not arrive.
     - Received the wrong item.
   - If the reason is already clear from the conversation, proceed to the next step.

3. **Request Supporting Information (if needed)**
   - If the shopper received the item and claims damage, defect, or incorrect product:
     - Request clear photos showing the issue.
     - Ask for the original packaging if relevant to the return.
   - If the item did not arrive:
     - Check the package status, tracking number, and tracking link.
     - If tracking shows delivered, ask the shopper to check with neighbors or household members.
     - If tracking shows delays or non-delivery, proceed to escalate.

4. **Determine Refund Path Based on Merchant Policy**
   - If the item is eligible for refund **without return required**:
     - Inform the shopper that a refund will be issued and provide a timeframe (e.g., "within 5–10 business days").
     - Proceed to process the refund and confirm it in the message.
   - If the item **must be returned** before refund:
     - Share return instructions, including return address, label (if provided), and any required RMA number.
     - Let the shopper know the refund will be processed once the return is received and inspected.
   - If the item is **non-refundable** (based on tags, order notes, or merchant rules):
     - Gently explain that the item is not eligible for a refund.
     - Offer an alternative if possible (e.g., store credit, replacement, discount on future order).

5. **Escalate if Manual Review is Required**
   - Escalate to a human agent if:
     - The shopper refuses return but still demands a refund.
     - The request is outside policy but may warrant an exception.
     - The shopper is upset or disputing a previous decision.

6. **Close the Loop with the Shopper**
   - Summarize what will happen next (refund processed, return instructions sent, escalation submitted).
   - Thank them for their patience and understanding.

---

## Monitoring for Performance: Audit Checklist

### Performance Metrics Review

| Metric | Goal | ✔️ Check |
|--------|------|---------|
| **Automation Rate** (chat & email) | ↑ week-over-week growth | ☐ |
| **Escalation Rate** | < 20% (target) | ☐ |
| **AI CSAT vs Human CSAT** | ±5% or better | ☐ |
| **Avg Resolution Time** | ↓ from pre-AI baseline | ☐ |

**Tip:** Flag any drops >10% or increases in escalations for deeper investigation.

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
| Check for **missing macros** based on flagged tickets | Create or revise as needed | ☐ |
| Confirm **Help Center content** is up-to-date | Especially for shipping, returns, promos | ☐ |
| Submit **macro or article updates** to relevant owners | Ensure prompt fixes | ☐ |

**Tip:** Keep a changelog of macro/HC updates impacting AI.

---

## Resources

### Help Center
- [Setting up AI Agent](https://docs.gorgias.com/en-US/set-up-and-go-live-with-ai-agent-500219)

### Blogs
- [Guidance Playbook](https://www.gorgias.com/playbooks/chapters/automate-5)

---

**For questions or updates to this playbook, contact:** matilda.lee@gorgias.com

