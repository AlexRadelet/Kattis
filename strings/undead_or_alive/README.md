# undead_or_alive

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `undeadOrAlive`)*

## Résumé

Classer un message selon la présence des émoticônes `:)` et `:(` : les deux présents (`double agent`), seulement `:)` (`alive`), seulement `:(` (`undead`), ou ni l'un ni l'autre (`machine`).

## Idée

Tester la présence des deux émoticônes avec l'opérateur `in`, en testant d'abord le cas où les deux sont présentes (le plus spécifique), puis chaque cas restant.

Ça fonctionne parce que les quatre catégories sont mutuellement exclusives et couvrent tous les cas possibles : tester le cas combiné en premier évite qu'il soit masqué par les tests individuels (si on testait `:)` seul en premier, un message contenant les deux émoticônes serait classé à tort comme `alive`).

## Algorithme

1. Lire la chaîne `s`.
2. Si elle contient à la fois `:)` et `:(` : afficher `double agent`.
3. Sinon si elle contient `:)` : afficher `alive`.
4. Sinon si elle contient `:(` : afficher `undead`.
5. Sinon : afficher `machine`.

## Complexité

- Temps : O(n), n étant la longueur de `s` (chaque `in` est linéaire).
- Mémoire : O(1) en plus de la chaîne d'entrée.

## Difficultés rencontrées

L'ordre des tests est important : tester `:)` seul avant le cas combiné donnerait une réponse incorrecte pour un message contenant les deux émoticônes. Le code actuel teste bien le cas combiné en premier.

## Ce que j'ai appris

- Quand des conditions se chevauchent, il faut toujours tester le cas le plus spécifique (l'intersection) avant les cas plus généraux.

## Améliorations possibles

Aucune : la logique est déjà claire et l'ordre des conditions est correct.
