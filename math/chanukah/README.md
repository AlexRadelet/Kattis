# chanukah

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `chanukah`)*

## Résumé

Pour chaque cas de test, calculer le nombre total de bougies allumées sur `num_of_dates` nuits de Hanoucca, sachant que la dernière nuit on allume une bougie supplémentaire (le chamash compte deux fois ce soir-là).

## Idée

Sommer 1 + 2 + ... + `num_of_dates` (une bougie de plus chaque nuit), puis ajouter une bougie supplémentaire pour la dernière nuit.

Ça fonctionne parce que la règle de Hanoucca est : nuit `j`, on allume `j` bougies (plus le chamash, compté une fois de plus la dernière nuit dans ce modèle). Faire la somme progressivement nuit par nuit, plutôt que d'utiliser directement la formule `n(n+1)/2`, rend la règle spéciale de la dernière nuit facile à greffer sans risquer une erreur de calcul.

## Algorithme

1. Lire le nombre de cas de test.
2. Pour chaque cas : lire le numéro du cas et le nombre de nuits.
3. Sommer `1 + 2 + ... + num_of_dates`, avec un `+j` supplémentaire à la dernière itération.
4. Afficher le numéro du cas et le total.

## Complexité

- Temps : O(num_of_dates) par cas de test.
- Mémoire : O(1).

## Difficultés rencontrées

Le `if j == num_of_dates: s += j` à l'intérieur de la boucle est facile à mal placer (avant/après le `s += j` principal) ; ici il s'exécute bien après l'ajout normal, donc la dernière nuit compte double comme voulu.

## Ce que j'ai appris

- Une somme `1 + 2 + ... + n` peut se calculer directement avec `n*(n+1)//2`, ce qui évite la boucle.

## Améliorations possibles

Version O(1) par cas de test :
```python
s = num_of_dates * (num_of_dates + 1) // 2 + num_of_dates
```
Utile si `num_of_dates` peut être très grand.
