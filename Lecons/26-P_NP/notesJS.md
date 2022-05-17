# 26/01 - 26. Classes P et NP. Problèmes NP-complets. Exemples. - Jules #

Développements:

   * 2-SAT est P
   * NP-complétude de clique-cover
   * **3/2 approximation du problème du voyageur de commerce (algo de Christofidès) <- choisi par le jury**


## Développement ##



## Questions et remarques ##



Sur quels documents Jules s'est appuyé pour préparer la leçon ?

-> Cormen et ? -> cf moodle



Pourquoi ces exemples ?

-> Ce sont des exemples qui permettent une belle progression dans la leçon + Tout dans la même source ;)

-> Exemple des graphes réutilisables pour d'autres leçons



Les problèmes de réductions polynomiales permettent de donner des bornes inf sur des complexités de problèmes, d'autres méthodes ?

-> Typiquement, sur le tri par comparaison, on peut montrer une borne inférieure en \Theta(n log(n)) ; [NDLR : De manière générale, la réponse serait "la théorie de l'information" qui permet de donner des bornes inférieures]



Est ce que vous savez autre chose sur la structure de la classe NP ?

-> Soit on répond par un théorème soir on répond par un problème selon le jury

-> Exemple : Factorisation d'entiers (?)



Si P = NP, la notion de NP-complétude que vous avez présenté, qu'est ce qu'elle devient ?

-> Avec la définition choisie, on ne peut rien sauver. Car ce sont des réductions polynomiales, et donc tout devient trivial si P=NP. Mais avec des réductions LOGSPACE par exemple, on peut sauver des choses. [??]



[Problèmes P-complets ??]

-> L'intuition qu'on a sur les problèmes P-complets c'est qu'il sont dur à paralléliser [contrairement à la prise de notes] ^^



(Pouvez-vous citer un problème qui est naturellement co-NP

-> La preuve qu'un nombre n'est pas premier c'est juste exposer un diviseur, c'est facile de voir que c'est dans co-NP. Bon ajd on sait que c'est dans P, mais c'est un bon exemple de truc qui est plus facile de montrer être dans co-NP que dans NP



[??]

-> Candy Crush (ie est-ce qu'on peut exploser un bonbon en particulier) est NP-complet



Est-ce que vous connaissez d'autres versions de SAT qui sont dans P ?

-> HORN-SAT est P-complet



Remarques sur le plan :

- la troisième partie est un peu une liste de problèmes, on aurait pu par exemple parler des concepts de barrière d'approximation, etc.

- Mentionner l'existence des SAT solvers, des solutions probabilistes, etc.

- Attention, bien penser à tout écrire dans l'intro car, le jour de la soutenance, on ne "pensera" pas à ajouter autre chose. (éviter les "je dirai ça à l'oral" sur l'intro/ouverture)
