# 26/01 - 10. Arbres : représentations et applications. - Hugo #

Développements :

   * Calcul d'un arbre couvrant minimum par Prim
   * **Link-cut tree** <- choisi par le jury


## Développement ##

Les arbres, en moyenne, sont déséquilibrés. Objectif : accélérer les parcours des arbres qui ont besoin de faire des longs chemins.

-> Voir moodle pour explications



## Questions ##



- Pourquoi commencer par les arbres hiérarchiquement enracinés ?

  Ça cache un peu les applications en informatique des arbres et le fait que c'est une structure essentielle.

   * -> J'utilise cette première partie pour commencer à avoir des définitions et commencer à donner des propriété. Pratique pour les parties suivante. Permet aussi de motiver les approches plus algorithmiques des parties suivantes.


- Les arbres généraux puis les mots de Dycke, pourquoi cette transition ?

   * -> ?? [globalement : pour les compter, et pour parler des représentations implicites en chaînes de caractère, typiquement XML]
   *

- Ce sont des tas binaires ou des tas pas binaires ?

   * -> Je ne l'ai pas très bien décris. Les tas non binaire sont beaucoup plus technique à présenter pour leur fonctionnement. Ces structures sont plus compliquées à manipuler car elle sont connçues pour optimiser leurs complexités sur certaines opérations.
- Pourquoi en deuxième et pas en troisième partie ?

- Pourquoi vous pouvez représenter vos tas comme un tableau ?

   * -> C'est à cause de cette représentation implicite de cette structure que je l'ai mise dans cette deuxième partie. Cette représentation est assez valide et différente de cette définition inductive donnée en début de partie. Le but est de présenter d'représentations des arbres planaires
- Je voulais vous faire dire que cette représentation de tas est liée à une certaine forme. On les dit "parfait". Pour moi, ici, il y a des mélanges de différentes choses.



- Différence complexité moyenne et amortie ?

   * -> Il existe beaucoup de définition de complexité. La complexité moyenne est l'espérance du temps d’exécution selon les différentes entrées possibles. La complexité amortie a pour principe de ne pas compter les opérations indépendamment, mais plutôt sur une suite d'opération (souvent pire des cas mais on peut aussi faire en moyenne). Une manière assez classique de montrer que c'est borné est de passer par des potentiels. Un exemple simple de travail avec complexité amortie, avoir un tableau de taille dynamique (2^n) et quand on atteint la limite de la taille du tableau, on double sa taille, ce qui est très long. Mais cela est fait très rarement donc on peut l'amortir.
   *

- Quel intérêt des arbres-splay ?

   * -> C'est un ABR. On n'a pas besoin de maintenir une structure différente d'un ABR naïf. Mais avec toutes ces opérations, on va obtenir une complexité amortie meilleure. L'intérêt que j'avais à le mettre dans mon plan, c'est que le link-cut tree fonctionne avec une analyse de complexité amortie.
- Ça ne se voit pas dans le plan.

   * -> Les arbres binaires de recherche, quand on les équilibre,  ne vont pas avoir une forme représentative d'un arbre moyen.


-  Page 2, votre exemple, c'est un arbre de syntaxe abstrait ?

   * -> L'objectif de mon dessin n'est pas d'être précis sur une correspondance avec un langage précis.
- Qu'est ce que ça apporte de présenter un programme par la forme de son arbre de syntaxe abstraite ?

   * -> Il faut pouvoir identifier des blocs et réduire ces blocs en opérations qu'un ordinateur peut comprendre.
- Si vous voulez écrire un interpréteur pour un langage de programmation. Ce que vous allez obtenir ne sera pas une chaîne de caractère du langage de programmation mais l'arbre de syntaxe abstraite du langage.

[[note de Manet : j'avais pas bien compris l'objectif de la question, qui était de donner la distinction entre un arbre de syntaxe abstraite (qui est un encodage dans un langage de programmation, typiquement un type de OCaml) et la décomposition hiérarchique du code (ce que j'ai dessiné en gros). Effectivement, dessiner ça c'est pas très précis]]



## Remarques ##



- Le plan est intéressant mais il semble il y avoir des trous. En particulier, on parle beaucoup de potentiel mais pas de coût amorti.

   * -> Je suis allé assez vite, il y avait beaucoup de choses à dire.


- Dans la partie "arbre hiérarchiquement enracinés", vous donnez la définition inductive mais les autres définitions ne sont pas données de manière inductive, c'est dommage puisque d'un point de vu informatique, les arbres mettent en valeur la récursivité.



- Sans les commentaires, la troisième colonne n'est pas claire du tout (Partie sur les arbres splay).

   * -> Principe : implémenter les opérations des ABR pour que chaque opération soit uniquement effectuée sur la racine de l'arbre. Pour ça, il faut modifier la structure de l'ABR via des rotations. Chaque opération commence par localiser la position du nœud sur lequel on veut intervenir, puis on le remonte à la racine, puis on effectue l'opération sur la racine.


- Je ne comprend pas pourquoi parler de génération, ça n'a pas de rapport.



- Attention au vocabulaire qui doit être précis.

- Pourtant, quand vous parlez on voit que vous savez de quoi vous parlez.
