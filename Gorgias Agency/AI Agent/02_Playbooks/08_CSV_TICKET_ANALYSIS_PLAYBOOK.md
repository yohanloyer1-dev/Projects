# 📊 CSV Ticket Analysis Playbook

## Objectif

Ce playbook détaille la méthodologie pour analyser un export CSV de tickets Gorgias et en extraire des insights actionnables. C'est la phase la plus différenciante d'un audit AI Agent — elle transforme des données brutes en arguments business concrets.

**Complémentaire à :** `ai_agent_audit_playbook.md` (Phase 3)

---

## Pré-requis

### Export CSV requis

**Source :** Statistics > Export > Ticket Messages

**Période recommandée :** 60 jours minimum (30 jours = trop peu de volume, 90 jours = fichier trop lourd)

**Colonnes essentielles :**

| Colonne | Usage |
|---|---|
| `ticket_id` | Identifier les tickets uniques |
| `body_text` | Analyser le contenu des échanges |
| `tags` | Classifier les tickets (ai_close, ai_handover, ai_ignore, ai_answered) |
| `AI_intent` | Comprendre la classification automatique |
| `agent_name` | Distinguer AI Agent vs humains vs outsourcing |
| `from_agent` | TRUE = message agent, FALSE = message client |
| `sent_datetime` | Chronologie des échanges |
| `ticket_channel` | Filtrer par canal (email, chat, etc.) |

**Colonnes supprimables si fichier trop lourd :** message_id, receiver_id, integration_id, customer_id, user_id

### Gestion des fichiers volumineux

Le fichier peut facilement dépasser 30 MB pour les comptes à fort volume. Stratégies de réduction :

1. **Supprimer les colonnes non essentielles** — souvent suffisant pour passer de 34 MB à 20 MB
2. **Filtrer par les top 5-10 intents** — concentrer l'analyse sur les plus gros volumes
3. **Diviser en 2-3 fichiers par période** — si tout le reste échoue

⚠️ **Piège courant :** Le CSV Gorgias utilise le séparateur `;` (point-virgule), pas `,`. Et il contient souvent 2 lignes d'en-tête avant les données (une ligne de métadonnées + la ligne de colonnes).

---

## Étape 1 — Vue d'ensemble du dataset

### Métriques de base

```
Total messages : X
Total tickets uniques : X
Messages par ticket (moyenne) : X
Plage de dates : du JJ/MM/AAAA au JJ/MM/AAAA
```

### Distribution par canal

```
Email : X tickets (Y%)
Chat : X tickets (Y%)
Instagram DM : X tickets (Y%)
Instagram Comment : X tickets (Y%)
WhatsApp : X tickets (Y%)
Autre : X tickets (Y%)
```

**Pourquoi c'est important :** AI Agent n'est souvent actif que sur email. Connaître la distribution par canal permet de calculer le potentiel réel d'automatisation sur chaque canal.

---

## Étape 2 — Identifier les agents

### Trouver le nom exact de l'AI Agent

⚠️ **Piège courant :** Le nom de l'AI Agent dans le CSV contient souvent des caractères spéciaux (emojis, apostrophes typographiques comme `'` vs `'`). Toujours commencer par lister tous les agents uniques.

```python
agents_set = set()
for row in reader:
    agent = row.get('agent_name', '').strip()
    if agent:
        agents_set.add(agent)

for a in sorted(agents_set):
    print(f"  '{a}' (len={len(a)})")
```

**Résultat attendu :** On identifie le nom exact de l'AI Agent (ex: `L'assistant cosmique Nébuleuse 🤖`), le nom de l'outsourcing (ex: `Camille`), et les éventuels autres agents.

### Répartition par agent

```
AI Agent : X tickets (Y%)
Outsourcing : X tickets (Y%)
Autres agents : X tickets (Y%)
```

**Insight clé :** Si l'AI Agent ne gère que 5-10% du volume en autonomie, le problème est structurel (configuration) pas technique (compétence de l'IA).

---

## Étape 3 — Analyse des tags (le funnel)

### Tags Gorgias à analyser

| Tag | Signification | Ce que ça révèle |
|---|---|---|
| `ai_close` | AI Agent a résolu le ticket | ✅ Succès |
| `ai_answered` | AI Agent a répondu | Nécessaire mais pas suffisant |
| `ai_handover` | AI Agent a transféré à un humain | ❌ Échec (potentiellement récupérable) |
| `ai_ignore` | AI Agent a été configuré pour ignorer | ⚠️ Volume inexploité |
| `ai_snooze` | AI Agent a mis le ticket en attente | Ticket en cours |

### Construire le funnel email

Pour le canal email uniquement :

```
Total tickets email : X
├── AI ignorés (ai_ignore) : X (Y%)        ← Levier 0 : réduire
├── AI tentés : X (Y%)
│   ├── AI résolus (ai_close) : X (Y%)     ← Succès actuel
│   ├── AI handover : X (Y%)               ← Levier 1 : récupérer
│   └── AI answered only : X (Y%)          ← À investiguer
```

### Combinaison critique : `ai_handover` + `ai_answered`

Les tickets avec DEUX tags — `ai_handover` ET `ai_answered` — sont le gisement principal d'amélioration. Ça signifie que l'AI Agent a su répondre correctement mais a quand même transféré. Le problème n'est pas la compréhension — c'est la confiance ou la configuration.

**Calcul :** Sur Nébuleuse, 98,2% des tickets handover avaient aussi le tag `ai_answered`. L'AI savait répondre mais transférait quand même.

---

## Étape 4 — Analyse des raisons de handover (le cœur de l'audit)

C'est l'analyse la plus précieuse et la plus différenciante. Elle nécessite de lire le contenu réel des réponses humaines post-handover.

### Méthode

Pour chaque ticket `ai_handover` + `ai_answered` :
1. Extraire les messages de l'agent humain (`from_agent = TRUE` et `agent_name != AI Agent`)
2. Analyser le `body_text` pour détecter des patterns d'action
3. Classifier dans une catégorie

### Patterns de détection (pour le marché français)

| Pattern dans la réponse humaine | Catégorie | Mots-clés à détecter |
|---|---|---|
| L'humain a traité un remboursement | `ACTION_REFUND` | remboursement, rembours, avoir, crédit, bon d'achat |
| L'humain a contacté la logistique | `ACTION_LOGISTICS` | logistique, entrepôt, transporteur, contacter la poste, enquête, relance |
| L'humain a envoyé une étiquette retour | `ACTION_RETURN` | retour, étiquette, bordereau, label, return |
| L'humain a traité un échange | `ACTION_EXCHANGE` | échange, échanger, nouveau modèle, remplacement |
| L'humain a réexpédié la commande | `ACTION_RESHIP` | renvoy, réexpédi, nouvel envoi, nouveau colis, réexped |
| L'humain a traité une garantie | `ACTION_WARRANTY` | garantie, SAV, service après-vente |
| L'humain a fait un geste commercial | `ACTION_DISCOUNT` | code promo, réduction, discount, geste commercial |
| L'humain a demandé des preuves | `INFO_REQUEST` | photo, vidéo, image, preuve |
| L'humain a demandé des détails | `INFO_DETAILS` | numéro de commande, référence, préciser, plus d'information |

### Patterns de détection (pour le marché anglophone)

| Pattern | Catégorie | Mots-clés |
|---|---|---|
| Refund processed | `ACTION_REFUND` | refund, refunded, credit, store credit, reimbursement |
| Logistics contact | `ACTION_LOGISTICS` | warehouse, carrier, investigation, tracking, logistics team |
| Return label sent | `ACTION_RETURN` | return label, return shipping, prepaid label, RMA |
| Exchange processed | `ACTION_EXCHANGE` | exchange, replacement, swap, new item |
| Order reshipped | `ACTION_RESHIP` | reship, resend, new shipment, sent again |
| Warranty claim | `ACTION_WARRANTY` | warranty, guarantee, defect, manufacturer |
| Discount/gesture | `ACTION_DISCOUNT` | discount code, coupon, promo code, goodwill |
| Proof requested | `INFO_REQUEST` | photo, video, picture, evidence, proof |

### Résultat attendu

```
=== POURQUOI L'HUMAIN A DÛ PRENDRE LE RELAIS ===

Actions nécessitant un accès backend : XX% des handovers
  - Remboursement : XX%
  - Contact logistique : XX%
  - Étiquette retour : XX%
  - Échange : XX%
  - Réexpédition : XX%
  - Garantie : XX%
  - Geste commercial : XX%
Demande d'information complémentaire : XX%
Autre / non classifié : XX%
```

**L'insight business :** Si 80%+ des handovers nécessitent une ACTION (pas juste de l'information), le problème n'est pas les guidances — c'est qu'AI Agent n'a pas les outils (Actions Shopify/intégrations) pour agir. C'est un argument commercial puissant.

Sur Nébuleuse : **92,6%** des handovers nécessitaient une action backend.

---

## Étape 5 — Analyse par intent (priorisation)

### Tableau de priorisation

Pour chaque intent, calculer :

| Intent | Volume | Success rate actuel | Handover rate | Tickets récupérables | Priorité |
|---|---|---|---|---|---|
| Intent A | X | Y% | Z% | Volume × Handover rate | 🔴/🟡/🟢 |

**Formule de priorisation :** `Volume × (1 - Success rate)` = nombre de tickets récupérables

Les intents à plus fort volume × plus fort taux de handover sont les quick wins.

### Comparaison AI vs Humain par intent

Pour les top intents, comparer les réponses AI Agent vs les réponses humaines sur les mêmes types de demandes :

```
=== INTENT: Order::Status ===
AI handles : X tickets → comment répond-il ?
Humain handles : X tickets → comment répond-il ?
Différence : L'AI donne le tracking, l'humain contacte en plus la logistique
→ Gap identifié : AI Agent manque l'action de contact logistique
```

**Pourquoi c'est précieux :** Cette comparaison side-by-side montre exactement ce qui manque à l'AI Agent pour chaque intent. C'est plus convaincant que des chiffres abstraits.

---

## Étape 6 — Extraction d'exemples concrets

### Exemples de handover (pour le rapport)

Pour chaque top catégorie de handover, extraire 1-2 exemples montrant :

1. **Le message du client** — la demande originale
2. **La réponse de l'AI Agent** — souvent pertinente et empathique
3. **La réponse de l'humain** — souvent une action simple (remboursement, contact logistique)
4. **Ce qu'AI Agent aurait pu faire** — avec la bonne configuration

### Exemples de succès (pour le rapport)

Extraire aussi 1-2 exemples où AI Agent a résolu le ticket de bout en bout. Ça prouve que le modèle fonctionne et que le problème est la configuration, pas la technologie.

### Format recommandé pour le rapport

```
📩 Client : "Bonjour, j'ai commandé le 1er décembre et je n'ai toujours 
   aucune nouvelle de ma commande, ça fait 15 jours..."

🤖 AI Agent : "Bonjour Candice, Merci pour votre message. Votre commande 
   #850213 est actuellement en transit via La Poste..."
   → AI Agent a bien identifié la commande et partagé le tracking
   → Mais a transféré à un agent humain

👤 Agent humain : "J'ai contacté notre équipe logistique pour comprendre 
   le statut de votre commande..."
   → L'humain a simplement contacté la logistique — une action que 
   l'AI pourrait faire avec la bonne Action Shopify
```

---

## Étape 7 — Calcul des leviers et projections

### Les 4 leviers d'amélioration

| Levier | Source | Taux de conversion estimé | Formule |
|---|---|---|---|
| **Réduire les ignorés** | Tickets `ai_ignore` sur des intents automatisables | 18% (70% coverage × 25% success) | Tickets ignorés × 18% |
| **Corriger les handovers** | Tickets `ai_handover` + `ai_answered` | 50% | Tickets handover × 50% |
| **Ajouter des Actions** | Handovers de type `ACTION_*` | 20% | Tickets action × 20% |
| **Améliorer les guidances** | Intents avec guidances sous-performantes | 15% variable | Cas par cas |

### Projection totale

```
Tickets actuellement résolus : X (Y%)
+ Levier 0 (ignorés) : +X tickets
+ Levier 1 (handovers) : +X tickets
+ Levier 2 (actions) : +X tickets
+ Levier 3 (guidances) : +X tickets
= Projection : X tickets (Y%)
```

⚠️ **Important :** Rester conservateur dans les estimations. Un client préfère être agréablement surpris que déçu. Les taux de conversion ci-dessus sont des estimations basses.

---

## Pièges et apprentissages

### Pièges techniques

1. **Séparateur CSV :** Gorgias exporte en `;` (point-virgule), pas en `,`. Toujours vérifier
2. **Encodage :** Utiliser `utf-8-sig` pour gérer le BOM Windows
3. **Lignes d'en-tête :** Le CSV peut avoir 1 ou 2 lignes avant les données réelles — toujours vérifier
4. **Caractères spéciaux dans agent_name :** Emojis, apostrophes typographiques (`'` vs `'`), accents — utiliser des patterns larges pour matcher
5. **Tags multiples :** Un ticket peut avoir plusieurs tags séparés par des virgules — toujours parser correctement

### Pièges méthodologiques

1. **Ne pas confondre `ai_answered` et `ai_close`** — `ai_answered` signifie que l'AI a répondu, pas qu'il a résolu. Le vrai succès c'est `ai_close`
2. **Distinguer email et global** — Le taux d'automatisation sur email est toujours plus élevé que le taux global (car AI Agent n'est souvent actif que sur email). Toujours préciser quel périmètre
3. **Les tickets `ai_ignore` ne sont pas des échecs de l'AI** — ce sont des tickets que l'AI est configuré pour ne pas traiter. C'est un choix de configuration, pas une limitation technique
4. **Les handovers ne sont pas tous récupérables** — certains nécessitent vraiment un humain (cas complexes, émotions fortes, escalade). Ne jamais promettre 0% de handover
5. **Le volume d'outsourcing ≠ le volume total** — certains tickets sont traités par des agents internes, d'autres par des bots non-AI (WhatsApp Simio, etc.)

### Bonnes pratiques de rédaction du rapport

1. **Utiliser "résoudre" plutôt que "clore"** — le client veut des problèmes résolus, pas des tickets fermés
2. **Utiliser "outsourcing" plutôt que le nom du prestataire** — le client peut changer de partenaire
3. **Chiffrer chaque recommandation** — volume de tickets, impact estimé en %
4. **Donner des exemples concrets** — les citations de tickets sont plus convaincantes que les chiffres seuls
5. **Éviter le ton consultant** — être direct, factuel, actionnable
6. **Ordonner par impact** — toujours présenter les leviers du plus gros impact au plus petit

---

## Script type (Python)

### Structure recommandée

```python
import csv
from collections import defaultdict

# 1. Charger le CSV
# Attention : séparateur ; et possible BOM
with open('fichier.csv', 'r', encoding='utf-8-sig') as f:
    # Sauter les lignes de métadonnées si nécessaire
    # next(f)  # décommenter si ligne de métadonnées
    reader = csv.DictReader(f, delimiter=';')
    
    tickets = {}
    ticket_messages = defaultdict(list)
    
    for row in reader:
        tid = row.get('ticket_id', '').strip()
        if tid not in tickets:
            tickets[tid] = {
                'intent': row.get('AI_intent', '').strip(),
                'tags': row.get('tags', '').strip(),
                'channel': row.get('ticket_channel', '').strip(),
                'agent': row.get('agent_name', '').strip(),
            }
        ticket_messages[tid].append({
            'from_agent': row.get('from_agent', '').strip(),
            'body': row.get('body_text', '').strip(),
            'agent_name': row.get('agent_name', '').strip(),
            'datetime': row.get('sent_datetime', '').strip(),
        })

# 2. Stats de base
print(f"Total messages: {sum(len(v) for v in ticket_messages.values())}")
print(f"Total tickets: {len(tickets)}")

# 3. Funnel par canal
email_tickets = {t: d for t, d in tickets.items() if 'email' in d['channel'].lower()}
ai_ignore = {t: d for t, d in email_tickets.items() if 'ai_ignore' in d['tags']}
ai_close = {t: d for t, d in email_tickets.items() if 'ai_close' in d['tags']}
ai_handover = {t: d for t, d in email_tickets.items() if 'ai_handover' in d['tags']}
ai_answered = {t: d for t, d in email_tickets.items() if 'ai_answered' in d['tags']}

# 4. Analyse des handovers (voir patterns de détection ci-dessus)
# ...

# 5. Priorisation par intent
# ...
```

---

## Checklist de livrables

À l'issue de cette analyse, tu dois avoir :

- [ ] Stats de base (messages, tickets, période, canaux)
- [ ] Funnel email complet (ignorés → tentés → résolus → handover)
- [ ] Répartition par agent (AI vs outsourcing vs autres)
- [ ] Top 15 intents par volume avec success rate et handover rate
- [ ] Catégorisation des raisons de handover (ACTION_REFUND, ACTION_LOGISTICS, etc.)
- [ ] Pourcentage de handovers nécessitant une action backend
- [ ] 3-5 exemples concrets de tickets (handover + succès)
- [ ] Tableau de priorisation des leviers avec impact estimé
- [ ] Projection chiffrée (de X% à Y% d'automatisation)

---

*Playbook créé en février 2026 — basé sur l'analyse de 41 419 messages / 12 024 tickets pour Nébuleuse Bijoux*
*À enrichir après chaque nouvel audit*
