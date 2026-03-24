# Nébuleuse Bijoux — AI Agent Performance Audit
## Consulting Analysis & Optimization Roadmap
**Period analysé :** 7 janvier – 8 février 2026  
**Préparé par :** Analyse AI Agent Gorgias  
**Objectif :** Atteindre 50% de taux d'automatisation

---

## EXECUTIVE SUMMARY

L'assistant cosmique Nébuleux est **opérationnel et techniquement bien configuré**, mais il souffre d'un problème structurel critique : il engage les clients, génère des réponses empathiques et appropriées, puis **se transfère vers un agent humain au lieu de résoudre**. Sur 891 tickets non réussis analysés, **91% aboutissent à un handover** — non pas parce que l'IA ne comprend pas les demandes, mais parce qu'elle manque des **chemins de résolution** nécessaires pour conclure.

La bonne nouvelle : ce problème est **entièrement résolvable par de la configuration et du contenu**, sans refonte technique. Le potentiel d'amélioration est considérable.

**Métriques actuelles vs objectif :**

| Métrique | Actuel | Objectif |
|----------|--------|----------|
| Coverage Rate | 41.1% | 65%+ |
| Success Rate | 23.9% | 45%+ |
| Taux de handover (tickets non réussis) | 91% | <50% |
| Taux d'automatisation global | ~24% | **50%** |
| CSAT AI Agent | 3.7 | 4.0+ |

---

## PARTIE 1 : DIAGNOSTIC — CE QUI SE PASSE VRAIMENT

### 1.1 Le Paradoxe de l'Engagement Sans Résolution

L'analyse des 891 tickets infructueux révèle un pattern systématique et révélateur. L'IA :

1. **Identifie correctement** la demande du client
2. **Rédige une réponse empathique et appropriée** en français
3. **Accède aux données Shopify** (numéros de commande, statuts, dates de livraison)
4. **Transfère au lieu de résoudre** — par manque de guidances de résolution

**Exemple concret — Return/Status :**
> *Client :* "Mon colis est chez vous depuis le 31 décembre, j'ai demandé un avoir..."  
> *IA :* "Bonjour Julie, je vous confirme que votre colis #834696 a bien été reçu avec le statut Succès... Je transmets votre demande à l'équipe appropriée..."  
> *Résultat : Handover* ❌

L'IA **sait que le retour est reçu**, mais n'a pas de guidance lui disant quoi faire ensuite. Elle transfère par défaut.

**Exemple concret — Warranty/Claim :**
> *Client :* "Ma boucle d'oreille ne clip plus, pouvez-vous m'indiquer la marche à suivre pour la garantie ?"  
> *IA :* "Votre article est bien couvert par la garantie... Je vais transmettre votre demande à l'équipe spécialisée..."  
> *Résultat : Handover* ❌

Pourtant, la guidance garantie **existe déjà et contient le formulaire Typeform**. Le problème : l'IA manque de **confiance pour finaliser** sans validation humaine.

---

### 1.2 Analyse des Handover Topics — Cause Racine Identifiée

Sur 891 tickets infructueux, **222 (25%) ont un handover topic explicite** configuré :

| Handover Topic | Tickets | % |
|----------------|---------|---|
| Enquiries about reimbursements | 98 | 44% |
| Enquiries about refunds | 91 | 41% |
| Les deux combinés | 14 | 6% |
| Customers requiring a discount code | 11 | 5% |
| Combinaison de 3 topics | 8 | 4% |

**Diagnostic critique :** Les topics de handover "remboursements" et "remboursements/refunds" sont **beaucoup trop larges**. Ils capturent des situations qui pourraient être résolues par l'IA — notamment les demandes de statut de retour et de confirmation de réception. Ces topics forcent des handovers pour des questions informatives qui ne nécessitent pas d'action humaine.

---

### 1.3 Carte des Intents — Priorités par Impact

#### TOP 10 INTENTS PAR VOLUME (période analysée)

| Intent | Tickets | Taux de succès | Potentiel | Handover topic |
|--------|---------|---------------|-----------|----------------|
| **Order/Status** | 164 | 54.9% | ⭐⭐⭐ | 1.2% |
| **Product/Quality Issues** | 131 | 38.2% | ⭐⭐ | 18.3% |
| **Warranty/Claim** | 95 | 29.5% | ⭐⭐⭐ | 12.6% |
| **Shipping/Delivered Not Received** | 84 | 15.5% | ⭐⭐ | 3.6% |
| **Return/Status** | 81 | **3.7%** | 🚨 CRITIQUE | **84%** |
| **Order/Missing Item** | 66 | 10.6% | ⭐⭐ | 4.5% |
| **Exchange/Status** | 59 | **0.0%** | 🚨 CRITIQUE | 40.7% |
| **Order/Damaged** | 58 | **6.9%** | ⭐⭐ | 29.3% |
| **Promotion & Discount/Issue** | 54 | 22.2% | ⭐⭐ | 14.8% |
| **Exchange/Request** | 54 | 25.9% | ⭐⭐ | 24.1% |

---

### 1.4 Trois Zones de Défaillance Distinctes

#### 🚨 ZONE ROUGE — Défaillance Totale (Success < 10%)

**Return/Status (81 tickets, 3.7% de succès)**
- 84% des tickets ont un handover topic actif
- Seulement 16% des tickets utilisent la knowledge base
- Sous-intents critiques : Delayed Return Processing (34 tickets, 0%), Unreceived Refund (15 tickets, 0%)
- L'IA sait lire les statuts Shopify mais n'a **aucune guidance sur les délais de traitement des retours**

**Exchange/Status (59 tickets, 0% de succès)**
- 40.7% handover topic rate
- Exchange Status Updates (56 tickets) = **0% de succès absolu**
- L'IA ne peut pas interroger le statut d'un échange car Nébuleuse gère les échanges manuellement
- **Absence totale de guidance sur les délais et processus d'échange**

#### ⚠️ ZONE ORANGE — Sous-Performance Significative (Success 10-30%)

**Shipping/Delivered Not Received (84 tickets, 15.5%)**
- Packages Marked Delivered Not Received (142 tickets, 27% sur la période complète)
- L'IA demande une déclaration sur l'honneur mais ne conclut pas
- Guidance existante mais les conditions de résolution sont trop contraignantes

**Order/Damaged (58 tickets, 6.9%)**
- 29.3% handover topic rate
- Requests for replacement/refund of damaged jewelry (78 tickets, 14%)
- La guidance demande une photo, puis transfère systématiquement

**Order/Missing Item (66 tickets, 10.6%)**
- Missing Earrings and Piercings (71 tickets, 21%)
- General Missing Items (62 tickets, 23%)

#### ✅ ZONE VERTE — Performant (Success > 40%)

**Order/Status (164 tickets, 54.9%)** — Bon mais améliorable  
**Jewelry Discoloration Issues (20 tickets, 40%/60%)** — Fonctionne bien  
**Shipping/Delay (49% de succès)** — Guidance bien conçue

---

### 1.5 État des Features — Ce Qui Manque

| Feature | État | Impact sur l'automatisation |
|---------|------|----------------------------|
| **Order Management — Track Order** | ❌ Non configuré | 🔴 Critique |
| **Order Management — Return Order** | ❌ Non configuré | 🔴 Critique |
| **Flows** | ❌ Aucune donnée | 🟠 Important |
| **Article Recommendations** | ❌ Aucune donnée | 🟡 Modéré |
| **Actions** | ⚠️ Quasi-inexistantes (1.8% sur Order/Status) | 🔴 Critique |
| **Chat** | ⚠️ Email uniquement dans les données | 🟠 Important |

**Constat majeur : 0% d'utilisation d'Actions sur 8 des 10 intents les plus volumétriques.** L'IA ne peut pas agir — elle ne peut que communiquer. Cela limite structurellement le taux de succès pour tout ce qui nécessite une vérification ou une action.

---

## PARTIE 2 : RECOMMANDATIONS — PLAN D'ACTION PRIORISÉ

### PRIORITÉ 1 — QUICK WINS (Impact immédiat, 1-2 semaines)

---

#### 🔧 QW1 — Activer Order Management (Track Order)

**Impact estimé : +8 à +12 points de taux d'automatisation**

C'est l'action avec le meilleur ratio effort/impact. La guidance WISMO existe (26 tickets, 81% handover) mais l'Order Management n'est pas activé sur le chat.

**Actions :**
1. Activer Order Management > Track Order sur le chat et le Help Center
2. Configurer les messages de statut en français
3. Activer le retour automatisé via le portail existant (nebuleusebijoux.com/a/return)
4. Lier la guidance WISMO à l'action Track Order

**Pourquoi ça marche :** Sur les 366 General Order Status Inquiries, 61.5% sont déjà résolus avec knowledge. Avec Track Order activé, les clients peuvent s'auto-servir et réduire le volume entrant.

---

#### 🔧 QW2 — Créer une Guidance Return/Status dédiée

**Impact estimé : +4 à +6 points de taux d'automatisation**

Return/Status est la défaillance la plus critique : 81 tickets, 3.7% de succès, 0% sur Delayed Return Processing. La guidance actuelle sur les retours couvre le *processus de retour* mais pas le *suivi d'un retour en cours*.

**Guidance à créer — "Quand un client demande où en est son retour" :**

```
WHEN : Le client demande le statut de son retour en cours

Étape 1 — Identifier la commande et le retour
- Rechercher la commande via [CUSTOMER_EMAIL] ou le numéro de commande
- Vérifier le statut de retour dans Shopify

Scénario 1 — Le retour n'a pas encore été reçu
THEN : Informer le client que le retour n'apparaît pas encore dans notre 
système et lui demander de confirmer qu'il a bien expédié le colis.
Partager le lien de suivi s'il est disponible.

Scénario 2 — Le retour a été reçu (statut "Succès")
THEN : 
- Confirmer la réception du colis
- Informer que le traitement prend entre 5 et 10 jours ouvrés
- Si la demande est un avoir : "Votre avoir sera disponible dans votre 
  compte dans les 5-10 jours ouvrés"
- Si la demande est un remboursement : "Le remboursement sera effectué 
  sous 5-10 jours ouvrés sur votre moyen de paiement"
- Clore le ticket

Scénario 3 — Le retour est en cours de traitement depuis > 10 jours
THEN : Transmettre à l'équipe avec note interne "Retour en attente > 10j"

Règle générale : Ne pas utiliser le topic de handover "remboursements" 
pour les simples demandes de statut.
```

---

#### 🔧 QW3 — Créer une Guidance Exchange/Status dédiée

**Impact estimé : +3 à +5 points de taux d'automatisation**

Exchange/Status est à **0% de succès absolu** sur 59 tickets. Exchange Status Updates (56 tickets) représente 100% du problème. L'IA n'a aucune guidance sur ce que sont les délais d'un échange.

**Guidance à créer — "Quand un client demande où en est son échange" :**

```
WHEN : Le client demande le statut de son échange en cours

Étape 1 — Identifier la commande d'échange
- Rechercher via [CUSTOMER_EMAIL] ou numéro de commande d'origine
- Vérifier s'il existe une commande d'échange associée

Scénario 1 — Une commande d'échange existe et est expédiée
THEN :
- Confirmer que l'échange a bien été expédié
- Partager le numéro de suivi [order.fulfillment.tracking_url]
- Indiquer la date d'expédition [order.fulfillment.created_datetime]
- Clore le ticket

Scénario 2 — L'échange est en cours de traitement (commande non expédiée)
THEN :
- Confirmer que la demande d'échange a bien été reçue
- Informer que les échanges sont traités sous 3-5 jours ouvrés
- Inviter à reprendre contact si non résolu après 7 jours
- Clore le ticket

Scénario 3 — Aucune commande d'échange trouvée
THEN : Transmettre à l'équipe avec note interne "Échange non trouvé"
```

---

#### 🔧 QW4 — Affiner les Handover Topics — Réduire le scope "remboursements"

**Impact estimé : +5 à +8 points de taux d'automatisation**

Le handover topic "Enquiries about reimbursements" capture actuellement **98 tickets** qui sont en grande partie des **simples demandes de statut**, pas des demandes d'action. Ce topic est trop large.

**Actions :**
1. Renommer "Enquiries about reimbursements" → "Requests to issue a new reimbursement"
2. Ajouter une clarification : "Ce topic s'applique uniquement quand le client demande un remboursement pas encore initié — pas pour les suivis de retour en cours"
3. Faire de même pour "Enquiries about refunds" → "Requests to process a new refund"
4. Cela libèrera immédiatement les Return/Status et Exchange/Status qui sont des suivis, pas des demandes d'action

---

#### 🔧 QW5 — Enrichir la Guidance Warranty avec une Conclusion Claire

**Impact estimé : +3 à +4 points**

La guidance garantie est bien structurée mais **toutes les branches terminent par "Hand over the ticket"** même quand l'IA a déjà partagé le formulaire Typeform. Il faut ajouter une option de clôture.

**Modification à apporter dans les Scénarios 3, 4 et 5 de la guidance garantie :**

```
APRÈS avoir partagé le formulaire de garantie https://icvk1xljokz.typeform.com/to/ssHc7vn6 :
- Si le client confirme avoir soumis le formulaire → Clore le ticket avec 
  message de confirmation
- Si le client a d'autres questions → Transmettre à l'équipe
- Ne pas transmettre systématiquement après envoi du formulaire
```

---

### PRIORITÉ 2 — AMÉLIORATIONS STRUCTURELLES (2-4 semaines)

---

#### 🏗️ S1 — Activer Order Management — Return Order

**Impact estimé : +3 à +5 points**

Le portail de retour existe (nebuleusebijoux.com/a/return) mais n'est pas connecté à Order Management dans Gorgias. L'activation permettrait aux clients de s'auto-servir depuis le chat sans contacter le support.

**Configuration recommandée :**
- Activer Return Order dans Order Management
- Lier au portail existant
- Configurer les messages de confirmation en français

---

#### 🏗️ S2 — Créer une Action "Confirm Return Receipt"

**Impact estimé : +2 à +4 points**

Pour les demandes de Return/Status où le retour est reçu (Scénario 2 de QW2), l'IA devrait pouvoir confirmer automatiquement sans handover. Une action simple qui lit le statut de retour Shopify et répond.

---

#### 🏗️ S3 — Enrichir la Guidance Order/Damaged avec des Délais Clairs

**Impact estimé : +2 à +3 points**

Order/Damaged (58 tickets, 6.9% succès) souffre du même problème que Return/Status : l'IA demande une photo, reçoit la photo, puis transfère. La guidance doit inclure les étapes post-photo :

```
IF : Photo reçue et bijou clairement endommagé
THEN : 
- Confirmer que le bijou est couvert par la garantie/SAV
- Partager le formulaire de réclamation
- Informer des délais de traitement (5-7 jours ouvrés)
- Clore le ticket après envoi du formulaire
```

---

#### 🏗️ S4 — Créer des Flows pour les FAQ à Volume Stable

**Impact estimé : +2 à +4 points**

Aucun Flow n'est actuellement configuré. Opportunités identifiées :

- **"Où est ma commande ?"** — Flow 3 étapes : vérification commande → statut → lien tracking
- **"Comment faire un retour ?"** — Flow 2 étapes : éligibilité → lien portail
- **"Conditions de livraison"** — Flow informatif 2 étapes

Les Flows permettent d'intercepter des demandes simples avant qu'elles ne touchent l'IA Agent, réduisant le volume à traiter.

---

#### 🏗️ S5 — Guidance Order/Missing Item — Ajouter une Résolution Directe

**Impact estimé : +2 à +3 points**

Missing Earrings (71 tickets, 21%) et General Missing Items (62 tickets, 23%) ont un taux de succès faible car l'IA confirme le problème mais transfère pour l'action.

**Guidance à améliorer :**
```
IF : Article manquant confirmé par le client (avec ou sans photo)
THEN :
- Vérifier le contenu de la commande Shopify
- Confirmer l'article manquant
- Informer que le réapprovisionnement sera expédié sous 3-5 jours ouvrés
- Ajouter note interne : "Article manquant : [NOM_ARTICLE] à expédier"
- Transmettre à l'équipe pour action (réexpédition)
- Clore avec message de confirmation au client
```

---

### PRIORITÉ 3 — OPTIMISATIONS AVANCÉES (1-2 mois)

---

#### 🚀 A1 — Activer le Chat et étendre l'AI Agent

Toutes les données analysées proviennent uniquement de l'email. L'activation de l'AI Agent sur le chat permettrait de :
- Capturer les demandes pré-achat (shipping, produits, disponibilité)
- Gérer les WISMO en temps réel
- Réduire le volume email entrant

**Intents chat à prioriser :** Shipping costs, Product availability, Gift card questions (taux de succès déjà élevés en email)

---

#### 🚀 A2 — Créer des Actions Avancées

Actions prioritaires à configurer :
1. **Cancel Order** — pour les demandes avant expédition
2. **Edit Shipping Address** — pour les corrections d'adresse (13 tickets, 41% succès actuel mais sans action directe)
3. **Check Return Status** — lecture automatique du statut Shopify

---

#### 🚀 A3 — Optimiser la Guidance Loyalty Points

Loyalty Points (10 tickets, 80% handover) et Loyalty Program Part 2 (12 tickets, 83% handover) sont quasi-entièrement transférés. La guidance est très complète mais toutes les branches techniques se terminent en handover.

**Solution :** Pour les questions simples (solde de points, comment utiliser), permettre à l'IA de conclure sans handover.

---

## PARTIE 3 : PROJECTION — CHEMIN VERS 50%

### Calcul de l'Impact Cumulé

| Action | Tickets impactés | Gain estimé (success rate) | Impact sur automatisation |
|--------|-----------------|---------------------------|--------------------------|
| QW1 — Order Management Track Order | ~100 | +30 pts sur WISMO | **+4 pts** |
| QW2 — Guidance Return/Status | 81 | +25 pts | **+3 pts** |
| QW3 — Guidance Exchange/Status | 59 | +30 pts | **+3 pts** |
| QW4 — Affiner Handover Topics | ~200 | libère les handovers | **+5 pts** |
| QW5 — Warranty conclusion | 95 | +15 pts | **+2 pts** |
| S1 — OM Return Order | ~50 | +25 pts | **+2 pts** |
| S3 — Order/Damaged guidance | 58 | +20 pts | **+2 pts** |
| S4 — Flows FAQ | ~80 | nouveaux tickets interceptés | **+3 pts** |
| **TOTAL ESTIMÉ** | | | **+24 pts** |

**Taux d'automatisation projeté : 24% actuel → 48-52%** ✅

---

### Tableau de Bord — Métriques à Suivre

| Métrique | Valeur actuelle | Objectif 30 jours | Objectif 60 jours |
|----------|----------------|-------------------|-------------------|
| Automation Rate | ~24% | 35% | 50% |
| Coverage Rate | 41.1% | 55% | 65% |
| Success Rate | 23.9% | 35% | 45% |
| Handover Rate (unsuccessful) | 91% | 75% | 60% |
| Return/Status success | 3.7% | 25% | 35% |
| Exchange/Status success | 0% | 20% | 30% |
| CSAT AI Agent | 3.7 | 4.0 | 4.2 |

---

## PARTIE 4 : SYNTHÈSE EXÉCUTIVE — POINTS CLÉS

### Ce qui fonctionne bien ✅

- **Nom et personnalité de l'IA** bien alignés avec la marque ("L'assistant cosmique Nébuleux")
- **Temps de réponse exceptionnels** : FRT 32s, RT 43s
- **Guidances qualitatives** : les textes existants sont bien rédigés, empathiques, en français
- **Order/Status** : 54.9% de succès — déjà solide, preuve que l'IA peut résoudre
- **Shipping costs/delivery times** : 86% de clôture, guidance très efficace
- **Blackening/oxidation guidance** : 82% de clôture — excellent
- **28 guidances actives** — base de connaissance substantielle

### Ce qui doit changer immédiatement 🚨

1. **Les handover topics "remboursements" sont trop larges** — ils bloquent des résolutions possibles
2. **Return/Status et Exchange/Status n'ont aucune guidance de suivi** — 0% de succès
3. **Order Management n'est pas activé** — manque à gagner immédiat
4. **0% d'Actions** sur 8 intents majeurs — l'IA ne peut qu'informer, pas agir
5. **Flows : zéro** — opportunité de déflexion non exploitée

### Insight stratégique

> L'AI Agent de Nébuleuse Bijoux n'a pas un problème de compréhension ni de qualité de réponse — il a un problème de **confiance pour conclure**. Chaque guidance qui se termine par "Hand over the ticket" est une opportunité perdue. La priorité numéro un est de **réécrire les conclusions de chaque guidance** pour permettre à l'IA de clore les tickets quand elle a fourni l'information ou l'action demandée.

---

*Document préparé pour usage interne et présentation client.*  
*Données basées sur l'export du 8 février 2026 — 891 tickets infructueux analysés + données de performance Periscope.*
