# 💰 Modèle Économique & Calcul ROI

## Objectif

Ce playbook standardise le calcul économique pour les audits AI Agent : coût actuel, coût AI Agent, projections, et ROI. Il s'assure que les chiffres présentés au client sont crédibles, conservateurs, et transparents dans leurs hypothèses.

**Complémentaire à :** `ai_agent_audit_playbook.md` (Phase 4)

---

## Données à collecter

### Coûts outsourcing

| Donnée | Source | Notes |
|---|---|---|
| Abonnement mensuel | Factures outsourcing | Fixe, ex: 299€/mois |
| Coût par ticket | Factures outsourcing | Variable, ex: 2,05€/ticket |
| Volume mensuel de tickets traités | Factures sur 6-14 mois | Prendre la moyenne |
| Coût total mensuel | Calcul | Abonnement + (volume × coût/ticket) |

⚠️ **Piège :** Ne pas utiliser un seul mois comme référence — le volume fluctue (pics saisonniers, soldes, Noël). Toujours prendre une moyenne sur 6+ mois.

**Exemple Nébuleuse :** Abonnement 299€ + ~5 700 tickets/mois × 2,05€ = ~12 000€/mois sur les 6 derniers mois.

### Coûts AI Agent Gorgias

Les plans AI Agent Gorgias (à vérifier — les prix peuvent changer) :

| Plan | Prix mensuel (USD) | Interactions incluses |
|---|---|---|
| Starter | ~$300 | 300 interactions |
| Growth | ~$640 | 800 interactions |
| Scale | ~$1,125 | 1,500 interactions |
| Enterprise | Sur devis | Personnalisé |

**Conversion USD → EUR :** Utiliser le taux actuel, arrondir au chiffre rond le plus proche.

⚠️ **Ce qui compte comme "interaction automatisée" :** Un ticket résolu par AI Agent sans intervention humaine. Les handovers ne comptent pas comme interaction facturée.

---

## Calcul du coût actuel

### Formule de base

```
Économie actuelle AI Agent = Tickets résolus par AI × Coût/ticket outsourcing
Coût AI Agent = Abonnement mensuel du plan
Économie nette = Économie outsourcing - Coût AI Agent
```

### Exemple

```
Tickets résolus par AI /mois : 488
Économie outsourcing : 488 × 2,05€ = 1 000€
Coût AI Agent : 589€ (plan à $640)
Économie nette : 1 000€ - 589€ = 411€/mois
```

---

## Projection à l'objectif cible

### Identifier l'objectif réaliste

| Situation actuelle | Objectif réaliste | Timeframe |
|---|---|---|
| < 10% automation | 25-35% | 2-3 mois |
| 10-20% automation | 35-45% | 1-2 mois |
| 20-30% automation | 40-50% | 1-2 mois |
| > 30% automation | 50%+ | Optimisation continue |

### Calculer les tickets projetés

```
Tickets email /mois = Total tickets email sur la période / Nombre de mois
Tickets projetés résolus = Tickets email /mois × Taux d'automatisation cible
```

### Estimer le changement de plan AI Agent

Si le nombre d'interactions projetées dépasse le plan actuel, prévoir le coût du plan supérieur.

### Formule de projection

```
PROJETÉ :
Tickets résolus par AI /mois : X (à Y% d'automatisation)
Économie outsourcing : X × Coût/ticket = Z€
Coût AI Agent : Plan adapté = W€
Économie nette /mois : Z€ - W€
Économie nette /an : (Z€ - W€) × 12
```

---

## Modèle complet

### Tableau de synthèse (format rapport)

| | Actuel | Projeté |
|---|---|---|
| Taux d'automatisation email | X% | Y% |
| Tickets résolus par AI /mois | X | X |
| Économie outsourcing /mois | X€ | X€ |
| Coût AI Agent /mois | X€ | X€ |
| **Économie nette /mois** | **X€** | **X€** |
| **Économie nette /an** | **X€** | **X€** |

### Projection par levier (format rapport)

| Levier | Mécanisme | Tickets récupérés (sur la période analysée) |
|---|---|---|
| Réduire les tickets ignorés | Élargir la couverture AI Agent | +X |
| Corriger les handovers systématiques | Permettre à AI Agent de conclure | +X |
| Ajouter des Actions | Remboursements, logistique, retours | +X |
| Améliorer les Guidances | Garantie, retour, échange | +X |
| **Total** | | **+X** |

---

## Règles de crédibilité

### Estimations conservatrices

Toujours utiliser des taux de conversion bas plutôt que optimistes :

| Levier | Taux optimiste | Taux conservateur (recommandé) | Justification |
|---|---|---|---|
| Tickets ignorés → résolus | 30-40% | 18% | 70% coverage × 25% success |
| Handovers → résolus | 70-80% | 50% | Tous ne sont pas récupérables |
| Actions → résolus | 40-50% | 20% | Implémentation progressive |
| Guidances → amélioration | 30%+ | 10-15% | Variable selon l'intent |

### Ce qu'il ne faut PAS faire

1. **Ne pas promettre 50%+ d'automatisation dès le mois 1** — c'est un objectif à 2-3 mois
2. **Ne pas oublier le coût du plan AI Agent** — toujours présenter l'économie NETTE, pas brute
3. **Ne pas ignorer les pics saisonniers** — le volume de décembre n'est pas celui de mars
4. **Ne pas compter les handovers comme des résolutions** — un ticket transféré coûte toujours à l'outsourcing
5. **Ne pas additionner les % d'impact des leviers naïvement** — il y a des chevauchements entre leviers

### Transparence des hypothèses

Toujours accompagner les projections d'une note sur les hypothèses :

```
*Note : ces projections sont basées sur le volume email uniquement. 
L'activation d'AI Agent sur le Chat et les futurs canaux augmentera 
significativement l'impact. Les taux de conversion utilisés sont 
conservateurs et basés sur les benchmarks observés.*
```

---

## Calcul avancé : impact de l'outsourcing

### Si le client envisage de réduire l'outsourcing

```
Réduction outsourcing possible = Tickets repris par AI × Coût/ticket
% de réduction du volume outsourcing = Tickets repris / Total tickets outsourcing
Nouveau coût mensuel outsourcing = Volume restant × Coût/ticket + Abonnement
```

⚠️ **Attention :** La réduction de l'outsourcing n'est pas linéaire. Même à 50% d'automatisation, le client aura toujours besoin d'un volume minimum d'agents humains pour les cas complexes, les pics, et la qualité.

### Si le client envisage de supprimer l'outsourcing

C'est un scénario avancé qui nécessite :
- Un taux d'automatisation > 70% stable
- Un plan de backup pour les pics (Noël, soldes)
- Au moins 1 personne interne capable de gérer les escalades

---

## Checklist

- [ ] Coûts outsourcing collectés (factures 6+ mois)
- [ ] Plan AI Agent actuel identifié avec coût
- [ ] Économie nette actuelle calculée
- [ ] Objectif d'automatisation défini et réaliste
- [ ] Projection par levier avec taux conservateurs
- [ ] Plan AI Agent projeté (si changement de plan nécessaire)
- [ ] Économie nette projetée (mensuelle et annuelle)
- [ ] Hypothèses documentées et transparentes

---

*Playbook créé en février 2026 — basé sur les calculs pour Nébuleuse Bijoux*
*Tarifs AI Agent à vérifier régulièrement car susceptibles de changer*
