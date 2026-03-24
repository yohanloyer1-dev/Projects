# Section 3: Test & Deploy AI Agent

**Total Articles:** 4  
**Last Updated:** August 2, 2026  
**Status:** Complete ✅

---

## Table of Contents

1. [Preview AI Agent Responses with Test Conversations](#preview-ai-agent-responses-with-test-conversations)
2. [How to Test Automation Features](#how-to-test-automation-features)
3. [Set Up and Go Live with AI Agent](#set-up-and-go-live-with-ai-agent)
4. [Set Up and Use AI Agent on Chat](#set-up-and-use-ai-agent-on-chat)

---

## Preview AI Agent Responses with Test Conversations

**URL:** https://docs.gorgias.com/en-US/preview-ai-agent-responses-with-test-conversations-1997823

Before deploying your AI Agent to your live channels, you can test how it responds to customer questions in a sandbox environment. Test conversations allow you to preview AI Agent's responses and validate that it's using your knowledge and settings correctly before going live.

### Requirements

- You must have an active AI Agent subscription
- You must have Lead or Admin permissions

### Start a Test Conversation

You can start a test conversation from the AI Agent > Test page in Gorgias.

1. From the main menu, go to AI Agent, then click Test
2. In the test conversation window, type a question or message as if you were a customer
3. Click Send to submit your message and receive a response from AI Agent
4. Review AI Agent's response, including the reasoning behind it
5. Continue the conversation by typing additional follow-up messages
6. Make changes to your knowledge or settings if needed, then test again

### Configure Your Test Conversation

You can customize your test conversation to simulate different scenarios and customer profiles.

1. From the AI Agent > Test page, click Settings in the top-right corner
2. Configure the following options:

**Channel** — Select which channel you want to test (Email or Chat). This affects how AI Agent formats its responses.

**Target audience** — Choose the customer profile you want to test:
- New customer with no order history
- Returning customer with existing orders
- VIP or high-value customer

**Language** — Select the language you want AI Agent to respond in

3. Click Save to apply your test settings

### Review AI Agent's Reasoning

For each response AI Agent generates, you can review its reasoning to understand how it came to its conclusion.

1. After AI Agent responds, click Show reasoning beneath the message
2. Review the decision-making summary, which shows:
   - What knowledge sources AI Agent considered
   - Why it chose specific sources
   - What actions it took (if any)
   - Whether it decided to hand over the conversation

3. Hover over knowledge icons to preview the specific content AI Agent used
4. Click on a knowledge source icon to open and review the full content

### Test Different Scenarios

To thoroughly validate AI Agent before going live, test a variety of scenarios:

**Common customer questions** — Ask questions that align with your most common support topics
**Edge cases** — Test questions that are outside your typical support scope to see how AI Agent handles them
**Product-specific questions** — Ask detailed questions about specific products to validate product recommendations
**Order-related inquiries** — Ask about order tracking, cancellations, returns, and other order management features
**Sensitive or escalation topics** — Test how AI Agent handles handover scenarios and sensitive subjects
**Different languages** — If you plan to support multiple languages, test AI Agent's responses in each language

### Make Improvements Based on Testing

After reviewing test responses, you can make improvements to AI Agent:

**Update knowledge** — If AI Agent's response is inaccurate or incomplete, update the relevant knowledge source (Guidance, Help Center article, or custom content)

**Adjust settings** — If AI Agent's tone or behavior isn't quite right, adjust AI Agent's tone of voice settings or create new Guidance

**Add new knowledge** — If AI Agent lacks information to answer a question, create new Guidance or Help Center articles

**Test again** — After making changes, run the same test conversation again to validate your improvements

---

## How to Test Automation Features

**URL:** https://docs.gorgias.com/en-US/how-to-test-automation-features-without-creating-billable-tickets-286870

You can use Test mode to verify that your automations (Flows, Order Management, and Article Recommendations) are working as intended without being charged for automated interactions.

### Requirements

- You must have an active AI Agent subscription
- You must have Lead or Admin permissions

### Test Your Automated Workflows

1. From the main menu, go to Settings
2. Under the Productivity section, select an automation feature:
   - Flows
   - Order Management
   - Article Recommendations
3. Select the Channels tab
4. Open the "Currently viewing" dropdown menu to select a Channel (Chat, Email, or Contact Form)
5. Click Test to review your automated workflow on the chosen channel
6. If you have more than one ecommerce store connected to Gorgias, use the dropdown menu in the top-right corner to switch between stores
7. Interact with your automation as a customer would to test its functionality
8. Click Exit to end the test experience

**Note:** Test mode does not create billable tickets or interactions. Use it as much as needed to validate your automations before deploying them to your live channels.

---

## Set Up and Go Live with AI Agent

**URL:** https://docs.gorgias.com/en-US/set-up-and-go-live-with-ai-agent-1997824

Once you've trained and tested your AI Agent, you can deploy it to your live support and sales channels. Here's how to set up and go live with AI Agent.

### Requirements

- You must have an active AI Agent subscription
- You must have a Shopify store connected to Gorgias
- You must have Lead or Admin permissions
- You must have completed training and testing of your AI Agent

### Pre-Deployment Checklist

Before deploying AI Agent to live channels, confirm the following:

- ✅ AI Agent has been trained with your brand's content (Help Center articles, website information, product details)
- ✅ Guidance has been created for common customer scenarios
- ✅ Actions have been set up for automated tasks (order cancellations, returns, subscription changes)
- ✅ Tone of voice and language settings have been configured
- ✅ Handover topics and exclusion rules have been defined
- ✅ Test conversations have been conducted and responses validated
- ✅ Your team is prepared to monitor AI Agent's performance

### Deploy AI Agent to Email

1. From the main menu, go to AI Agent, then click Deploy
2. Select Email from the deployment options
3. Toggle Email to ON to enable AI Agent on your email channel
4. Configure the following email-specific settings:
   - **AI Agent name** — The name displayed in automated email responses
   - **Greeting** — Customize how AI Agent greets customers in emails
   - **Response style** — Choose whether responses are formal or conversational
5. Click Save to deploy AI Agent to email

### Deploy AI Agent to Chat

1. From the main menu, go to AI Agent, then click Deploy
2. Select Chat from the deployment options
3. Toggle Chat to ON to enable AI Agent on your chat channel
4. Configure the following chat-specific settings:
   - **Initial greeting** — Customize AI Agent's first message to customers
   - **Handover instructions** — Write instructions for how AI Agent should hand over to human agents when chat is online or offline
   - **Response length** — Choose to keep responses concise for the chat experience
5. Click Save to deploy AI Agent to chat

### Deploy AI Agent to SMS

1. From the main menu, go to AI Agent, then click Deploy
2. Select SMS from the deployment options
3. Toggle SMS to ON to enable AI Agent on your SMS channel
4. Configure SMS-specific settings:
   - **Character limit awareness** — AI Agent will adapt responses to SMS constraints
   - **Response style** — Choose communication style appropriate for text messages
5. Click Save to deploy AI Agent to SMS

### Monitor Performance After Going Live

Once AI Agent is deployed to live channels, monitor its performance:

1. Go to Statistics > AI Agent to view performance reports
2. Check automation rate, CSAT scores, and resolution rates
3. Review the Intents page to understand what topics AI Agent is handling
4. Give feedback on AI Agent tickets to coach it toward better performance
5. Make adjustments to knowledge or settings based on performance data

---

## Set Up and Use AI Agent on Chat

**URL:** https://docs.gorgias.com/en-US/set-up-and-use-ai-agent-on-chat-1997825

AI Agent can greet customers, answer questions, and assist shoppers in real-time through your Chat channel. Here's how to set up and configure AI Agent specifically for Chat.

### Requirements

- You must have an active AI Agent subscription
- You must have Chat enabled in your Gorgias account
- You must have Lead or Admin permissions
- AI Agent must have been trained with your brand content

### Enable AI Agent on Chat

1. From the main menu, go to AI Agent, then click Deploy
2. Select Chat
3. Toggle Chat to ON
4. Click Save

### Configure AI Agent Chat Settings

Once enabled, configure chat-specific behaviors:

1. From the main menu, go to AI Agent > Settings
2. Review and adjust:
   - **AI Agent name** — The name displayed in chat
   - **Initial greeting** — First message AI Agent sends to customers
   - **Tone of voice** — How AI Agent communicates in chat (professional, friendly, casual)
   - **Language** — Primary language for chat responses

### Set Up Handover Instructions for Chat

AI Agent needs to know how to hand over conversations to your human team in different scenarios.

1. Go to AI Agent > Deploy > Chat
2. Scroll to Handover instructions
3. Configure instructions for different chat scenarios:

**When chat is online** — Write instructions for how AI Agent should hand over when your team is available
- Example: "Hand over to the next available agent and let the customer know they're about to speak with a team member"

**When chat is offline** — Write instructions for how AI Agent should handle the conversation when no agents are available
- Example: "Let the customer know chat is offline but offer to capture their email for follow-up"

4. Click Save

### Test AI Agent on Chat

Before deploying to live customers:

1. Go to AI Agent > Test
2. Click Settings and select Chat as the channel
3. Simulate customer conversations to validate responses
4. Test different scenarios (common questions, escalations, product inquiries)
5. Review AI Agent's reasoning to understand its response logic

### Monitor Chat Performance

After deploying AI Agent to chat:

1. Check Statistics > AI Agent > AI Agent for chat-specific metrics
2. Review average response time and customer satisfaction
3. Monitor which intents AI Agent is handling most frequently
4. Check handover rate to ensure it's appropriate
5. Review tickets that AI Agent handled to identify improvement opportunities

### Customize Chat Behavior Over Time

As you learn how AI Agent performs on chat:

1. Update Guidance based on common handover topics
2. Refine handover instructions based on customer feedback
3. Add new knowledge sources to improve coverage
4. Adjust AI Agent's tone of voice if needed
5. Monitor and optimize based on performance metrics

---

**End of Section 3: Test & Deploy AI Agent**

