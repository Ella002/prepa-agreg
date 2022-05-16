# 24/11 - 5. Implémentations et applications des piles et des files [Fanny]



Développements :

   1. Balayage de Graham (application de pile) **<- choisi par le jury**
   1. File de priorité / Tas binomiaux


## Développement : balayage de Graham

### Présentation tableau



Concept du balayage de Graham: étant donné des points en coordonnées cartésiennes, on cherche l'enveloppe convexe de l'ensemble de point.

Intérêt de la pile: on part d'un point, et on empile les autres en fonction de leur angle



### Présentation code



Code Python :

   * classe Pile, avec la pile sous forme de tableau. Définition des fonctions de base de la pile.
   * Algo de graham : on prend le point le plus bas, on ordonne selon les angles, on empile le premier point puis on boucle sur les points (dans l'ordre des angles)
       * Tant que le nouveau point fait tourner à gauche, on dépile le sommet de la pile
       * À la fin on empile le nouveau point
   * Fonctions intermédiaires :
       * calcul angle (à l'aide de vecteurs)
       * minimum
       * tri de points
   * Complexité :
       * calcul angle = constant
       * recherche minimum = linéaire
       * ordonner points = n log(n)
       * algo principal = on empile chaque point une fois, et on le dépile au plus une fois. Complexité bornée par la complexité du tri : n log(n)
   * Correction
       * Invariant : à la fin de l'étape i, la pile contient les sommets de l'enveloppe convexe des i premiers point considérés
           * Montrer la convexité : comme on tourne à droite, c'est vrai
           * Montrer l'appartenance à l'enveloppe :
               * Si on a pas dépilé : c'est facile
               * Si on a dépilé : On montre que l'ancien triangle est contenu dans le nouveau triangle. Preuve par dessin pas super facile à transcrire






## Questions (et remarques) du jury



### Sur le développement

CT : Ca veut dire quoi trier selon angle croissant ?

F : On trie les points du nuage en fonction des angles entre l'axe des abscisses et la demi-droite p\_1p\_i 



CT : Est-ce que vous pouvez ennoncer l'invariant dont vous parliez ?

F : À l'étape i, la pile contient les sommets définissant l'enveloppe convexe de [p\_1...p\_i]

CT : Comment inclure des tests et assertions pour vérifier la véracité de l'invariant lors de l'exécution ?

F : On peut écrire une fonction qui vérifie si un point est dans l'enveloppe convexe définie par une liste de points et l'utiliser pour écrire les tests

CT : comment vous feriez ça?

F : se ramener au cas où on a un triangle

CT : Si on a la fonction EstDansConvexe(point, List[point]) -> bool, comment on écrit les tests ? (Y: c'est très la question de GL)

F : for j in range(i): assert est\_dans\_conv(lp\_ord[j], pile\_au\_rang\_i)



EC : pourquoi arctan? C'est un peu violent, non?

F : Probablement, mais c'est déjà implémenté donc c'était plus rapide

### 

EC : Pourauoi une pile plutôt qu'une liste?

F : On pourrait prendre une liste, mais...

EC : Est-ce que l'ordre gauche/droite ou droite/gauche a une importance

F : Non, donc on pourrait travailler avec une file aussi, ca ne poserait pas de problème

EC : question sur la taille à laquelle il a répondu tout seul



EC : Dans les indices sur la pile, la pile vide c'est l'indice -1 ?

F : Oui, c'est pour que iTete pointe vers le sommet de la pile



#### Remarques



CT: très bien les dessins géométriques, mais pour une leçon sur les piles il aurait fallu représenter la pile et les modifications qu'on fait. Montrer le déroulement de l'algorithme sur un exemple.



CT : Il faut mettre l'algorithme quelque part pour ne pas que le jury soit perdu dans les explications (par exemple sur le plan)



CT : pour l'implémentation de la pile, très bien d'avoir fait une classe, m



CT : Complexité, terminaison, correction : **obligatoire**. Pour la preuve : c'est pas assez formel là. Soit il faut mettre des tests d'assert dans le code, soit il faut le prouver formellement, mais montrer "avec les mains" n'est pas suffisant.



CT : Ne pas hésiter à prendre son temps pour être clair (genre écrire "Algorithme de Graham" plutôt que "Algo. Graham").



CT : le niveau de commentaires et les types c'était bien ! Eventuellement rajouter les invariants en commentaire



Maël : euh, à quel moment mettre des commentaires ça ressemble à une anti-sèche et on va se faire taper dessus ?

Réponse : il faut respecter "les limites du bon codage"





### Sur le plan



EC : Liste chainée : pointeur en C ou de base en Ocaml. On a l'impression qu'en Ocaml on sait pas trop ce qu'on manipule. Vous pouvez expliquer plus en détail ?

F : Si on veut faire une liste chaînée : en C on le fait avec des pointeurs, en OCaml c'est accessible directement au développeur, les pointeurs sont cachés sous le tapis

EC : Donc en Ocaml on connait la librairie et pas en C ?

F : Oui en gros.



CT : Comment vous feriez une pile en C ?

F : je définirais un type structuré :

```c

struct pile { int valeur; struct pile *suivant };

```

EC : vous faites pas typedef?

F : on peut



CT : Vous dites que certaines implems (liste chaînée) coûtent cher en mémoire, d'autre non, comment choisir ? (je paraphrase de ouf)

F : pour une liste chaînée il y a plus d'infos à stocker, alors qu'avec un tableau tout est directement disponible

CT : Vous pourriez pas faire une liste chaînée en Python ?

F : si, mais certaines structures sont plus pratiques dans certains langages



CT : Qu'est-ce qui se passe quand on veut empiler et que le tableau est plein

F : Dans mon implem, ça lève une exception (y a des assertions)



EC : vous connaissez la taille max, du coup tableau ça marche bien?

F : oui



EC : accès aux deux en temps constant???

F : accès au premier élément

EC : j'achète



CT : comment vous implémenteriez une file en OCaml ?

F : 

```ocaml

f = Array.make n 0

i = n-1

j = n-1

```



CT : je prends une file de taille 3, je mets 1 2 et 3.

F : dessins expliquant ce qui se passe



EC : Comment on détermine si une file est vide ?

F : Cas i = j, plus flag pour différencier du cas file pleine



CT : pourriez-vous expliquer les schémas pour les représentations chaînées d'une file?

F : *dessine au tableau*



EC: comment vous libéreriez la mémoire?

F: en C, free. En Ocaml et Python, c'est géré automatiquement par compilateur ou interpréteur.

EC: pas le compilateur en Ocaml, mais ok. (Y: Garbage Collector en Caml)



CT : Et du coup la représentation circulaire

F : La fin de la liste chaînée pointe vers le début plutôt que NULL, ce qui libère le pointeur [début].



CT : Vous parlez d'ordonancement de processus avec des file. Expliquez-moi

F : Si on a pas de priorité, on peut utiliser une deque et *Fanny explique vitef le work stealing*

CT: j'avais en tête un système simple, ou processeur prend processus en tête de file, et le remet à la fin s'il n'a pas fini quand il doit passer à la suite



CT : Vous parlez de complexité amortie, expliquez-moi.

F : Potentiel P(s) = #elt de p1, complexité amortie opération = c+ différence de potentiel

CT : Comment on utilise ces deux fonctions pour démontrer la complexité amortie

F : Quand on défile, soit on ne transvase pas et dans ce cas le potentiel ne change pas, soit on doit transvaser et dans ce cas la différence de potentiel compense la complexité du transfert (grosse paraphrase).



CT: vous pouvez définir la complexité amortie? En moyenne?

F : amorti c'est la définition ci-dessus, en moyenne c'est sur plusieurs exécutions(?) 





#### Remarques



Le plan peut être plus compact et contenir plus de choses.

Par exemple si on met du Python et du OCaml, autant mettre du C pour éviter les questions désagréables.



Ne pas dire que la file et la pile sont analogues, peu pédagogique.



Attention à j = i qui représente à la fois la file vide et remplie.



Pas d'implémentation des files -> Ajouter une page d'annexe avec les implems.



Liste chaînée circulaire vs pas circulaire, pas de grosse diff, juste le dire à l'oral



Pour le développement, mettre l'algo en annexe.

La complexité amortie doit être définie si on l'utilise dans le plan (j'ai l'impression que ça contredit un peu ce que disait Gilles Dowek avec son "le jury n'attend pas un développement niveau lycée").



Manque de mise en contexte : piles et files importantes, mais pas plus de détails. Faire une liste de quelques algorithmes utilisant les piles et files

CT : "de tous temps les informaticiens". Sylvain Schmitz: pas content mais ça contredit un peu ce que disait Sylvain Schmitz, non ?

En vrai, non, on en parlait avec lui ok

o







Ajout au plan :

   * Tri par insertion (+plein d'autres) pour la pile
   * Dijkstra avec niveaux de couleurs pour les files




### Exercices

EF : Calcul de distance de Manhattan dans un tableau avec des obstacles en utilisant une file d'attente. Le monde est rond, c'est une chambre à air, c'est un tore. On veut calculer toutes les distances à partir d'un point donné



(insert exercice pas clair,  mais joli dessin de Fanny)



   * créer matrice (en fait c'est un tableau ie unidimensionnel) de distance, +inf pour les obstacles, -1 partout, 0 au point de départ
   * init : point de départ dans la file
   * tant que la file n'est pas vide
       * pour chaque voisin non bloqué
           * on met à jour la distance éventuellement
           * on l'ajoute à la file


(en fait elle fait un parcours en largeur du graphe si j'ai bien compris. Y: oui, c'est un algo de distance minimale dans un graphe, plus les obstacles)



CT : imaginons des opérations arithmétiques. Expliquez comment on peut utiliser une pile pour l'évaluer. Exemple $ 2 3 + 5 * $

(ça s'appelle la Notation Polonaise Inversée, pour référence)



"Faut avoir un arbre en tête", Emannuel Chailloux



Solution : on lit l'opération de gauche à droite. Quand on rencontre une valeur, on l'empile. Quand on rencontre un opérateur n-aire, on dépile n valeurs, on fait le calcul, et on rempile le résultat.



Cet exemple **doit** être dans la leçon



Exercice : On considère $ ((2 + 3) * (2 + 4)) $. Hypothèse: toutes les opérations sont parenthésée, et correctement. Simuler avec 2 piles (une piles des opérandes et une pile des valeurs). En fonction du symbole lu :

   * Si '(', on ne fait rien
   * Si valeur, on empile sur la pile des valeurs
   * Si opérande, on empile sur la pile des opérandes
   * Si ')', on applique la première opérande de sa pile aux 2 premiers éléments de la pile des valeurs, et on me


(apparemment c'est utilisé dans plusieurs trucs qu'on n'utilise plus)



Exercice : illustrer les parcours en profondeur et en largeur à l'aide de piles et de files.

   * Parcours en largeur : file
   * Parcours en profondeur : pile


Références:

   * Cormen
   * Froidevaux -> malle \o/ aprè on peut demander qu'il soit dans la malle, non ?
   * Référence pour Manhattan: non x)
