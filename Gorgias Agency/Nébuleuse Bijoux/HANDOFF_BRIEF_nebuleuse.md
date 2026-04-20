# 🔁 HANDOFF BRIEF — Nébuleuse Bijoux AI Agent Audit
## Pour la prochaine conversation Claude

**Instruction d'ouverture pour le nouveau chat :**
> "Je travaille sur l'audit AI Agent Gorgias pour Nébuleuse Bijoux (nebuleusebijoux.com). J'ai une conversation précédente très complète avec toi sur ce sujet. Peux-tu la retrouver et reprendre exactement là où on s'est arrêtés ?"

---

## CONTEXTE COMPLET DU PROJET

### Qui
- **Client :** Nébuleuse Bijoux — bijouterie e-commerce française
- **Outil :** Gorgias AI Agent ("L'assistant cosmique Nébuleux")
- **Partenaire support actuel :** One Pilot (gère quasi tout le SAV humain)
- **Yohan** = consultant Gorgias qui prépare un audit pour le client

### Objectif
Produire un **rapport HTML en français**, partageable par lien, orienté **opportunités d'automatisation**, pour montrer au client le potentiel inexploité et ce que Yohan va travailler pour améliorer le coverage rate et l'automation rate.

---

## MÉTRIQUES CLÉS (tout est analysé)

### Chiffres réels (corrigés)
| Métrique | Valeur | Période |
|----------|--------|---------|
| **AI Agent Automation Rate** | **8.61%** | 60 jours |
| **AI Agent Automation Rate** | **7.65%** | 30 jours |
| Overall automation rate | 9.3% / 8.23% | 60j / 30j |
| Automated interactions | 886 / 387 | 60j / 30j |
| Coverage Rate | 41.1% (+8%) | 28j |
| Success Rate | 23.9% (-8%) | 28j |
| CSAT | 3.7/5 (+14%) | 28j |
| FRT | 32s | 28j |
| Coût économisé | $2,197 | 60j |
| Temps agents économisé | 1j 04h | 60j |
| **Objectif cible** | **50%** | — |

**Note importante :** La baisse récente (22%) est due à la fin du BFCM qui gonflait le volume de tickets facilement automatisables (suivi colis, promos).

### Top 10 Intents (28 jours)
| Intent | Tickets | Success | Handover Topic |
|--------|---------|---------|---------------|
| Order/Status | 164 | 54.9% | 1.2% |
| Product/Quality Issues | 131 | 38.2% | 18.3% |
| Warranty/Claim | 95 | 29.5% | 12.6% |
| Shipping/Delivered Not Received | 84 | 15.5% | 3.6% |
| **Return/Status** | **81** | **3.7% 🚨** | **84%** |
| Order/Missing Item | 66 | 10.6% | 4.5% |
| **Exchange/Status** | **59** | **0% 🚨** | 40.7% |
| Order/Damaged | 58 | 6.9% | 29.3% |
| Promotion & Discount/Issue | 54 | 22.2% | 14.8% |
| Exchange/Request | 54 | 25.9% | 24.1% |

---

## ÉTAT DE LA CONFIGURATION (confirmé par screenshots)

### Ce qui est configuré mais cassé/inactif
| Feature | État | Problème |
|---------|------|---------|
| **Track Order (OM)** | ✅ Activé | ⚠️ "No response configured" |
| **Return Order (OM)** | ✅ Activé | OK mais non optimisé |
| **Cancel Order (OM)** | ❌ Désactivé | — |
| **Report Order Issue (OM)** | ✅ Activé | — |
| **Action "Get order info"** | ❌ Toggle OFF | Créée mais inactive |
| **Action "Update shipping address"** | ❌ Toggle OFF | Créée mais inactive |
| **Flows** | ❌ Zéro données | Jamais déployés |
| **Article Recommendations** | ❌ Zéro données | Jamais déployés |
| **Chat** | ❌ Non déployé | Email uniquement |

### Ignore Rule (bien configurée)
Bloque l'IA sur : `order/cancel`, `refund/request`, `refund/status` + sentiments négatifs + tags "Negative"/"Annulation commande" + emails partenaires (Centrelog, Baback, Galeries Lafayette)

### Handover Topics (trop larges — problème identifié)
- "Enquiries about reimbursements" → 98 tickets bloqués
- "Enquiries about refunds" → 91 tickets bloqués  
- "Customers requiring a discount code" → 11 tickets
**Ces topics capturent des suivis de statut qui pourraient être résolus.**

### Knowledge Base
- 28 guidances actives (bien rédigées, en français)
- Help Center : https://nebuleusebijoux.com/pages/faqs (synced Gorgias)
- **Nouveau site web lancé cette semaine** → resync à prévoir (pas urgent)
- Actions à réactiver : "Get order info" + "Update shipping address"

---

## INSIGHT CLÉ — ONE PILOT

One Pilot gère le SAV humain de Nébuleuse Bijoux. Leur KB prouve que les cas "impossibles à automatiser" sont en réalité **envoyés en Send & Close par les agents humains**.

### Topics One Pilot à extraire (priorités pour Guidances Gorgias)
| # | Sujet | Lien avec défaillances Gorgias |
|---|-------|-------------------------------|
| **304** | Suivi commande / Expédition / Livraison | Order/Status, WISMO |
| **306** | Retour/Échanges/Suivi d'un retour | Return/Status 3.7%, Exchange/Status 0% |
| **307** | Produits défectueux / Non conformes | Product/Quality, Warranty |
| **308** | Mauvais articles reçus / Oubli | Order/Missing Item |
| **302** | Annulation de la commande | Order/Cancel |
| **303** | Modification de la commande | Order/Edit |
| **203** | Opérations commerciales / Codes promos | Promo & Discount |
| **105** | Programme de Fidélité | Account/Other |
| **401** | Cartes cadeaux | Gift card queries |

**Ce qu'on a déjà vu dans la KB One Pilot (screenshot 306) :**
- Structure : Cas 1 Conditions → Cas 2 Procédure → **Cas 3 Suivi et gestion** → Cas 4 Remboursement
- Template exact visible pour "Option 2 : Online Store" → échange dans les 30j
- Ticketing tool: Gorgias + **Send & Close** confirmé

---

## FICHIERS PRODUITS DANS CETTE CONVERSATION

Tous dans `/mnt/user-data/outputs/` :
- `nebuleuse_bijoux_ai_agent_audit.md` — analyse complète en anglais (draft)
- `HANDOFF_BRIEF_nebuleuse.md` — ce fichier

### CSVs analysés (disponibles dans `/mnt/user-data/uploads/`)
1. `ListofunsuccessfulAIAgentSupporttickets...csv` — 891 tickets infructueux
2. `KnowledgewithMostHandOvers...csv` — top guidances par handover rate
3. `ThelistofKnowledgeresources...csv` — ressources utilisées par intent
4. `ofSupportticketsusedaKnowledge...csv` — tickets utilisant knowledge par intent
5. `AIAgentSupportSuccessratebytop10ticketintent...csv` — success rate top 10

---

## CE QUI RESTE À FAIRE (séquence recommandée)

### Étape 1 — One Pilot KB Extraction (PROCHAIN)
Utiliser Claude Code ou extension Chrome pour extraire les articles prioritaires de One Pilot (304, 306, 307, 308, 302, 303, 203, 105, 401).

**Script Chrome Extension :**
Pour chaque article listé ci-dessus dans la KB One Pilot Nébuleuse Bijoux :
1. Ouvrir l'article
2. Copier l'arborescence complète (tous Cas, Sous-cas, Possibilités)
3. Copier chaque template de réponse exact
4. **Noter le "Sending status" (Send & Close vs Send & Keep Open)** — critique
5. Noter les conditions d'éligibilité et délais mentionnés

### Étape 2 — Rapport HTML Final
**Langue :** Français intégral  
**Format :** HTML auto-contenu, partageable par lien  
**Angle :** Opportunités d'automatisation (pas post-mortem)  
**Sections prévues :**
1. Résumé exécutif — état actuel vs potentiel
2. Analyse des intents — où se perdent les tickets
3. Features inexploitées (OM, Actions, Flows, Chat)
4. One Pilot comme preuve que c'est automatisable
5. Plan d'action priorisé (Quick Wins vs Structurel)
6. Projection : chemin vers 50%

**Données de performance à intégrer dans le rapport :**
- Automation rate réel : 8.61% → objectif 50%
- 891 tickets infructueux analysés
- 91% handover rate sur les échecs
- $2,197 économisés en 60 jours (base à extrapoler)
- 1j 04h de temps agent économisé

---

---

## DONNÉES COMPLÈTES — TOUS LES INTENTS (891 tickets infructueux)

### Classement complet par volume
| ticket_intent | ticket_intent_detail | Tickets |
|---|---|---|
| Exchange:Status | Exchange Status Updates | 55 |
| Shipping:Delivered Not Received | Packages Marked Delivered Not Received | 54 |
| Order:Status | General Order Status Inquiries | 43 |
| Order:Damaged | Requests for replacement/refund of damaged jewelry | 35 |
| Return:Status | Delayed Return Processing | 35 |
| Product:Quality Issues | Jewelry Defects and Breakages | 29 |
| Exchange:Request | Exchange Due to Defective or Mismatched Items | 26 |
| Order:Missing Item | Missing Earrings and Piercings | 26 |
| Order:Missing Item | General Missing Items | 23 |
| Product:Quality Issues | Earring Closure Malfunctions | 17 |
| Shipping:Delay | Delayed Orders Awaiting Delivery | 17 |
| Return:Status | Unreceived Refund After Returning Item | 17 |
| Order:Edit | Change or add items in order | 17 |
| Warranty:Claim | Warranty claims for defective jewelry products | 16 |
| Order:Damaged | Earring Replacement Requests | 15 |
| Order:Payment | Payment adjustments and refunds issues | 14 |
| Shipping:Change Address | Address corrections before shipment | 13 |
| Order:Status | Order Not Received After Shipping | 12 |
| Return:Request | Return Process Issues | 12 |
| Account:Other | Fidelity Points and Account Status Issues | 12 |
| Order:Wrong Item | Other | 11 |
| Product:Quality Issues | Jewelry Discoloration Issues | 11 |
| Promotion & Discount:Issue | Loyalty Points Redemption Issues | 11 |
| Warranty:Claim | Warranty Claims with Defective Clasps | 10 |
| Return:Status | Delayed Refund After Return | 9 |

**Intents secondaires notables (5-8 tickets) :**
Product:Availability (replacement parts + restock), Return:Request (standard + defective), Order:Refund (delivery delays), Shipping:Delivered Not Received (returned to sender), Warranty:Claim (defect documentation, oxidation), Promotion & Discount:Issue (loyalty conflicts, discount errors)

**Intents à très faible volume mais à surveiller :**
- Piercing:Healing Complications (2) — sensible
- Product:Quality Issues > Piercing Infection Concerns (1) — très sensible
- Order:Cancel (3) — bloqué par ignore rule
- Wholesale:Information (1)

---

## DONNÉES COMPLÈTES — TOUTES LES GUIDANCES

### Guidances à FORT taux de succès (closed_or_wait_rate > 70%) ✅
| Guidance | Type | Exécutions | Succès |
|---|---|---|---|
| How do I follow my order? | snippet | 6 | 100% |
| Where can I find info on tracking? | snippet | 9 | 100% |
| How can I track my package? | snippet | 10 | 90% |
| When shopper asks about jewelry care | guidance | 13 | 92% |
| How long does shipping take? | snippet | 8 | 88% |
| When shopper asks about shipping costs | guidance | 44 | **86%** |
| How can I get a discount? | snippet | 7 | 86% |
| Jewelry blackens/oxidizes | guidance | 44 | **82%** |
| Back in stock | guidance | 39 | 74% |
| Lost jewelry/clasp | guidance | 92 | **72%** |

### Guidances CRITIQUES à fort volume mais taux élevé de handover ⚠️
| Guidance | Type | Exécutions | Handover |
|---|---|---|---|
| Order issues / shipping issues | guidance | **571** | 47% |
| Malfunctioning product / warranty | guidance | **302** | 50% |
| WISMO (NEW) | guidance | 120 | 44% |
| Loyalty Points usage | guidance | 47 | **79%** |
| Exchanges | guidance | 88 | 57% |
| Returns | guidance | 35 | 63% |
| Promotions/discounts (New) | guidance | 66 | 44% |
| Confirm order/payment | guidance | 54 | 39% |

### Guidances à très fort handover (>80%) — opportunités de réécriture 🚨
| Guidance | Exécutions | Handover | Problème |
|---|---|---|---|
| Loyalty Program Part 1 | 22 | **82%** | Toutes branches → handover |
| Loyalty Program Part 2 | 12 | **83%** | Toutes branches → handover |
| What is return/refund policy? | 8 | **88%** | Snippet trop vague |
| Create/edit/merge accounts | 7 | **86%** | Pas de résolution autonome |
| Loyalty Points returns | 11 | **82%** | Pas de réponse directe |
| Affiliation Ambassador Part 2 | 11 | **82%** | Commission queries → handover |

### Snippets à 100% de succès (déjà parfaits) ✅
How should I care for my jewelry, Can delivery times be extended, Where can I initiate a return, What materials are used (multiple versions), Piercing FAQs (bar lengths, size guidelines, aftercare)

---

## PATTERN QUALITATIVE — COMMENT L'IA TRANSFÈRE

**Phrase type de fin de message avant handover** (extrait de 891 tickets) :
- *"Je vais transmettre votre demande à l'équipe appropriée qui pourra vous aider"*
- *"Un agent va reprendre votre demande pour un suivi spécialisé"*
- *"Vous serez bientôt recontactée pour un suivi adapté à votre situation"*
- *"Ils reviendront vers vous rapidement pour vous aider"*
- *"Notre équipe dédiée va examiner en détail et vous accompagner"*

**Insight clé :** L'IA rédige systématiquement une réponse empathique complète ET PUIS transfère. Elle n'abandonne pas — elle conclut trop tôt. La guidance manquante n'est pas "comment répondre" mais "quand et comment clore".

---

## EXPORT EN ATTENTE — À INTÉGRER DANS LA PROCHAINE CONVERSATION

**Export Gorgias demandé mais pas encore reçu :**
- Liste complète de TOUS les tickets traités par l'AI Agent (pas seulement les infructueux)
- Incluant le corps du message client et la réponse IA
- Permettra d'identifier les patterns de succès + les opportunités détaillées sur les tickets résolus
- **À uploader dans la prochaine conversation dès réception**

---

## SCREENSHOT DATA — RÉSUMÉ COMPLET

| Screenshot | Contenu | Insight |
|---|---|---|
| Ignore Rule | Bloque order/cancel, refund/request, refund/status + sentiments négatifs + tags Negative/Annulation commande + emails Centrelog/Baback/Galeries Lafayette | Bien configurée |
| Actions page | "Get order info" (OFF) + "Update shipping address" (OFF) | 2 actions créées mais inactives |
| Order Management | Track Order ✅ MAIS "No response configured" ⚠️, Return Order ✅, Cancel Order ❌, Report Issue ✅ | Track Order cassé = fix rapide |
| Performance by feature | Flows: no data, Article Reco: no data, Order issues reportés: "I didn't get my refund" 66%, "I'd like to return" 33% | Aucune feature de déflexion active |
| Performance 60j | Overall 9.3% (+77%), AI Agent 8.61% (+94%), $2,197 saved, 1d 04h time saved | Vraie baseline = 8.61% |
| Performance 30j | Overall 8.23% (-22%), AI Agent 7.65% (-22%) | Baisse = fin BFCM, pas dégradation |
| One Pilot KB 306 | Retour/Échanges — Cas 3 Suivi visible, templates Send & Close confirmés | Preuve d'automatisabilité |
| One Pilot KB liste 1 | Topics 102-304+ visible | Sujets prioritaires identifiés |
| One Pilot KB liste 2 | Topics 302-409 visible (307 défectueux, 308 mauvais articles, 401 cartes cadeaux, 403 avis, 404 cas inconnu) | Liste complète topics |

---

## TRANSCRIPT COMPLET
Disponible dans le système à :
`/mnt/transcripts/2026-02-10-16-08-01-nebuleuse-bijoux-ai-agent-audit-setup.txt`
(+ continuation de cette session dans les transcripts récents)
