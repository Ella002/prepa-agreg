# 04/04 - 02. Paradigmes de programmations impératif, fonctionnel, objet - Maël #

Développements :

    - Fonction récursive ; récursive terminale ; dérécursivité ; passage par continuation

    - **Application de la POO pour l'addition d'une calculatrice <-- Choix du jury**



Rq : cf transparents de Xavier Leroy pour le Dev 1



## Développement ##



Dev: **Application de la POO pour l'addition d'une calculatrice**

Le but est de montrer que c'est pratique



**Objectif** : Être capable d'avoir des Expressions, calculer une expression et l'afficher.



Expression :

   * Constante
   * Triplet (Expression, op, Expression)


En prog fonc, on définirait un type abstrait et on aurait des fonctions d'évaluation



    def eval (expr) :

   * switch
       * case 'c':
           * return val
       * case '+':
           * return eval(ExprG) + eval(ExprD)


Le problème c'est que quand on veut rajouter des opérations, il faut rallonger le code...

Si cette fonction a été extremement testée mais qu'on a besoin de faire une modification, on devra transformer directement le code final. Est-ce qu'on a vraiment envie de faire ça ?



En POO, on pourrait définir une seule classe Expression qui reprend le type abstrait et la manière de penser



class Expression :

        - valeur

        - ExpressionG

        - ExpressionD

        - Operation



En fait c'est mieux de faire quelque chose de plus modulaire

On définit une classe abstraite

   * `Expression`
   *     - `eval()`
   *     - `print()`
Puis deux sous-classes:

   * `Constante`
       * - valeur
       * - `eval()`
       * - `print()`
   * `ExpressionBinaire`
       * - `exprG`
       * - `opp`
       * - `exprD`


Et on peut même plutôt faire une ExpressionBinaire abstraite, dont chaque opération (addition, soustraction, etc) est une sous-classe

Avantages:

    On a une vision globale de l'architecture du projet avant même d'écrire le code

    On peut modifier l'affichage en modifiant simplement les fonctions d'affichage des différentes classes

    On va aussi pouvoir tester indépendemment nos fonctions pour un module donné.

    Si on veut rajouter une option (racine, log, ...) il suffit de rajouter une nouvelle classe qui serait une expression linéaire. On pourrait faire cela sans modifier le code initial.



Exemple plus concret qu'une calculatrice: outil permettant de calculer des orbites spatiales, où y a plusieurs méthodes possibles, et on fait en sorte que la personne spécialisée d'un domaine vienne écrire la méthode de ce domaine: tant que la méthode suit la classe abstraite des méthodes, il n;y a pas besoin de maîtriser ou modifier le reste du code.



[Le développement n'est pas très long]



## Questions ##



### Sur le développement ###



Q: En programmation, la présentation initiale correspond à l'implementation fonctionnelle. Quel serait le type des expressions ?

Q: En OCAML par exemple.

R: Ce serait un type abstrait, personnalisé.

R  (Jury): ça s'appelle un type somme en l'occurence, type algébrique de manière générale



Q: Si on rajoute des expressions unaires, je dois rajouter un constructeur ?

R: Oui, je rajoute un constructeur dans un type.



Q: A chaque case, au lieu d'écrire du code, je pourrais aussi faire un appel à une sous fonction pour diviser le code.

R: Oui, on pourrait rajouter une sous-fonction. Mais dans ce cas, la sous-fonction eval sera accessible a l'entièreté du code alors que dans la programmation objet, on peut aussi choisir la visibilité.



Q: Sur la notion de tests, pour tester plus, on peut on peut le faire sasn tester const. / on ne peut pas tester plus sans tester const

R: oui.

Q: du coup, pour séparer les tests?

R: on peut tester plus sans tester fois, une fois qu'on a testé const.



Q: ?

R: On gagne du temps car les attributs sont réutilisés dans la sous-classe, de même que les méthodes.



Q: l'utilisation d'eval dans toutes les classes, c'est un design pattern, lequel? [NDY: c'est très pas au programme ça]

R: Euuuuuuuuh.

R-Q (Jury) : C'est le pattern de visiteur. Qui est un peu plus générique que ça, vous avez un exemple ?

R (Yaëlle): c'est quand les carnivores du zoo ils ont leur propre fonction mangerViande

R (jury): c'est un patron de développement basé sur le parcours de l'ensemble de la structure

Q: Comment on généralise sur des structures qui ont besoin de passer la main à d'autres morceaux ?

R: ... [NDManet moi non plus j'ai rien compris]











### Sur le plan ###



Q: Si je prend Python, c'est impératif, fonctionnel, ... ?

R: Multi-paradigme.

Q: on s'abstrait de la notion d'état ?

R: On garde le contexte, on n'a pas de vraie fonction [pure].



[*Questions confuses*]

R: La portée d'une fonction est seulement limitée à ses paramètres, alors qu'une procédure peut accéder à des variables globales, etc...



Q: Un identificateur, c'est quoi la différence entre les deux paradigmes impératifs et fonctionnels ?

R: X dans un langage impératif, fait référence à une case mémoire définie et X dans un langage fonctionnel va être associé définitivement à une valeur



Q: En impératif, pour répéter du code, on a des boucles while qui travaillent jusqu'à ce que la mémoire aie changé

R: En fonctionnel, on joue sur la pile des appels

Q: Elle est où cette pile ?

Q: Quand vous exécutez une fonction en impératif et en fonctionnel il ne se passe pas la même chose : en impératif vous allez chercher des trucs dans la mémoire, en fonctionnel dans l'environnement.

R: Un appel à une fonction crée un nouvel environment existant uiquement lors de l'éxécution de la fonction.



Q: Qui s'occupe de la pile ? C'est vous ? Et en impératif, il n'y a pas de pile ?

R: Si, mais



Q: En paradigme objet, c'est quoi les trucs plus compliqués qu'une calculette ?

R: On a vu l'héritage [...] où on a au moins la même chose ; C'est possible d'hériter de plusieurs classes mais ça devient plus...

Q: C'est pas difficile dans ces cas complexes de donner du sens à tout ça (avec multi-héritage et redéfinitions) ?

R: Si



Q: C'est possible en Python ?

R: Oui, il y a une règle bizarre pour savoir quand il y a plusieurs solutions

Rq (Jury): non c'est pas bizarre, c'est *très* bizarre.



## Remarques ##



### Sur le développement ###



### Sur le plan ###



Rq: Vous avez dit que l'impératif c'était bien parce que c'est accessible à des non-informaticien·ne·s...

Q: Pouvez-vous me citer un langage très utilisé qui n'utilise que de l'impératif et pas de fonctionnel ?

R: C

R: Ce que je voulais dire, c'est que c'est plus facile pour quelqu'un·e dont c'est pas le corps de métier de faire un script impératif que de chercher

Rq: oui pour 10 lignes mais pas pour 50 lignes. Et en vrai les gens font du R [NDManet et du Excel] qui est fonctionnel.



Rq: Une des propriétés de l'objet c'est d'attacher les méthodes (donc le fonctions) aux objets



Rq: Un truc assez important de ce sujet c'est que les mécanismes d'exécution sont très différents et ça n'apparaît pas assez



### Générales ###



Rq: Si on n'est pas capable de présenter un développement, il ne faut pas le proposer car cela mettrait fin immédiatement à la leçon, il vaut mieux faire moins que d'être bloqué.



Rq: Ne pas dire que l'objet est indispensable pour les gros projets sous peine de vexer la partie du jury qui ne programme pas en objet.



Rq : Il faut creuser un peu plus, en objet il aurait fallu citer le "pattern visiteur" et savoir répondre aux questions ; en fonctionnel parler d'ordre supérieur...



Rq : Fonctionnel = variables non mutables



Un dessin qui fonctionne bien c'est :

    (identificateur)    (valeur)     (mémoire)

et en fonctionnel on n'a que les deux premiers
