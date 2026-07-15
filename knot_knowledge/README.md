# knot_knowledge

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `KnotKnowledge`)*

Thème : Recherche

## Résumé

Étant donné deux listes `Xi` et `Yi` de même taille, trouver le premier élément de `Xi` qui n'apparaît pas dans `Yi`.

## Idée

Parcourir `Xi` dans l'ordre et tester l'appartenance de chaque élément à `Yi` avec `in`, en s'arrêtant au premier élément absent.

Ça fonctionne parce que le problème demande explicitement le *premier* élément manquant selon l'ordre de `Xi` : un parcours séquentiel avec arrêt anticipé (`break`) donne directement la bonne réponse sans traitement supplémentaire.

## Algorithme

1. Lire `n` et les deux listes `Xi`, `Yi`.
2. Parcourir `Xi` par indice.
3. Pour chaque élément, vérifier s'il est absent de `Yi` avec `not in`.
4. Afficher le premier élément absent trouvé et arrêter.

## Complexité

- Temps : O(n²) dans le pire cas, car `Xi[i] not in Yi` est un test en O(n) sur une liste, répété jusqu'à n fois.
- Mémoire : O(n) pour stocker les deux listes.

## Difficultés rencontrées

`in` sur une `list` est linéaire : pour de grandes valeurs de `n`, la complexité quadratique peut devenir trop lente. Convertir `Yi` en `set` rendrait chaque test O(1) en moyenne.

## Ce que j'ai appris

- Le test d'appartenance `in` a un coût très différent selon le type de conteneur (`O(n)` pour une liste, `O(1)` en moyenne pour un `set`) : le choix de structure de données a un impact direct sur la complexité globale.

## Améliorations possibles

```python
n = int(input())
Xi = list(map(int, input().split()))
Yi = set(map(int, input().split()))
for x in Xi:
    if x not in Yi:
        print(x)
        break
```
Passe la complexité de O(n²) à O(n).
