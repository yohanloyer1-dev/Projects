# 📋 Standard Helpdesk and AI Agent Implementation Playbook (2025)

**Source:** https://www.notion.so/18a1ae2178f5802c949bcdce81936028  
**Last Updated (Notion):** February 23, 2026  
**Version:** v1_LATEST (Extracted February 24, 2026)

---

## Overview

This playbook defines implementation workflows and activation criteria for the complete Helpdesk product suite, including:

- **Helpdesk** - Core support ticket management
- **Automate** - Workflow automation with Flows
- **AI Agent** - AI-powered support automation (Support Agent + Shopping Assistant)

---

## Product Activation Definitions

### What is "Activated"?

A product is **activated** when it is:

1. **Technically set up** - All required configurations complete
2. **Actively used** - Team is using it for customer interactions
3. **Delivering value** - Measurable improvement in key metrics
4. **Monitored** - Regular review and optimization happening

### Activation Criteria by Product

#### Helpdesk Activation

A Helpdesk is **activated** when:

- ✅ Ticket routing is configured
- ✅ Views and tags are set up for team workflow
- ✅ At least 80% of support requests are managed through Gorgias
- ✅ Team has adopted daily review routines
- ✅ Performance metrics are being tracked (FRT, RT, CSAT)

#### Automate Activation (Flows)

Automate is **activated** when:

- ✅ At least 1 Flow is set up and live
- ✅ Flow has >50% success rate
- ✅ Team understands when/how to create Flows
- ✅ Team is reviewing Flow performance regularly

#### AI Agent Activation

AI Agent is **activated** when:

- ✅ AI Agent is enabled on at least one channel (Email or Chat)
- ✅ Knowledge sources are configured (minimum: Shopify sync + 5 Guidances)
- ✅ Automation rate is >10% (email) or >15% (chat)
- ✅ Team is actively monitoring and improving responses
- ✅ Escalation rate is <20%
- ✅ AI CSAT is within ±5% of human agent CSAT

---

## Multi-Product Implementation Workflow

### Phase 1: Foundation (Week 1-2)

**Focus:** Get Helpdesk set up as the central support system

**Deliverables:**
- Ticket routing configured
- Views and tags created
- Team training on basic ticket handling
- Performance baseline established

**Owner:** Implementation Specialist

### Phase 2: Workflows (Week 3-4)

**Focus:** Automate repetitive processes with Flows

**Deliverables:**
- 2-3 Flows identified and created
- Flow success rates tracked
- Team trained on Automation

**Owner:** Implementation Specialist + Merchant

### Phase 3: AI Agent Setup (Week 5-6)

**Focus:** Launch AI Agent on primary channel

**Deliverables:**
- AI Agent enabled on Email and/or Chat
- Knowledge sources configured
- Initial Guidances created
- Handover rules configured

**Owner:** Implementation Specialist + CSM

### Phase 4: Optimization (Week 7+)

**Focus:** Improve performance through continuous feedback

**Deliverables:**
- Automation rate improvements
- Guidance refinements
- Actions added
- Performance targeting goals

**Owner:** CSM + Merchant

---

## Views, Tags, and Automation Setup

### Standard Helpdesk Views

Create these foundational views for support team workflow:

| View Name | Purpose | Filter |
|-----------|---------|--------|
| **Inbox** | All unhandled tickets | Status = "open" |
| **Assigned to Me** | Your personal queue | Assigned to = current user |
| **AI Agent** | Monitor AI performance | Tag = "ai_*" |
| **Urgent** | High priority items | Priority = "high" |
| **Waiting** | Awaiting customer response | Tag = "waiting" |
| **Closed** | Resolution history | Status = "closed" |

### Tag Strategy for AI Agent

When using AI Agent, implement these tags:

| Tag | Purpose | Auto-Applied |
|-----|---------|--------------|
| `ai_close` | Closed by AI | ✅ Yes |
| `ai_handover` | Escalated to human | ✅ Yes |
| `ai_processing` | Currently being processed | ✅ Yes |
| `ai_snooze` | Waiting for customer response | ✅ Yes |
| `ai_ignore` | Intentionally ignored by AI | ✅ Yes |
| `ai_feedback_needed` | Needs review/training | 🔘 Manual |
| `needs_guidance` | Missing knowledge source | 🔘 Manual |

### Automation Rules for Workflow

Set up these automation rules to optimize workflow:

**Rule 1: Auto-Tag Handovers**
- When: Ticket is created with handover intent
- Then: Auto-tag with `ai_handover` + `needs_review`

**Rule 2: Customer Response Snooze**
- When: AI closes ticket with snooze intent
- Then: Auto-tag with `ai_snooze` + auto-hide for 3 days

**Rule 3: Low CSAT Flag**
- When: CSAT rating ≤ 2 stars
- Then: Auto-tag with `ai_feedback_needed` + assign to team lead

**Rule 4: Guidance Gap**
- When: Ticket is marked as "handover - missing guidance"
- Then: Auto-tag with `needs_guidance` + add to backlog view

---

## Customer Journey Mapping

### The Complete Support Journey with Multi-Product Activation

```
Customer Initiates Contact
    ↓
┌──────────────────────────────────────────────────────┐
│ CHANNEL ENTRY POINT                                  │
│ • Email                                              │
│ • Chat                                               │
│ • Contact Form                                       │
│ • Social (if integrated)                             │
└──────────────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────────────┐
│ AI AGENT - INITIAL RESPONSE LAYER                    │
│ • Analyzes customer intent                           │
│ • References Guidance & Knowledge Sources            │
│ • Determines if eligible for AI resolution           │
└──────────────────────────────────────────────────────┘
    ↓
    ├─ [Branch A] AI Can Resolve
    │       ↓
    │   • Provides instant answer
    │   • Tags with ai_close
    │   • Ticket auto-resolved
    │   • CSAT survey sent 24h later
    │       ↓
    │   Customer Satisfied → End
    │   Customer Unsatisfied → Feedback to Guidance
    │
    ├─ [Branch B] Requires Action
    │       ↓
    │   • AI offers self-serve action
    │   • Examples: Cancel order, track package, request return
    │   • Integrates with Shopify/systems
    │       ↓
    │   Action Succeeds → Resolved
    │   Action Fails → Escalate
    │
    └─ [Branch C] Needs Human Escalation
            ↓
        • Ticket marked ai_handover
        • Routed to Helpdesk inbox
        • Assigned to available agent
            ↓
        ┌──────────────────────────────────────────────┐
        │ HELPDESK - HUMAN AGENT LAYER                 │
        │ • Reviews AI notes and history               │
        │ • Provides personalized resolution           │
        │ • May use Macros or create new Guidance      │
        │ • Closes ticket or requests more info        │
        └──────────────────────────────────────────────┘
            ↓
        • Ticket tagged with agent name
        • CSAT survey sent after close
        • Ticket stored in View for analytics
            ↓
        [End - Customer resolution complete]
```

### Journey Decision Points

**At AI Initial Response:**

- **Intent Classification:** Does AI recognize the customer's request?
  - YES → Proceed
  - NO → Escalate to human

- **Knowledge Coverage:** Is there relevant Guidance/Help Center content?
  - YES → Use it to respond
  - NO → Escalate or offer self-serve option

- **Eligibility:** Can this be handled by AI (not a sensitive/angry issue)?
  - YES → Proceed with response
  - NO → Escalate with context

**At Action Point:**

- **Action Availability:** Does an Action exist for this request?
  - YES → Offer action to customer
  - NO → Escalate

- **Action Eligibility:** Does customer meet action conditions?
  - YES → Execute action
  - NO → Explain limitation and escalate

---

## Metrics for Measuring Implementation Success

### Helpdesk Metrics

| Metric | Baseline Goal | Success Target | Review Frequency |
|--------|---------------|-----------------|------------------|
| **First Response Time (FRT)** | Track current | ↓ 30% improvement | Weekly |
| **Resolution Time (RT)** | Track current | ↓ 20% improvement | Weekly |
| **Volume Handled** | Track current | ↑ 50% increase | Monthly |
| **Agent CSAT** | Track current | ≥ 85% | Monthly |
| **Tickets/Agent/Day** | Track current | ↑ 25% improvement | Weekly |

### Automation (Flows) Metrics

| Metric | Goal | Success Indicator |
|--------|------|-------------------|
| **Flows Created** | ≥ 3 | High-volume processes automated |
| **Flow Success Rate** | ≥ 50% | Users completing flow to resolution |
| **Deflection Rate** | ≥ 30% | Tickets avoided through flows |
| **User Adoption** | ≥ 60% | Team using flows regularly |

### AI Agent Metrics

| Metric | Goal | Success Indicator |
|--------|------|-------------------|
| **Automation Rate** | ≥ 10-15% | Consistent week-over-week growth |
| **Escalation Rate** | < 20% | Appropriate handover of complex issues |
| **AI CSAT vs Human CSAT** | ±5% | Quality comparable to human team |
| **Guidance Coverage** | ≥ 80% | Most intents have supporting guidance |
| **Action Usage** | ≥ 2 actions active | Self-serve options available |
| **Shopping Assistant Conversion** | ≥ 2% lift | If enabled, measurable AOV/conversion impact |

### Combined Product Metrics

| Metric | Goal | Success Indicator |
|--------|------|-------------------|
| **Overall Automation Rate** | ≥ 25-30% | AI + Flows handle 1 in 4 interactions |
| **Support Cost per Ticket** | ↓ 40% | Efficiency gains from automation |
| **Customer Satisfaction** | ≥ 4/5 | Maintained or improved CSAT |
| **Team Productivity** | ↑ 35% | More tickets handled same headcount |
| **Merchant Expansion** | ≥ 1 product add | Often upgrade after success |

---

## AI Agent-Specific Implementation Steps

### AI Agent Setup Checklist

**Pre-Setup (Week 1)**
- [ ] Merchant has active AI Agent subscription (USD-6)
- [ ] Shopify store connected and permissions updated
- [ ] Email and/or Chat channels set up
- [ ] Team access configured

**Knowledge Configuration (Week 2)**
- [ ] Shopify sync started
- [ ] Help Center set up (minimum 10 articles)
- [ ] 5+ custom Guidances created
- [ ] Tone of voice defined

**Channel Enablement (Week 3)**
- [ ] AI Agent enabled on Email
- [ ] AI Agent enabled on Chat (if desired)
- [ ] Handover topics configured
- [ ] Views created in Helpdesk

**Optimization (Weeks 4+)**
- [ ] Monitor automation rate
- [ ] Review handover tickets
- [ ] Refine Guidances
- [ ] Add Actions as needed
- [ ] Enable Flows integration

### Common Objections & Responses

**Objection:** "AI might give bad responses"

**Response:** "We start with AI in training mode, review responses, and improve gradually. You're in full control, and we've built in safeguards like handover for sensitive topics."

**Objection:** "Our business is too unique for AI"

**Response:** "Guidance is designed specifically for your unique business. We create it based on your policies and train AI on your specific scenarios."

**Objection:** "Will it replace our team?"

**Response:** "AI handles repetitive questions, freeing your team for complex or high-value interactions. Most clients see improved team satisfaction."

**Objection:** "How long before we see results?"

**Response:** "Automation rates typically improve 5-10% in the first month, with ongoing improvements as we refine."

---

## Activation Timeline

### 30-Day Implementation Plan

**Week 1: Foundation**
- Helpdesk setup complete
- Channels configured
- Initial team training

**Week 2: Knowledge**
- Help Center articles created/imported
- 5 core Guidances written
- Tone of voice defined

**Week 3: Launch**
- AI Agent enabled on primary channel
- Initial performance monitoring begins
- Team starts providing feedback

**Week 4-8: Optimization**
- Analyze automation metrics
- Refine Guidances based on performance
- Add Actions
- Implement Flows
- Target: 10%+ automation rate achieved

**Ongoing: Long-term Success**
- Monthly performance reviews
- Quarterly Guidance audits
- Continuous merchant education
- Expansion discussions

---

## Key Success Factors

1. **Clear Knowledge Sources** - Well-written Guidance is foundation of AI Agent success
2. **Team Buy-In** - Support team must trust and actively use AI Agent
3. **Regular Feedback Loops** - Continuous improvement through monitoring and refinement
4. **Realistic Expectations** - Automation takes time and requires investment
5. **Documentation** - Keep Guidance and Help Center up-to-date
6. **Escalation Handling** - Clear handover process protects customer experience
7. **Metric Tracking** - Regular monitoring of automation rate, CSAT, escalations

---

**For detailed Guidance writing and AI Agent optimization, refer to the AI Agent Playbook in NOTION_SOURCES/ folder.**

