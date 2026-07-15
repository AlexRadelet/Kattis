# rating_problems

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `RatingProblems`)*

Thème : Mathématiques

## Résumé

Sur `n` notes attendues dont seulement `k` sont connues (chacune entre -3 et 3), calculer la moyenne minimale et maximale possible une fois les `n-k` notes restantes prises en compte.

## Idée

Si toutes les notes sont connues (`k == n`), la moyenne est fixée. Sinon, les `n-k` notes manquantes peuvent chacune valoir au minimum -3 et au maximum 3 : la moyenne minimale s'obtient en supposant qu'elles valent toutes -3, la moyenne maximale en supposant qu'elles valent toutes 3.

Ça fonctionne parce que la moyenne est une fonction monotone de chaque note individuelle : pour minimiser (resp. maximiser) la moyenne, il faut minimiser (resp. maximiser) chaque note inconnue indépendamment, donc les mettre toutes à leur extrême.

## Algorithme

1. Lire `n` (nombre total de notes) et `k` (nombre de notes connues).
2. Lire les `k` notes connues.
3. Si `k < n` : calculer la moyenne min/max en ajoutant `-3*(n-k)` ou `3*(n-k)` à la somme connue, divisé par `n`.
4. Si `k == n` : afficher deux fois la moyenne exacte.

## Complexité

- Temps : O(k) pour lire et sommer les notes.
- Mémoire : O(k) pour stocker les notes.

## Difficultés rencontrées

Le programme ne stocke `notes` que pour calculer `sum(notes)` : la liste elle-même n'est jamais relue individuellement, donc un simple accumulateur suffirait.

## Ce que j'ai appris

- Pour une moyenne à bornes extrêmes, il suffit de raisonner sur la somme totale plutôt que sur chaque combinaison de notes possibles : borne min/max de la somme, puis diviser.

## Améliorations possibles

Accumuler la somme directement pendant la lecture, sans construire la liste `notes` :
```python
n, k = map(int, input().split())
total = sum(int(input()) for _ in range(k))
if k < n:
    print((total - 3*(n-k)) / n, (total + 3*(n-k)) / n)
else:
    print(total / n, total / n)
```
