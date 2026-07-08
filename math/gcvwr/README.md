# gcvwr

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `GCVWR`)*

## Résumé

Étant donné le poids nominal brut d'un véhicule (`G`), le poids à vide (`T`) et le poids de plusieurs passagers, calculer la charge de remorquage restante autorisée (90% de la capacité restante, moins le poids des passagers).

## Idée

Calculer 90% de la différence `G - T` (capacité utile du véhicule), puis soustraire le poids total des passagers.

Ça fonctionne parce que la règle du problème est directement une formule arithmétique : 90% de `(G - T)` représente la limite de charge autorisée, et chaque passager consomme une partie de cette capacité proportionnellement à son poids.

## Algorithme

1. Lire `G`, `T` et `N` (nombre de passagers, non utilisé directement dans le calcul car `sum` traite toute la ligne).
2. Lire et sommer les poids des passagers.
3. Calculer `9*(G-T)//10 - x` et l'afficher.

## Complexité

- Temps : O(N) pour lire et sommer les poids.
- Mémoire : O(1).

## Difficultés rencontrées

`9*(G-T)//10` utilise une division entière : pour calculer correctement 90% d'un entier sans passer par les flottants, multiplier par 9 avant de diviser par 10 (plutôt que diviser par 10 puis multiplier par 9) évite une perte de précision supplémentaire par arrondi.

## Ce que j'ai appris

- L'ordre des opérations (`9*(G-T)//10` vs `(G-T)//10*9`) change le résultat d'une division entière : multiplier avant de diviser garde plus de précision.

## Améliorations possibles

Aucune : la formule est déjà appliquée directement, sans calcul intermédiaire superflu.
