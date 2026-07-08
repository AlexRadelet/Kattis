# dungeon_master

[Lien vers Kattis](https://open.kattis.com/problems/dungeon)

## Résumé

Dans une grille 3D composée de rochers (`#`) et de cases vides (`.`), trouver le nombre minimal de minutes pour aller de la case de départ (`S`) à la sortie (`E`), en se déplaçant d'une case par minute dans l'une des 6 directions (nord, sud, est, ouest, haut, bas), ou déterminer que c'est impossible.

## Idée

Faire un parcours en largeur (BFS) depuis `S`, où chaque case du donjon est un nœud et chaque déplacement valide vers une case voisine (non rocheuse, dans les limites de la grille) est une arête de poids 1. La distance à laquelle `E` est découvert pendant le BFS est le nombre minimal de minutes.

Ça fonctionne parce que dans un graphe non pondéré, le BFS garantit que la première fois qu'un nœud est atteint, c'est via le plus court chemin (en nombre d'arêtes) depuis la source — ici, chaque arête représentant exactement une minute, "plus court chemin" et "temps minimal" coïncident.

Un BFS est le choix naturel plutôt qu'un DFS ou un Dijkstra : DFS ne garantit pas le plus court chemin, et Dijkstra serait inutilement complexe puisque toutes les arêtes ont le même poids (1 minute) — le BFS est optimal et le plus simple à implémenter dans ce cas.

## Algorithme

1. Lire `L`, `R`, `C` (niveaux, lignes, colonnes) jusqu'à rencontrer `0 0 0`.
2. Lire la grille 3D et repérer les positions de `S` et `E`.
3. Initialiser un tableau de distances 3D à `-1` (non visité), avec `dist[S] = 0`.
4. Faire un BFS depuis `S` avec une file (`deque`), en explorant les 6 directions à chaque étape, en ignorant les rochers et les cases déjà visitées.
5. Une fois le BFS terminé, lire `dist[E]` : si toujours `-1`, afficher `Trapped!`, sinon afficher `Escaped in <dist[E]> minute(s).`.

## Complexité

- Temps : O(L·R·C) par cas de test (chaque case est visitée une fois, avec 6 voisins constants à examiner).
- Mémoire : O(L·R·C) pour la grille et le tableau de distances.

## Difficultés rencontrées

- Le format d'entrée contient une ligne vide après chaque niveau (et potentiellement entre les cas de test), mais ce n'est pas garanti de façon totalement uniforme. La solution lit les lignes via une fonction `next_line()` qui saute automatiquement toute ligne vide, que ce soit avant l'en-tête `L R C` ou entre deux niveaux — ça évite de dépendre d'un nombre exact de lignes vides.
- Le format de sortie exige un point final (`"Escaped in 11 minute(s)."`) et `Trapped!` avec un point d'exclamation : facile de rater ces détails de ponctuation qui font échouer la comparaison stricte de Kattis.

## Ce que j'ai appris

- BFS sur une grille 3D fonctionne exactement comme sur une grille 2D : il suffit d'ajouter une troisième coordonnée et deux directions de déplacement supplémentaires (haut/bas).
- Traiter une grille de caractères comme un graphe implicite (sans construire de liste d'adjacence explicite) est une technique courante et efficace pour ce type de problème : les voisins se calculent à la volée à partir des coordonnées.
- Lire toute l'entrée d'un coup (`sys.stdin.read().split("\n")`) et avancer un curseur manuel est plus robuste face aux lignes vides irrégulières que d'utiliser `input()` répété.

## Améliorations possibles

Arrêter le BFS dès que `E` est extrait de la file (au lieu de toujours vider toute la file) économiserait un peu de temps en pratique, sans changer la complexité dans le pire cas — non nécessaire ici vu la petite taille de grille (max 30×30×30), mais utile à savoir pour des grilles plus grandes.
