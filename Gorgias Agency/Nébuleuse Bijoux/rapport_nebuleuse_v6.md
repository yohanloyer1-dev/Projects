# Optimisation AI Agent — Nébuleuse Bijoux

L'objectif de ce rapport est d'analyser l'état actuel d'automatisation et d'utilisation d'AI Agent dans le but d'avoir un plan d'action clair pour augmenter le taux d'automatisation jusqu'à atteindre 50%.

---

# Méthodologie

Ce rapport est le résultat d'une analyse approfondie menée sur plusieurs axes :

**Revue des statistiques AI Agent** — Analyse des métriques globales (taux d'automatisation, couverture, succès, CSAT), de la performance par intent, et de l'évolution mensuelle sur les 60 derniers jours.

**Analyse des handovers par guidance** — Pour chaque guidance active, calcul du taux de handover pour identifier les instructions qui transfèrent au lieu de résoudre.

**Analyse approfondie des tickets** — Export et traitement de 41 419 messages sur 12 024 tickets. Classification des réponses humaines post-handover pour comprendre pourquoi AI Agent transfère, et quantification des raisons (remboursement, logistique, retour, échange, etc.).

**Revue des fonctionnalités d'automatisation Gorgias** — Audit des fonctionnalités activées et non activées : Order Management, Actions, Flows, déploiement par canal, handover topics, et configuration des réponses.

**Analyse de conversion par canal** — Étude des données de conversion sur 6 mois pour identifier l'impact business potentiel d'AI Agent sur le chat pré-achat.

---

# En Bref

## Situation actuelle

AI Agent a répondu en moyenne à 1 300+ tickets par mois depuis sa mise en place, avec un taux moyen d'automatisation dans les 8%. Les demandes résolues avec le plus de succès sont l'entretien des bijoux (92%), les frais de livraison (86%), l'oxydation (82%), le réassort (74%) et le suivi de commande (55%).

**Chiffres clés :**

| | Aujourd'hui | Objectif |
|---|---|---|
| Taux d'automatisation AI Agent | 8,1% | **50%** |
| Taux d'automatisation sur email | 18,1% | **50%** |
| Taux de couverture | 38,9% | 65% |
| Taux de succès | 25,3% | 45% |
| CSAT AI Agent | 3,5/5 | 4,0/5 |
| Coût outsourcing mensuel moyen | ~12 000 €/mois | **~6 000 €/mois** |

## L'impact déjà mesurable d'AI Agent

Même avec seulement 8,1% d'automatisation, AI Agent a déjà transformé la réactivité du support, ce qui est le critère principal pour une bonne satisfaction client :

| Métrique | Avant AI Agent | Avec AI Agent | Amélioration |
|---|---|---|---|
| Temps de 1ère réponse | 14h 07min | 23min 20s | **97% plus rapide** |
| Temps de réponse moyen | 4h 58min | 7min 46s | **97% plus rapide** |
| Temps de résolution | 20h 01min | 1h 37min | **92% plus rapide** |
| Réponse humaine après handover | 18h 33min | 2h 10min | **88% plus rapide** |

## Les constats principaux

L'analyse approfondie de **41 419 messages** sur **12 024 tickets** (60 jours) révèle une opportunité claire : AI Agent en l'état actuel sait bien répondre (c'était la première étape importante à tester), mais il n'est pas prêt pour résoudre totalement autant de tickets que voulu.

Les raisons sont multiples et identifiées :

- **AI Agent n'a pas la possibilité de performer certaines actions** — 92,6% des tickets repris par One Pilot nécessitent une action concrète (remboursement, enquête logistique, envoi d'étiquette retour) qu'AI Agent ne peut pas encore effectuer
- **Certains sujets sont transférés directement à One Pilot** — Les handover topics et les guidances actuelles sont configurés pour transférer plutôt que résoudre, même sur des demandes de suivi simples
- **36,7% des tickets email sont ignorés** — AI Agent ne tente même pas de répondre à un tiers des demandes, dont beaucoup sont des intents classiques (suivi de retour, suivi de commande, garantie)
- **AI Agent n'est pas disponible sur le Chat** — Un canal à fort potentiel de conversion qui repose entièrement sur One Pilot
- **Les Flows sont inutilisés** — Zéro parcours guidé en place pour intercepter les demandes simples avant la création d'un ticket

---

# Analyse approfondie des tickets

## Emails

Sur les 5 263 tickets emails ces 60 derniers jours :

| Étape | Tickets | % du total email |
|---|---|---|
| Total tickets email | 5 263 | 100% |
| Ignorés par AI Agent (jamais répondus) | 1 933 | **36,7%** |
| Répondus par AI Agent | 3 330 | 63,3% |
| → Résolus par AI Agent | 955 | **18,1%** |
| → Transférés (handover) | 1 768 | 33,6% |

Observation clé : Plus d'un tiers des tickets (36,7%) est ignoré par AI Agent. Il y a forcément une partie de ces demandes qui peuvent être traitées — suivi de retour (300 tickets), suivi de commande (265), demande de garantie (218), colis non reçu (213). Ce n'est pas un volume marginal, c'est un levier majeur pour automatiser + : si AI Agent tentait de répondre à ces tickets, même avec un taux de succès modeste de 25%, cela représenterait 47% d'augmentation des tickets résolus par AI Agent.

## Pourquoi les tickets sont transférés : les handovers

Sur les 1 744 tickets où AI Agent a répondu puis transféré, l'analyse du contenu de la réponse de One Pilot révèle que **92,6% des reprises impliquaient une action concrète** que AI Agent ne peut pas encore faire :

| Raison du transfert | Tickets | % des handovers |
|---|---|---|
| Traitement de remboursement | 764 | **43,8%** |
| Contact logistique / enquête transporteur | 495 | **28,4%** |
| Envoi étiquette / instructions retour | 145 | 8,3% |
| Traitement d'échange | 114 | 6,5% |
| Prise en charge garantie / SAV | 53 | 3,0% |
| Réexpédition commande | 27 | 1,5% |
| Geste commercial / code promo | 17 | 1,0% |
| Demande de preuves (photo/vidéo) | 12 | 0,7% |
| Demande d'informations complémentaires | 7 | 0,4% |
| Autres | 110 | 6,3% |

La raison principale des handovers: AI Agent transfère systématiquement dès qu'une action est nécessaire. Si l'on permet à AI Agent de traiter les remboursements ou ouvrir une réclamation dans Shipup, on adresse directement + de 2/3 des raisons de handover.

## Exemples concrets : AI Agent vs One Pilot sur les mêmes types de demandes

Les exemples suivants sont extraits directement des tickets et illustrent le pattern récurrent : AI Agent donne une bonne réponse, puis transfère au lieu de conclure.

### Exemple 1 — Suivi de commande (Order::Status)

**201 handovers sur cette catégorie**

> **Cliente :** *« J'ai commandé le 1er décembre et je n'ai toujours aucune nouvelle de ma commande, ça fait 15 jours. Pouvez-vous m'aider ? »*
>
> **AI Agent répond :** *« Bonjour Candice, merci beaucoup pour votre message et je comprends bien votre inquiétude concernant l'absence de nouvelles de votre commande du 1er décembre. Je suis désolée pour ce délai et le manque d'information. Votre commande #850213 est actuellement non expédiée. Je vais transmettre votre dossier... »*
>
> **One Pilot prend le relais :** *« Je vous confirme avoir pris contact avec notre équipe logistique afin de comprendre le statut de votre commande. Pas d'inquiétude, nous trouvons toujours une solution 💪 »*

**Analyse :** AI Agent a correctement identifié la commande, vérifié le statut Shopify, et fourni une réponse empathique. Mais au lieu de donner directement les délais de préparation et de rassurer la cliente, il transfère. One Pilot fait ensuite exactement ce qu'AI Agent aurait pu faire : contacter la logistique et confirmer les délais. Avec une guidance complète et la possibilité d'ouvrir une réclamation transporteur, AI Agent pourrait résoudre ce type de ticket de bout en bout.

### Exemple 2 — Suivi d'échange (Exchange::Status)

**131 handovers sur cette catégorie**

> **Client :** *« J'ai déposé le colis retour N° XT246773554TS le mardi 9 décembre en point relais mais je n'ai pas d'informations de suivi. Pouvez-vous me dire quand je vais recevoir l'échange ? »*
>
> **AI Agent répond :** *« Merci pour votre message et pour les détails fournis. Je comprends que vous souhaitez avoir des informations sur le retour et l'échange de la boucle d'oreille. Je vais transmettre votre demande à notre équipe spécialisée... »*
>
> **One Pilot prend le relais :** *« D'après le lien de suivi de votre colis, ce dernier est toujours en transit. Il ne devrait plus tarder à nous être livré. Dès réception, nous nous engageons à effectuer l'échange dans un délai maximum de 30 jours. »*

**Analyse :** AI Agent reconnaît le sujet mais admet immédiatement son incapacité — *« Je vais transmettre »*. Or la réponse de One Pilot est factuelle et basée sur des informations accessibles : statut de transit du colis et délai standard de traitement (30 jours). C'est typiquement le genre de réponse qu'AI Agent pourrait donner pour résoudre le ticket sans intervention de One Pilot.

### Exemple 3 — Suivi de retour (Return::Status)

**152 handovers sur cette catégorie**

> **Cliente :** *« Je viens vers vous afin de savoir où en est mon retour et remboursement d'une paire de boucles d'oreilles (retour depuis le 28 novembre) »*
>
> **AI Agent répond :** *« Merci de nous avoir contactés au sujet de votre retour et remboursement. Je comprends que vous souhaitez suivre l'état de ce processus. Je vais transmettre votre demande à l'équipe compétente qui pourra vous apporter une réponse précise... »*
>
> **One Pilot prend le relais :** *« Nous avons bien reçu votre colis et notre équipe logistique va bientôt le vérifier. Nous nous engageons à vous apporter une réponse dans un délai maximum de 30 jours dès réception de ce dernier. »*

**Analyse :** Même schéma : AI Agent capitule immédiatement alors que One Pilot donne une réponse standard (confirmation de réception + délai de 30 jours). Avec une guidance couvrant les différents statuts de retour et les délais standards, AI Agent pourrait traiter ce type de demande directement.

### Exemple 4 — Ce qui marche : AI Agent résout un échange avec succès ✅

> **Cliente :** *« Ma commande a bien été reçue et tous les articles sont conformes hormis une boucle Livie dont le fermoir est défectueux. Quelle est la démarche à suivre pour faire échanger cet article ? Il s'agit d'un cadeau. »*
>
> **AI Agent résout :** *« Votre commande ayant été livrée il y a moins de 30 jours, vous êtes tout à fait éligible à un échange ✨ »* → envoie le lien du portail retour, explique la procédure, confirme les délais.

**Analyse :** Quand AI Agent dispose d'une guidance complète avec les conditions d'éligibilité, le lien du portail et les délais, il résout le ticket de bout en bout. C'est la preuve que le modèle fonctionne — il suffit de le reproduire sur les autres intents.

## Tendance d'automatisation mensuelle

| Mois | Tickets | AI résolus | Taux |
|---|---|---|---|
| Décembre 2025 | 5 212 | 347 | 6,7% |
| Janvier 2026 | 4 626 | 447 | **9,7%** |

L'amélioration entre décembre et janvier (+3 points) montre que les ajustements de guidances ont un effet mesurable.

---

# Ce que les données montrent

## Répartition des demandes clients (données 60 jours)

Voici le top 15 des types de demandes principales avec les métriques de performance actuelles :

| Type de demande | Volume (60j) | AI résolus | Taux actuel | Handovers | Potentiel |
|---|---|---|---|---|---|
| Garantie / réclamation | 1 455 | 60 | 4,1% | 112 | ⬆️ 20% |
| Suivi de commande | 780 | 259 | 33,2% | 201 | ⬆️ 55% |
| Problèmes qualité produit | 574 | 118 | 20,6% | 134 | ⬆️ 40% |
| Suivi de retour | 535 | 14 | 2,6% | 152 | ⬆️ 25% |
| Disponibilité produit | 418 | 70 | 16,7% | 28 | ⬆️ 35% |
| Colis livré non reçu | 355 | 40 | 11,3% | 120 | ⬆️ 30% |
| Suivi d'échange | 327 | 19 | 5,8% | 131 | ⬆️ 25% |
| Article manquant | 265 | 25 | 9,4% | 112 | ⬆️ 25% |
| Remboursement | 257 | 4 | 1,6% | 40 | ⬆️ 15% |
| Promotions / codes promo | 197 | 23 | 11,7% | 65 | ⬆️ 30% |
| Demande d'échange | 192 | 47 | 24,5% | 92 | ⬆️ 40% |
| Bijou endommagé | 176 | 13 | 7,4% | 90 | ⬆️ 25% |
| Demande de retour | 170 | 18 | 10,6% | 54 | ⬆️ 30% |
| Retard de livraison | 158 | 51 | 32,3% | 55 | ⬆️ 50% |
| Détails produit | 145 | 18 | 12,4% | 15 | ⬆️ 30% |

**Ce qui fonctionne déjà bien :** L'entretien des bijoux (92%), les frais de livraison (86%), l'oxydation (82%), le réassort (74%), le bijou perdu/fermoir (72%) et le suivi de commande (33%). Ces résultats prouvent qu'AI Agent est capable de résoudre efficacement quand il dispose d'instructions complètes.

**Là où se trouve le potentiel :** La garantie (1 455 tickets, 4,1%), le suivi de retour (535 tickets, 2,6%) et le suivi d'échange (327 tickets, 5,8%) représentent **2 317 tickets sur 60 jours** avec un taux de résolution quasi nul — non pas parce que les demandes sont complexes, mais parce qu'AI Agent n'a pas encore d'instructions ni d'actions pour traiter ces cas de bout en bout.

## Comment AI Agent traite les demandes aujourd'hui

L'analyse qualitative des tickets non résolus montre un schéma récurrent :

**Étape 1** — AI Agent identifie correctement la demande du client
**Étape 2** — Il répond de façon empathique et pertinente
**Étape 3** — Il accède aux données Shopify (commande, statut, dates)
**Étape 4** — Il transfère à un agent humain au lieu de conclure

Ce schéma se retrouve dans les guidances les plus utilisées. Le taux de handover des guidances confirme l'ampleur de l'opportunité :

| Guidance | Tickets | Handovers | Taux de handover |
|---|---|---|---|
| WISMO (suivi de commande) | 23 | 21 | 91% |
| Loyalty (3 guidances cumulées) | 18 | 15 | 83% |
| Problèmes commande / livraison | 108 | 69 | 64% |
| Garantie / produit défectueux | 191 | 116 | 61% |
| Échanges | 53 | 32 | 60% |
| Promotions / offres | 47 | 24 | 51% |
| Bijou perdu / fermoir | 86 | 40 | 47% |

*Note : Le taux de handover des guidances (ex: WISMO à 91%) mesure spécifiquement les tickets passés par cette guidance, tandis que le taux de résolution par intent (ex: Suivi de commande à 33%) mesure l'ensemble des tickets de ce type, y compris ceux résolus via d'autres chemins comme Track Order ou des réponses directes.*

## Les instructions qui performent déjà

Plusieurs instructions en place démontrent le potentiel d'AI Agent quand il dispose de chemins de résolution complets :

| Instruction | Volume | Taux de résolution |
|---|---|---|
| Entretien des bijoux | 13 | 92% |
| Frais de livraison | 44 | 86% |
| Oxydation / noircissement | 44 | 82% |
| Réassort / disponibilité | 39 | 74% |
| Bijou perdu / fermoir | 92 | 72% |
| Suivi de commande (tracking) | 164 | 55% |

L'objectif est de reproduire ce niveau de performance sur les sujets encore sous-exploités, et de mettre à profit les fonctionnalités sous/non-utilisées.

## État des fonctionnalités Gorgias non utilisées

| Fonctionnalité | État actuel | Opportunité |
|---|---|---|
| **Order Management — Track Order** | ✅ Activé | ⚠️ Manque la réponse pour les commandes non encore expédiées (« No response configured ») |
| **Order Management — Return Order** | ✅ Activé | À optimiser — le portail retour existe déjà (nebuleusebijoux.com/a/return) |
| **Order Management — Cancel Order** | ❌ Désactivé | À évaluer selon la politique d'annulation |
| **Actions existantes** | ✅ « Get order info » et « Update shipping address » actives | Besoin de nouvelles actions complémentaires (notamment Baback + Loyoly) |
| **Flows** | ❌ Non déployés | Zéro données — potentiel important pour les FAQ et parcours guidés |
| **AI Agent sur Chat** | ❌ Non déployé | Canal de conversion pré-achat avec la plus forte attente de réactivité |

---

# Les 4 grandes opportunités

1. **Réduire les tickets ignorés** — 1 933 tickets email (36,7%) que AI Agent n'essaie même pas de traiter, dont beaucoup sont des intents classiques
2. **Corriger les handovers systématiques** — 1 744 tickets où AI Agent a répondu correctement mais transféré inutilement
3. **Permettre à AI Agent de performer des actions** — 92,6% des reprises par One Pilot impliquent une action (remboursement, logistique, retour) qu'AI Agent ne peut pas encore faire
4. **Activer AI Agent sur le Chat** — + de 5% des demandes avec un fort potentiel d'automatisation et de génération de revenus

---

# L'opportunité 💸💸 : AI Agent sur le Chat

## Le chat convertit + que n'importe quel autre canal

Le chat est le canal où les clients ont les attentes les plus fortes en termes de réactivité. C'est aussi le canal qui convertit le mieux en pré-achat : les clients qui posent une question sur le chat sont dans une démarche d'achat active. Aujourd'hui, chaque conversation chat repose entièrement sur la disponibilité des agents One Pilot — AI Agent n'y est pas encore déployé.

## Le weekend convertit mieux — mais manque de couverture

L'analyse des données de conversion sur **6 mois** (août 2025 – février 2026) confirme un contraste net et durable :

| | Taux de conversion | Part des tickets | Part des conversions |
|---|---|---|---|
| **Weekend (ven-sam-dim)** | **17,1%** | 38% | **46%** |
| Semaine (lun-jeu) | 12,3% | 62% | 54% |

Le vendredi est le jour avec le meilleur taux de conversion (**17,5%**), suivi du dimanche (**17,0%**) et du samedi (**16,5%**). Le trio vendredi-samedi-dimanche représente 38% des tickets mais génère **46% des conversions**.

## 16 jours de weekend avec zéro conversion

Sur 6 mois, **16 samedis et dimanches** n'ont produit **aucune vente** malgré 108 conversations chat créées sur ces jours-là. Le pattern est clair : ce sont principalement des jours où le temps de réponse était trop long ou inexistant, ce qui explique l'abandon des clients. Sur les weekends avec au moins une conversion, le taux moyen dépasse 20% — ce qui signifie qu'environ **22 ventes ont potentiellement été perdues** sur ces seuls 16 jours par manque de réactivité.

## Pourquoi?

Le weekend est le moment où les clients achètent le plus (meilleur taux de conversion), mais c'est aussi celui où le support est le moins réactif. AI Agent sur le chat répondrait instantanément aux questions pré-achat le samedi et dimanche — exactement quand les clients sont le + à même d'acheter.

Il faudrait considérer la mise en place de Shopping Assistant à terme pour capitaliser sur les ventes et conversions sur le chat.

---

# Plan d'action

Ce plan d'action est basé sur l'analyse des 28 guidances actuellement en place, des données de tickets, et des fonctionnalités Gorgias activées et non activées.

## Phase 1 — Quick Wins (Semaines 1-2)

Ces actions sont rapides à mettre en place et auront un impact mesurable dès leur déploiement.

### Réduire les tickets ignorés (ai_ignore)

**Aujourd'hui :** 1 933 tickets email (36,7%) sont ignorés par AI Agent. Parmi eux, on retrouve des intents courants : Return/Status (300), Order/Status (265), Warranty (218), Shipping/Delivered Not Received (213).

**Opportunité :** Revoir les règles d'exclusion (Prevent AI from answering) qui bloquent AI Agent sur ces sujets. Beaucoup de ces tickets sont de simples demandes de suivi ou d'information que AI Agent peut traiter avec les bonnes guidances.

**Impact estimé :** +338 tickets résolus sur la période → +3% à +5% d'automatisation

---

### Affiner les handover topics

**Aujourd'hui :** Les handover topics « Enquiries about reimbursements » et « Enquiries about refunds » capturent ~189 tickets dont une majorité sont de simples demandes de suivi — pas des demandes d'action nécessitant un agent humain.

**Opportunité :** Restreindre ces règles aux demandes de nouveau remboursement uniquement. Les simples suivis de statut (« Où en est mon remboursement ? ») pourront alors être traités par AI Agent.

**Impact estimé :** +5% à +7% d'automatisation

---

### Optimiser la guidance WISMO pour réduire les handovers

**Aujourd'hui :** La guidance WISMO est la plus détaillée du compte avec 4 scénarios et ~12 sous-scénarios. Mais elle a un taux de handover de 91% parce que **presque tous les chemins finissent par un handover** — y compris des cas où AI Agent pourrait conclure.

**Analyse de la guidance actuelle :**

| Scénario | Conclusion actuelle | Peut être résolu ? |
|---|---|---|
| Colis en transit ≤5 jours | ✅ Résolu (tracking + statut) | Déjà OK |
| Colis en transit ≥6 jours (Colissimo, Standard, Express) | ❌ Handover | ⚠️ Pourrait informer + conclure |
| Colis en transit ≥6 jours (Lettre Suivie, Mondial Relay) | ❌ Handover | ⚠️ À évaluer |
| Commande Unfulfilled | ❌ Handover (vérification tag "Doublon nom") | ✅ 80%+ résolvable |
| Colis retourné à l'expéditeur | ❌ Handover | ❌ Justifié |
| Livré mais non reçu | ❌ Handover | ❌ Justifié |
| Tracking inactif | ❌ Handover | ❌ Justifié |
| Livré, confirmation | Handover après question | ⚠️ Pourrait conclure |

**Opportunité :**
- **Scénario 3 (Unfulfilled)** — Les commandes non expédiées sans le tag "Doublon nom" peuvent recevoir une réponse standard : *« Votre commande est en cours de préparation et sera expédiée sous 2 à 4 jours ouvrés. »* Au lieu de transférer systématiquement
- **Sous-scénario 2.6 (livré, confirmation)** — Si le client ne signale pas de non-réception, AI Agent peut confirmer la livraison et clôturer
- **Compléter Track Order** — Ajouter la réponse pour les commandes « Unfulfilled » dans Order Management

**Impact estimé :** +4% à +6% d'automatisation

---

### Optimiser la guidance garantie pour clôturer après le formulaire

**Aujourd'hui :** La guidance garantie est la plus sollicitée en volume : 1 455 tickets, seulement 60 résolus (4,1%). La guidance est bien structurée avec 6 scénarios (fermoir, achat boutique, achat online <30j, 31-364j, garantie expirée, fermoir perdu) + une section B (warranty details/claims). Le problème : **les scénarios 3 et 4 font handover après envoi du formulaire Typeform** au lieu de conclure.

**Analyse de la guidance actuelle :**

| Scénario | Conclusion actuelle | Peut être résolu ? |
|---|---|---|
| Fermoir (Scénario 1) | Envoie vidéo Instagram → formulaire → End flow | ✅ Résolu |
| Achat boutique (Scénario 2) | Redirige vers boutique → **Handover** | ⚠️ Pourrait conclure |
| Achat online <30j (Scénario 3) | Formulaire Typeform → **Handover** | ✅ Pourrait conclure |
| Achat online 31-364j (Scénario 4) | Formulaire Typeform → **Handover** | ✅ Pourrait conclure |
| Garantie expirée (Scénario 5) | Informe expiration → End flow | ✅ Résolu |
| Fermoir perdu (Scénario 6) | Lien achat fermoir → End flow | ✅ Résolu |
| Demande d'info garantie (Section B) | Page politique + formulaire → End flow | ✅ Résolu |

**Opportunité :**
- **Scénarios 3 et 4** — Après envoi du formulaire Typeform, remplacer le handover par un message de clôture : *« Nous avons bien reçu votre demande. Notre équipe va examiner votre réclamation et reviendra vers vous sous X jours. »*
- **Scénario 2 (achat boutique)** — Après avoir redirigé vers la boutique, conclure le ticket au lieu de transférer

**Impact estimé :** +2% à +3% d'automatisation

---

### Créer une guidance pour le suivi de retour

**Aujourd'hui :** 535 tickets/60j à 2,6% de résolution. La guidance « If a shopper asks about returns » couvre bien le process de demande de retour (conditions, éligibilité, portail retour, emballage) avec 6 scénarios. Mais il **n'existe aucune guidance pour le suivi d'un retour en cours** — un client qui demande « où en est mon retour ? » ou « quand serai-je remboursé ? » n'a pas de chemin de résolution.

Le scénario 6 de la guidance retours (suivi de remboursement) fait handover systématique : *« Hand over the ticket (refunds must be handled manually). »*

**Opportunité :** Créer une guidance dédiée « Suivi de retour / Return Status » couvrant :
- **Colis retour en transit** → Communiquer le statut de tracking et le délai standard de 30 jours
- **Colis retour reçu, en traitement** → Confirmer la réception et le délai de traitement
- **Retour traité, remboursement émis** → Confirmer et communiquer le délai bancaire (2-5 jours ouvrés)
- **Retour en attente >10 jours** → Transférer à un agent

**Impact estimé :** +3% à +4% d'automatisation

---

### Créer une guidance pour le suivi d'échange

**Aujourd'hui :** 327 tickets/60j à 5,8% de résolution. La guidance « Exchanges » couvre bien le process de demande d'échange (conditions 30 jours, même pièce gold/silver, même prix, lien portail). Mais comme pour les retours, il **n'existe aucune guidance pour le suivi d'un échange en cours**. Un client qui demande « quand vais-je recevoir mon échange ? » tombe dans le vide.

**Opportunité :** Créer une guidance dédiée « Suivi d'échange / Exchange Status » couvrant :
- **Colis retour en transit** → Communiquer le statut et le délai de 30 jours dès réception
- **Colis reçu, échange en traitement** → Confirmer la réception et le délai
- **Échange expédié** → Partager le tracking du nouvel envoi
- **Délai dépassé** → Transférer à un agent

**Impact estimé :** +3% à +4% d'automatisation

---

### Déployer AI Agent sur le Chat

Comme démontré dans la section précédente, le chat est le canal de conversion pré-achat avec la plus forte attente de réactivité, et les weekends présentent le meilleur taux de conversion. Déployer AI Agent sur le chat permettrait de :

- Répondre instantanément aux questions pré-achat 24h/24, 7j/7
- Capturer les ventes perdues les weekends sans couverture humaine
- Gérer les demandes de suivi simples directement en chat
- Libérer les agents outsourcing pour les cas complexes et la conversion

Les guidances actuelles (shipping costs, gift card, back in stock, loyalty, entretien, etc.) sont déjà prêtes pour le chat — elles couvrent les questions pré-achat les plus fréquentes.

**Impact estimé :** +3% à +5% d'automatisation

---

## Phase 2 — Intégrations & Actions (Semaines 3-4)

### Créer de nouvelles Actions

Les Actions « Get order info » et « Update shipping address » sont déjà en place. L'analyse des handovers montre que **92,6% des reprises** par l'outsourcing impliquent une action concrète. Les nouvelles actions prioritaires :

| Action | Handovers adressés | Impact |
|---|---|---|
| **Traiter un remboursement** | 764 tickets (43,8% des handovers) | Le plus gros levier |
| **Ouvrir une réclamation transporteur** | 495 tickets (28,4%) | Second levier |
| **Envoyer étiquette retour** | 145 tickets (8,3%) | Automatisation des retours |
| **Initier un échange** | 114 tickets (6,5%) | Traitement des échanges |

Intégrations spécifiques :
- **Actions Baback** — pour vérifier les statuts de retour/échange et déclencher les remboursements
- **Actions Loyoly** — pour répondre aux questions fidélité (solde de points, transfert entre comptes, statut du rang). La guidance Loyalty actuelle transfère pour le transfert de points (scénario 4), les points manquants >5j (scénario 5b), et la perte de statut (scénario 6)
- **Actions Shopify custom** — Cancel Order pour les commandes non expédiées, Check Return/Exchange Status

Chaque nouvelle action permet à AI Agent de vérifier et agir directement au lieu de transférer.

**Impact estimé :** +315 tickets résolus → +3% à +5% d'automatisation

---

### Optimiser la guidance problèmes commande / livraison

**Aujourd'hui :** La guidance « Order issues or shipping issues » couvre 7 scénarios détaillés, mais **presque tous finissent par un handover** :

| Scénario | Conclusion actuelle |
|---|---|
| Produit endommagé — photo montre dommage clair | **Handover** (reship ou remboursement) |
| Produit endommagé — bijou wearable | ✅ Résolu (demande confirmation satisfaction) |
| Fermoir/boucle ne ferme pas | ✅ Résolu via guidance garantie (vidéo Instagram) |
| Code Mondial Relay manquant | ✅ Résolu (redirige vers site Mondial Relay) |
| Mauvais produit / article manquant | **Handover** après confirmation |
| Mauvaise adresse / mauvais point relais | **Handover** (si client ne peut récupérer) |
| Livré non reçu | **Handover** (sworn statement) |
| Modification commande | **Handover** immédiat |

**Opportunité :** Les cas de produit endommagé avec photo claire pourraient être résolus en redirigeant vers le formulaire garantie Typeform + message de clôture, au lieu de transférer pour un reship manuel.

**Impact estimé :** +2% d'automatisation

---

### Mettre en place les Flows pour les questions fréquentes sur le chat

Créer des parcours guidés pour les demandes les plus courantes sur le chat. Les Flows interceptent les demandes simples en offrant des réponses structurées avant la création d'un ticket.

**Suggestions de Flows prioritaires :**

| Flow | Volume de référence | Contenu |
|---|---|---|
| Garantie / réclamation | 1 455 tickets | Expliquer la politique garantie → rediriger vers le formulaire Typeform → confirmer les délais |
| Suivi de commande | 780 tickets | Demander le n° de commande → afficher le statut → proposer de contacter un agent si besoin |
| Retour / échange | 862 tickets (535+327) | Expliquer la politique → rediriger vers le portail retour → confirmer les délais |
| Problèmes livraison | 355 tickets | Identifier le type de problème → fournir les informations de suivi → proposer un report |

**Impact estimé :** +2% à +3% d'automatisation

---

### Ajouter des scénarios Report Order Issue

Actuellement, 3 scénarios par défaut sont disponibles. Pour mieux correspondre aux cas spécifiques de la bijouterie, ajouter :

| Scénario | Description |
|---|---|
| Bijou oxydé / noirci à la réception | Produit reçu déjà oxydé (≠ usure normale) |
| Fermoir cassé / défaillant | Problème mécanique sur le fermoir |
| Taille non conforme | Bague ou bracelet ne correspond pas à la taille commandée |
| Gravure incorrecte | Erreur sur une gravure personnalisée |
| Colis incomplet | Un ou plusieurs articles manquants dans le colis |

---

## Phase 3 — Optimisations avancées (Mois 2)

### Actions Avancées (API)

Intégrations profondes via API Shopify, Baback et Loyoly pour un traitement de bout en bout : remboursements automatiques, statuts de retour en temps réel, gestion des points fidélité.

---

### Préparer l'extension vers de nouveaux canaux

AI Agent sera disponible sur **WhatsApp et Instagram** courant été 2026. Chez Nébuleuse, ces canaux représentent déjà un volume significatif :

| Canal | Tickets (60j) | Part du volume |
|---|---|---|
| Instagram Comment | 2 883 | 24,0% |
| Instagram DM | 1 358 | 11,3% |
| Chat | 841 | 7,0% |
| WhatsApp | 65 | 0,5% |

Le déploiement d'AI Agent sur ces canaux ouvrira un potentiel d'automatisation supplémentaire majeur.

---

# Projection économique

## Coût actuel outsourcing

Sur la base de 299 €/mois d'abonnement + 2,05 €/ticket, le coût mensuel moyen des 6 derniers mois est de **~12 000 €/mois**.

## Coût AI Agent

Nébuleuse est actuellement sur le plan à **$640/mois** (~589 €) pour 800 interactions automatisées. À 50% d'automatisation sur email (~1 414 interactions/mois), le plan passerait à **$1 125/mois** (~1 035 €) pour 1 500 interactions.

## Projection à 50% d'automatisation sur email

Le chemin vers 50% d'automatisation sur le canal email repose sur 4 leviers :

| Levier | Mécanisme | Tickets récupérés (60j) |
|---|---|---|
| Réduire les tickets ignorés | Élargir la couverture AI Agent aux 1 933 tickets email ignorés | +338 |
| Corriger les handovers systématiques | Permettre à AI Agent de conclure au lieu de transférer | +884 |
| Ajouter des Actions | Remboursements, logistique, retours, échanges | +315 |
| Améliorer les Guidances | Garantie, retour, échange, qualité produit | +337 |
| **Total** | | **+1 874** |

**Projection :** de 955 tickets résolus (18,1%) à **2 829 tickets résolus (53,8%)** sur le canal email.

## Impact financier net

| | Actuel | Projeté |
|---|---|---|
| Tickets résolus par AI /mois | 488 | **1 414** |
| Économie outsourcing /mois | 1 000 € | 2 900 € |
| Coût AI Agent /mois | 589 € | 1 035 € |
| **Économie nette /mois** | **411 €** | **1 865 €** |
| **Économie nette /an** | **~4 900 €** | **~22 400 €** |

*Note : ces projections sont basées sur le volume email uniquement. L'activation d'AI Agent sur le Chat et les futurs canaux (Instagram, WhatsApp) augmentera significativement l'impact.*

---

# Roadmap

## Chemin vers 50% d'automatisation

| Action | Tickets impactés/mois | Impact estimé |
|---|---|---|
| Réduire les tickets ignorés | ~960 | +3% à +5% |
| Affiner les handover topics | ~189 | +5% à +7% |
| Optimiser la guidance WISMO | ~390 | +4% à +6% |
| Optimiser la guidance garantie | ~727 | +2% à +3% |
| Créer guidance suivi de retour | ~267 | +3% à +4% |
| Créer guidance suivi d'échange | ~163 | +3% à +4% |
| Nouvelles Actions (Baback, Loyoly, Shopify) | ~525 | +3% à +5% |
| Optimiser guidance problèmes livraison | ~175 | +2% |
| AI Agent sur le Chat | ~420 | +3% à +5% |
| Flows FAQ sur le chat | ~200 | +2% à +3% |
| Report Order Issue (scénarios bijouterie) | ~88 | +1% à +2% |
| Actions avancées API | ~200 | +2% à +3% |
| **Total** | | **+33% à +52%** |

---

# Prochaines étapes

1. Revoir les règles d'exclusion (ai_ignore) pour libérer les 1 933 tickets email ignorés
2. Affiner les handover topics « reimbursements » et « refunds »
3. Optimiser la guidance WISMO — ajouter la résolution pour les commandes Unfulfilled et les colis livrés
4. Optimiser la guidance garantie — clôturer après envoi du formulaire Typeform (scénarios 3 et 4)
5. Créer une guidance « Suivi de retour » (colis en transit, reçu, remboursement émis)
6. Créer une guidance « Suivi d'échange » (colis en transit, reçu, échange expédié)
7. Déployer AI Agent sur le Chat
8. Créer de nouvelles Actions (Baback pour retours/échanges, Loyoly pour fidélité, Shopify pour remboursements)
9. Optimiser la guidance problèmes commande/livraison — résoudre les cas de produit endommagé via formulaire garantie
10. Mettre en place les Flows pour les questions fréquentes sur le chat
11. Ajouter les scénarios Report Order Issue spécifiques bijouterie
12. Créer des actions avancées via API (Shopify, Baback, Loyoly)
13. Préparer le déploiement AI Agent sur WhatsApp et Instagram (été 2026)

---

*Données basées sur l'analyse de 41 419 messages sur 12 024 tickets (14 déc 2025 – 10 fév 2026), les métriques AI Agent, les données de conversion sur 6 mois (août 2025 – février 2026), et les coûts outsourcing sur 14 mois.*
