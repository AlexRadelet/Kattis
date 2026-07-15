# shiritori

[Lien vers Kattis](https://open.kattis.com/problems/shiritori)

Thème : Structures de données (ensemble / set)

## Résumé

Deux joueurs disent des mots à tour de rôle : chaque mot doit commencer par la dernière lettre du mot précédent et ne jamais avoir été utilisé auparavant. Déterminer si la partie se déroule sans accroc (`Fair Game`) ou quel joueur perd en premier, et à quel tour.

## Idée

Maintenir un `set` des mots déjà utilisés (pour tester l'appartenance en O(1)) et une variable `previous` pour le dernier mot joué. À chaque tour, vérifier dans l'ordre : le mot a-t-il déjà été utilisé ? Sinon, s'enchaîne-t-il correctement avec le mot précédent ? Si l'une des deux règles est violée, le joueur du tour courant perd.

Ça fonctionne parce que les deux règles du jeu (pas de répétition, bon enchaînement de lettres) sont exactement les deux tests effectués, dans l'ordre où elles doivent être vérifiées à chaque tour. Un `set` est le choix déterminant ici : avec `n` mots pouvant aller jusqu'à une grande taille, tester l'appartenance dans une `list` serait O(n) par tour (O(n²) au total) et provoquerait un dépassement de temps, alors qu'un `set` garde chaque test en O(1) en moyenne.

## Algorithme

1. Lire `N` (nombre de mots joués).
2. Pour chaque tour `i` de `1` à `N` : lire le mot.
3. Si le mot est déjà dans `used_words`, ou si sa première lettre ne correspond pas à la dernière lettre du mot précédent, afficher quel joueur perd (`Player 1` si `i` est impair, `Player 2` sinon) et arrêter.
4. Si aucune règle n'est violée, ajouter le mot à `used_words` et le retenir comme `previous`.
5. Si tous les tours se déroulent sans violation, afficher `Fair Game`.

## Complexité

- Temps : O(N) en moyenne (chaque test d'appartenance à un `set` est O(1) amorti).
- Mémoire : O(N) pour stocker les mots déjà utilisés.

## Difficultés rencontrées

- Utiliser une `list` au lieu d'un `set` pour `used_words` passe le temps d'exécution de O(N) à O(N²), ce qui dépasse la limite de temps de Kattis sur les entrées volumineuses — c'est l'erreur initiale rencontrée sur ce problème.
- Déterminer quel joueur a perdu à partir de la parité du tour (`i % 2`) suppose que le joueur 1 commence toujours au tour 1 : à vérifier que cette convention correspond bien à l'énoncé.

## Ce que j'ai appris

Règle générale pour choisir une structure de données :

- besoin de tester « est-ce que j'ai déjà vu cet élément ? » → `set` ;
- besoin de garder un ordre → `list` ;
- besoin d'associer clé/valeur → `dict`.

Ici, le `set` est exactement le bon outil : seule l'appartenance compte, ni l'ordre des mots ni une valeur associée ne sont nécessaires.

## Améliorations possibles

Aucune : la solution est déjà en complexité optimale (il faut au minimum lire chaque mot une fois).
