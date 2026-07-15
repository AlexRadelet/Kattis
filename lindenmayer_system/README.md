# lindenmayer_system

[Lien vers Kattis](https://open.kattis.com/problems/lindenmayersystem)

Thème : Simulation

## Résumé

Étant donné un ensemble de règles de réécriture (un caractère → une chaîne de remplacement) et une chaîne de départ, appliquer ces règles simultanément à tous les caractères pendant `n` itérations, puis afficher la chaîne finale.

## Idée

Représenter les règles dans un dictionnaire `caractère → remplacement`, puis, à chaque itération, reconstruire la chaîne caractère par caractère en remplaçant chaque caractère par sa règle si elle existe, ou en le gardant tel quel sinon (`rules.get(c, c)`).

Ça fonctionne parce qu'un système de Lindenmayer applique ses règles en parallèle sur toute la chaîne à chaque étape (contrairement à une réécriture séquentielle où l'ordre des remplacements changerait le résultat) : construire la nouvelle chaîne en un seul passage sur l'ancienne, sans modifier `current` pendant qu'on le lit, respecte naturellement cette simultanéité. Utiliser un dictionnaire pour les règles donne un accès O(1) à la règle de n'importe quel caractère, ce qui est plus direct qu'une recherche linéaire dans une liste de règles à chaque caractère.

## Algorithme

1. Lire `r` (nombre de règles) et `n` (nombre d'itérations).
2. Lire les `r` règles au format `gauche -> droite` et les stocker dans un dictionnaire.
3. Lire la chaîne de départ.
4. Répéter `n` fois : reconstruire la chaîne en remplaçant chaque caractère par sa règle (ou lui-même si absent des règles).
5. Afficher la chaîne finale.

## Complexité

- Temps : O(n · L_max), où L_max est la longueur de la chaîne à la dernière itération (la longueur peut croître de façon exponentielle selon les règles, donc L_max peut devenir très grand rapidement).
- Mémoire : O(L_max) pour stocker la chaîne courante.

## Difficultés rencontrées

- Si une règle n'existe pas pour un caractère donné, il faut le conserver tel quel dans la chaîne de sortie plutôt que de le supprimer ou de lever une erreur — `dict.get(c, c)` gère ce cas par défaut de façon concise.
- La longueur de la chaîne peut croître très vite (exponentiellement selon les règles) : pour un `n` grand, la mémoire et le temps peuvent devenir un goulot d'étranglement, même si l'algorithme lui-même est linéaire par itération.

## Ce que j'ai appris

- `dict.get(clé, défaut)` est le moyen idiomatique de gérer une correspondance "remplacer si une règle existe, sinon garder tel quel" sans `if/else` explicite.
- Reconstruire une chaîne entière à chaque étape (plutôt que de la modifier en place) est nécessaire quand la transformation doit être simultanée sur tous les éléments, un pattern qu'on retrouve dans les automates cellulaires et les simulations de croissance.

## Améliorations possibles

Si le nombre d'itérations est grand et que seule la longueur finale de la chaîne est demandée (pas son contenu), il est possible de calculer la croissance de longueur par caractère avec de l'algèbre linéaire (une matrice de transition), évitant de construire la chaîne complète.
