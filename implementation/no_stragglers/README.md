# no_stragglers

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `NoStragglers`)*

## Résumé

Suivre des groupes de personnes qui entrent (`IN`) et sortent (`OUT`) d'un lieu, et déterminer combien de personnes restent à l'intérieur une fois tous les évènements traités.

## Idée

Maintenir un compteur `SUM` : ajouter le nombre de personnes à chaque évènement `IN`, le soustraire à chaque évènement `OUT`. À la fin, `SUM` représente le nombre net de personnes restantes.

Ça fonctionne parce que chaque évènement modifie le nombre de personnes présentes de façon indépendante et additive : il n'est pas nécessaire de savoir *qui* est entré ou sorti, seulement le solde net, donc un simple compteur suffit (pas besoin de structure pour suivre les identités).

## Algorithme

1. Lire le nombre d'évènements `N`.
2. Pour chaque évènement, lire la personne (non utilisée), la direction et le nombre de personnes concernées.
3. Ajouter ou soustraire ce nombre à `SUM` selon la direction.
4. Si `SUM == 0`, afficher `NO STRAGGLERS`, sinon afficher `SUM`.

## Complexité

- Temps : O(N).
- Mémoire : O(1).

## Difficultés rencontrées

Le champ `person` est lu mais jamais utilisé : il fait partie du format d'entrée sans influencer le calcul. Facile d'oublier de le lire, ce qui désalignerait le parsing des colonnes suivantes.

## Ce que j'ai appris

- Quand un problème ne demande qu'un solde net, un compteur unique suffit ; pas besoin de structures pour modéliser des entités individuelles si leur identité n'intervient pas dans le résultat.

## Améliorations possibles

Aucune : la solution est déjà linéaire et minimale en mémoire.
