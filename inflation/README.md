# inflation

[Lien vers Kattis](https://open.kattis.com/problems/inflation)

Thème : Recherche (recherche binaire sur la réponse)

## Résumé

Étant donné `n` ballons de capacités `1, 2, ..., n` et `n` bonbonnes d'hélium de quantités données, associer à chaque ballon exactement une bonbonne (sans jamais dépasser sa capacité, sous peine d'explosion), en maximisant le taux de remplissage minimal garanti sur tous les ballons. Afficher ce taux, ou `impossible` si aucune association ne fonctionne.

## Idée

Combiner deux techniques : une **recherche binaire sur la réponse** (le taux de remplissage minimal `x`, un réel entre 0 et 1) et une **vérification gloutonne de faisabilité** pour un `x` donné (`can_fill`).

Pour un `x` fixé, `can_fill` trie les bonbonnes par quantité croissante, puis traite les ballons par capacité croissante (1, 2, ..., n) : pour chaque ballon, il prend la plus petite bonbonne encore disponible dont la quantité est `>= x * capacité` (assez pour atteindre le taux visé). Si cette bonbonne dépasse la capacité du ballon, elle le ferait exploser : infaisable. S'il n'y a plus de bonbonne disponible : infaisable.

Ça fonctionne parce que la fonction "x est-il atteignable ?" est monotone : si un taux `x` est faisable, tout taux inférieur l'est aussi (on peut toujours se permettre moins) — cette monotonie est exactement ce qui autorise une recherche binaire sur `x` plutôt qu'un essai exhaustif. La stratégie gloutonne (traiter les ballons du plus petit au plus grand, leur assigner systématiquement la plus petite bonbonne suffisante) est optimale par un argument d'échange : réserver les grandes bonbonnes pour les grands ballons ne peut jamais nuire, puisqu'une bonbonne trop grande pour un petit ballon le ferait exploser, alors qu'elle reste utilisable pour un ballon plus grand.

## Algorithme

1. Lire `n` et les quantités d'hélium, les trier par ordre croissant.
2. Vérifier que `x = 0` est faisable (sinon, aucune association ne respecte les contraintes de capacité même sans exigence de remplissage : afficher `impossible`).
3. Recherche binaire sur `x` entre `0.0` et `1.0` (60 itérations, largement suffisant pour la précision demandée) : à chaque étape, tester `can_fill(mid)` et resserrer l'intervalle du côté faisable.
4. Afficher la borne inférieure convergée avec 10 décimales.

## Complexité

- Temps : O(n log n) pour le tri, puis O(60 · n) pour la recherche binaire (chaque appel à `can_fill` est O(n) grâce au pointeur `index` qui ne recule jamais) — dominé par O(n log n).
- Mémoire : O(n) pour la liste triée des bonbonnes.

## Difficultés rencontrées

- Le cas `x = 0` doit être testé à part avant de lancer la recherche binaire : si même un remplissage nul n'est pas assignable sans faire exploser un ballon (une bonbonne trop grande pour toute capacité restante), la réponse est directement `impossible`, indépendamment de toute optimisation du taux.
- Le nombre d'itérations de la recherche binaire (60) est choisi empiriquement pour garantir la précision de sortie demandée (10 décimales) sur l'intervalle `[0, 1]` — un nombre trop faible tronquerait la précision.
- Comprendre pourquoi le pointeur `index` dans `can_fill` ne recule jamais (avance de façon monotone) est la clé de la complexité O(n) par appel : la fonction dépend implicitement du fait que le tri croissant des bonbonnes garantit qu'une bonbonne "sautée" pour un ballon ne peut jamais redevenir utile pour un ballon suivant plus grand.

## Ce que j'ai appris

- **Recherche binaire sur la réponse** : quand la question « x est-il atteignable ? » est monotone en `x`, on peut chercher la meilleure valeur de `x` par dichotomie même si `x` est un réel, en fixant un nombre d'itérations plutôt qu'une condition d'arrêt exacte.
- **Argument d'échange glouton** : trier les deux côtés (ballons par capacité, bonbonnes par quantité) et les apparier dans le même ordre est une stratégie gloutonne classique pour ce type de problème d'appariement sous contrainte.

## Améliorations possibles

Aucune : la complexité est déjà quasi optimale (le tri initial est incontournable, et la recherche binaire ajoute un facteur logarithmique négligeable en pratique grâce au nombre fixe d'itérations).
