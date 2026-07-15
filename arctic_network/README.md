# arctic_network

[Lien vers Kattis](https://open.kattis.com/problems/arcticnetwork)

Thème : Graphes (arbre couvrant minimal, Union-Find)

## Résumé

Relier P avant-postes entre eux, sachant que S canaux satellites peuvent connecter n'importe quelle paire d'avant-postes gratuitement (distance illimitée) ; pour toutes les autres liaisons, il faut poser des câbles dont la longueur est la distance euclidienne. Minimiser la plus longue liaison câblée nécessaire.

## Idée

Construire l'arbre couvrant minimal (MST) du graphe complet où chaque avant-poste est un nœud et chaque arête pèse la distance euclidienne entre deux avant-postes. Les `S` satellites permettent de remplacer gratuitement les `S-1` arêtes les plus longues du MST (elles "fusionnent" `S` composantes sans câble) : la réponse est donc la plus longue arête restante, c'est-à-dire la `S`-ième plus grande arête du MST.

Ça fonctionne parce qu'un MST minimise déjà la somme des longueurs de câble nécessaires pour connecter tous les avant-postes — et retirer ses `S-1` arêtes les plus longues (en les remplaçant par du satellite) est la façon optimale de réduire la plus longue arête restante : retirer n'importe quelle arête plus courte laisserait une arête plus longue non couverte, ce qui serait pire. Un algorithme de Kruskal est le choix naturel ici : il construit le MST en ajoutant les arêtes par ordre croissant de poids, ce qui donne directement la liste triée dont on a besoin pour identifier les arêtes les plus longues.

## Algorithme

1. Lire le nombre de cas de test `T`.
2. Pour chaque cas : lire `S` (satellites) et `P` (avant-postes), puis les coordonnées des avant-postes.
3. Si `S >= P`, tous les avant-postes peuvent être connectés par satellite : afficher `0.00`.
4. Sinon, générer toutes les arêtes possibles (distance euclidienne entre chaque paire), les trier par poids croissant.
5. Construire le MST avec Kruskal (Union-Find), en s'arrêtant dès que `P-1` arêtes ont été ajoutées.
6. Afficher la `S`-ième plus grande arête du MST (`mst[-S]`), avec 2 décimales.

## Complexité

- Temps : O(P² log P) par cas de test — dominé par la génération des O(P²) arêtes et leur tri.
- Mémoire : O(P²) pour stocker toutes les arêtes.

## Difficultés rencontrées

- Le cas `S >= P` doit être traité à part : dès qu'il y a au moins autant de satellites que d'avant-postes, aucun câble n'est nécessaire, et tenter de calculer `mst[-S]` sur une liste plus courte que `S` provoquerait une erreur d'index.
- Comprendre pourquoi la réponse est `mst[-S]` et non `mst[-(S-1)]` ou `mst[-1]` demande de bien visualiser que les satellites remplacent des *arêtes*, pas des *avant-postes* : `S` satellites couvrent au plus `S-1` arêtes du MST (un satellite à lui seul ne remplace rien, il faut le combiner à un autre point déjà connecté ou à un autre satellite).

## Ce que j'ai appris

- Le pattern « Union-Find avec compression de chemin » (`find` récursif qui réattache directement à la racine) est la structure de référence pour Kruskal et pour tout problème de connectivité dynamique par fusion de composantes.
- Un problème de "minimiser la plus longue arête" sur un graphe connexe se ramène très souvent à un MST : c'est une propriété classique (le MST minimise aussi le maximum de ses arêtes parmi tous les arbres couvrants possibles, pas seulement leur somme).

## Améliorations possibles

Pour un très grand nombre d'avant-postes, générer O(P²) arêtes devient trop coûteux ; des structures comme un arbre KD ou une triangulation de Delaunay permettent de ne considérer qu'un sous-ensemble d'arêtes candidates garanties de contenir le MST, ramenant la complexité à O(P log P).
