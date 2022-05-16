# 05-10 - 11. Exemples d’algorithmes d’approximation et d’algorithmes probabilistes - Axel #



Candidat : Axel Kugelmann

Jury : Serge Haddad, Marc Lelarge



Plan :

   1. Algorithmes d'approximation
       1. Définition
       1. 2-approximation du problème d'ordonnancement
       1. 2-approximation du problème du sac à dos
       1. 2-approximation de Vertex-Cover par relaxation linéaire [DEV] (numéroté 1.3 sur le manuscrit)
   1. Algorithmes probabilistes
       1. Algorithmes de Las Vegas
       1. Algorithmes de Monte Carlo [DEV]
   1. Conclusion et ouvertures
       1. Algorithmes d'approximation
       1. Algorithmes probabilistes


Développements :

   * **2-approximation de Vertex-Cover par relaxation linéaire <-- eeeeeeh zébardiiiii**
   * Preuve zero-knowledge d'identité


## Développement ##



On veut couvrir toutes les arêtes, avec le moins de sommets possibles.



## Questions ##







SH: la relaxation est résoluble en temps poly, comment?

C'est une forme générale, méthode de l'ellipsoïde

SH : Polynomial, c'est quoi le degré ?

R : Jsp mais c'est pas beau. Et en pratique on fait du simplexe, c'est exponentiel en pire des cas mais très rapide en pratique

RSH : oui très bien, en vrai

SH: en fait le pb de vertex cover c'est de la programmation linéaire à valeurs entières (ILP). Quand est-ce que la ILP est polynomiale.

R: Jsp, la prog linéaire est totalement hors-programme

RSH: quand la matrice induite est totalement unimodulaire, id est a toutes ses sous-matrices qui ont det 0,1 ou -1.





QML : pour l'exemple 1 (la fleur), vous pouvez expliquer pourquoi c'est ça la solution ?

R : Pour le discret, je l'ai construit pour que ça soit facile de le montrer. [le fait]

Pour le continu, on peut montrer que le problème général a toujours une solution à valeurs dans {0, 0.5, 1}. Alors on discrimine selon le centre de la fleur, et c'est facile à montrer.



SH: tu connait une approximation très simple?

R:oui on prends les 2 extremités d'une arête non couverte jusqu'à obtenir une couverture.





R : La méthode est un peu plus générale que le problème, on peut par exemple mettre des poids sur les sommets et minimiser ça

QSH : Alors justement j'allais poser la question



QSH : Sur le plan : tu dis que les approx c'est pour les problèmes NP-complets

R : Oui mais en fait pas que

Q : T'as un exemple ? Linéaire peut-être

R : Oui, la sélection de la médiane / du k-ième est linéaire mais il y a un algo probabiliste beaucoup plus simple











## Remarques ##

/!\ attention à l'orthographe



SH: très bon développement



ML : Pour le devt, t'aurais pu introduire la notion de coût à part [mdr c'est la même remarque que moi pour mon plan]



SH : C'est marrant, toutes tes approximations sont non-optimales



SH: il faudrait parler de dérandomisation.
