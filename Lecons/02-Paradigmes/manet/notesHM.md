# 23/05 - 2. Paradigmes de programmation : impératif, fonctionnel, objet. Exemples et applications - Hugo #

Candidat : Hugo Manet

Jury : Sylvain Schmitz, Jean-Jacques Levy


Plan :

1. Paradigme impératif

2. Paradigme fonctionnel

3. Paradigme objet


Développements :

- Compilation de fonctions d'ordre supérieur

- Implémentation de méthodes virtuelles en C <- Choisi par le jury



## Développement ##

Explication du principe basé sur le schéma du plan

Montrage du code



## Questions ##

Q  :

R  : Les problèmes mentionnés sont des problèmes très concrets d'alignement, mais dans d'autres langages comme python l'alignement n'existe pas trop. Mais il y a des problèmes sur des diagrammes d'héritage plus grands [schéma du problème du diamant en héritage].

C'est un problème assez fondamental, et les langages ont différentes manières de le résoudre (par exemple, python définit un ordre précis et prend le premier qui marche). En C++ on fait un héritage virtuel, i.e. on fait un pointeur virtuel au lieu de mettre l'objet dans la même structure.



Q : Vous avez dit que Java vous avez l'héritage multiple. Il me semblait que c'était caché et que c'était que de l'héritage d'interfaces.

R : Je ne connais pas Java

### Plan ###

Q : Paradigme fonctionnel, vous avez dit que c'est map-reduce, que c'est pour faire des maths ? Il manque le fait que l'ordre d'évaluation est arbitraire donc permet de faire du parallélisme, une présentation dans ce sens irait mieux.

R : Oui



Q : La transparence référentielle, ca veut dire que l'évaluation ne dépend pas de l'environnement. Pourtant, on peut définir une sous fonction avec des arguments par exemple.

R : Les valeurs utiles de la fonction seront fixées à la création de la fonction en calculant sa fermeture. On ne dépend pas des définitions après la fonction.



Q : Tu as dit isomorphisme de Curry-Howard, qu'est-ce que c'est ?

R : J'ai ouvert une boite de Pandore. Décrit la curryfication [c'est pas ça mdr]



Q : Je fais du Ocaml. Est-ce que c'est un langage fonctionnel ? Quels sont les langages fonctionnels

R : Il faut différencier langage et paradigme. Un langage fonctionnel va guider l'utilisateur à utiliser un paradigme fonctionnel. On citera le lambda calcul, Haskell, ...



Q : Stratégies d’évaluation des fonctions ?

R : C’est compliqué en haskell, par ex l’évaluation paresseuse



Q : En objet, permet de mettre de la modularité. Mais c’est quoi la grande différence entre impératif et objet ?

R : Objet plus strict sur possession des méthodes et variables. Encapsulation des données

-> [J-J Levy] prog objet : guidée par les données, impératif : guidée par le programme



## Remarques ##

RJJL: il faut appuyer pourquoi le this est coloré en c++ et pas en c.

RJJL: il aurait fallu executer le  C++.

RSS: il  aurait fallu partir du code C++ puis le schema puis la traduction en C.

Reste un peu trop dans les détails, préférerait une présentation plus synthétique

Implémentation qui marche c’est bien

* Curry-Howard c’est isomorphisme entre les preuves et les programmes
* Bien d’avoir fait les 3 paradigmes, on pourrait en ouverture évoquer d’autres paradigmes (par ex la prog logique)
