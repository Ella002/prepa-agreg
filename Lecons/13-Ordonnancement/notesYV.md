# 13/06 - 13. Algorithmes d’ordonnancement de tâches et de gestion de ressources. - Yaëlle #

## Plan ##

1. Algo d'ordonnancement

	1. Introduction

    2. Sur un système par lots

    3. Sur un système interactif

    4. Sur un système temps-réel

2. Gestion de la mémoire

    1. Mémoire virtuelle

    2. Algo optimal

    3. Algo basé sur les pages de travail



## Développement ##

- Différents algo d'ordonnancement sur un exemple
- **algo de remplacement avec pages de travail** <- choisi par le jury

I)pages de travail simple

Pages de travail: w(k,t)={ensemble des pages accédés sur les k dernières références à l'instant t}

registre à décalage de k cases [...] >> [nouvelle | ...]
couteux à maintenir
-> notion basée sur le temps d'exécution
tau : w(tau,t) ={pareil sur les tau dernieres ms}

[exemple sur trois pages avec annotations différentes]

Page 2 : temps 1213, ref = 0 [page supprimée]
Page 1 : temps 2084 [passe à 2204], ref=1
Page 0 : temps 1620, ref = 0

temps actuel = 2204, tau = 600
d'abord page 0 sélectionnée pour suppression, car pas modifiée




II) page de travail en horloge

```
   1620, 0 ---------> 2020, 1
        ^                          |
        |                           |
        |                           |
   1213, 0  <--------- 2014, 1 <--/--
       ^
       ||
```


## Questions ##

Q:pourquoi le temps c'est  mieux que le nombre?
Dans le registre à décalage, on met à jour à chaque modification des pages, mais pour la table, on modifie les dates au moment de l'exécution de l'algo d'éviction.


Q : À quoi sert le sens de l'horloge. Il va y avoir des opérations anti-horaires ?
R : Non, mais ça indique l'ordre à faire. Et le sens sert à l'insertion

[Rq]SF : Reprendre des choses du développement 1 pour le 2 ? Pour éviter 40 min du questions.
R :

### Plan ###

Q : Vous avez marqué qu'il n'y avait qu'un seul processeur. Est-ce très moderne ?
R : Non, mais ça se généralise.

Q : On a l'impression que tous les processus sont indépendants. Sinon, qu'est-ce qui se passe ?
R : On a un graphe de dépendance
Q : et comment ça marche ?
R : Je pense que c'est compliqué, et je ne connais pas d'algorithme
RJury : je pense que ça peut se rapprocher de la leçon d'avant sur les algos gloutons, etc

Q : Sur l'ordonancement par priorité, c'est quoi le domaine des priorités ?
R : Ça dépend du système. En [...], il y a les processus utilisateurs, ceux de l'OS...

Q : quand on parle de deux processus qui ont besoin de communiquer, c'est quoi l'impact des priorités dessus ?

R : Bah quand un processus attend un autre, on va augmenter la priorité du dépendu

Q : Mais qui gère les priorités ?

R : C'est l'OS qui décide, mais on peut avoir des priorités localement

Q : et ça n'a pas d'impact sur le domaine des priorités ?
RJury : on voit du coup qu'il y a des priorités qui ne doivent pas être accessibles par d'autres gens que l'OS.

Q : Vous avez mis "ordonnancement temps-réel", vous pouvez préciser ?
R : Bah il y a une différence entre les problèmes interactifs, et ceux pour lesquels il y a des deadlines
Q : et en cas de dépassement ?
R : ça dépend des systèmes, certains suppriment, d'autres essayent de minimiser
Q : Vous connaissez une implémentation de temps réel ?
R : Euh, bah on a un algo ici... un exemple qui peut exister, c'est sur un système qui traite les données d'un capteur, l'intérêt est de traiter les données avant de recevoir les suivantes
RJury : [truc sur VMZenith..?]


## Remarques ##

[RdManet : j'adore ta couleur de surlignage @Thomas]
[Rdthomas: c'est un algo d'eviction de cache son dev ou bien j'ai rien compris?]

Rq : Au moment où le Tanenbaum est sorti j'avais pas de cheveux blancs, c'est dire !

Rq : Mieux spécifier les algos du développement.
