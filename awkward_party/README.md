# awkward_party

[Lien vers Kattis](https://open.kattis.com/problems/awkwardparty)

Thème : Structures de données (dictionnaire)

## Résumé

Étant donné une séquence de langues parlées par des invités, trouver l'écart minimal (en nombre de positions) entre deux occurrences de la même langue.

## Idée

Parcourir la séquence une seule fois en maintenant un dictionnaire `last_seen` qui associe à chaque langue la dernière position où elle a été vue. Dès qu'une langue déjà vue réapparaît, calculer l'écart avec sa dernière occurrence et mettre à jour le minimum courant.

Ça fonctionne parce que pour minimiser l'écart entre deux occurrences d'une même valeur, seule la paire d'occurrences *consécutives* (les plus proches l'une de l'autre) peut donner l'écart minimal pour cette valeur : comparer chaque occurrence à la précédente immédiate suffit, pas besoin de comparer à toutes les occurrences antérieures. Un dictionnaire donne un accès O(1) à "la dernière position vue" pour n'importe quelle langue, ce qui permet de résoudre le problème en un seul passage.

## Algorithme

1. Lire `n` et la liste des langues.
2. Parcourir la liste avec son index `i`.
3. Si la langue courante est déjà dans `last_seen`, mettre à jour `answer` avec `min(answer, i - last_seen[langue])`.
4. Enregistrer la position courante comme dernière occurrence de cette langue.
5. Afficher `answer` (initialisé à `n`, qui sert de valeur "aucune répétition trouvée" si aucune langue ne se répète).

## Complexité

- Temps : O(n).
- Mémoire : O(n) pour le dictionnaire, dans le pire cas où toutes les langues sont distinctes.

## Difficultés rencontrées

Il faut se convaincre que comparer uniquement à la *dernière* occurrence (et non à toutes les occurrences précédentes de la même langue) suffit à trouver l'écart minimal global : comme on veut le minimum sur toutes les langues confondues, et que pour une langue donnée l'écart minimal entre ses propres occurrences est forcément entre deux occurrences consécutives, un seul passage avec "dernière position vue" capture bien tous les écarts minimaux candidats.

## Ce que j'ai appris

Pattern récurrent sur Kattis : « ai-je déjà vu cette valeur, et si oui, où ? » se résout avec un `dict` (valeur → dernière position), pas un `set` (qui ne répondrait qu'à « déjà vue ? » sans dire où). Le choix entre `set` et `dict` dépend de si on a seulement besoin de l'appartenance ou aussi d'une information associée.

## Améliorations possibles

Aucune : la solution est déjà en O(n), optimale puisqu'il faut au minimum lire chaque élément une fois.
