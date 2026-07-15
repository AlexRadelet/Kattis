# finding_a

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `FindingAnA`)*

Thème : Chaînes de caractères

## Résumé

Afficher la sous-chaîne d'une chaîne donnée qui commence à la première occurrence du caractère `'a'`.

## Idée

Parcourir la chaîne caractère par caractère jusqu'à trouver un `'a'`, puis afficher tout le reste de la chaîne à partir de cette position (`s[i:]`).

Ça fonctionne parce que le slicing Python `s[i:]` extrait directement la sous-chaîne du premier `'a'` jusqu'à la fin, sans avoir à la reconstruire manuellement caractère par caractère.

## Algorithme

1. Lire la chaîne `s`.
2. Parcourir les indices de `s`.
3. Dès que `s[i] == "a"`, afficher `s[i:]` et arrêter.

## Complexité

- Temps : O(n) dans le pire cas (le `'a'` est en fin de chaîne, ou absent).
- Mémoire : O(n) pour la sous-chaîne affichée.

## Difficultés rencontrées

Si la chaîne ne contient aucun `'a'`, la boucle se termine sans rien afficher. Il faut vérifier si l'énoncé garantit la présence d'au moins un `'a'`, sinon un cas de sortie par défaut serait nécessaire.

## Ce que j'ai appris

- `str.index()` ou l'opérateur `in` permettent de trouver une sous-chaîne sans boucle explicite.

## Améliorations possibles

```python
s = input()
i = s.index("a")
print(s[i:])
```
Plus direct, mais lève une `ValueError` si `'a'` est absent — à garder tel quel si l'énoncé garantit sa présence, sinon combiner avec un `if "a" in s`.
