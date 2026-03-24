# Section 4: Automation Features - Flows & Order Management

**Total Articles:** 16  
**Last Updated:** August 2, 2026  
**Status:** Complete ✅

---

## Table of Contents

### Flows (11 articles)
1. [Flows 101](#flows-101)
2. [Flow Builder](#flow-builder)
3. [Create a Flow](#create-a-flow)
4. [Flow Steps](#flow-steps)
5. [Analyze Flow Drop-off Performance](#analyze-flow-drop-off-performance)
6. [Creating Flow Variables Using JSONPath](#creating-flow-variables-using-jsonpath)
7. [HTTP Request Step in Flows](#http-request-step-in-flows)
8. [Add Email to Klaviyo via Flows](#add-email-to-klaviyo-via-flows)
9. [Show LoyaltyLion Points Balance via Flows](#show-loyaltylion-points-balance-via-flows)
10. [Manage Recharge Subscription via Flows](#manage-recharge-subscription-via-flows)
11. [Templates for One-Step Flows](#templates-for-one-step-flows)

### Order Management (5 articles)
12. [Order Management 101](#order-management-101)
13. [Configure Track Order Option](#configure-track-order-option)
14. [Configure Cancel Order Option](#configure-cancel-order-option)
15. [Order Statuses and Possible Shopper Actions](#order-statuses-and-possible-shopper-actions)
16. [Return Flow with Loop Returns](#return-flow-with-loop-returns)

---

## FLOWS

## Flows 101

**URL:** https://docs.gorgias.com/en-US/flows-101-252069

**Requirements:**
- You must have an active AI Agent subscription
- Flows is supported on Shopify, BigCommerce and Magento 2 stores

Flows are automated Q&A conversation scenarios that operate across multiple channels and assist shoppers with personalized guides, answers, and recommendations. They let you create custom multi-step paths to answer your shoppers' questions based on their preferences.

### Examples of How to Use Flows

- Product recommendations
- Sizing guides
- Return policies (if you have multiple)
- Shipping policies (if these change based on location)
- Warranty claims
- How-to guides (when products require education)
- Report order issue scenarios
- Triage questions before they reach an agent

### Key Features

**Channel agnostic** — Flows are available at the store level. You can display different Flows per Chat and enable them for each of your Chat integrations and channels. The same Flow can be made available in Chat, Help Center, and Contact Form.

**Multiple store support** — You'll have as many Flow menus as store integrations.

**Flexible configuration** — You can create, edit, change, or disable Flows for each of your Chat integrations and channels.

### FAQs

**How many steps can a Flow have?**
Steps are the building blocks of Flows, so you can create as many as you see fit.

**How many answers can an option step have?**
An option can have up to 6 different answers (horizontal steps). If you need more than 6, we recommend having 5 answers and including an "Other" answer, leading to more options.

**How many Flows can be created/enabled?**
You can create as many Flows as you'd like. You can enable up to 6 Flows per integration.

---

## Flow Builder

**URL:** https://docs.gorgias.com/en-US/flow-builder-256475

The Flow builder has a tree-type layout that reflects the multiple paths you can build for your customers, depending on the topic.

### Flow Builder Interface

| Element | Name | Description |
|---------|------|-------------|
| 1 | Name | For internal use only — it won't be visible to your customers |
| 2 | Navigation panel | Use this to zoom in, out, and navigate through the builder — particularly helpful for large Flows |
| 3 | Steps | Every step is a block — it can be a single action or a set of actions |
| 4 | Buttons | Choose to discard or save the changes made to a Flow — you'll also have the Save button here for new Flows |
| 5 | Language | Use this to translate the Flow into multiple languages. Using the Save option will save the incomplete Flow as a Draft so it won't be listed under Channels |

---

## Create a Flow

**URL:** https://docs.gorgias.com/en-US/create-a-flow-256472

You'll need to use the Flow builder to create your Flows. Every time you create one, it'll be saved in a disabled state so you can enable it in the desired channel manually.

### Create and Publish a Flow

1. Go to Settings from the main menu, then select Flows
2. Select Create Custom Flow
3. Alternatively, select Create From Template to start with a pre-built Flow based on common use cases
4. Enter a name for your Flow (this isn't visible to shoppers)
5. Select the Trigger button and enter a name (this will be visible to shoppers in Chat and used to start the Flow — for example, "How do I know my shoe size?")
6. Select the + icon under the trigger to add option steps and select the type of step from the dropdown menu
7. Continue to add steps to create paths and, when you're happy with the setup, click on the End Flow node and select the desired end step
8. Select Publish to finish

### Save a Flow as a Draft

Saving Flows as drafts allows you to preserve your work without having to complete all the steps or leave the Flow builder.

1. If you want to keep working on your Flow before publishing it, select the Save button in the upper right corner instead of the Publish button
2. Flow drafts can be saved as incomplete, but they have to have a title
3. They'll be labeled as Draft and won't appear in your Channels settings, so there's no chance of making them visible to your shoppers by accident
4. When you're happy with the Flow, select the Publish button in the upper right corner which will take you to the Channels tab, so you can enable the Flow and make it visible to your shoppers in the selected channels
5. Once the Flow is published, it can't be changed back to draft again. However, you can duplicate it and it'll be automatically saved as a draft

### Add Flows to Your Channels

Once your new Flow has been created, enable it in the desired channels — these are the channels where your trigger will be displayed.

1. Go to Settings from the main menu
2. Select Flows > Channels
3. Open the Currently viewing dropdown menu to select a Channel for your Flows (Chat, Email, Contact Form)
4. Select Add Flow to display up to 6 Flows on the selected channel

**Tip:** If you want to see what your Flow looks like on a channel, use Test mode to review the Flow without creating billable tickets.

---

## Flow Steps

**URL:** https://docs.gorgias.com/en-US/flow-steps-(triggers-options-ends)-315394

Here you can see all the steps, options, and types of ends you can set up in Flows.

### Types of Steps

Steps are the building blocks used to create Flows. There are 3 types in the Flow builder:

**Trigger** — This button appears when a Flow is published. The Flow will start when a customer clicks on it. There can only be one trigger per Flow.

**Options** — These are the 8 types of steps that are offered within a Flow.

**End** — This is the final step in a Flow. Each path of steps must conclude with an end step.

### Types of Options

Options are the types of responses customers can give when moving through a Flow. There are 8 types in the Flow builder:

1. **Multiple choice** — Display up to 6 customizable options for customers to choose from
2. **Collect text reply** — Allow customers to write a response with up to 5,000 characters
3. **Collect file upload** — Allow customers to upload up to 5 files
4. **Automated answer** — Display customizable short-text answers
5. **Order selection** — Allow customers to select from up to 5 of their most recent orders. This step can be used only after the Customer login step
6. **HTTP request** — Integrate external web services or data sources into a Flow, send and receive data via HTTP requests, and use data received from said step as variables in subsequent ones
7. **Customer login** — Prompt the shopper to log in with their details so this data can be used for HTTP requests or an order selection step. Customers will be able to authenticate if they have an order in your store
8. **Conditions** — Create multiple paths for personalized customer experience, based on variables (money spent, subscription frequency, loyalty points, etc)

### HTTP Request Step Details

By default, HTTP step will create two branches:

- **Success** — triggered when the request is successful, initializing the next step
- **Error** — set to create a ticket whenever the request fails or returns a status code of 400 or above

The action is done in the back-end, but you can follow up with an Automated answer step to inform the customer of the action.

### Types of Ends

Ends are the final step in a Flow. There are 3 types in the Flow builder:

1. **Create a ticket** — Create a ticket in your help desk and select if you want it pre-tagged and pre-assigned. The ticket will include the full customer path through Flows
2. **Ask for feedback** — Give customers the option to confirm their questions have been answered (no ticket created), or that they need more help (ticket created). If the ticket is created, you can have it pre-tagged and pre-assigned
3. **End interaction** — The interaction will end and be considered automated. Customers won't be able to create a ticket and must leave the Flow to ask for further support

---

## Analyze Flow Drop-off Performance

**URL:** https://docs.gorgias.com/en-US/analyze-your-flows-drop-off-performance-629715

After you've built and published a Flow, you can use Analysis mode to evaluate its effectiveness.

### Requirements

- You must have an active AI Agent subscription
- You must have Admin or Lead permissions to see Flow Analysis

### Open Your Flow Analysis

You can find and access the Analysis for a Flow from the Automate Performance by Feature report in your Statistics. Alternatively, you can open a Flow in the Flow Builder then select Analysis.

1. Go to Statistics
2. Scroll down to Automate, then select the Performance by feature report
3. Select Analyze Flow next to the Flow that you want to review

### Filter Analysis Results by Date

Use the calendar to filter the results of your Flow's Analysis by date. You can select dates based on when data for the latest version of the Flow is available.

**Note:** Your date range may cover a period of time where you had a different version of the Flow published. When this happens, we only show data for the most recent version of the Flow.

### How to Read Your Flow's Analysis

Your Analysis always shows data for the latest version of the Flow. Analysis data resets whenever you make a change to the Flow so you can always evaluate how the current state of the Flow performs.

If you've published your Flow in multiple languages, the Analysis includes data from the latest version of all published languages.

### Overall Flow Performance

Use the main Analysis stats to see how your Flow is performing overall:

| Stat | Description |
|------|-------------|
| Total starts | The total number of shoppers who started the Flow from the beginning |
| Automation rate | The % of shoppers whose inquiries the Flow resolved |
| Automated | The number of shoppers that completed the Flow and are considered automated |
| Drop off | The total number of shoppers who started a Flow and left before reaching the end |
| Tickets created | The total number of shoppers who started a Flow and created a support ticket |

### Stats for Flow Steps

Use the stats for each step card in the Flow to understand which steps shoppers select most frequently. You can also identify where shoppers drop-off and fail to continue with the Flow.

Steps with a high % of drop off may indicate an opportunity to revisit the step and make changes.

### Stats for Flow Ends

By looking at the end cards in your Flow, you can understand where shoppers frequently conclude and whether the end successfully resolved their inquiry.

---

## Creating Flow Variables Using JSONPath

**URL:** https://docs.gorgias.com/en-US/creating-flow-variables-using-jsonpath-373084

When using our HTTP request Flow step, you can create variables using the response you received from a third party to leverage it in subsequent steps (for example, get a customer's loyalty point balance).

You can create variables from your response by defining their JSONPath (JavaScript Object Notation).

### What is JSONPath?

JSONPath is like a map that helps you find specific data inside JSON (JavaScript Object Notation) format, which is a way to organize information in a neat, readable way.

JSON is a popular way to store and transport data. For example, a simple contact might look like this in JSON:

```json
{
 "name": "Alice",
 "phone": "123-456-7890"
}
```

JSONPath lets us pick out specific pieces of information from JSON data.

### Steps to Access Data

1. **Start at the Root** — In JSONPath, `$` symbolizes the start of the data. Think of it as the outermost box
2. **Find Your Way** — Use the names (keys) in the JSON to navigate. For example, to find Alice's phone number, you would use `$.phone`

### Examples

**Accessing Data**

To get Alice's name from our example, you use `$.name`.
Result: Alice

**Accessing Nested Data**

Imagine you have another box inside labeled address with a city:

```json
{
 "name": "Alice",
 "address": {
   "city": "Wonderland"
 }
}
```

To find the city, use `$.address.city`.
Result: Wonderland

---

## HTTP Request Step in Flows

**URL:** https://docs.gorgias.com/en-US/http-request-step-in-flows-436910

**Note:** To use this feature, you should have some familiarity with making HTTP requests to communicate with other applications. Otherwise, it is recommended that you ask a developer for help.

With the HTTP request Flow steps, you can use data and execute actions from third-party apps to make your Flows more powerful and automate a variety of requests, so your team can focus on the more complex issues.

### Create an HTTP Request in Flows

1. Go to Settings > Flows
2. Create a new Flow or select a Flow that you've already built
3. Select the + icon to add a step in the Flow, then select HTTP Request
4. Configure the HTTP Request:
   - Choose the HTTP method: GET, POST, PUT, DELETE
   - Enter the endpoint URL and any necessary query parameters or headers
   - For POST, PUT, and PATCH methods, specify the request body
5. Click Test Request to ensure you get a 200 OK status code and then click Publish to set the Flow live in your connected channels

### HTTP Request Branches

By default, HTTP step will create two branches:

- **Success** — triggered when the request is successful, moving to the next step
- **Error** — activated when the request fails or returns a status code of 400 or above, by default creates a ticket

### Supported Variables

You can leverage variables created from previous steps to use them in your HTTP request:

| Step name | Variables you can leverage | Data types |
|-----------|----------------------------|-----------|
| Collect text reply | Response from customer | String |
| Multiple choice | Option chosen by your customer | String |
| Customer login | Customer first name, last name, full name, phone number | String |
| Order selection | Order number, total amount, date | Number, date |
| HTTP request | Any custom variable you have generated | Custom |
| Collect file upload | Attachments provided by the customer | Array |

### Access Event Logs

You can get data about all HTTP requests being made from your step via CSV export, directly in the HTTP request configuration.

### Use Cases

- Add customer to Klaviyo list
- Show LoyaltyLion points balance
- Manage Recharge subscriptions

---

## Add Email to Klaviyo via Flows

**URL:** https://docs.gorgias.com/en-US/add-email-to-klaviyo-via-flows-438155

You can create a Flow with HTTP request that will automatically create a Klaviyo profile for your customer as soon as they leave their name and email address.

### Steps

1. Start the Flow with the Trigger button "Keep me informed about updates and promotions"
2. Add a Collect text reply step and ask for the customer's first name
3. Add another Collect text reply step and ask for the customer's email address
4. Add HTTP request Flow step with the following information:
   - Request name: Add customer to Klaviyo list
   - URL: https://a.klaviyo.com/api/profiles
   - HTTP method: POST
5. Add two headers:
   - authorization: Klaviyo-API-Key your private Klaviyo API key
   - revision: copy the date from this page in the format of YYYY-MM-DD
6. Select application/json in the Request body drop-down menu and use the provided script with variables
7. Test your request and add an Automated answer step to inform the customer they've been subscribed
8. Set the ending to Ask for feedback or End interaction
9. Click Publish to go live

---

## Show LoyaltyLion Points Balance via Flows

**URL:** https://docs.gorgias.com/en-US/show-loyaltylion-points-balance-via-flows-438457

You can create a Flow with HTTP request that will automatically show LoyaltyLion points to your customer upon their request.

### Steps

1. Start the Flow with the Trigger button "How many loyalty points do I have?"
2. Add a Customer login step — customers get a one-time code via email or SMS
3. Add HTTP request Flow step with the following information:
   - Request name: Loyalty point balance
   - URL: https://api.loyaltylion.com/v2/customers?email=ADD VARIABLE CUSTOMER EMAIL
   - HTTP method: GET
4. Add Header:
   - authorization: Basic [your base64-encoded token:secret]
5. Add three Variables:
   - points_approved | $.customers[0].points_approved | number
   - points_spent | $.customers[0].points_spent | number
   - rewards_claimed | $.customers[0].rewards_claimed | number
6. Test your request and add an Automated answer step displaying the points balance
7. Set the ending to Ask for feedback or End interaction
8. Click Publish to go live

---

## Manage Recharge Subscription via Flows

**URL:** https://docs.gorgias.com/en-US/manage-recharge-subscription-via-flows-438584

You can create a Flow with HTTP request that will enable your customers to manage their Recharge subscriptions without involving your team.

### Steps Overview

1. Start the Flow with Trigger "I'd like to manage my subscription"
2. Add Customer login step
3. Add first HTTP request to get Recharge customer ID
4. Add second HTTP request to get subscription and address ID
5. Add Multiple choice step to offer options (Update email, Update shipping address, Cancel subscription, Something else)
6. For each path, add appropriate HTTP request and Automated answer steps
7. Publish when complete

### Multiple Choice Paths

**Update Email Address** — Customer provides new email, HTTP PUT request updates Recharge customer email

**Update Shipping Address** — Customer provides address details (Address 1, Address 2, City, State, ZIP), HTTP PUT request updates address

**Cancel Subscription** — Customer provides cancellation reason, HTTP POST request cancels subscription

**Something Else** — Ends with Create ticket for human agent review

---

## Templates for One-Step Flows

**URL:** https://docs.gorgias.com/en-US/templates-for-one-step-flows-243755

We've gathered the top one-step Flows that give a quick response to shoppers. These questions are used the most across our entire customer base and below are several templates to get you started.

### Available Templates

- What's your shipping policy?
- How do I manage my subscription?
- Where can I get a discount?
- How do I make a return?
- Returns & Exchanges
- Size & Fit

Choose the relevant ones and replace the bolded text with details for your business.

### Template Categories

**Orders and Delivery**
- What is your shipping policy?
- Where is my order?
- Can I cancel or change my order?
- How do I return an item?
- Are there any return fees?
- How often do you restock?

**Commercial Offers (discounts, loyalty programs)**
- Do you have any discounts?
- Do you have a rewards program?

**Product and Brand**
- How do I pick the right size?
- How is [product name] different from other products on the market?
- What type of ingredients do you use?
- What's your mission at [brand name]?

For detailed template content and customization guidance, refer to the official documentation.

---

## ORDER MANAGEMENT

## Order Management 101

**URL:** https://docs.gorgias.com/en-US/order-management-101-81861

**Requirements:**
- You must have an active AI Agent subscription
- Order Management is only supported on Shopify stores (not compatible with BigCommerce or Magento 2)

Order Management allows your customers to check their order status, tracking number, and shipping information, as well as create templated tickets when reporting order issues. Your customers don't need to start a live Chat with your agents to get the needed information — Order Management can automate up to 30% of your live Chat ticket volume.

### Default Enablement

Track and Return will automatically be enabled on your account, but can be disabled anytime.

### Customer Authentication

Shoppers can log in to Order Management on your Chat, Help Center, or Contact Form by inputting a one-time password (6-digit verification code) via email or SMS. The code is sent in the same language as the Chat, Help Center or Contact Form where they initiated Order Management.

### Order Management Options

**Track** — Provides customers with a detailed timeline of order events (order shipped, order in transit, order delivered, etc.), synced directly from Shopify. You can also add a general message in case you are experiencing delays with order shipping.

**Return** — Allows customers to submit a return request for eligible orders. The Return button will only show for orders that meet your eligibility criteria. The flow can be configured with or without a Loop Returns integration.

**Cancel** — Allows customers to submit a cancellation request for eligible orders. The Cancel button will only show on orders that meet your eligibility criteria.

**Report order issue** — Provides customers with a selection of issues tailored to each specific order. The options shown will depend on each order's attributes (financial status, delivery status, fulfillment status, etc.).

**Order Summary** — You can get a summary of information about the customer's order from Order Management:
- Shipping information
- Billing information
- Payment information

### FAQs

**Once the shopper starts a Chat with an agent and it's still ongoing, when will the Chat revert to the Order Management portal?**

Once the customer starts a Chat with you, they'll still be able to go back to the Order Management dashboard by clicking on the back arrow in the Chat's header. However, if the last message in the Chat was your agent's message and the customer didn't get back to you for 24 hours, the Chat will revert to Order Management on its own.

**I'm seeing an error message on my Order Management settings page. What should I do?**

If you're seeing this error, you don't seem to have an active Shopify store integration or an active Chat integration at the moment. You must integrate your Shopify store with Gorgias and activate the Chat integration to enable the Order Management portal.

---

## Configure Track Order Option

**URL:** https://docs.gorgias.com/en-US/configure-track-order-option-315730

The Track Order option allows customers to view the journey of their shipped item, including time and date stamps for when the order was placed, confirmed, shipped, and the destination address. The information is updated in real-time, directly pulled from Shopify.

Shoppers can also report any issues they're having from the tracking screen.

### Setup Steps

1. Go to Settings > Order Management
2. If you have more than one ecommerce store connected to Gorgias, use the dropdown menu in the top right-hand corner to switch between stores
3. Enable Track Order using the toggle
4. Select Track Order to create a custom message when shoppers track their orders
5. We recommend using this message to remind shoppers of your expected shipping timeframes
6. Select Save Changes

---

## Configure Cancel Order Option

**URL:** https://docs.gorgias.com/en-US/configure-cancel-order-option-315739

The Cancel Order option allows customers to submit a request to cancel an order (order information is pulled directly from Shopify).

### Setup Steps

1. Go to Settings > Order Management
2. If you have more than one ecommerce store connected to Gorgias, use the dropdown menu in the top right-hand corner to switch between stores
3. Select Cancel Order
4. Use the dropdown menu to select an Eligibility window for cancelling orders
   - Here you're choosing what status an order should be in to allow customers to cancel (unfulfilled, Processing Fulfillment, Pending Delivery)
5. Under Response text, write a custom reply message to respond to cancellation requests
6. Select Save Changes

**Tip:** You can preview the Cancel Order experience by clicking on the preview on the right-hand side. To view the preview in a different channel select the desired channel from the dropdown.

---

## Order Statuses and Possible Shopper Actions

**URL:** https://docs.gorgias.com/en-US/order-statuses-and-possible-shopper-actions-81862

This guide covers all supported shipment statuses in Order Management and actions accessible by shoppers depending on the presented status.

### Gorgias Order Statuses

| Gorgias Order Status | Status Description |
|---|---|
| Unfulfilled | Order is unfulfilled and fulfillment is pending |
| Processing Fulfillment | Order fulfillment has been acknowledged and is in processing |
| Pending Delivery | Order fulfillment hasn't been shipped yet; label being purchased and printed |
| Attempted Delivery | Order delivery was attempted but unable to be completed |
| Ready for Pickup | Order is ready for pickup at a shipping depot or location |
| In Transit | Order is being transported by the carrier to final destination |
| Out for Delivery | Order is being delivered to final destination |
| Delivered | Order was successfully delivered to final destination |
| Failed Delivery | Something went wrong; tracking number was invalid or shipment canceled |
| Status unavailable (blank) | Fulfillment status unknown |
| Cancelled | Order fulfillment was canceled |
| Failed Fulfillment | Order fulfillment failed or there was an error |
| Partially Refunded | Order payments have been partially refunded |
| Refunded | Order payments have been refunded |

### Actions Availability by Status

Depending on the order shipment status, customers can take certain actions:

| Gorgias Order Status | Track | Cancel | Return | Report Issue |
|---|---|---|---|---|
| Unfulfilled | ✓ | ✓ | ✗ | ✓ |
| Processing Fulfillment | ✓ | ✓ | ✗ | ✓ |
| Pending Delivery | ✓ | ✓ | ✗ | ✓ |
| Attempted Delivery | ✓ | ✗ | ✓ | ✗ |
| Ready for Pickup | ✓ | ✗ | ✓ | ✗ |
| In Transit | ✓ | ✗ | ✓ | ✗ |
| Out for Delivery | ✓ | ✗ | ✓ | ✗ |
| Delivered | ✓ | ✗ | ✓ | ✓ |
| Failed Delivery | ✓ | ✗ | ✓ | ✗ |
| Status unavailable | ✓ | ✓ | ✗ | ✓ |
| Cancelled | ✗ | ✗ | ✓ | ✗ |
| Failed Fulfillment | ✗ | ✗ | ✓ | ✗ |
| Partially Refunded | ✗ | ✗ | ✗ | ✓ |
| Refunded | ✗ | ✗ | ✓ | ✗ |

---

## Return Flow with Loop Returns

**URL:** https://docs.gorgias.com/en-US/articles/return-flow-103988

**Requirement:** Automation features like Order Management are only available for accounts with an active AI Agent subscription.

You can connect your Loop Returns integration with the Return Order option in Order Management.

### Shopper Experience

**In Chat:**
1. Customer accesses the "Track and manage my orders" section in Chat
2. Selects "Return an order"
3. Chooses the order they want to return
4. Clicks Return and is redirected to the Loop Returns portal (already logged in)

**In Help Center:**
1. Visitor clicks on the Return option at the top
2. Picks the order they want to return
3. Clicks Return and is redirected to the Loop Returns portal (already logged in)

### How to Connect

1. Go to Settings -> All apps
2. Search for Loop Returns and connect it
3. Go to the Automate menu
4. Choose your store and navigate to Order Management
5. Click on Return Method
6. Select Loop Returns as your new return method

---

**End of Section 4: Automation Features - Flows & Order Management**

