# Nébuleuse Bijoux — Conversation Gaia AI (Gorgias) : Returns & Exchanges

> **Context :** This document is a transcription of a past conversation held with **Gaia**, the AI assistant built into Gorgias. The conversation was focused on analysing Nébuleuse Bijoux's internal returns & exchanges policy in order to improve AI Agent automation.
>
> The conversation could not be completed inside Gaia due to two limitations:
> 1. **Text volume** — the full internal policy was too large to paste in a single session without triggering errors.
> 2. **Screenshot processing** — Gaia was unable to process the volume of screenshots needed to read the full internal KB.
>
> This is why the work was continued in two separate MD files:
> - **This file** — the transcript of the Gaia conversation, preserved for context and continuity.
> - **`nebuleuse_internal_policy_returns_exchanges.md`** — the full internal returns & exchanges policy, transcribed from all 77 KB screenshots into a structured Markdown document.

---

## Conversation Transcript

---

### Message 1

**Yohan:**

Hey the conversations failed the last 3 times - if there is too much information to process please let me know before you encounter any issue.

I'm going to paste below the prompts from our previous conversation. Messages are separated by "answer" after the first one then "NEXT". You were basically analyzing batches of screenshots of the merchants' internal policy. I'd like to pick up the conversation and send you all the batches again.

---

Hey, the last two conversations ended up in errors. If you think there is too much data to process or there might be another error coming up, please let me know so we can avoid it.

That being said, I have laid out a plan of improvement that we can do to reach 50% automation. I'm going to share the plan with you below, but basically we have already delivered on step 1.1, 1.2, 1.3, and 1.4. The two major points that we need to focus on are 1.5 and 1.6, specifically around returns and exchanges requests:

> Based on a comprehensive 60-day audit of 41,419 messages across 12,024 tickets, I have identified a clear path to increase AI Agent automation from 8.1% to 50% through optimization of guidances, actions, and feature enablement.

#### Key Insight

AI Agent performs well at identification and response — the issue is unnecessarily transferring tickets to human agents rather than concluding them, and not having AI Agent able to perform actions.

#### Economic Impact

| Metric | Current | Target (50%) | Improvement |
|---|---|---|---|
| Automation Rate | 8.1% | 50% | +41.9% |
| Tickets/month resolved | 488 | 1,414 | +928 |
| Monthly outsourcing cost | ~€12,000 | €6,000 | -€6,000 |
| AI Agent cost | €589 | €1,035 | +€446 |
| Net monthly savings | €411 | €5,554 | +€1,454 |
| Annual net savings | ~€4,900 | ~€66,648 | +€61,716 |

---

#### 📋 Current Baseline (60-day audit)

**Performance Metrics**

| Metric | Current | Target |
|---|---|---|
| Automation Rate | 8.1% | 50% |
| Coverage Rate | 38.9% | 65% |
| Success Rate | 25.3% | 45% |
| CSAT | 3.5/5 | 4.0/5 |
| First Response Time | 23min 20s | <30min |
| Handover Rate | 33.6% | <15% |

**Problem Areas Identified**

- **Systematic Handovers (1,744 tickets):** 91% of unsuccessful tickets: AI gives complete response → transfers unnecessarily
- **Ignored Tickets (1,933 emails, 36.7%):** Email tickets never attempted due to broad ignore rules
- **Missing Guidances:**
  - Return/Status: 2.6% success (535 tickets)
  - Exchange/Status: 5.8% success (327 tickets)

**What Works Well (Success >70%)**

- Jewelry care: 92% | Shipping costs: 86% | Oxidation: 82%

---

#### 🎬 Phase 1 — Quick Wins (Weeks 1-2)

**Target Impact: +15% to +25% automation | Effort Level: Low**

**Task 1.1: Reduce Ignored Tickets**
- Timeline: 3 days | Impact: +3% to +5% automation | Tickets recovered: ~338
- What to do: Review ai_ignore rules, remove overly broad blocks for Return/Status, Order/Status, Warranty

**Task 1.2: Affine Handover Topics**
- Timeline: 3 days | Impact: +5% to +7% automation | Tickets recovered: ~95
- What to do: Separate "reimbursements" topic into status checks (AI) vs. new refund requests (handover)

**Task 1.3: Optimize WISMO Guidance**
- Timeline: 4 days | Impact: +4% to +6% automation | Tickets recovered: ~15
- What to do: Add response for Unfulfilled orders, reduce handover triggers → Create Shipup action to start a "reclamation" with the transporter

**Task 1.4: Optimize Warranty Guidance**
- Timeline: 4 days | Impact: +2% to +3% automation | Tickets recovered: ~20
- What to do: Replace handover with conclusion message after Typeform submission

**Task 1.5: Create Return/Status Guidance**
- Timeline: 5 days | Impact: +3% to +4% automation | Tickets recovered: ~125
- What to do: Create guidance for tracking return status at each stage

**Task 1.6: Create Exchange/Status Guidance**
- Timeline: 5 days | Impact: +3% to +4% automation | Tickets recovered: ~95
- What to do: Create guidance for tracking exchange status at each stage

**Task 1.7: Deploy AI Agent to Chat**
- Timeline: 3 days | Impact: +3% to +5% automation | Tickets recovered: ~210 tickets/60 days
- What to do: Enable AI Agent on Chat channel, monitor CSAT and response times

**Phase 1 Summary**
- Total Impact: +23% to +34% automation
- Total Tickets Recovered: +893 tickets
- Expected new automation rate: 8.1% → ~30-35%

---

Before I send you a lot of screenshots detailing the internal returns and exchanges policy of the merchant, I need you to review the way we are dealing with returns and exchanges currently with AI agents. What is the status quo of the guidelines? What are the main reasons we are handing over tickets? What are the replies that agents are sending when we are handing over tickets?

Once you have a clear picture of the current situation, on that topic I'm going to send you all the internal policy of the merchant so you can analyse it, review it, compare it to the existing guidelines and the analysis you've just done. The output should be to either optimise existing guidelines or create new ones. Let me know if that is clear and if you have any questions. Before we start, I also would like you to analyse the tags that we are using in order to identify the channel the orders were placed on, such as:
- marketplaces directly in the Shopify store
- in-store
- on Mirakl, etc.

You can do that by searching for the tag on order #310639. We're going to use these tags moving forward to adapt the guidelines based on the channel of the orders.

---

### Answer 1

**Gaia:**

Current Status Quo — Returns & Exchanges with AI Agent

Here's the full picture, Yohan. This is structured in three parts: (1) current guidances, (2) handover analysis, and (3) order channel tags.

#### 1. Current Guidances

Two active guidances exist:

**📄 "If a shopper asks about returns" (id: 2469111, last updated Mar 11)**

This is a fairly detailed guidance covering 6 scenarios:

- **Scenario 1 — Return eligibility:** checks if order is found, calculates 30-day window from delivery, branches by purchase channel (online store → return portal link, Nébuleuse Boutique Marais → in-store exchange, BHV Corner → specific hygiene rules for earrings/piercings)
- **Scenario 2 —** How to pack a return
- **Scenario 3 —** Returning multiple orders together
- **Scenario 4 —** Return process (directs to return portal)
- **Scenario 5 —** Managing an existing return request (add items, or hand over for any other update)
- **Scenario 6 —** Refund/reimbursement status → always hands over (acknowledges, says processing can take 30 days, then hands over)

> **Key observation:** Scenario 6 (refund status) is also listed as an excluded handover topic in the AI Agent config: "Customer asking about the status of a pending refund, store credit, or financial processing of a ret..." — so AI is explicitly told to hand over these tickets.

**📄 "When a shopper asks about exchanges" (id: 2949239, last updated Nov 2025)**

This is a simpler guidance:
- If within 30 days: eligible for exchange of same piece in gold/silver, same price → shares exchange portal link
- If different value item → hand over
- If over 30 days → hand over (with internal note)
- Else (any other case) → hand over

> **Key observation:** This guidance has 3 out of 4 paths ending in handover. Only the "same piece, same price, within 30 days" path resolves autonomously.

---

#### 2. Handover Analysis (Last 60 Days)

**Volume breakdown by intent and outcome**

| Intent | Handover (topics) | Handover (other) | Auto-resolved | Total |
|---|---|---|---|---|
| Status (return/refund status) | 146 | 56 | 23 | 227 |
| Request (new return/exchange request) | 57 | 42 | 50 | 149 |
| Information | 5 | 2 | 4 | 11 |
| Other | — | 3 | — | 3 |

The dominant pattern is clear: "Status" tickets are the #1 problem. **202 out of 227 status tickets (89%) are handed over.** These are customers asking "Where is my return? Have you received my package? When will I get my refund?"

**What AI says before handing over**

The AI's responses follow an almost identical template across all handover tickets. Here are representative examples:

> "Je comprends votre préoccupation concernant le retour de votre commande. Je transmets votre demande à l'équipe dédiée qui va examiner la situation..."

> "Merci pour votre message. Je vais transmettre votre demande à l'équipe spécialisée qui pourra examiner votre dossier..."

> "Je comprends votre inquiétude concernant le remboursement... Je transmets votre demande à l'équipe concernée..."

Pattern: AI acknowledges → says "I'll transfer to the team" → hands over. It provides **zero actionable information** to the customer. This is the core problem your plan identified — the AI gives a complete-sounding response but resolves nothing.

**What human agents actually do after handover**

For return status inquiries (most common):
1. Check if the return parcel was received by logistics: *"Nous avons bien reçu votre colis et notre équipe logistique va bientôt le vérifier."*
2. Set the 30-day processing expectation: *"Nous nous engageons à vous apporter une réponse dans un délai maximum de 30 jours dès réception de ce dernier."*
3. Trigger the refund when confirmed: *"Nous venons de déclencher votre remboursement. Vous le recevrez sur le moyen de paiement que vous avez utilisé dans un délai de 2 à 5 jours ouvrés."*
4. Handle stock issues for exchanges: *"Les modèles sont actuellement en rupture de stock, ce qui explique que l'échange n'ait pas encore pu être finalisé. Nous pouvons vous proposer un avoir..."*
5. Issue store credits (avoirs) with codes: *"Vous avez reçu un avoir de 38,00€. Le code à utiliser est : bahwirxp60"*

For new return/exchange requests:
1. Direct to the return portal (AI already does this in some cases)
2. Explain the process step by step: *"Rendez-vous sur notre centre de retours avec votre numéro de commande et votre adresse e-mail. Suivez les instructions et sélectionnez les articles."*
3. Confirm approval and send return label: *"Votre demande de retour a bien été approuvée. Je vous transmets votre étiquette de retour ci-jointe."*

---

#### 3. Order Channel Tags

| Channel | Identifier | Volume |
|---|---|---|
| Online Store (web) | source_name = 'web' + tag Online Store | ~92,700 orders |
| POS — In-Store (all locations) | source_name = 'pos' + tag POS | ~56,000 orders |
| POS — Marais | Tag contains `PL - Marais` | ~6,300 orders |
| POS — St-Germain | Tag contains `PL - St-Germain` | ~3,000 orders |
| Choose (marketplace) | source_name = 'Choose' | ~7,400 orders |
| Galeries Lafayette (Mirakl) | source_name = 'Galeries Lafayette' + tags contain `Galeries Lafayette`, `Mirakl` | ~1,770 orders |
| BaBack (exchange platform) | source_name = '6591049' + tags contain `BABACK`, `BB_EXCHANGE` | ~4,200 orders |
| Draft Orders (internal) | source_name = 'shopify_draft_order' — used for warranty replacements (Garantie), defective items (Défectueux), forgotten items (Oubli), lost parcels (Colis Bloqué/Perdu), return-to-sender (retour expéditeur) | ~24,700 orders |
| TikTok | source_name = 'tiktok' | ~200 orders |
| Etsy | source_name = 'etsy' | ~71 orders |
| Faire (wholesale) | source_name = 'faire' or 'Faire' | ~86 orders |

For order #310639 specifically: Tags = `Galeries Lafayette`, `Mirakl`, `Ship by 2024/04/04` with source_name = `Galeries Lafayette`. So this is a Mirakl/Galeries Lafayette marketplace order.

**Key tags for guidance logic:**
- `&&&order.order_tags&&&` containing `'Mirakl'` or `'Galeries Lafayette'` → marketplace order (different return policy)
- `&&&order.order_tags&&&` containing `'POS'` → in-store purchase
- `&&&order.order_tags&&&` containing `'PL - Marais'` → Nébuleuse Boutique Marais
- `&&&order.order_tags&&&` containing `'BABACK'` or `'BB_EXCHANGE'` → exchange already processed via BaBack platform
- `&&&order.order_tags&&&` containing `'Garantie'` or `'Défectueux'` → warranty/defective replacement order

---

#### Summary & Next Steps

The core problem is crystal clear:

1. **Return/refund STATUS tickets (89% handover rate, ~200 tickets/60 days):** AI has no ability to check return processing status. It can't tell the customer whether the parcel was received, whether the refund was triggered, or give a timeline. The guidance explicitly hands over for refund status (Scenario 6), and it's also an excluded handover topic.
2. **Exchange guidance is too restrictive (3/4 paths → handover):** Only same-piece/same-price exchanges resolve autonomously. Different-value exchanges, expired windows, and "anything else" all hand over — even though human agents often just redirect to the return portal.
3. **Missing channel-aware logic:** The return guidance has some channel branching (online vs Marais vs BHV) but doesn't handle Galeries Lafayette/Mirakl, Choose, or BaBack orders — which together represent ~13,000+ orders.

I'm ready for the merchant's internal policy. Once you share it, I'll:
- Compare it against the current guidances and the handover patterns above
- Identify what can be automated vs what genuinely needs human intervention
- Draft optimized/new guidances with channel-aware branching using the tag system we just mapped
- Focus on reducing the ~200 status handovers and the exchange handover rate

Send the policy whenever you're ready! 🌙

---

### Message 2

**Yohan:** *(Batch 1 screenshots sent)*

---

### Answer 2

**Gaia:**

Batch 1 Summary — Internal Policy: "306 Retour/Échanges/Suivi d'un retour"

This is the merchant's internal knowledge base (macros/procedures) that agents follow. It's organized as a decision tree. Here's the full structure I've captured:

#### Cas 1: Conditions générales de retour

**Sous-cas 1: Client souhaite un échange**

Step 1: Check if order appears in Shopify → two possibilities

**Possibilité 1: Commande apparaît sur Shopify** → Step 1: Identify the purchase channel via order source/tags

| Channel | Exchange Policy | Key Detail |
|---|---|---|
| Option 1: Mirakl | 30 days from receipt for return only (no exchange offered) | "Nous ne proposons malheureusement pas d'échange." — Ask which items to return, agent handles it |
| Option 2: Online Store | 30 days from receipt, exchange for same piece in GOLD or SILVER, same size choice, same price only | Direct to return portal link |
| Option 3: BHV Corner | Earrings & piercings: no return/exchange (BHV hygiene policy). Titanium piercings: 7 days. Rings/necklaces/bracelets: 30 days for exchange | Must bring receipt to BHV |
| Option 4: Boutique Marais | 30 days from receipt to exchange | Must bring order number or receipt to boutique in person |

**Possibilité 2: Commande n'apparaît pas sur Shopify** → Redirect to partner store's return policy: "Nous vous invitons à vous référer à la politique de retour de la boutique partenaire... Malheureusement nous n'avons pas la main sur leur politique de retour et d'échange." → Send & Close

---

**Sous-cas 2: Délai pour effectuer un retour**

Step 1: Check if order appears in Shopify

**Possibilité 1: Commande apparaît sur Shopify** → Check purchase channel:

| Channel | Return Window | Special Periods |
|---|---|---|
| Option 1: Online Store | 30 days from receipt | Has special period overrides: Noël (01/12–31/12/2025) and Black Weeks (01/11–01/12/2025) — separate sub-rules for ≤30 days and >30 days |
| Option 2: Mirakl | 30 days from receipt | ≤30 days: return via Galeries Lafayette account. >31 days: window expired, inform & close |
| Option 3: BHV Corner | Same as exchange rules (earrings/piercings no return, titanium 7 days, others 30 days) | — |
| Option 4: Boutique Marais | 30 days from receipt, must bring order/receipt to boutique | — |

**Possibilité 2: Commande n'apparaît pas sur Shopify** → Same redirect to partner store policy → Send & Close

---

**Sous-cas 3: Frais de retour**

→ Check shipping country:
- Option 1: France 🇫🇷, Belgique 🇧🇪, Allemagne 🇩🇪, Espagne 🇪🇸, Luxembourg 🇱🇺, Pays-Bas 🇳🇱, Portugal 🇵🇹 *(details not yet shown)*
- Option 2: Tout autre pays *(details not yet shown)*

Remaining sub-cases visible in sidebar (not yet detailed):
- Sous-cas 4: Demande de retour pour une commande à 0€ (recommande car produit perdu/défectueux etc)
- Sous-cas 5: Un bijou acheté sur le site peut-il être retourné en boutique ?
- Sous-cas 6: Retourner les bijoux cadeaux de la commande

Other top-level cases visible:
- Cas 2: Procédure de retour
- Cas 3: Suivi et gestion de la demande de retour
- Cas 4: Remboursement

**Key Gaps vs. Current AI Guidance**

Already from Batch 1, I can see several important differences:

1. **Mirakl/Galeries Lafayette: No exchange, return only** — The current AI exchange guidance doesn't distinguish Mirakl orders at all. The internal policy explicitly says "Nous ne proposons pas d'échange" for Mirakl and the agent handles the return manually.
2. **BHV Corner has identical rules for both exchange and return** — The current AI guidance partially covers this but the internal policy is more explicit (earrings/piercings = no return OR exchange, titanium piercings = 7 days, others = 30 days).
3. **Special holiday periods (Noël, Black Weeks)** — The internal policy has extended/modified return windows during these periods. The current AI guidance has no awareness of seasonal overrides.
4. **Order not found in Shopify = partner store** — Both exchange and return flows have a clean "redirect to partner store policy" path that closes the ticket. The current AI guidance partially handles this but could be more decisive.
5. **Channel detection via order tags** — The internal policy uses the Shopify order source to identify the channel. We now have the tag mapping to automate this (Mirakl, POS, PL - Marais, etc.).

---

### Message 3

**Yohan:** *(Batch 2 screenshots sent)*

---

### Answer 3

**Gaia:**

Batch 2 carefully reviewed. Here's everything I've extracted:

Batch 2 Summary — Remaining Cas 1 sub-cases + Cas 2: Procédure de retour

#### Cas 1 (continued)

**Sous-cas 3: Frais de retour (Return shipping costs)**

> 🟡 Key policy rule (yellow banner): 5€ return fee charged when the return reason is: *L'article ne me plaît pas / Taille trop grande / Taille trop petite* — and refund is via Remboursement/Bon d'achat (refund or store credit). No fee for: *Défectueux / Mauvais article reçu* and for exchange requests.

| Destination | Policy |
|---|---|
| Option 1: FR, BE, DE, ES, LU, NL, PT | Prepaid return label provided after approval. Drop off at Chronopost relay point. 5€ fee deducted for "rétractation" (change of mind) returns. Direct to return portal if not yet initiated. |
| Option 2: All other countries | Customer receives email with instructions + return shipping cost amount to pay. Direct to return portal if not yet initiated. |

> **AI guidance gap:** The current guidance has zero mention of the 5€ fee or the free-return exceptions. This is important information customers ask about.

---

**Sous-cas 4: Demande de retour pour une commande à 0€ (replacement orders for lost/defective products)**

> 🔴 Key policy rule (red banner): The customer must submit a return request on the replacement order (at 0€) and the refund must be processed on the original order.

Step 1: Check for the "Garantie" tag on the order in Shopify

| Scenario | Policy |
|---|---|
| Possibilité 1: "Garantie" tag present (SAV/defective replacement) | Direct to return portal on the new replacement order (0€ one). 30-day window from delivery. After approval, confirmation email with shipping instructions. |
| Possibilité 2: No "Garantie" tag (paid with loyalty points) | Same return process via portal, 30 days. Additional step: "Je vous invite à nous recontacter une fois le retour reçu dans notre entrepôt afin que nous puissions vous recréditer les points fidélité." |

> **AI guidance gap:** Current guidance has no awareness of 0€ replacement orders or the Garantie tag logic. This is a niche but important scenario.

---

**Sous-cas 5: Un bijou acheté sur le site peut-il être retourné en boutique ?**

Step 1: Where was/will the jewelry be purchased?

| Scenario | Policy |
|---|---|
| Possibilité 1: Boutique Nébuleuse | Yes — can return/exchange online-purchased items at the Parisian boutique. Bring order number, within 30 days of delivery. |
| Possibilité 2: Points de vente partenaires | No — cannot return/exchange online items at partner stores or BHV corner. But can do online return via portal within 30 days. |
| Possibilité 3: Not specified | Offer both options: online return via portal (30 days) OR visit a Nébuleuse Parisian boutique with order number within 30 days. |

> **AI guidance gap:** The current guidance partially covers this (Marais boutique) but doesn't explicitly state that online items cannot be returned at BHV or partner stores. The "not specified" fallback is also missing.

---

**Sous-cas 6: Retourner les bijoux cadeaux de la commande**

Policy: If the customer wants to return all items including gift items, they must include the gift items in the return request. Direct to return portal with order number and email. After approval, confirmation email with shipping instructions.

Available in FR and EN (bilingual macro).

---

#### Cas 2: Procédure de retour

**Sous-cas 1: Comment emballer son retour ?**

> 🟠 Internal note: "La logistique identifie tout de suite la demande de retour grâce au numéro de suivi sur l'étiquette"

Policy: Any protective packaging is fine. Key requirement: use the return label provided so logistics can identify and process the return.

**Sous-cas 2: Retourner plusieurs commandes dans 1 colis**

Policy: One return request per order via the return portal. Each approved return generates its own label. One package per return request — cannot combine multiple orders in one package.

**Sous-cas 3: Comment faire un retour ?**

Same channel-based decision tree:

Step 1: Check if order appears in Shopify → same Possibilité 1/2 split

Possibilité 1: Order in Shopify → Check channel:
- **Option 1: Online Store** → Check delivery date → ≤30 days: check shipping country (FR/BE/DE/ES/LU/NL/PT vs other) → direct to return portal. >30 days: window expired.
- **Option 2: Mirakl** *(details not shown in this batch but structure visible)*
- **Option 3: BHV Corner** *(macro visible)*
- **Option 4: Boutique Nébuleuse (Marais)/Saint-Germain** *(macro visible — note: Saint-Germain is now included!)*

Possibilité 2: Order not in Shopify → redirect to partner store policy

> **New finding:** Option 4 now includes Saint-Germain alongside Marais — the current AI guidance only mentions Marais.

---

#### Running Gap Analysis (Batches 1+2 combined)

| Policy Element | In Internal KB | In Current AI Guidance | Gap? |
|---|---|---|---|
| 5€ return fee (change of mind) | ✅ | ❌ | YES |
| Free returns for defective/wrong item/exchanges | ✅ | ❌ | YES |
| Mirakl = return only, no exchange | ✅ | ❌ | YES |
| Chronopost drop-off for EU returns | ✅ | ❌ | YES |
| Non-EU: customer pays return shipping | ✅ | ❌ | YES |
| 0€ replacement order (Garantie tag) | ✅ | ❌ | YES |
| Loyalty points re-credit after return | ✅ | ❌ | YES |
| Online items can be returned at Boutique Nébuleuse | ✅ | Partial | Partial |
| Online items CANNOT be returned at BHV/partners | ✅ | ❌ | YES |
| Saint-Germain boutique (not just Marais) | ✅ | ❌ | YES |
| Gift items must be included in return | ✅ | ❌ | YES |
| One package per return request | ✅ | ✅ | OK |
| Holiday period return extensions | ✅ | ❌ | YES |

Ready for Batch 3! I'm expecting Cas 3 (return tracking/management) and Cas 4 (refund/reimbursement) — these are the highest-impact sections for reducing those ~200 status handovers. Send whenever you're ready 🌙

---

*— End of captured conversation. Batches 3+ could not be processed by Gaia due to context/size limitations. See `nebuleuse_internal_policy_returns_exchanges.md` for the full policy covering Cas 3 and Cas 4.*
