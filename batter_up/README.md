# batter_up

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `batterup`)*

Thème : Implémentation

## Résumé

Calculer la moyenne des valeurs positives ou nulles d'une liste, en ignorant les valeurs négatives.

## Idée

Filtrer la liste pour ne garder que les éléments `>= 0`, puis calculer la moyenne classique (somme divisée par nombre d'éléments restants).

Ça fonctionne parce que le problème demande explicitement d'exclure les scores négatifs du calcul de moyenne. Filtrer d'abord puis moyenner ensuite est le moyen le plus direct de respecter cette règle, sans avoir à suivre un compteur séparé pendant la lecture.

## Algorithme

1. Lire (et ignorer) la première ligne d'entrée.
2. Lire la liste de valeurs.
3. Filtrer les valeurs négatives.
4. Afficher la moyenne des valeurs restantes avec 9 décimales.

## Complexité

- Temps : O(n), n étant le nombre de valeurs.
- Mémoire : O(n) pour la liste filtrée.

## Difficultés rencontrées

Le format de sortie exige une précision fixe (`.9f`) : un simple `print(sum(a)/len(a))` ne suffirait pas si Kattis vérifie le nombre de décimales.

## Ce que j'ai appris

- `filter` + `lambda` est une façon concise d'exclure des éléments selon une condition simple.
- Le format `f"{x:.9f}"` garantit un nombre fixe de décimales, utile pour les problèmes à tolérance numérique stricte.

## Améliorations possibles

`list(filter(lambda x: x >= 0, a))` peut être remplacé par une compréhension `[x for x in a if x >= 0]`, plus lisible et sans `lambda`.
