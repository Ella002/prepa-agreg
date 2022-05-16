# 01/12 - Structures de données. Exemples, applications.

Développements :

    - Simulateur d'agriculture (python) **<- choisi par le jury**

    - Link cut tree (C/C++)



### Plan (11 min /10)

### Développement (25 min/20)







### Questions sur le développement



Q : Les arbres splay, c'est des AVL non ?

R : Même genre d'opérations, mais effectuées de façons ~~stochastique~~ (en fait non). Idée : à chaque fois qu'on accède à un élément, on le fait remonter []à la racine[].



Q : Quel est le lien avec les tableau à redimensionnement dynamique ?

R : Pour présenter la complexité amortie 





Q : Quel est le lien entre la complexité amortie et la complexité en moyenne ?

R : Complexité en moyenne : espace de probabilité, il peut y avoir des trucs qui se passent mal (par ex, arbre qui finit très déséquilibré) mais très rare.

Complexité amortie : prend en compte la moyenne aussi mais aussi dans le pire des cas, et du coup la moyenne depuis le début va rester raisonnable



Q : Et donc, quelle est la différence entre les deux ?

R : Dans les systèmes critiques, on va éviter les algo qui peuvent avoir un pire cas affreux (pour pas casser par ex) et aussi source aléatoire n'est pas parfaite et donc pourrait être utilisé par malveillance : pas robuste



Q: En complexité amortie qu'est ce que vous connaissez qui donne des résultats (meilleurs qu'en complexité en moyenne ?)

R : On les deux exemples du cours : le tableau dynamique et l'arbre splay. Le link-cut tree utilise aussi une implémentation avec complexité amortie.

Il est possible, pour beaucoup de problèmes, de prévoir la complexité amortie d'une implémentation pour créer une implémentation en complexité constante pour chaque opération.

Pour l'exemple de l'arbre splay, c'est plus rapide et facile à utiliser qu'un arbre rouge noir, qui est un équivalent sans complexité amortie. (note de Manet : J'ai peut-être dit ça à l'oral, mais c'est pas plus rapide, juste plus rapide à coder ^^)



*Le jury n'a plus de questions et demande aux gens dans la salle si ils en ont*

* Le public n'en a pas non plus *



Q : J'ai pas compris tout à l'heure d'où venait le log^2 ?

R : Dans ma représentation, l'arbre est un tableau dans lequel les fils de la case i sont sur les indice 2i et 2i+1.

Calculer une somme revient à remonter l'arbre pour calculer la somme (avec une opération à chaque noeud), donc cela fait O(log(n))

De plus, pour la 2D, on a des arbres binaires d'arbres binaires, donc pour obtenir le résultat d'une feuille, on doit remonter à la racine en faisant une opération sur un arbre binaire à chaque fois, d'où log(n)^2 (si l'espace est carré, sinon pas très différent)



Q : Sur votre exemple, qu'est-ce que vous voulez en extraire ? 

R : Le but est de répondre efficacement à l'interface qui permet:

   * d'ajouter sur un rectangle
   * d'effectuer une requête pour savoir combien de pluie est tombée sur un champ
Q : Donc pas de maximisation ou quoi ?

R : Pas du tout. Mais on pourrait changer la somme sur un champ par d'autres opérations (maximum, etc...) ce qui peut rendre l'algorithme actuel caduc (ex : rajouter qqch à un intervalle pour le max), il faut donc un peu modifier les opérations. Par exemple : set le max sur tout un intervalle, ne fonctionne efficacement pas en 2D, mais fonctionne en 1D avec une solution paresseuse, en modifiant des nœuds internes de l'arbre binaire (plutôt que les feuilles). Note : la solution paresseuse n'est pas plus efficace à long terme, parce qu'au bout d'un moment, il faudra faire descendre toutes les annotations paresseuses. (Note de Manet : en gros c'est efficace en 1D parce qu'on peut résumer toutes les opérations paresseuses en une seule, mais plus en 2D+ parce qu'il faut garder une description complexe)

La solution paresseuse fonctionne aussi pour la somme, mais elle était trop complexe pour être présentée en début de cours.

Mais en dimension supérieure, cela ne marche plus car on a pas une représentation simple de la valeur aux feuilles.



Q : Quelle solution vous proposeriez si vous aviez des max en 2D ? Des quad tree ?

R : Je ne suis pas certain qu'il y ait des solutions plus efficaces. Le quad tree permet de passer d'un problème quadratique à un problème linéaire.



Q : Qu'est-ce qu'un quad tree ?

R : Comme un arbre quaternaire, il y a un fils en haut à droite, en haut à gauche, et pareil en bas. Si on a une requête sur une zone rectangulaire, on peut faire des requetes simples sur les rectangles qui le composent.

Le problème, c'est que quel que soit le rectangle de requête, on va avoir un nombre linéaire de rectangles élémentaire dont on doit aggréger la solution. Dans la solution que j'ai présentée pour la somme, la complexité est cependant en log^2.

Il existe aussi une solution indépendante de la taille des rectangles mais linéaire en le nombre de requetes précédentes. Sur un petit nombre de requetes, ce serait efficace. Si l'espace de base est à coordonnées réelles, on devra passer par une structure de ce type.









### Questions + Remarques sur le plan



Rq : C'est "Algorithmique"

Rq : Premier exemple un peu abrupt ("ça cache le reste") (Note de la prise de note : cf SAC À DOS)

Ne pas faire un exemple trop appliqué et concret, car ça prend trop de temps à expliquer (RIP les praticiens, faisons tous des intégrales doubles discrètes)

Rq : Attention, on ne sait pas si n désigne le coté ou la surface, il faut le préciser !



Rq : Cette leçon est assez difficile car très large, donc on ne sait pas comment la dérouler. J'ai l'impression qu'on a zappé beaucoup de choses en se concentrant sur l'exemple.

De plus, l'articulation avec la complexité et les listes chaînées est pas très claire ("Je ne suis pas sur du cheminement"). Cela manque d'un fil directeur



Q: Séparer structure statique et dynamique est une bonne idée. Mais on ne voit pas à quoi sert les structures chaînées.

R: J'ai pas trouvé de bon problème que ça résout, qui ne soit pas soluble facilement sans.

Q : Un arbre quelconque ? Si il n'est pas équilibré ?

R : Mon objectif était de parler de listes chaînées avant les arbres.



Q : Dans les structures dynamiques : le tableau dynamique ?

R : Mis au dernier moment, parce que la complexité amortie était trop abrupte sans

Rq : Le tableau dynamique est un exemple suffisant pour la complexité amortie.



Rq : plan trop dense, on a pas parlé de tout.



Rq : Il vaut ptet mieux présenter les structures, et juste mentionner les exemples/les utiliser comme développement.



Rq : L'exemple est bien pour attirer des élèves de terminale, mais pas pour une leçon.



Q : Est-ce que la complexité n'est pas TROP importante (moitié) dans votre plan ?



Q : On pourrait proposer en développement que la hauteur moyenne d'un ABR est en log ?

R  :Borner la profondeur max est technique, mais calculer l'espérance ça se fait.



Remarques sur les tas et les arbres cartésiens, les distributions uniformes de données.



Rq : Imprécisions sur le vocabulaire : analyse de l'algo et l'efficacité de l'algo. La complexité amortie n'est pas une propriété de l'algorithme.
