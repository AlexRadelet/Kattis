# intervals

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `intervals`)*

## Résumé

Étant donné `n` intervalles horaires (sur une journée de 24 heures) et un seuil `k`, compter combien d'heures sont couvertes par au moins `k` intervalles.

## Idée

Utiliser un tableau de 24 compteurs (une case par heure). Pour chaque intervalle `[a, b)`, incrémenter chaque heure couverte. À la fin, compter les heures dont le compteur atteint au moins `k`.

Ça fonctionne parce que la plage horaire est bornée et petite (24 heures) : un tableau fixe indexé par heure permet d'accumuler directement, pour chaque heure, le nombre d'intervalles qui la couvrent, sans structure plus complexe.

## Algorithme

1. Lire `n` (nombre d'intervalles) et `k` (seuil de couverture).
2. Initialiser un tableau `ar` de 24 zéros.
3. Pour chaque intervalle `[a, b)`, incrémenter `ar[i]` pour chaque heure `i` de `a` à `b-1`.
4. Compter et afficher le nombre d'heures dont le compteur est `>= k`.

## Complexité

- Temps : O(n × 24) dans le pire cas, soit O(n) puisque la plage (24) est une constante.
- Mémoire : O(24), donc O(1) en pratique.

## Difficultés rencontrées

La borne supérieure `b` est exclue (`range(a, b)`), donc un intervalle `[a, b)` couvre les heures `a` à `b-1`. Une erreur classique serait d'utiliser `range(a, b+1)` et de compter une heure de trop.

## Ce que j'ai appris

- Quand le domaine (ici 24 heures) est petit et fixe, un tableau de comptage direct est plus simple qu'une structure de type "sweep line" avec tri d'évènements, tout en restant efficace.

## Améliorations possibles

Pour un domaine beaucoup plus grand, une approche par tableau de différences (`ar[a] += 1`, `ar[b] -= 1`, puis somme préfixe) éviterait la boucle interne et ramènerait le coût à O(n + plage) au lieu de O(n × plage).
