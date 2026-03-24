# Section 7: Testing, Compatibility, FAQs & Security

**Total Articles:** 5  
**Last Updated:** August 2, 2026  
**Status:** Complete ✅

---

## Table of Contents

1. [Compatibility of Automation Features with Ecommerce Stores](#compatibility-of-automation-features)
2. [How AI Agent Uses Vision to Understand Images](#how-ai-agent-uses-vision)
3. [Best Practices: Prepare Shopping Assistant for Sales Conversations](#best-practices-shopping-assistant)
4. [Security and Privacy FAQ for Gorgias AI Agent](#security-and-privacy-faq)
5. [Troubleshooting Common Issues](#troubleshooting-common-issues)

---

## Compatibility of Automation Features with Ecommerce Stores

**URL:** https://docs.gorgias.com/en-US/compatibility-of-automation-features-with-ecommerce-store-providers-1749413

This article explains which ecommerce stores are compatible with Gorgias's automation features.

### Requirements

- AI Agent and other automation features require an active AI Agent subscription

### Feature Compatibility Matrix

| Feature | Shopify | BigCommerce | Magento 2 | WooCommerce | Prestashop |
|---------|---------|-------------|-----------|------------|-----------|
| **AI Agent** | ✅ Supported | ❌ Not Supported | ❌ Not Supported | ❌ Not Supported | ❌ Not Supported |
| **Flows** | ✅ Supported | ✅ Supported | ✅ Supported | ❌ Not Supported | ❌ Not Supported |
| **Order Management** | ✅ Supported | ❌ Not Supported | ❌ Not Supported | ❌ Not Supported | ❌ Not Supported |
| **Article Recommendation** | ❌ Not Supported | ✅ Supported | ✅ Supported | ❌ Not Supported | ❌ Not Supported |

### Key Points

- **Shopify** — Fully compatible with all automation features
- **BigCommerce & Magento 2** — Support Flows and Article Recommendations, but not AI Agent or Order Management
- **WooCommerce & Prestashop** — Limited support; mostly Flows functionality

### What This Means

- **If you use Shopify** — You have access to all automation features including AI Agent and Order Management
- **If you use other platforms** — You can use Flows but won't have access to AI Agent or Order Management
- **Planning to expand** — Consider platform compatibility when evaluating which features to implement

### Migration Considerations

If you're planning to migrate to a different ecommerce platform, verify feature compatibility to ensure you won't lose automation capabilities.

---

## How AI Agent Uses Vision to Understand Images

**URL:** https://docs.gorgias.com/en-US/how-ai-agent-uses-vision-to-understand-images-1997855

AI Agent can read and understand images that customers send in email tickets or through other channels.

### What AI Agent Can Do With Images

**Recognize damaged products** — AI Agent can identify:
- Torn or broken items
- Stains or discoloration
- Packaging damage
- Assembly issues

**Understand product context** — AI Agent can:
- Identify product type and variant
- Understand usage context
- Recognize product issues
- Assess severity of damage

**Support visual troubleshooting** — AI Agent can help with:
- Installation or assembly issues
- Product defect diagnosis
- Before/after comparisons
- Product identification

### Supported Image Formats

- **JPG** — Standard photo format
- **PNG** — Images with transparency
- **WebP** — Modern web image format
- **GIF** — Including static GIFs
- **Screenshots** — System screenshots and diagrams

### Image Size Limitations

- Maximum image size: 20MB per image
- Recommended: Images 2-10MB for optimal processing
- Multiple images per ticket supported

### How to Enable Image Understanding

1. Image understanding is enabled by default with AI Agent
2. No additional configuration needed
3. AI Agent automatically analyzes images in tickets

### Benefits of Image Understanding

- **Better issue diagnosis** — Visual information improves accuracy
- **Reduced back-and-forth** — AI Agent can understand issues immediately
- **Faster resolution** — Issues with visual components resolve quicker
- **Reduced human review** — AI handles image analysis automatically

### Privacy Considerations

- Images are processed securely
- Images are not stored long-term
- Images are not used for training external models
- Customer privacy is protected

---

## Best Practices: Prepare Shopping Assistant for Sales Conversations

**URL:** https://docs.gorgias.com/en-US/best-practices-prepare-shopping-assistant-for-sales-conversations-1997856

To maximize Shopping Assistant's sales effectiveness, prepare your AI Agent with the right content and settings.

### Content Preparation

**Product Information** — Ensure all products have:
- Clear, compelling descriptions
- Benefit-focused copy (not just features)
- Use cases and customer scenarios
- Comparison information vs. alternatives
- Answer common questions about each product

**Sales Objection Handling** — Create Guidance that addresses:
- Price concerns
- Size/fit concerns
- Durability/quality questions
- Shipping/delivery questions
- Return policy concerns

**Cross-sell and upsell content** — Document:
- Complementary products that go well together
- Premium alternatives
- Popular bundle recommendations
- High-value additions

### Setting Up Sales Scenarios

**Create Guidance for common sales conversations:**

1. "New customer browsing" — First-time visitor needs guidance
2. "Customer comparing products" — Help them make decision
3. "Abandoned cart recovery" — Customer hesitating on purchase
4. "VIP customer" — Premium experience for top customers
5. "Customer with concerns" — Address objections

### Configure Discount Strategy

- **Positioning discounts as value** — Frame discounts as rewards, not desperation
- **Strategic timing** — Offer discounts when customer is most likely to convert
- **Personalized offers** — Different discounts for different customer segments
- **Urgency** — Use time-limited offers to encourage decisions

### Train on Successful Sales Interactions

1. Review your best sales conversations with live agents
2. Extract the patterns and techniques that work
3. Encode these techniques into AI Agent Guidance
4. Test with similar customer scenarios

### Messaging and Tone

**For Sales conversations, avoid:**
- Overly promotional language
- Pressure tactics
- Repeated offers of the same discount
- Aggressive upselling

**Instead, focus on:**
- Understanding customer needs
- Recommending solutions
- Building confidence in purchases
- Providing value

### Test Different Approaches

1. Deploy one sales approach
2. Monitor Shopping Assistant analytics for conversion rates
3. A/B test different discount strategies
4. Optimize based on performance data

### Monitor Sales Performance

Track key metrics:
- **Conversion rate** — % of Shopping Assistant conversations resulting in purchase
- **Average order value** — Are recommendations increasing order size?
- **Discount code usage** — Are offered discounts being used?
- **Customer satisfaction** — Are customers happy with recommendations?

---

## Security and Privacy FAQ for Gorgias AI Agent

**URL:** https://docs.gorgias.com/en-US/security-and-privacy-faq-for-gorgias-ai-agent-1997987

This FAQ addresses common questions about security, privacy, and data handling with Gorgias AI Agent.

### Large Language Model (LLM) Questions

**Q: Which large language model (LLM) does AI Agent use?**

A: AI Agent uses a combination of multiple secure LLM providers, including OpenAI, Anthropic, and internally fine-tuned models from Gorgias.

**Q: What is used to train my AI Agent?**

A: Your AI Agent's ability to recognize language comes from state-of-the-art LLMs from leading providers (OpenAI and Anthropic), plus proprietary Gorgias models.

Your AI Agent's ability to answer questions comes from:
- Your Shopify order and fulfillment data
- Your Gorgias Help Center and Guidance
- Public URLs you connect
- Documents you upload
- Custom product information

### Data Privacy Questions

**Q: Do you use my data to train external LLMs?**

A: No. The data AI Agent accesses does not train large language models from OpenAI or other third-party providers.

**Key details about our relationships with external AI providers:**

**Zero Data Retention** — OpenAI does not use data submitted through the API to train its models or improve future versions. Data is used only for processing the immediate request.

**No Long-Term Storage** — OpenAI has a zero data retention policy for API interactions. Once the request is processed, the data is not stored or logged.

**Q: How long is my data stored?**

A: 
- **Interaction data** — Deleted after processing. Not stored, reused, or saved
- **Training data** — Never used for external LLM training
- **Customer messages** — Stored only for conversation history, not for model training

### Security Questions

**Q: Is my data encrypted?**

A: Yes. All data is encrypted in transit and at rest using industry-leading encryption standards.

**Q: Where is my data hosted?**

A: Your data is maintained on Google Cloud Platform (GCP). Gorgias uses multiple servers globally and hosts data on the server closest to your location.

For example, if you're in the European Union, your server is located in the EU.

**Q: Is Gorgias compliant with data privacy regulations?**

A: Yes. Gorgias maintains compliance with:
- **GDPR** — European data privacy regulation
- **CCPA/CPRA** — California privacy laws
- **HIPAA** — Healthcare data privacy (if applicable)
- **All applicable privacy laws** — In your jurisdiction

### Compliance and Certifications

**Q: What certifications does Gorgias have?**

A: Gorgias maintains:
- **SOC 2, Type 2 compliance** — Since 2020
- **HIPAA compliance** — For healthcare data
- **Regular penetration tests** — By third-party security experts
- **Regular security audits** — To ensure highest standards

### Data Handling Questions

**Q: How is personally identifiable information (PII) protected?**

A: Gorgias uses:
- **Encryption** — Industry-leading encryption for PII
- **Access controls** — Strict controls on who can access data
- **Audit logging** — Tracking all access to PII
- **Secure transmission** — HTTPS and encryption in transit

PII protected includes:
- Names
- Email addresses
- Phone numbers
- Locations
- IP addresses
- Payment information

**Q: Can customers ask Gorgias to delete their data?**

A: Yes. Customers can request data deletion through privacy/GDPR requests, which Gorgias processes according to applicable laws.

### Safety and Quality Questions

**Q: How does Gorgias prevent AI Agent from providing harmful information?**

A: Gorgias implements multiple safety measures:

**Grounded Responses** — AI Agent only answers based on verified content from your knowledge sources. If it can't find an answer, it won't respond.

**Quality Assurance Checks** — Every response passes through an internal QA system using a second AI model. Responses only send if they meet a high confidence threshold.

**Exclusion and Handover Topics** — You define topics AI Agent should ignore or hand off to humans.

**Transparency and Review** — Every AI-generated message is labeled "Automated." You can review and audit responses.

**Q: What happens if AI Agent provides incorrect information?**

A: 
1. You can review the response and give feedback
2. You can edit the knowledge source to correct the information
3. AI Agent learns from your feedback for similar future questions
4. Systematic feedback helps improve overall accuracy

### Transparency Questions

**Q: Can I see how AI Agent made a decision?**

A: Yes. For every AI Agent response, you can:
- View the reasoning behind the response
- See which knowledge sources it used
- Understand what context it considered
- Review the decision-making process

**Q: Can I audit AI Agent's responses?**

A: Yes. You can:
- Review all AI-generated tickets
- See which responses are marked "Automated"
- Access detailed reasoning for each response
- Export audit logs for compliance purposes

### Additional Resources

**For more information:**
- Visit Gorgias's Trust Center
- Review Privacy Policy
- Review Terms of Service
- Contact Gorgias Security Team for specific questions

---

## Troubleshooting Common Issues

**URL:** Not a primary documentation page, but included here for completeness

### AI Agent Not Responding

**Possible causes:**
- AI Agent not enabled on the channel
- No relevant knowledge available
- Topic marked as handover-only
- AI Agent confidence below threshold

**Solutions:**
1. Check if AI Agent is enabled in Deploy settings
2. Add more knowledge about the topic
3. Remove the topic from handover list (if appropriate)
4. Give feedback to improve confidence

### AI Agent Responding Incorrectly

**Possible causes:**
- Outdated knowledge
- Conflicting Guidance
- Missing context
- Ambiguous instructions

**Solutions:**
1. Review and update relevant knowledge
2. Clarify Guidance using WHEN/IF/THEN structure
3. Test conversation to see what information AI Agent is using
4. Give negative feedback to prevent similar errors

### Low Automation Rate

**Possible causes:**
- Insufficient knowledge
- Too many handover topics
- Guidance not covering common scenarios
- Customer language doesn't match knowledge

**Solutions:**
1. Use Intents page to identify underperforming topics
2. Add relevant Guidance for common scenarios
3. Reduce handover topics if appropriate
4. Review and update knowledge to match customer language

### Incorrect Auto-Tagging

**Possible causes:**
- Tags not properly configured
- Ambiguous ticket content
- Tags not matching conversation topic

**Solutions:**
1. Review tag configuration rules
2. Provide feedback on mistaggged tickets
3. Simplify tag structure if too complex
4. Use different rule for specific scenarios

### Actions Not Executing

**Possible causes:**
- Action not referenced in Guidance
- Conditions not met
- Third-party app integration issue
- Permission problems

**Solutions:**
1. Verify action is referenced in Guidance
2. Check action conditions are met
3. Test third-party app integration
4. Check API credentials and permissions

---

**End of Section 7: Testing, Compatibility, FAQs & Security**

