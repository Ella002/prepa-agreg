# 09/02 - 25. Analyses lexicale et syntaxique. Applications. — Yaëlle #



Coucou Coucou, comment ca va ?

J'ai plus bcp de batterie, je vais pas trop noter On est 4, vive la redondance





/!\ Plan : coquille, dans II.2) Data inclus aussi le texte à analyser





Développements

   1. **Exemple OCamllex <- O. Carton a envie de voir ce que ça donne (montrer à quel point c'est pas facile)**
   1. Analyse LL(1) pour le langage de l'arithmétique


## Développement ##



On veut faire de la reconnaissance de motifs sur des recettes de cuisine.

On veut transformer :

int "g" text -> add txt(g, int)

int "tbsp" txt -> add txt("cl", convert int)

int txt -> add txt(None, int)



[ouvre le code .mll]



Première partie : des définitions en OCaml (types, quelques fonctions)

Deuxième partie : des raccourcis ("digit" au lieu de "['0'-'9']" typiquement

Troisième partie : les règles (plus précises que celles au tableau). Attention à mettre "int txt -> ..." à la fin pour pas que ça empêche les autres d'agir

Dernière partie : pied de page en OCaml. Souvent vide (quand c'est envoyé dans du Yacc par exemple). Ici, simple.



[compile et fait tourner les tests]



[le développement termine un peu court par rapport aux 20min]



## Questions ##



### Développement ###

Q (SS) : Est-ce que vous pouvez essayer de montrer le code OCaml produit et le commenter ?

R : Le code produit est décomposé en des tables et des matchs sur les caractères lus par rapport aux tables



Q (OC) : Les tables, conceptuellement, elles correspondent à quoi ?

R (SS) : Ce sont les tables de transition des automates, mais elles sont compressées bizarrement



Q(SS) : Comment est-ce que vous feriez à la main sur votre exemple, sans outil aussi puissant que Ocamllex

R : On va avoir un automate pour chaque motif. Je suppose que dans OCamllex iels ont fusionné les débuts des automates

Q(SS) : vous pouvez en dessiner une version simple à la main, par règle ?

R : [dessin] il faut faire attention à faire des automates déterministes



Q (SS) : Les expressions de l'analyseur syntaxique sont $a$ $a*c$ et $b+\varepsilon$. L'entrée est $aaaaab$. Comment se passe la reconnaissance ?

R : [dessins] Hum il ne peut pas y avoir epsilon dans les langages, sinon on ne va reconnaître que ça.



Q (OC) : Vous avez mentionné XML, comment fait-on pour parser du XML ? [NdA : note, XML c'est une grammaire contextuelle, donc le parsing est assez violent] Pourquoi ne fait-on pas avec votre méthode d'analyse syntaxique pour le XML ?

R : Euh

Q (SS) : Quelles seraient les règles de la grammaire algébrique ?

R : [quelques trucs]

R (OC)  : XML a été fait pour que ce soit totalement non ambigu, donc il n'y a pas besoin d'un outil aussi puissant que yacc



Q (SS) : Pourquoi on a une grammaire aussi compliquée pour faire un analyseur syntaxique d'expression arithmétique (cf grammaire donnére pour rat en cours de ocmpil)

R : C'est plus compliqué mais l'avantage c'est que c'est LL1 et non-ambigu

Q (SS) : Est-ce qu'il y a un lien entre être LL1 et être non-ambigu ?

R : Intuitivement, si c'est ambigu, on peut pas savoir quel arbre de dérivation suivre, donc c'est pas LL1.

Q(SS) : sur cet exemple, si on essaye d'appliquer l'algo donc de construire le tableau, qu'est ce qui se passe ?

R : Si on essaie de construire le tableau, on aurait un truc du genre "Si je lis +, j'applique telle règle", mais ici on a plusieurs choix pour plus.

Q (SS) : [propose une grammaire non-ambigue] qu'est-ce que vous pensez de celle-là ?

R : Ca marche pas, il faudrait les plus à gauche [NdA : je crois que sa grammaire marche en vrai ! C'est celle qu'on avait donné en cours pour les ratexp]

Q (SS) : Si j'inverse l'ordre dans ma grammaire, est-ce que ça change quelque chose ?

R (SS) : en fait oui, ça change que c'est une récursivité à gauche ; bref



Q(SS) : Étant donné une grammaire, existe-t-il un algorithme qui la mette en forme LL1 ?

R : Non, tous les langages ne sont pas LL1.

Q(SS) : Vous avez un exemple ?

R(SS) : Langage inhéremment ambigus, non déterministes, et même des non-ambigus déterministes non-LL1...

Q(SS) : Du coup c'est embêtant, mais pourquoi on étudie quand même LL1 ?

R : Ca marche bien quand c'est simple, mais il y a d'autres techniques sinon

Q (SS) : Pourquoi les gens utilisent quand même LL1 si c'est très restrictif ?

R (SS) : L'algorithme s'implémente de manière simple, par une implémentation récursive



### Cours ###

Q (SS) : Est-ce qu'on peut faire de l'analyse syntaxique pour n'importe quelle grammaire ? C'est un problème de décision

R : Je dirais que non ?

R (SS) : C'est décidable par un algorithme dynamique (CYK, ou Earley qui est plus simple)

On utilise pas ces algo pour des langages de programmation parce que pour un programme, on ne veut vraiment pas d'ambiguité (= plusieurs sémantiques du programme)

"c'est vraiment très mal"



Q (SS) : est-ce qu'on peut dire si une grammaire est ambigüe ?

R : Non ?

Q (SS) : Peut-on dire si une grammaire est déterministe ?

R (SS) : Non plus. En pratique, on utilise les grammaires LLk pour garantir toutes ces propriétés nécessaires à une bonne compilation.

Remarque (profs) : En général, sur les grammaires, la plupart des questions de ce style sont indécidables, ou certaines (précises, rares et simples) sont P-complètes aussi. Il y a même des théories





## Remarques ##



OC : Je suis sceptique sur les développements où on montre du code. On passe pas mal de temps à décrire des points techniques, mais ça met pas beaucoup le candidat en valeur.

SS : Si on fait ça, il faut entrer dans le fonctionnement interne, typiquement ici il faut bien connaître, et présenter soi-même pendant le développement

OC : en fait, pour arriver à du code avec de la substance, il faut quand même pas mal de temps.

Axel : dans [https://agreg-info.org/files/2021/12/descriptionLecon.pdf](https://agreg-info.org/files/2021/12/descriptionLecon.pdf),

SS : Quand on prend des exemples, c'est bien de prendre des exemples réaliste, mais il faut aussi produire des exemples plus "corner case"

OC : d'ailleurs le jury va poser la question sinon.



SS : Vous donnez un algo dynamique en O(n^2), mais en pratique, on utilise un algo linéaire (enfin, fois la taille de l'automate qui est considéré constant)

SS : en pratique, entre analyse lexicale et syntaxique, c'est la lexicale la plus longue.



SS : C'est quoi la différence entre le langage naturel (groupe nominal, verbe, etc) et ce genre de choses ?

R (SS) : Il y a de l’ambiguïté dans les langages naturels. De plus, les langues naturels ont des phrases beaucoup plus courtes que le nombre de mots d'un programme informatique, du coup la performance par rapport à la longueur du texte est beaucoup plus critique.

Aussi, un truc important dans les langages informatiques c'est qu'on veut rejeter les phrases mal formées, alors qu'en langage naturel on peut accepter un peu n'importe quoi et essayer d’interpréter après.



OC : Il faut vraiment montrer que l'analyse lexicale et syntaxique ne se limite pas à la compilation. On en a tout le temps besoin lors de la lecture de données dans un programme par exemple. "La compilation c'est générique de ce qu'on fait en informatique" [NdManet on dirait quelqu'un qui t'explique que ta machine à laver est Turing-complète <3] parce qu'on prend des données, et on sort d'autres données.

Notamment, ça explique le succès de formats comme JSON, XML, parce que ça simplifie cette étape avec des librairies pré-existantes.



SS : En parlant de format à la con : la compilation LaTeX vers PDF... C'est dangereux : la façon de "parser" dépend de ce qu'on a lu avant, c'est infernal, personne ne veut faire ça.



SS : Il faudrait aussi expliquer pourquoi on fait une différence entre analyse lexicale et syntaxique ? Pourquoi deux passages ?

R (Yaelle) : [...]

R (SS) : c'est des considérations entre ingénierie et performance. Et effectivement il y a de l'information contextuelle.



Yaelle : j'ai utilisé [tel livre], c'est bien, iels utilisent des poissons.
