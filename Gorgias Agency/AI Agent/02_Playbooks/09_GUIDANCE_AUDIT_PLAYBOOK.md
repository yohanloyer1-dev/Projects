# 🔍 Guidance Audit Playbook

## Objectif

Ce playbook détaille comment auditer systématiquement les guidances existantes d'un client pour identifier les handovers évitables et les optimisations possibles. C'est le pont entre l'analyse quantitative (CSV) et les recommandations actionnables.

**Complémentaire à :** `ai_agent_audit_playbook.md` (enrichit la Phase 3) et `08_CSV_TICKET_ANALYSIS_PLAYBOOK.md`

---

## Quand utiliser ce playbook

- Après l'analyse CSV des tickets (tu connais les volumes et taux de handover par intent)
- Avant de rédiger le plan d'action (tu as besoin de comprendre POURQUOI les guidances sous-performent)
- Le client a déjà des guidances en place (au moins 5-10)

---

## Phase 1 — Collecte des guidances

### Comment récupérer les guidances

**Option 1 — Screenshots (recommandé)**
- Demander au client des screenshots de chaque guidance ouverte dans Gorgias
- Avantage : rapide, conserve la mise en forme, visible en un coup d'œil

**Option 2 — Copier-coller le texte**
- Le client copie-colle le contenu de chaque guidance dans le chat
- Avantage : analysable, searchable
- Inconvénient : perd la structure visuelle

**Option 3 — Export si possible**
- Certaines configurations permettent un export
- Rarement disponible directement

⚠️ **Limite pratique :** Les uploads de fichiers ont une limite. Si le client a 25+ guidances, prioriser les guidances à fort volume (identifiées dans l'analyse CSV) et demander les autres en copier-coller.

### Informations à capturer pour chaque guidance

| Information | Pourquoi |
|---|---|
| **Nom / titre** | Identifier la guidance |
| **Déclencheur** ("When a shopper...") | Comprendre quand elle s'active |
| **Nombre de scénarios** | Évaluer la complexité |
| **Pour chaque scénario : conclusion** (End flow vs Handover) | Identifier les handovers évitables |
| **Conditions de handover** | Comprendre les critères de transfert |
| **Liens/outils partagés** (formulaires, portail retour, etc.) | Évaluer ce que l'AI peut faire |
| **Règles générales** | Comprendre les contraintes |

---

## Phase 2 — Analyse scénario par scénario

### Le framework d'analyse

Pour chaque guidance, créer un tableau :

| Scénario | Conclusion actuelle | Peut être résolu par AI ? | Pourquoi ? |
|---|---|---|---|
| Scénario 1 | ✅ End flow | ✅ Déjà OK | — |
| Scénario 2 | ❌ Handover | ✅ Oui | Pourrait conclure après [action] |
| Scénario 3 | ❌ Handover | ⚠️ Partiellement | Nécessite [condition] |
| Scénario 4 | ❌ Handover | ❌ Non | Nécessite intervention humaine réelle |

### Classification des handovers

**🟢 Handover évitable — AI peut conclure**
- La guidance envoie un formulaire / lien / info PUIS transfère → devrait conclure après l'envoi
- La guidance vérifie un statut PUIS transfère → devrait communiquer le statut et conclure
- La guidance demande une info PUIS transfère une fois reçue → devrait traiter et conclure

**🟡 Handover partiellement évitable — nécessite une Action**
- La guidance identifie le besoin (remboursement, reship) mais ne peut pas agir → nécessite une Action Shopify/intégration
- Le handover est justifié AUJOURD'HUI mais pourrait être évité AVEC la bonne Action

**🔴 Handover justifié — nécessite un humain**
- Cas émotionnellement sensibles (plainte grave, client furieux)
- Décisions commerciales complexes (geste commercial exceptionnel)
- Vérifications manuelles nécessaires (fraude, cas particulier)
- Interventions physiques (contacter un transporteur, vérifier un entrepôt)

---

## Phase 3 — Patterns récurrents à chercher

### Pattern 1 : "Formulaire puis handover"

**Symptôme :** La guidance partage un formulaire (Typeform, Google Form, portail retour) puis transfère systématiquement au lieu de conclure.

**Exemple réel (Nébuleuse) :** Guidance garantie — envoie le formulaire Typeform puis fait handover sur 4/6 scénarios.

**Solution :** Ajouter une étape de clôture après l'envoi du formulaire : *"Nous avons bien noté votre demande. Notre équipe va l'examiner et reviendra vers vous sous X jours ouvrés."*

**Impact typique :** +2% à +5% d'automatisation selon le volume

### Pattern 2 : "Trop de chemins vers le handover"

**Symptôme :** La guidance est très détaillée avec de nombreux scénarios, mais presque tous se terminent par un handover. Seuls 2-3 chemins permettent de conclure.

**Exemple réel (Nébuleuse) :** Guidance WISMO — 12 sous-scénarios, seulement 2-3 concluent (colis en transit <5 jours, colis livré). Taux de handover : 91%.

**Solution :** Identifier les scénarios intermédiaires qui pourraient conclure : commande en préparation, colis en transit avec délai normal, livraison confirmée.

**Impact typique :** +3% à +6% d'automatisation

### Pattern 3 : "Process initial couvert, suivi manquant"

**Symptôme :** La guidance couvre bien la demande initiale (comment faire un retour, comment demander un échange) mais n'a aucune guidance pour le suivi (où en est mon retour ? quand serai-je remboursé ?).

**Exemple réel (Nébuleuse) :** Guidance retours — 6 scénarios pour le process de retour, 0 scénario pour le suivi. Guidance échanges — idem.

**Solution :** Créer une guidance dédiée au suivi couvrant : en transit, reçu, en traitement, terminé, délai dépassé.

**Impact typique :** +3% à +4% d'automatisation par guidance manquante

### Pattern 4 : "Handover topic trop large"

**Symptôme :** Un handover topic (dans les Settings) capture des tickets qui pourraient être traités par AI Agent. Ex : "Enquiries about refunds" capture autant les demandes de nouveau remboursement (justifié) que les simples suivis "où en est mon remboursement ?" (automatisable).

**Exemple réel (Nébuleuse) :** Les handover topics "reimbursements" et "refunds" capturaient ~189 tickets dont la majorité étaient de simples suivis.

**Solution :** Restreindre le handover topic aux demandes d'action uniquement, et laisser les demandes de suivi passer par les guidances.

**Impact typique :** +5% à +7% d'automatisation

### Pattern 5 : "Règle d'exclusion trop agressive"

**Symptôme :** Les règles "Prevent AI from answering" bloquent AI Agent sur des intents que les guidances pourraient traiter.

**Exemple réel (Nébuleuse) :** 1 933 tickets email (36,7%) étaient ai_ignore, incluant Return/Status (300), Order/Status (265), Warranty (218) — des intents pour lesquels des guidances existaient.

**Solution :** Revoir les règles d'exclusion et ne conserver que celles qui sont vraiment nécessaires.

**Impact typique :** +3% à +5% d'automatisation

### Pattern 6 : "Guidance bien structurée mais handover de prudence"

**Symptôme :** La guidance est complète, bien écrite, mais fait handover "par prudence" — souvent parce qu'elle a été écrite dans un esprit de couverture de risque plutôt que de résolution.

**Solution :** Ajouter des conditions de clôture explicites. Ex : au lieu de "If the customer confirms, handover to an agent", mettre "If the customer confirms receipt and is satisfied, thank them and close the ticket."

---

## Phase 4 — Audit de la base de connaissance outsourcing

### Pourquoi c'est important

Si le client utilise un prestataire d'outsourcing (One Pilot, etc.), celui-ci a souvent une base de connaissance très détaillée avec des arbres de décision multi-niveaux. Cette base contient exactement les process que l'AI Agent devrait suivre.

### Comment récupérer cette base

1. **Demander au client** de partager les process de son outsourcing (parfois accessible via un outil comme Chrome Extension)
2. **Screenshots des arbres de décision** — capturer les flows de décision pour les top intents
3. **Process écrits** — récupérer les instructions textuelles

### Ce qu'on cherche

- Des arbres de décision détaillés (si X alors Y, sinon Z)
- Des réponses pré-rédigées pour chaque cas
- Des statuts intermédiaires (ex : 10 statuts différents pour un retour sur Baback)
- Des règles de gestion commerciale (seuils de remboursement, gestes commerciaux autorisés)

### Comment exploiter

Chaque process outsourcing peut être converti en guidance AI Agent :
- Les conditions → deviennent les scénarios
- Les réponses pré-rédigées → deviennent le contenu des guidances
- Les actions manuelles → deviennent des candidats pour des Actions Shopify
- Les escalades → deviennent les points de handover justifiés

---

## Phase 5 — Synthèse et plan d'action

### Format de sortie recommandé

Pour chaque guidance auditée :

```
### [Nom de la guidance] — [Volume tickets/60j] — [Taux de handover]%

**État actuel :**
- X scénarios configurés
- Y scénarios concluent (End flow)
- Z scénarios font handover

**Analyse :**
[Tableau scénario par scénario]

**Opportunités :**
1. [Scénario X] — peut conclure après [action]
2. [Scénario Y] — nécessite une Action [type]

**Impact estimé :** +X% d'automatisation
```

### Priorisation

Prioriser les optimisations par : `Volume de tickets × Taux de handover × Facilité d'implémentation`

| Priorité | Critères |
|---|---|
| 🔴 Critique | Volume > 500 tickets/60j ET handover > 80% ET fix simple (ajout étape clôture) |
| 🟡 Important | Volume > 200 tickets/60j ET handover > 50% |
| 🟢 Nice to have | Volume < 200 tickets/60j OU handover < 50% OU fix complexe |

---

## Checklist de sortie

À l'issue de cet audit, tu dois avoir :

- [ ] Liste complète des guidances avec nombre de scénarios
- [ ] Tableau scénario par scénario pour les top 5-10 guidances
- [ ] Identification des patterns (formulaire→handover, suivi manquant, etc.)
- [ ] Classification des handovers (évitable / partiellement / justifié)
- [ ] Recommandations chiffrées par guidance
- [ ] Plan d'action priorisé par impact
- [ ] Si applicable : analyse de la base de connaissance outsourcing

---

*Playbook créé en février 2026 — basé sur l'audit de 28 guidances pour Nébuleuse Bijoux*
*À enrichir après chaque nouvel audit pour documenter de nouveaux patterns*
