# Section 6: AI Agent Settings, Integrations & Advanced Features

**Total Articles:** 19  
**Last Updated:** August 2, 2026  
**Status:** Complete ✅

---

## Table of Contents

### AI Agent Settings (3 articles)
1. [Customize How AI Agent Behaves](#customize-how-ai-agent-behaves)
2. [Let AI Agent Autofill Tags and Ticket Fields](#let-ai-agent-autofill-tags-and-ticket-fields)
3. [Customize How AI Agent Hands Over Chats to Live Agents](#customize-how-ai-agent-hands-over-chats-to-live-agents)

### Connect AI Agent with Other Apps (13 articles)
4. [Create an Action to Connect AI Agent to Other Apps](#create-an-action-to-connect-ai-agent-to-other-apps)
5. [Create Actions: Use Advanced Options](#create-actions-use-advanced-options)
6. [View Event Logs for AI Agent Actions](#view-event-logs-for-ai-agent-actions)
7. [AI Agent Actions: Make Changes to Shopify Orders](#ai-agent-actions-make-changes-to-shopify-orders)
8. [AI Agent Action: Send Loop Returns Portal Deep Link](#ai-agent-action-send-loop-returns-portal-deep-link)
9. [AI Agent Action: Send Return Shipping Status from Loop](#ai-agent-action-send-return-shipping-status-from-loop)
10. [AI Agent Actions: Manage Recharge Subscriptions](#ai-agent-actions-manage-recharge-subscriptions)
11. [Support Actions: Connect AI Agent to ShipStation](#support-actions-connect-ai-agent-to-shipstation)
12. [Support Actions: Connect AI Agent to ShipBob](#support-actions-connect-ai-agent-to-shipbob)
13. [Support Actions: Connect AI Agent to ShipHero](#support-actions-connect-ai-agent-to-shiphero)
14. [AI Agent Actions: Shipmonk](#ai-agent-actions-shipmonk)
15. [AI Agent Actions: Manage Skio Subscriptions](#ai-agent-actions-manage-skio-subscriptions)
16. [AI Agent Actions: Loop Subscriptions](#ai-agent-actions-loop-subscriptions)

### Report Order Issue (3 articles)
17. [Report Order Issue 101](#report-order-issue-101)
18. [Default Scenarios](#default-scenarios)
19. [Create a New Scenario to Report Order Issues](#create-a-new-scenario-to-report-order-issues)

---

## AI AGENT SETTINGS

## Customize How AI Agent Behaves

**URL:** https://docs.gorgias.com/en-US/customize-how-ai-agent-behaves-1997836

You can customize various aspects of how AI Agent interacts with customers to align with your brand and business needs.

### Requirements

- You must have an active AI Agent subscription
- You must have Lead or Admin permissions

### Access AI Agent Settings

1. From the main menu, go to AI Agent
2. Click Settings
3. Configure the following options:

### AI Agent Name

Set a custom name for your AI Agent that will be displayed to customers in conversations.

**Tips:**
- Use a name that feels friendly and aligns with your brand
- Keep it concise (1-2 words work best)
- Examples: "Maya", "Alex", "Assistant", "Support Bot"

### Tone of Voice

Set how AI Agent communicates with customers:

- **Professional** — Formal, business-like tone suitable for B2B or premium brands
- **Friendly** — Warm, approachable tone that feels personable
- **Casual** — Relaxed, conversational tone for fashion, lifestyle, or youth-focused brands
- **Technical** — Precise, detailed tone for technical or specialist products
- **Custom** — Write specific instructions about how AI Agent should communicate

### Language Settings

- **Primary language** — Select the main language AI Agent responds in
- **Multi-language support** — If enabled, AI Agent can respond in customers' preferred languages (80+ languages supported)

### Handover Topics

Define topics that should automatically be handed over to human agents:

- **Add exclusion topic** — Add topics you don't want AI Agent to handle
- **Examples:** Legal questions, billing disputes, complaints

### Auto-Tagging

Configure whether AI Agent automatically tags tickets:

- **Enable auto-tagging** — Allow AI Agent to add tags to tickets
- **Define tag categories** — Set up which tags AI Agent should use

### Additional Settings

- **Response length preference** — Short, Medium, or Long responses
- **Emoji usage** — Enable or disable emojis in responses
- **Channel-specific rules** — Different settings for Email, Chat, SMS

---

## Let AI Agent Autofill Tags and Ticket Fields

**URL:** https://docs.gorgias.com/en-US/let-ai-agent-autofill-tags-and-ticket-fields-1997837

AI Agent can automatically populate ticket tags and custom fields based on the conversation content, improving organization and routing.

### Requirements

- You must have an active AI Agent subscription
- You must have Lead or Admin permissions

### Enable Auto-Tagging

1. From the main menu, go to AI Agent > Settings
2. Scroll to Auto-tagging section
3. Toggle Auto-tagging to ON
4. Select which tags AI Agent should use

### Configure Tag Rules

Define which tags AI Agent should apply based on conversation context:

**By topic** — Tag tickets based on the customer's inquiry topic
- "Returns", "Shipping", "Products", "Billing"

**By sentiment** — Tag tickets based on customer sentiment
- "Happy", "Neutral", "Frustrated", "Angry"

**By customer type** — Tag based on customer status
- "New Customer", "Returning Customer", "VIP", "Bulk Order"

**By order status** — Tag based on order information
- "Pre-purchase", "Post-purchase", "Refund Request"

### Autofill Custom Fields

If you use custom ticket fields, AI Agent can populate them automatically:

1. Define which fields AI Agent should populate
2. Set rules for what values to populate based on conversation content
3. Review filled fields to ensure accuracy

### Benefits of Auto-Tagging

- **Better routing** — Tickets are automatically routed to appropriate teams
- **Improved analytics** — Accurate tagging enables better reporting
- **Faster agent response** — Context is already captured when agents receive tickets
- **Automation** — Use tags to trigger Rules and automations

### Monitor Auto-Tagging Accuracy

1. Review sample tickets to check tagging accuracy
2. Adjust tag rules if needed
3. Give feedback on incorrect tags to improve AI Agent's tagging

---

## Customize How AI Agent Hands Over Chats to Live Agents

**URL:** https://docs.gorgias.com/en-US/customize-how-ai-agent-hands-over-chats-to-live-agents-1997838

You can customize the handover process to ensure smooth transitions from AI to human agents.

### Requirements

- You must have an active AI Agent subscription
- You must have Lead or Admin permissions

### Access Handover Settings

1. From the main menu, go to AI Agent > Deploy > Chat
2. Scroll to Handover section
3. Configure handover instructions

### Handover Scenarios

**When chat is online** — When human agents are available to handle chats:

- Write instructions for how AI Agent should notify customers
- Example: "A member of our team will be with you shortly"
- Specify queue time expectations

**When chat is offline** — When no agents are available:

- Write instructions for how AI Agent should handle the situation
- Option 1: Collect customer information and create a ticket
- Option 2: Offer alternative contact methods (email, callback)

### Handover Instructions Best Practices

- **Be transparent** — Let customers know they're being transferred to a human agent
- **Set expectations** — Provide estimated wait time if available
- **Be helpful** — Offer alternatives if wait time is long (callback, email)
- **Maintain context** — Ensure handover includes full conversation history

### Automatic Handover Triggers

AI Agent automatically hands over in these situations:

- **Confidence threshold** — When AI Agent isn't confident in its answer
- **Handover topic** — Topics you've marked for human handling
- **Customer request** — When customer explicitly asks for a human
- **Escalation required** — For sensitive or complex issues

### Manual Handover

Agents can manually hand over back to AI Agent if the issue doesn't require human intervention:

- Configure when this is appropriate
- Ensure clear communication with customers about the handoff

---

## CONNECT AI AGENT WITH OTHER APPS

## Create an Action to Connect AI Agent to Other Apps

**URL:** https://docs.gorgias.com/en-US/create-an-action-to-connect-ai-agent-to-other-apps-1997839

Actions allow AI Agent to perform tasks in connected third-party apps, like canceling orders or managing subscriptions.

### Requirements

- You must have an active AI Agent subscription
- You must have Lead or Admin permissions
- The third-party app must be integrated with Gorgias

### Access Actions Settings

1. From the main menu, go to AI Agent
2. Click Support Actions
3. Review pre-built actions or create new ones

### Pre-Built Actions Available

- **Shopify** — Cancel orders, update customer information
- **Loop Returns** — Create returns, check return status
- **Recharge** — Manage subscriptions, process refunds
- **ShipStation** — Check shipment status
- **ShipBob** — Update shipment information
- **And more** — Additional integrations available

### Create a Custom Action

1. From Support Actions, click Create Action
2. Define the action:
   - **Name** — What this action does (e.g., "Cancel Order in Shopify")
   - **Description** — Details about when to use this action
   - **App** — Which app this action connects to
   - **Task** — The specific task to perform
3. Set conditions for when AI Agent should use this action
4. Test the action with sample data
5. Save and enable the action

### Action Best Practices

- **Clear naming** — Use descriptive names so AI Agent understands when to use them
- **Specific conditions** — Define exactly when this action should be used
- **Error handling** — Specify what should happen if the action fails
- **Verification** — Always verify critical actions (refunds, cancellations) before completion

---

## Create Actions: Use Advanced Options

**URL:** https://docs.gorgias.com/en-US/create-actions-use-advanced-options-1997840

Advanced options allow you to create sophisticated actions with conditions, approvals, and integrations.

### Requirements

- You must have an active AI Agent subscription
- You must have Lead or Admin permissions
- Technical knowledge of API integrations recommended

### Advanced Action Configuration

**Conditional logic** — Create actions that behave differently based on customer data:
- IF customer is VIP, THEN apply VIP pricing
- IF order is within 15 days, THEN allow cancellation
- IF customer has made 5+ purchases, THEN expedite action

**Approval workflows** — Require human approval for high-risk actions:
- High-value refunds
- Subscription cancellations
- Account changes

**Data transformation** — Convert data from one format to another:
- Parse customer information
- Calculate values
- Format responses

**Error handling** — Specify what happens if an action fails:
- Automatic retry
- Hand over to human
- Provide alternative solution

**Logging and tracking** — Monitor all action executions:
- View event logs
- Debug failures
- Track success rates

---

## View Event Logs for AI Agent Actions

**URL:** https://docs.gorgias.com/en-US/view-event-logs-for-ai-agent-actions-1997841

Event logs show you every time AI Agent uses an Action, including whether it succeeded or failed.

### Access Event Logs

1. From the main menu, go to AI Agent > Support Actions
2. Click Event Logs
3. View logs of all action executions

### Key Information in Event Logs

**Timestamp** — When the action was executed

**Action** — Which action was used

**Status** — Success, Failed, Pending, etc.

**Customer** — Which customer the action affected

**Details** — Specific information about what happened

### Filter Event Logs

- **By action type** — See logs for a specific action
- **By status** — View only successful, failed, or pending actions
- **By date range** — Look at specific time periods
- **By customer** — Track all actions for a specific customer

### Use Event Logs to Debug Issues

1. If an action fails, check the event logs
2. Review the error message
3. Identify the cause
4. Make necessary adjustments to the action configuration
5. Test again

---

## AI Agent Actions: Make Changes to Shopify Orders

**URL:** https://docs.gorgias.com/en-US/ai-agent-actions-make-changes-to-shopify-orders-1997842

AI Agent can make certain changes to Shopify orders directly, such as canceling orders or updating customer information.

### Supported Actions

**Cancel Order** — AI Agent can submit order cancellations to Shopify

**Update Customer Information** — AI Agent can update:
- Customer email address
- Shipping address
- Billing address
- Phone number

**Add Tags** — AI Agent can add tags to orders for organization

### Action Conditions

- Order must meet cancellation eligibility criteria
- Customer must be verified
- Action must be within scope of permissions
- Order data must be valid

### Using Shopify Actions in Guidance

1. Reference Shopify Actions in your Guidance
2. AI Agent will use the action when the conditions are met
3. Example: "IF customer asks to cancel, THEN use [Cancel Order in Shopify]"

---

## AI Agent Action: Send Loop Returns Portal Deep Link

**URL:** https://docs.gorgias.com/en-US/ai-agent-action-send-loop-returns-portal-deep-link-1997843

When integrated with Loop Returns, AI Agent can send customers a direct link to their return portal.

### Requirements

- Loop Returns integration must be connected
- Customer must have an eligible order for return

### How It Works

1. Customer requests a return
2. AI Agent sends them a deep link to the Loop Returns portal
3. Customer can immediately start their return process
4. AI Agent can track return status

### Benefits

- **Faster returns** — Customers can start returns immediately
- **Self-service** — Reduces support team workload
- **Better tracking** — AI Agent integrates with return status

---

## AI Agent Action: Send Return Shipping Status from Loop

**URL:** https://docs.gorgias.com/en-US/ai-agent-action-send-return-shipping-status-from-loop-1997844

AI Agent can check and communicate return shipping status from Loop Returns to customers.

### Requirements

- Loop Returns integration must be connected
- Customer must have an active return

### How It Works

1. Customer asks about their return status
2. AI Agent queries Loop Returns
3. AI Agent reports current status and tracking information
4. Customer receives immediate update

---

## AI Agent Actions: Manage Recharge Subscriptions

**URL:** https://docs.gorgias.com/en-US/ai-agent-actions-manage-recharge-subscriptions-1997845

When integrated with Recharge, AI Agent can manage customer subscriptions directly.

### Supported Actions

**Skip Shipment** — Customer can skip upcoming orders

**Update Frequency** — Customer can change subscription frequency

**Update Products** — Customer can modify products in their subscription

**Pause Subscription** — Customer can temporarily pause subscription

**Cancel Subscription** — Customer can cancel with reason tracking

### Benefits

- **Reduces churn** — Customers can manage subscriptions without calling support
- **Improves retention** — Offering alternatives to cancellation
- **Self-service** — Reduces support team workload

---

## Support Actions: Connect AI Agent to ShipStation

**URL:** https://docs.gorgias.com/en-US/support-actions-connect-ai-agent-to-shipstation-1997846

Connect ShipStation to allow AI Agent to access shipment and tracking information.

### Setup Requirements

- ShipStation account connected to Gorgias
- API credentials configured

### Capabilities

- View shipment status
- Check tracking information
- Update shipping address (if not yet shipped)
- Provide tracking links to customers

---

## Support Actions: Connect AI Agent to ShipBob

**URL:** https://docs.gorgias.com/en-US/support-actions-connect-ai-agent-to-shipbob-1997847

Connect ShipBob to allow AI Agent to access fulfillment and shipment data.

### Setup Requirements

- ShipBob account connected to Gorgias
- API credentials configured

### Capabilities

- Check fulfillment status
- View inventory levels
- Track shipments
- Access carrier information

---

## Support Actions: Connect AI Agent to ShipHero

**URL:** https://docs.gorgias.com/en-US/support-actions-connect-ai-agent-to-shiphero-1997848

Connect ShipHero to allow AI Agent to access fulfillment operations data.

### Setup Requirements

- ShipHero account connected to Gorgias
- API credentials configured

### Capabilities

- Check shipment status
- View order fulfillment stage
- Access tracking information
- Monitor inventory

---

## AI Agent Actions: Shipmonk

**URL:** https://docs.gorgias.com/en-US/ai-agent-actions-shipmonk-1997849

Connect Shipmonk for AI Agent to access fulfillment and shipping data.

### Setup Requirements

- Shipmonk account connected
- API integration enabled

### Capabilities

- Check fulfillment status
- View shipment tracking
- Access inventory information

---

## AI Agent Actions: Manage Skio Subscriptions

**URL:** https://docs.gorgias.com/en-US/ai-agent-actions-manage-skio-subscriptions-1997850

When integrated with Skio, AI Agent can manage subscription orders.

### Supported Actions

- Skip next order
- Pause subscription
- Update order frequency
- Modify subscription products

---

## AI Agent Actions: Loop Subscriptions

**URL:** https://docs.gorgias.com/en-US/ai-agent-actions-loop-subscriptions-1997851

When integrated with Loop, AI Agent can manage Loop subscription features.

### Supported Actions

- Manage orders
- View subscription status
- Skip shipments
- Pause/resume subscriptions

---

## REPORT ORDER ISSUE

## Report Order Issue 101

**URL:** https://docs.gorgias.com/en-US/report-order-issue-101-1997852

The Report Order Issue feature allows customers to report problems with their orders through Order Management.

### What Is Report Order Issue?

Report Order Issue is an automation feature that allows customers to report order problems (damaged items, wrong items, missing items) without needing to start a live chat.

### Available Issue Types

- **Damaged item**
- **Missing item**
- **Wrong item**
- **Item quality issue**
- **Defective product**
- **Custom issues** (you can define your own)

### How Customers Use It

1. Customer accesses Order Management
2. Selects an order
3. Clicks "Report Order Issue"
4. Selects the issue type
5. Provides details and optionally uploads images
6. Submits the report
7. A ticket is created for your team to review

### Benefits

- **Self-service** — Customers can report issues without live chat
- **Reduced workload** — Automates initial issue collection
- **Better documentation** — Captures issue details automatically

---

## Default Scenarios

**URL:** https://docs.gorgias.com/en-US/default-scenarios-1997853

Gorgias comes with default order issue scenarios that are available immediately.

### Pre-Built Scenarios

- **Damaged in shipping** — Item arrived damaged or broken
- **Missing item** — Order was incomplete
- **Wrong item** — Different item than ordered
- **Item quality** — Product doesn't match description
- **Other** — Custom issue

### How Scenarios Work

1. Each scenario appears as an option when customers report an issue
2. Selecting a scenario creates a ticket with appropriate context
3. Your team receives ticket with issue type pre-filled
4. Can create Rules to auto-tag or auto-assign these tickets

---

## Create a New Scenario to Report Order Issues

**URL:** https://docs.gorgias.com/en-US/create-a-new-scenario-to-report-order-issues-1997854

You can create custom scenarios for issue types specific to your business.

### Create a Custom Scenario

1. From the main menu, go to Settings > Order Management
2. Scroll to Report order issue
3. Click Create custom scenario
4. Define:
   - **Issue name** — What customers see (e.g., "Wrong color")
   - **Description** — Details about this issue type
   - **Instructions** — What to ask customers

### Use Cases for Custom Scenarios

- **Product-specific issues** — "Stitching defect in shirt"
- **Service-specific issues** — "Delivery timing issue"
- **Return-specific issues** — "Item doesn't fit expectations"
- **Quality issues** — "Color not as pictured"

### Benefits of Custom Scenarios

- **Better categorization** — Issues are labeled with your terminology
- **Improved routing** — Can auto-assign to appropriate team
- **Better analytics** — Track specific issue types
- **Faster resolution** — Your team knows exactly what the issue is

---

**End of Section 6: AI Agent Settings, Integrations & Advanced Features**

