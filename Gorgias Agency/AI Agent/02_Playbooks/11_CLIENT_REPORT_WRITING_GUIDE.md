# ✍️ Guide de Rédaction du Rapport Client

## Objectif

Ce guide capture les bonnes pratiques et les erreurs à éviter lors de la rédaction d'un rapport d'audit AI Agent pour un client. Il est basé sur 6 itérations de rapport et 30+ corrections avec retour client direct.

**Complémentaire à :** `ai_agent_audit_playbook.md` (Phase 5)

---

## Principes fondamentaux

### 1. Orienté opportunités, pas post-mortem

Le rapport doit montrer **ce qui est possible**, pas seulement ce qui ne marche pas. Le client sait déjà que son taux est bas — il veut savoir comment l'améliorer.

**❌ Mauvais :** "L'AI Agent ne résout que 8% des tickets, ce qui est très en dessous des standards."
**✅ Bon :** "Le chemin de 8% à 50% d'automatisation est clair — voici les 4 leviers identifiés."

### 2. Direct et factuel, pas consultant

Éviter le jargon consultant, les formulations creuses, et les phrases qui n'apportent pas d'information concrète.

**❌ Mauvais :** "Dans une optique d'optimisation continue de votre stratégie customer-centric..."
**✅ Bon :** "1 933 tickets email sont ignorés par AI Agent. En réduisant ce chiffre, +338 tickets résolus."

### 3. Chaque recommandation est chiffrée

Jamais de recommandation sans volume de tickets et impact estimé.

**❌ Mauvais :** "Améliorer les guidances pourrait augmenter le taux d'automatisation."
**✅ Bon :** "La guidance garantie traite 1 455 tickets avec un taux de résolution de 4,1%. En ajoutant une étape de clôture après le formulaire → +2% à +3% d'automatisation."

---

## Vocabulaire

### Mots à utiliser

| Utiliser | Au lieu de | Pourquoi |
|---|---|---|
| **Résoudre** | Clore / fermer | Le client veut des problèmes résolus, pas des tickets fermés |
| **Outsourcing** | [Nom du prestataire] | Le client peut changer de partenaire |
| **Instructions** | Guidances | En français, "guidance" est un anglicisme — utiliser "instructions" |
| **Transférer** | Handover | En français dans le rapport client |
| **Taux d'automatisation** | Automation rate | Traduire les métriques |
| **Canal email** | Email channel | Idem |
| **AI Agent** | Le bot / l'IA | Garder le nom produit Gorgias |

### Mots à éviter

| Éviter | Pourquoi |
|---|---|
| "Malheureusement" | Trop négatif, crée un sentiment d'impuissance |
| "Problème" (en titre) | Remplacer par "Opportunité" ou "Levier" |
| "Clôturer les tickets" | Implique qu'on ferme sans résoudre |
| "Le client" (en parlant au client) | Utiliser "vous" ou le nom de la marque |
| Jargon technique non expliqué | Toujours expliciter (CSAT, FRT, etc.) |
| "Il faudrait" / "On devrait" | Trop passif — utiliser l'impératif ou le futur |

---

## Structure recommandée du rapport

### 1. Méthodologie (court)

Expliquer en 3-4 lignes ce qui a été analysé : nombre de messages, tickets, période, sources de données. Donne de la crédibilité sans être verbeux.

### 2. Situation actuelle (les chiffres clés)

KPIs principaux en un coup d'œil. Pas d'analyse ici — juste les faits.

### 3. Ce que les données montrent (analyse)

Le funnel email, les raisons de handover, les intents par volume. C'est le cœur analytique.

### 4. Analyse des instructions (guidances)

Pour les top intents : état actuel de la guidance, scénarios, points d'amélioration.

### 5. Impact sur les temps de réponse

FRT, RT, temps de résolution — prouver que l'AI Agent est déjà plus rapide.

### 6. Opportunités business

Chat pré-achat, conversion weekend, canaux additionnels. Les leviers au-delà du support.

### 7. Plan d'action (3 phases)

Phase 1 Quick Wins → Phase 2 Intégrations → Phase 3 Avancé. Chaque action chiffrée.

### 8. Projection économique

Coût actuel → Coût projeté → Économie nette.

### 9. Roadmap

Tableau récapitulatif de toutes les actions avec impact estimé.

### 10. Prochaines étapes

Liste ordonnée des actions concrètes à réaliser.

---

## Erreurs fréquentes (retour d'expérience)

### Erreur 1 : Confondre les métriques email et globales

Le taux d'automatisation sur email est TOUJOURS plus élevé que le taux global (parce que AI Agent n'est souvent actif que sur email). Toujours préciser :

**❌** "Le taux d'automatisation est de 18,1%."
**✅** "Le taux d'automatisation sur le canal email est de 18,1% (8,1% en global, car AI Agent n'est pas encore déployé sur le chat)."

### Erreur 2 : Présenter les handover topics comme des guidances

Les handover topics (Settings > Handover topics) ne sont pas des guidances. Ce sont des règles de blocage qui empêchent AI Agent de traiter certains types de demandes. Ne pas les confondre.

### Erreur 3 : Oublier de mentionner ce qui marche

Si le rapport ne parle que des problèmes, le client se sentira attaqué. Toujours inclure :
- Les guidances qui performent bien (ex: "Entretien bijoux à 92% de résolution")
- Les gains déjà réalisés (ex: "97% de réduction du temps de première réponse")
- Les exemples de tickets résolus avec succès

### Erreur 4 : Ordonner par ordre alphabétique au lieu de l'impact

Toujours ordonner les listes par impact décroissant :
- Les intents : du plus gros volume au plus petit
- Les leviers : du plus gros impact au plus petit
- Les actions : de la plus rapide à implémenter à la plus complexe

### Erreur 5 : Utiliser le nom du prestataire d'outsourcing

Toujours dire "l'outsourcing" ou "le prestataire" au lieu du nom (One Pilot, etc.). Le client pourrait changer de prestataire, et le rapport doit rester pertinent.

### Erreur 6 : Ton trop "consultant"

Les phrases génériques qui n'apportent rien :
- "Dans le cadre de notre analyse approfondie..."
- "Il est important de noter que..."
- "Ceci représente une opportunité significative..."

Remplacer par des faits directs :
- "L'analyse de 41 419 messages montre que..."
- "92,6% des transferts impliquent une action backend."
- "+338 tickets récupérables en réduisant les exclusions."

### Erreur 7 : Mauvais positionnement des canaux

Le chat n'est pas qu'un canal de support — c'est un canal de conversion pré-achat. Le positionner en Phase 1 (quick win) plutôt qu'en Phase 3. L'argument business est plus fort que l'argument support.

### Erreur 8 : Promettre des chiffres trop précis

**❌** "Nous atteindrons exactement 47,3% d'automatisation."
**✅** "L'objectif est d'atteindre 50% d'automatisation, avec une projection conservatrice à 53,8% basée sur les 4 leviers identifiés."

### Erreur 9 : Oublier le contexte saisonnier

Le volume de tickets varie considérablement selon la saison (Noël, soldes, Black Friday). Les projections basées sur une période de pic (décembre) ne sont pas représentatives du volume annuel moyen. Toujours préciser la période analysée et ses spécificités.

---

## Itérations avec le client

### Anticiper les retours

Sur 6 versions de rapport, voici les types de retours les plus fréquents :

1. **Corrections factuelles** (40%) — "Track Order est activé, pas désactivé" / "Le formulaire garantie est sur Typeform, pas Google Forms"
2. **Ton et formulation** (25%) — "Trop consultant" / "Reformuler en plus direct"
3. **Ordre de présentation** (15%) — "Mettre le chat en Phase 1" / "Ordonner par impact"
4. **Données manquantes** (10%) — "Ajouter les coûts outsourcing sur 6 mois" / "Inclure les données de conversion"
5. **Ajouts de contenu** (10%) — "Ajouter la section sur les weekends" / "Inclure le plan de canaux futurs"

### Process recommandé

1. **V1** — Première version basée sur les données analysées. Envoyer pour validation des faits
2. **V2** — Corriger les erreurs factuelles + intégrer les données business du client
3. **V3** — Ajuster le ton, l'ordre, et les formulations selon le feedback
4. **V4+** — Itérations finales sur les détails

⚠️ **Ne pas chercher à livrer un rapport parfait en V1.** Le client a des informations que tu n'as pas (configuration exacte, coûts réels, contexte business). Les itérations sont normales et productives.

---

## Langue et localisation

### Rapport en français

Si le client est français, le rapport entier doit être en français :
- Titres de sections en français
- Métriques traduites (taux d'automatisation, temps de réponse, satisfaction)
- Exemples de tickets en français
- Seuls les noms de features Gorgias restent en anglais (AI Agent, Track Order, Handover topics)

### Mots Gorgias à garder en anglais

Ces termes sont des noms de features produit et ne se traduisent pas :
- AI Agent
- Track Order / Return Order
- Handover topics
- Actions
- Flows
- Help Center
- Shopping Assistant
- Order Management

---

## Format de livraison

### Markdown (recommandé pour le contenu)

- Archivable, modifiable, versionnable
- Facile à itérer avec le client
- Se convertit en HTML/PDF si nécessaire

### HTML interactif (optionnel pour la présentation)

- Effet WOW pour la présentation client
- Nécessite un alignement avec la charte graphique du client
- Plus long à produire — ne s'engage que si le client le demande
- Prévoir un design sobre et élégant, pas un dashboard SaaS

⚠️ **Leçon apprise :** Si tu proposes un dashboard HTML, aligne-toi dès le départ avec l'identité visuelle du client (logo, couleurs, typo). Un dashboard générique sera toujours rejeté. Demander des exemples visuels / références de design au client AVANT de commencer.

---

*Guide créé en février 2026 — basé sur 6 itérations du rapport Nébuleuse Bijoux*
*À enrichir après chaque nouveau rapport client*
