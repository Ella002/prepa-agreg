# 12/01 - 12. Stratégies algorithmiques (dont [...]) - Emmanuel



1) DPR

-> Illustration par tri fusion

autres exemples : tri rapide, sélection kème élément...

Introduction de la structure d'arbres



2) Algos gloutons et prog dynamique

 - Pour problèmes d'optimisation

Pour les gloutons, illustration: sac à dos. Pas de solution optimale en version entière, que en version fractionnaire

Propriétés :

   * sous-structure optimale
   * Choix glouton: il existe une méthode pour sélectionner une solution optimale
Exemples : Dijkstra, sélection d'activité (premier développement)



Programmation dynamique: si on a pas choix glouton, comment on résout ?

Prog dynamique = on résoud sous-problèmes, de plus en plus grands, jusqu'à avoir la solution.

Exemple: sac à dos entier, ou découpe de bar (???)



Développement 2: utilisation de programmation dynamique pour du calcul avec de l'incertain



qqch

Calcul descendant, nécessitant mémoïsation

Approche ascendante: on part des petits, et on construit les solutions des plus grands à partir de la résolution des petits



[Plan à continuer avec le retour sur trace]



Q (GD): Difficultés de la leçon :

   * C'est vaste, c'est difficile de savoir comment aller loin dans chacune
   * Les devt pratiques risquent d'être longs à coder (Gilles Dowek n'est pas d'accord)
   * GD : Il y a beaucoup de trucs, mais il n'y a pas beaucoup de livres qui donnent une définition précise de "diviser pour règner" (par exemple).
Q (GD): Comment les parer?

   * Jules: avoir un problème fil rouge (sac à dos?) qui permet d'illustrer les différentes techniques. GD: ça suffit pas, on peut pas illustrer une méthode générale avec un exemple => il faut plusieurs exemples pour chacun. Mais c'est bien d'en avoir un commun
GD: Qd on a un cas très général, on peut se demander si c'est possible de donner des propriétés uniformes sur tout ça.

   * Réduire la taille du problème (idée de diviser pour régner)
   * GD: "tous les algorithmes de la catégorie DPR on peut faire quelque chose de commun" -> calculer la complexité de résolution
       * (Hein?)
GD: à quoi ça sert ces stratégies à part calculer des trucs en commun?

C'est aussi un guide, des idées pour trouver des solutions et algorithmes.



=> solutions = un ensemble d'exemples bien choisis, des résultats généraux, un guide pour inventer de nouveaux algorithmes



GD : C'est quoi le "retour sur trace" ?

On va explorer l'arbre des possibles en revenant en arrière quand on a pas une solution

C'est la traduction française de "backtracking"



Emmanuel: Cormen exprime bien diviser pour régner, glouton et programmation dynamique, mais pas backtracking



GD: Y a un lien entre les 4?

   * explication similarités et différences
   * Entre glouton et dynamique le lien est que le glouton sait quel chemin prendre dans une décomposition dynamique. (NDLR) En gros ça pourrait être un dynamique avec un seul sous-appel
   * SG : Pour le DPR, une des différences c'est typiquement que les sous-problèmes sont indépendants, alors que ce n'est pas le cas dans un dynamique


(SG): Quel est l'intérêt de branch and bound par rapport à backtracking ? Paradigme proche de backtracking ? Qu'est-ce qu'on fait de plus?

   * En choisissant la bonne fonction, on peut élaguer des branches et s'éviter de tout explorer, gagnant en temps et en complexité


GD : De tous ces ensembles, lequel serait le plus général ? Dont les autres stratégies seraient des cas particuliers

   * Retour sur trace


GD : Oui, et j'aurais organisé le plan en commençant comme ça



GD : Laissons de côté diviser pour régner qui ne sert que quand on a des résultats indépendants. On a retour sur trace, comment on définit un algorithme glouton?

C'est l'algo où on explore qu'une branche.

=> on peut résoudre avec un algo glouton qui trouve une très mauvaise solution, mais au moins il est rapide.



GD: Comment tu définirais prog dyn par rapport à backtracking? Caractéristique de la prog dyn?

Mémoïsation => on se rend compte quand on retombe sur le même problème, et ne pas refaire le calcul



GD : Par contre DPR j'arrive plus difficilement à le classifier là-dedans



SG : On peut utiliser le glouton comme une borne dans le backtracking, et tout mélangeeeeeer \o/

Ça permet d'élaguer l'espace à explorer dans le backtracking. Exemple : dans le sac à dos, bornes avec le glouton fractionnaires



Quels développements intéressants?

Proposition Emmanuel: un sur les algos glouton, et un, pratique, introduction à la prog dyn

Remarque GD: deux choix ambitieux. Ok si on peut les préparer dans le temps imparti...

Quelles options plus simples?

=> développement pratique = n'importe quel algo DPR (tri, ...)

GD : Attention, tri rapide c'est pas un DPR le plus élémentaire

Deux types de DPR: division bête, mais reconstruction compliquée, ou division maline et reconstruction simple



/!\ toujours avoir sa botte du développement facile, comme filet de sécurité sous le trapèze volant



Tous algorithmes DPR ont propriété: n éléments, division en n/2 et n/2, coût résolution pour chaque division + coût reconstruction

=> développement théorique possible: théorème maître. Ou au moins une version plus simple / classique (version dans Berstel Beauquier Eléments d'algorithmique)

Le cas général est casse-gueule et il faut éviter d'essayer.



GD (à l'assemblée) : L'agreg c'est un problème d'optimisation compliqué : un truc trop trivial c'est pas très récompensé, mais se planter sur un trop trop compliqué c'est catastrophique. Il faut essayer de viser un truc qui soit epsilon en-dessous de la barre où vous vous plantez.
