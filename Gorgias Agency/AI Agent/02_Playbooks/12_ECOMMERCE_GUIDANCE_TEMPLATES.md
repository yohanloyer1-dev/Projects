# 📝 Templates de Guidances E-commerce

## Objectif

Ce fichier contient des templates de guidances prêts à adapter pour les cas d'usage e-commerce les plus courants. Chaque template est structuré en scénarios avec des points de conclusion (End flow) et de transfert (Handover) clairement identifiés.

**Basé sur :** L'analyse de 28 guidances pour Nébuleuse Bijoux et les patterns récurrents identifiés dans les audits.

---

## Principes de rédaction des guidances

### Structure d'une bonne guidance

```
When a shopper [déclencheur]

Scénario 1 — [Condition]
THEN:
1. [Action 1]
2. [Action 2]
→ End flow / Handover (justifié par [raison])

Scénario 2 — [Condition]
THEN:
1. [Action 1]
→ End flow

General rules:
- [Règle 1]
- [Règle 2]
```

### Règles d'or

1. **Chaque scénario a une conclusion explicite** — "End flow" ou "Handover" avec justification
2. **Minimiser les handovers** — Si l'AI peut informer et conclure, il ne transfère pas
3. **Toujours proposer un next step au client** — Ne jamais laisser le client dans le vide
4. **Les liens sont des hyperlinks cliquables** — Pas des URLs brutes
5. **Le ton est empathique mais efficace** — Reconnaître le problème, donner la solution, conclure
6. **Utiliser les variables Shopify** — [ORDER_STATUS], [TRACKING_URL], [ORDER_DELIVERED_AT] etc.

### Anti-patterns à éviter

| Anti-pattern | Pourquoi c'est un problème | Solution |
|---|---|---|
| Handover après envoi de formulaire | L'AI a déjà donné l'info → devrait conclure | Ajouter message de clôture après le formulaire |
| Handover "par prudence" | Augmente le taux de handover sans raison | Ajouter des conditions de clôture explicites |
| Pas de guidance pour le suivi | Le client revient et tombe dans le vide | Créer guidance dédiée au suivi |
| Scénario catch-all → handover | Tous les cas non prévus transfèrent | Ajouter un message informatif avant le transfert |
| Trop de sous-scénarios | L'AI se perd dans la complexité | Regrouper les cas similaires |

---

## Template 1 : Suivi de commande (WISMO)

**Intent :** Order::Status
**Volume typique :** Le #1 ou #2 intent sur la plupart des comptes e-commerce

```
When a shopper asks about the status of their order

Scénario 1 — Order is fulfilled (shipped) and in transit < [X] days
THEN:
1. Confirm the order has been shipped
2. Share the tracking link: [TRACKING_URL]
3. Provide the carrier name and estimated delivery date
4. Reassure: "Your package is on its way and should arrive within [X] business days."
→ End flow

Scénario 2 — Order is fulfilled and in transit > [X] days
THEN:
1. Acknowledge the delay and apologize
2. Share the tracking link for the latest status
3. Advise the customer to check with the carrier / wait 24-48h for tracking updates
4. If the tracking shows no movement for > [Y] days → Handover
→ End flow (si mouvement récent) / Handover (si blocage confirmé)

Scénario 3 — Order is unfulfilled (not yet shipped)
THEN:
1. Confirm the order has been received and is being prepared
2. Provide the standard processing time: "[X] to [Y] business days"
3. Reassure: "You will receive a shipping confirmation email with tracking once it ships."
→ End flow

Scénario 4 — Order is delivered (confirmed by carrier)
THEN:
1. Confirm the delivery based on carrier data
2. Ask if the customer has received the package
3. If they confirm receipt → End flow
4. If they report non-receipt → Handover (investigation needed)

Scénario 5 — Order is returned to sender
THEN:
1. Inform the customer that the package has been returned to the warehouse
2. Apologize for the inconvenience
→ Handover (reship or refund decision needed)

General rules:
- Always start by checking the order status via Shopify data
- Adjust [X] days thresholds based on the merchant's typical shipping times
- During promotional/holiday periods, mention that delivery times may be extended
```

**Points de personnalisation :** Délais (X jours), transporteurs, messages de marque.

---

## Template 2 : Suivi de retour (Return Status)

**Intent :** Return::Status
**Volume typique :** Souvent dans le top 5 — et souvent ABSENT des guidances

```
When a shopper asks about the status of their return

Scénario 1 — Return package is in transit (not yet received by warehouse)
THEN:
1. Acknowledge the inquiry
2. If a return tracking number exists, share the tracking status
3. Inform standard processing time: "Once we receive your return at our warehouse, 
   processing takes [X] to [Y] business days."
4. Reassure: "You'll receive a confirmation email once your return is processed."
→ End flow

Scénario 2 — Return package received, processing in progress
THEN:
1. Confirm that the return has been received at the warehouse
2. Inform that processing is underway
3. Provide timeline: "Refund/exchange processing takes [X] business days from receipt."
→ End flow

Scénario 3 — Return processed, refund issued
THEN:
1. Confirm the return has been processed
2. Inform that the refund has been issued
3. Provide bank processing timeline: "The refund will appear on your account 
   within 5-10 business days depending on your bank."
→ End flow

Scénario 4 — Return processed, store credit / gift card issued
THEN:
1. Confirm the return has been processed
2. Inform that store credit has been issued to their account
3. Explain how to use the credit on next purchase
→ End flow

Scénario 5 — Return initiated more than [X] days ago, no update
THEN:
1. Acknowledge the concern about the delay
2. Apologize for the wait
→ Handover (manual investigation needed)

General rules:
- Always check return status data before responding
- If no return tracking exists, ask if the customer has shipped the package yet
- Be proactive about providing timelines — customers want dates, not vague reassurances
```

**Pourquoi ce template est important :** C'est le gap le plus fréquent. La plupart des clients ont une guidance pour "comment faire un retour" mais PAS pour "où en est mon retour".

---

## Template 3 : Suivi d'échange (Exchange Status)

**Intent :** Exchange::Status
**Même logique que le suivi de retour, adapté aux échanges**

```
When a shopper asks about the status of their exchange

Scénario 1 — Return package in transit, exchange not yet started
THEN:
1. Confirm the exchange request has been registered
2. If return tracking exists, share the status
3. Inform: "Once we receive your return, we'll ship the replacement within 
   [X] business days."
→ End flow

Scénario 2 — Return received, exchange being prepared
THEN:
1. Confirm receipt of the returned item
2. Inform the exchange is being prepared
3. Provide timeline for shipment of the new item
→ End flow

Scénario 3 — Exchange shipped
THEN:
1. Confirm the replacement has been shipped
2. Share the tracking information for the new package
3. Provide estimated delivery date
→ End flow

Scénario 4 — Exchange delayed (> [X] days since return received)
THEN:
1. Acknowledge the delay and apologize
→ Handover (manual investigation)

General rules:
- Check both the return status AND the new shipment status
- Proactively inform about next steps
- Standard exchange timelines: [customize per merchant]
```

---

## Template 4 : Garantie / Réclamation produit

**Intent :** Warranty::Claim, Product::Quality Issues
**Particulièrement pertinent pour :** bijouterie, accessoires, électronique, produits durables

```
When a shopper reports a defective product or warranty claim

Scénario 1 — No photo provided
THEN:
1. Acknowledge the situation and apologize
2. Ask for a clear photo/video of the defect
3. Wait for the customer's response
→ Continue to appropriate scenario once photo received

Scénario 2 — Photo received, order within warranty period (< [X] months/year)
THEN:
1. Acknowledge the defect and apologize
2. Check if a previous warranty claim exists for this product [if tracking available]
3. If this is the first claim:
   - Share the warranty claim form: [FORM_URL]
   - Inform timeline: "Our team will review your claim within [X] business days."
   - Provide reassurance
   → End flow
4. If this is a repeat claim (2nd+):
   - Inform the customer about the warranty policy for repeated claims
   → Handover (commercial decision needed) OR End flow with specific response

Scénario 3 — Photo received, order outside warranty period (> [X] months/year)
THEN:
1. Acknowledge the situation
2. Inform that the warranty period has expired
3. Apologize sincerely
4. Optionally: offer a goodwill gesture (discount code for next purchase)
→ End flow

Scénario 4 — Product purchased from a reseller / physical store
THEN:
1. Acknowledge the situation
2. Redirect to the point of purchase for warranty claims
3. Provide contact information for the store if available
→ End flow

General rules:
- Always start by checking the order date to determine warranty eligibility
- Be empathetic — the customer is disappointed
- After sharing a form, ALWAYS add a closing message (don't handover)
- Track warranty claims per product/customer to detect patterns
```

---

## Template 5 : Problèmes de livraison

**Intent :** Order::Damaged, Order::Missing Item, Shipping::Delivered Not Received

```
When a shopper reports a delivery issue

Scénario 1 — Product received damaged, photo shows clear damage
THEN:
1. Acknowledge and sincerely apologize
2. If warranty/claim form exists → share it
3. Inform timeline for processing
→ End flow (after form) / Handover (if reship/refund decision needed and no form)

Scénario 2 — Product received damaged, cosmetic but functional
THEN:
1. Acknowledge the concern
2. Ask if the product is still usable/wearable
3. If yes: offer a small goodwill gesture (discount on next order)
→ End flow

Scénario 3 — Wrong product received
THEN:
1. Acknowledge and apologize for the error
2. Ask for a photo of the received product
→ Handover (reship correct product + return label)

Scénario 4 — Missing item in package
THEN:
1. Acknowledge and apologize
2. Confirm the order contents
→ Handover (investigation + reship)

Scénario 5 — Package marked as delivered but not received
THEN:
1. Acknowledge the concern
2. Advise checking with neighbors, building manager, safe spots
3. Advise waiting 24-48h (sometimes carrier marks early)
4. If still not received after 48h → Handover (carrier investigation)

Scénario 6 — Wrong address provided by customer
THEN:
1. Inform that the address on the order is [ADDRESS]
2. If package not yet shipped → attempt address update
3. If already shipped and customer can't retrieve → Handover

General rules:
- Always request photos for damage claims
- Be empathetic — delivery issues are frustrating
- For carrier investigations, set expectations on timeline
```

---

## Template 6 : Promotions et codes promo

**Intent :** Promotion & Discount::Issue

```
When a shopper asks about promotions or has issues with a discount code

Scénario 1 — Shopper asks about current promotions
THEN:
1. Share the current active promotions (if any)
2. Provide the promo code and conditions
→ End flow

Scénario 2 — Discount code doesn't work
THEN:
1. Ask for the exact code they're trying to use
2. Check if the code is valid and active
3. Common issues: expired, minimum purchase not met, wrong product category, 
   already used, not combinable with other offers
4. Inform the customer about the specific issue
→ End flow

Scénario 3 — Shopper wants a discount but none available
THEN:
1. Inform that there are no active promotions currently
2. Invite them to sign up for the newsletter for future offers
3. Mention the loyalty program if applicable
→ End flow

Scénario 4 — Shopper applied wrong code after purchase
THEN:
1. Acknowledge the frustration
→ Handover (manual price adjustment needed)

General rules:
- Never invent or share codes that don't exist
- Be transparent about promotion conditions
- If no promotions are running, don't apologize — redirect to other value (loyalty, etc.)
```

---

## Comment adapter ces templates

### Pour chaque client

1. **Remplacer les [X] par les valeurs réelles** — délais de livraison, période de garantie, etc.
2. **Ajouter les liens spécifiques** — formulaire de garantie, portail retour, FAQ
3. **Adapter le ton** — selon le Tone of Voice configuré dans AI Agent
4. **Ajouter les scénarios spécifiques au produit** — bijouterie (oxydation, fermoir), mode (taille, couleur), tech (compatibilité, mise à jour)
5. **Vérifier la cohérence avec les handover topics** — s'assurer qu'un handover topic ne bloque pas les scénarios de la guidance

### Checklist avant déploiement

- [ ] Tous les [placeholders] remplacés par des valeurs réelles
- [ ] Liens vérifiés et fonctionnels
- [ ] Pas de chevauchement avec d'autres guidances
- [ ] Pas de chevauchement avec le Help Center / Store Sync
- [ ] Les scénarios de conclusion (End flow) sont maximisés
- [ ] Les handovers restants sont justifiés
- [ ] Le ton est cohérent avec le Tone of Voice configuré

---

*Templates créés en février 2026 — basés sur l'analyse de Nébuleuse Bijoux et les best practices Gorgias*
*À enrichir avec les patterns découverts chez chaque nouveau client*
