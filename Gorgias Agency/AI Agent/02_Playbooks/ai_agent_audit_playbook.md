# 🔍 AI Agent Performance Audit Playbook

## Objectif

Ce playbook décrit la méthodologie complète pour auditer la performance d'un AI Agent Gorgias, identifier les leviers d'amélioration, et produire un rapport d'audit actionnable. Il est basé sur le process développé et éprouvé lors de l'audit Nébuleuse Bijoux (décembre 2025 – février 2026).

Ce playbook est **complémentaire** au AI Agent Implementation Playbook existant. L'Implementation Playbook couvre le setup initial et les calls de suivi. Ce Audit Playbook couvre l'analyse approfondie de performance pour les clients existants qui veulent passer au niveau supérieur.

---

## Quand utiliser ce playbook

- Le client a AI Agent en place depuis **au moins 30 jours**
- Le taux d'automatisation est **inférieur à l'objectif** (généralement < 30%)
- Le client veut comprendre **pourquoi** AI Agent ne résout pas plus de tickets
- Le client envisage de **réduire ses coûts** d'outsourcing/support
- Tu veux produire un **rapport d'audit commercial** pour justifier des améliorations

---

## Phase 1 — Collecte de données (Jour 1)

### 1.1 Données Gorgias à récupérer

#### Screenshots obligatoires

| Donnée | Où la trouver | Pourquoi |
|---|---|---|
| **Intents page** (toutes les pages) | AI Agent > Intents | Vue d'ensemble des intents, taux de succès, volume, CSAT par intent |
| **Overview Report** | Statistics > AI Agent > Overview | Automation rate, FRT, RT, CSAT globaux |
| **Performance par agent** | Statistics > Support Performance > Agents | Comparer AI Agent vs agents humains sur FRT, RT, résolution |
| **Guidances en place** | AI Agent > Knowledge > Guidance | Liste des guidances existantes avec métriques (tickets, handovers, CSAT) |
| **Handover topics** | AI Agent > Settings > Handover topics | Comprendre ce qui est bloqué par configuration |
| **Actions en place** | AI Agent > Support Actions | Voir les actions existantes et leur utilisation |
| **Deploy settings** | AI Agent > Deploy | Quels canaux sont actifs (email, chat, SMS) |
| **Order Management** | Settings > Order Management | Track, Return, Cancel — quelle config |

#### Export CSV obligatoire

**Ticket messages export** — C'est la donnée la plus précieuse. Exporter via Statistics > Export :

- **Période :** Au minimum 30 jours, idéalement 60 jours
- **Colonnes essentielles :** ticket_id, body_text, tags, AI_intent, agent_name, from_agent, sent_datetime, ticket_channel
- **Colonnes supprimables si fichier trop lourd :** message_id, receiver_id, integration_id, customer_id, user_id (pas customer_email — utile pour le contexte)

⚠️ **Limitation de taille :** Le fichier peut dépasser 10-30 MB pour les gros volumes. Si c'est le cas :
- Supprimer d'abord les colonnes non essentielles
- Si toujours trop lourd, filtrer par les top 5 intents à plus fort volume
- En dernier recours, diviser en 2-3 fichiers par période

### 1.2 Données business à demander au client

| Donnée | Pourquoi |
|---|---|
| **Coût mensuel outsourcing** (factures si possible) | Calculer le ROI et les économies projetées |
| **Coût par ticket** | Base du calcul économique |
| **Tech stack support** (retours, abonnements, fidélité) | Identifier les Actions à créer |
| **Politique retour/échange/garantie** | Écrire les guidances |
| **Identity / brand guidelines** | Si rapport HTML prévu |
| **Objectif d'automatisation** | Cadrer les recommandations |

### 1.3 Données optionnelles (pour rapport premium)

| Donnée | Pourquoi |
|---|---|
| **Données de conversion par canal** (revenue CSV) | Démontrer l'impact business du chat/pré-achat |
| **Base de connaissance outsourcing** (screenshots) | Identifier les process à convertir en guidances |
| **CSAT historique** | Mesurer l'évolution |

---

## Phase 2 — Analyse des métriques (Jour 2)

### 2.1 Analyse de l'Overview Report

Extraire les KPIs suivants :

| KPI | Ce qu'on cherche |
|---|---|
| **Automation rate** | Le chiffre de base — d'où on part |
| **Coverage rate** | % des tickets que AI Agent tente de traiter |
| **Success rate** | % des tickets tentés qui sont résolus |
| **CSAT AI Agent** | Satisfaction client avec AI Agent |
| **FRT / RT** | Temps de réponse — prouver l'impact immédiat d'AI Agent |

**Calcul clé :** `Automation rate = Coverage × Success rate`

Si l'automation rate est basse, identifier si c'est un problème de **couverture** (AI Agent ne tente pas assez de tickets) ou de **succès** (AI Agent tente mais ne résout pas).

### 2.2 Analyse des Intents

Pour chaque intent, noter :

| Intent | Volume | Success rate | CSAT | Improvement potential |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

**Prioriser par :** `Volume × (1 - Success rate)` = nombre de tickets récupérables

Les intents à plus fort "improvement potential" × volume sont les quick wins.

### 2.3 Analyse des Guidances

Pour chaque guidance active, calculer le **taux de handover** :

`Taux de handover = Handover tickets / Total tickets`

Un taux de handover > 50% signale une guidance qui ne va pas assez loin dans la résolution. C'est un levier direct.

---

## Phase 3 — Analyse approfondie des tickets (Jour 2-3)

C'est la phase la plus importante et la plus différenciante. Elle nécessite l'export CSV des messages.

### 3.1 Vue d'ensemble du dataset

Avec le CSV, calculer :

```
Total messages
Total tickets uniques
Avg messages par ticket
Plage de dates
```

### 3.2 Analyse par agent (qui fait quoi)

Identifier la répartition :

```
Tickets assignés à AI Agent : X (Y%)
Tickets assignés à l'outsourcing : X (Y%)
Tickets assignés à d'autres : X (Y%)
```

**Insight attendu :** Si AI Agent ne gère que 5-10% du volume en autonomie, c'est un signal fort que le problème est structurel (config, pas compétence).

### 3.3 Analyse du funnel par canal

Pour le canal email (canal principal d'AI Agent) :

```
Total tickets email : X
AI ignorés (ai_ignore tag) : X (Y%)
AI tentés : X (Y%)
  → AI résolus (ai_close) : X (Y% des tentés)
  → AI handover : X (Y% des tentés)
```

**Insight clé :** Si un pourcentage élevé de tickets sont ignorés (>20%), c'est un levier MAJEUR. Ce sont des tickets que AI Agent ne tente même pas — souvent à cause de règles d'exclusion trop larges ou de handover topics trop agressifs.

### 3.4 Analyse des tags

Les tags Gorgias les plus importants à analyser :

| Tag | Signification |
|---|---|
| `ai_close` | AI Agent a résolu le ticket |
| `ai_answered` | AI Agent a répondu (mais pas forcément résolu) |
| `ai_handover` | AI Agent a transféré à un humain |
| `ai_ignore` | AI Agent a été configuré pour ignorer ce ticket |
| `ai_snooze` | AI Agent a mis le ticket en attente |

**Calcul :** Pour les tickets `ai_handover` + `ai_answered` → AI Agent a répondu correctement mais transféré. C'est le gisement principal d'amélioration.

### 3.5 ⭐ Analyse des raisons de handover (le cœur de l'audit)

C'est l'analyse la plus précieuse. Pour les tickets tagués `ai_handover` + `ai_answered`, analyser le body_text de la réponse de l'agent humain qui a pris le relais pour comprendre **pourquoi** le transfert était nécessaire.

**Méthode :** Scanner le body_text des réponses humaines après handover pour détecter des patterns :

| Pattern dans la réponse humaine | Catégorie | Ce que ça signifie |
|---|---|---|
| "remboursement", "rembours", "avoir", "crédit" | **ACTION_REFUND** | L'humain a traité un remboursement |
| "logistique", "entrepôt", "transporteur", "enquête" | **ACTION_LOGISTICS** | L'humain a contacté la logistique |
| "retour", "étiquette", "bordereau", "label" | **ACTION_RETURN** | L'humain a envoyé une étiquette retour |
| "échange", "remplacement", "nouveau modèle" | **ACTION_EXCHANGE** | L'humain a traité un échange |
| "renvoy", "réexpédi", "nouvel envoi" | **ACTION_RESHIP** | L'humain a réexpédié la commande |
| "garantie", "SAV", "service après-vente" | **ACTION_WARRANTY** | L'humain a traité une garantie |
| "code promo", "réduction", "geste commercial" | **ACTION_DISCOUNT** | L'humain a fait un geste commercial |
| "photo", "vidéo", "preuve" | **INFO_REQUEST** | L'humain a demandé des preuves |

**Résultat attendu :** Un tableau comme celui-ci :

```
Actions requiring backend/tool access: XX% des handovers
  - Refund processing: XX%
  - Logistics contact: XX%
  - Return label: XX%
  - Exchange processing: XX%
  - Warranty handling: XX%
Information gathering: XX%
Other: XX%
```

**Ce que ça prouve :** Si 80%+ des handovers nécessitent une ACTION, alors le problème n'est pas les guidances — c'est qu'AI Agent n'a pas les outils (Actions Shopify) pour agir. C'est un argument commercial puissant pour justifier la mise en place d'Actions.

### 3.6 Extraction d'exemples concrets

Pour le rapport, extraire **1-2 exemples concrets par catégorie** montrant :

1. Ce que le client a demandé
2. Comment AI Agent a répondu (souvent bien)
3. Comment l'humain a pris le relais (souvent pour une action simple)
4. Ce qu'AI Agent aurait pu faire avec la bonne configuration

Et aussi **1-2 exemples de succès** où AI Agent a résolu le ticket de bout en bout — pour prouver que le modèle fonctionne.

---

## Phase 4 — Calcul économique (Jour 3)

### 4.1 Coût actuel

```
Coût outsourcing mensuel = Abonnement + (Tickets × Coût/ticket)
```

Si les factures sont disponibles, utiliser les montants réels des 6 derniers mois pour une moyenne fiable.

### 4.2 Projection par levier

Pour chaque levier d'amélioration, estimer :

| Levier | Tickets récupérables | Taux de conversion estimé | Tickets résolus |
|---|---|---|---|
| Réduire les tickets ignorés | X | 25% | X |
| Corriger les handovers structurels | X | 50% | X |
| Ajouter des Actions | X | 30% | X |
| Améliorer les Guidances | X | variable | X |

**Estimations conservatrices recommandées :**
- Tickets ignorés → si AI tente 70% et résout 25% = ~18% de récupération
- Handovers structurels → récupérer 50% est réaliste avec des guidances complètes
- Actions → 30% des tickets nécessitant une action seront automatisés
- Guidances → variable selon l'intent, entre 10% et 20% d'amélioration

### 4.3 ROI projeté

```
Économie mensuelle = Tickets résolus supplémentaires × Coût/ticket
Économie annuelle = Économie mensuelle × 12
ROI = Économie annuelle / Coût des améliorations (temps, outils, abonnement)
```

---

## Phase 5 — Rédaction du rapport (Jour 3-4)

### Structure recommandée du rapport

1. **En Bref** — Situation actuelle, chiffres clés, constat principal
2. **Analyse approfondie des tickets** — Funnel email, répartition agents, raisons de handover, exemples concrets
3. **Ce que les données montrent** — Intents par volume/taux, guidances existantes, fonctionnalités non utilisées
4. **Opportunités business** — Chat pré-achat, conversion weekend, etc.
5. **Plan d'action en 3 phases** — Actions immédiates → structurelles → avancées
6. **Projection économique** — Coût actuel, leviers, économie projetée
7. **Roadmap & jalons** — Tableau de progression avec objectifs chiffrés
8. **Prochaines étapes** — Liste ordonnée des actions

### Bonnes pratiques de rédaction

- **Éviter le ton consultant** — être direct, factuel, actionnable
- **Utiliser "résoudre" plutôt que "clore"** — le client veut des problèmes résolus, pas des tickets fermés
- **Utiliser "outsourcing" plutôt que le nom du prestataire** — le client peut changer de partenaire
- **Chiffrer chaque recommandation** — volume de tickets, impact estimé en %
- **Donner des exemples concrets** — les citations de tickets sont plus convaincantes que les chiffres seuls
- **Distinguer email et global** — le taux d'automatisation sur email est toujours plus élevé que le taux global (car AI Agent n'est souvent actif que sur email)

---

## Phase 6 — Présentation au client (Jour 5)

### Format recommandé

- **Rapport Markdown** pour le contenu détaillé (archivable, modifiable)
- **Dashboard HTML interactif** pour la présentation (WOW effect, brand-aligned)
- **Les deux se complètent** — le HTML pour l'impact visuel, le Markdown pour la référence

### Points clés à mettre en avant lors de la présentation

1. **Le funnel email** — montrer visuellement les 3 étapes (ignoré → tenté → résolu)
2. **Les exemples de tickets** — lire 2-3 exemples en live, c'est ce qui convainc le plus
3. **Le tableau des raisons de handover** — 92%+ sont des actions → besoin d'Actions Shopify
4. **La projection économique** — pas de chiffres astronomiques, rester crédible
5. **Le plan d'action** — montrer que c'est faisable en 4-6 semaines

---

## Checklist de livraison

### Documents à fournir au client

- [ ] Rapport d'audit (Markdown et/ou HTML)
- [ ] Exemples de tickets avec analyse (intégrés au rapport)
- [ ] Plan d'action priorisé avec impacts estimés
- [ ] Projection économique avec hypothèses transparentes
- [ ] Roadmap de progression avec jalons mesurables

### Données à archiver pour le suivi

- [ ] Export CSV des tickets (pour référence future)
- [ ] Screenshots des métriques actuelles (baseline)
- [ ] Liste des guidances existantes avec métriques
- [ ] Configuration actuelle (handover topics, actions, deploy settings)

---

## Annexe : Script d'analyse type

### Étape 1 — Stats de base

```python
# Compter tickets uniques, messages, agents
# Période, canaux, distribution
```

### Étape 2 — Funnel par canal

```python
# Pour chaque canal:
#   Total tickets
#   Tickets ai_ignore
#   Tickets ai_close
#   Tickets ai_handover
#   Tickets ai_answered
```

### Étape 3 — Analyse des handovers

```python
# Pour les tickets ai_handover + ai_answered:
#   Analyser le body_text de l'agent humain
#   Classifier par pattern (refund, logistics, return, etc.)
#   Compter par catégorie
```

### Étape 4 — Extraction d'exemples

```python
# Pour chaque top intent:
#   Trouver 1-2 tickets handover avec AI response + human response
#   Trouver 1-2 tickets ai_close (success) pour comparaison
```

### Étape 5 — Projections

```python
# Calculer les leviers:
#   Levier 0: reduce ai_ignore → X tickets × 25% = Y
#   Levier 1: fix handovers → X tickets × 50% = Y
#   Levier 2: add Actions → X tickets × 30% = Y
#   Levier 3: improve Guidances → variable
```

---

## Métriques de référence (benchmarks)

Sur la base des audits réalisés, voici des ordres de grandeur typiques :

| Métrique | Début (pré-audit) | Post-optimisation | Bon niveau |
|---|---|---|---|
| Automation rate global | 5-10% | 20-30% | 40-50% |
| Automation rate email | 15-20% | 35-45% | 50%+ |
| Coverage rate | 30-40% | 55-65% | 70%+ |
| Success rate | 20-30% | 35-45% | 50%+ |
| CSAT AI Agent | 3,0-3,5 | 3,5-4,0 | 4,0+ |
| % tickets ignorés | 30-40% | 10-15% | <10% |
| Handover rate (sur guidances) | 50-70% | 30-40% | <30% |

---

*Playbook créé en février 2026 — basé sur l'audit Nébuleuse Bijoux*
*À mettre à jour après chaque nouvel audit pour enrichir les benchmarks et la méthodologie*
