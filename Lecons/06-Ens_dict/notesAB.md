# 04/04 - 06. Implémentations et applications des ensembles et des dictionnaires - Aurore #

Développements :

- Utiliser la structure UNION-FIND pour trouver un arbre couvrant minimal. Algorithme de Kruskal.

- **B-arbres : présentation et opérations <-- Choix du jury**



## Dévt ##

Principe :

   * Plusieurs clés par noeud, chaque fils est entre deux clés
   * Toutes les feuilles ont la même hauteur
Degré minimal global `t`

Un sommet `x` à `x.n` clés vérifie `x.n <= 2t-1` et `t-1 <= x.n` (sauf la racine)



Si on a `N` clés en tout, alors la hauteur `h <= log\_t( (n+1)/2 )`

[demo]

Insérer une clé :

   * Si la feuille est incomplète, c'est bon
   * Sinon, on partage le noeud (ce qui rajoute une clé à l'étage d'au-dessus)
Il faut donc que le noeud au-dessus ne soit pas complet : quand on descend quelque part, on s'assure juste avant que son père est non complet (en partageant si nécessaire)

Algorithme de l'insertion :

```
    Inserer(x,k)

        Entrer: x noeud non plein

   *     k élément à insérer"
   * Si  x feuille insérer k
   * Sinon trouver le pointeur vers le noeud x'
       * si x' complet, partager(x')
       *  y = nouveau noeud
       * Insérer (y,k)
```

Suppression :

Facile si la feuille a plus de (t-1) clés

Sinon, si elle a exactement (t-1) clés, deux cas :

   * soit c'est aussi le cas d'un voisin, auquel cas on les fusionne
   * soit on pique une clé à un voisin


Contenu du tableau :


```
               M

            /     \

           DH     QTx

         / |  \

       BC  FG  JKL



    t degré minimal t>1

    x.n clés

    Si x racine 1<=x.n<=2t-1

    Si x non racine t1<=x.n<=



    n clés

    h<logt((n-1)/2)



    1 elmt                   1

    2(t-1) elmts            / \

    2t(t-1) elmts        t-1   t-1

    2t^2(t-1) elmts



    n >= 1 + (t-1) * Σ(de i=1 à h) t^i

    h <= logt((n+1)/2)



    t=3 * 2t - 1 = 5



          ..Nw..       | INSERER (x, k)

            |          | Entrées x noeud non plein

          PQRST        |         k élément à insérer

                       | Si x feuille :

          .NRW         |     insérer k

         /    \        | sinon :

        PQ    ST       |     trouver le pointeur vers le noeud x

                       |     Si x complet :

                       |          partager(x)

                       |     y = nouveau noeud

                       |     INSERER(y, k)



t = 3 INSERER(Q, L)
```


           GMPTX





## Questions ##



### Sur le développement ###



Q: Est ce que c'est au moment d'une opération qu'on se débarrasse des nœuds complets ou est-ce qu'on ne doit pas en avoir ?

R: C'est au moment de l'insertion, le nœud dans lequel on insert ne doit pas être complet.



Q: Comment on choisit `t` ?

Q: C'est quoi le rôle de `t` ?

R: Si on choisit un t plus grand le nombre  C'est un compromis, si les nœuds sont trop grands c'

Q: Il y a une formule pour choisir ?

Q: Si je stocke des entiers de manière répartis uniformément, il y a peut-être des résultats ?

R: Peut-être, j'en connais pas.



Q: Complexité INSÉRER / SUPPRIMER ?

R: O(h) pour l'insertion et O(h) pour la suppression

R: Le partage se fait en temps constant car on impacte pas l'arbre sur une grande hauteur.



Q: Si j'ai des nœuds avec beaucoup d'éléments on va alors parcourir une liste en plus, c'est surprenant que la complexité ne dépende pas de t.

R: Je suis partie du principe que `t` est une constante petite, mais les opérations sont souvent en O(t)



Q: Vous avez dit "toutes les feuilles sont à la même hauteur", c'est notoirement faux sur les ABR même équilibrés. Comment ça marche ?

R: En fait, s'il faut augmenter la hauteur lors d'une insertion, on l'augmente par le haut (en partageant la racine)



Q: Quand j'ai besoin d'un algo, je vais chercher dans un catalogue. Comment je choisis ?

R: Dépend de l'espace de stockage qu'on a. Dépend des opérations qu'on veut faire.

Q: Concrètement, B-arbre contre ABR pour recherche-insertion-suppression, en termes de complexité, et taille de stockage ?

R: Dans un ABR, la hauteur est plus petite, tout ce qui va être recherche/insertion/suppression va être plus rapide ? Mais ça dépend de la largeur aussi...



### Sur le plan ###



Q: Connaissez vous d'autres façons de représenter les ensembles que les arbres ? ABR pour les ensembles ordonnés mais il y a d'autres types d'ensembles, par exemple, ensembles de mots. Comment peut-on les définir ?

R: Les automates cf cours de langage



[question sur "oui mais donner une définition inductive c'est aussi définir un ensemble d'objet" mais perso je trouve ça bizarre limite hors-sujet]



Q: Revenons à l'ensemble de mots, avec des arbres, comment on les représente ?

R: On peut partir d'une racine et ...

Si je veux représenter un arbre avec les mots (abc, aba, bc), il faut que je définisse quel chemin prendre en fonction de la prochaine lettre. -> Arbre lexicographique

   *

   * a /     \ b
   *  0         1
   b /\ c      \ c

     0              1

a /\ c

 1    1



Q: Est-ce que travailler avec des ensembles d'ensembles (d'entiers par exemple) ça pose des problèmes par rapport à des ensembles d'objets plus simples ?

Q: Différence tester différences entre deux valeurs entières et deux valeurs quelconques ?

Q: Vous avez dit qu'il fallait comparer les éléments à insérer, mais s'il n'y a pas d'ordre intrinsèque on fait comment ?

R: avec la structure UNION-FIND, on a un représentant et ... ? help [NDLR : il faut sérialiser ou un truc du genre]





## Remarques ##



### Sur le développement ###



Rq: L'algorithme d'insertion présenté devrait être expliqué de manière plus formelle. Pourquoi ne pas l'avoir projeté ?

-> C'est quelque chose de supplémentaire à préparer. La classe n'approuve pas le fait de le présenter avec le vidéoprojecteur.

Rq: Le pseudo-code n'est pas suffisamment détaillé.



Rq: Un technique bien c'est : à l'introduction on fait un plan top-down [?], et après on rentre dans le détail



Rq: Il faudrait vérifier la réponse sur la complexité car le t a un impacte sur la complexité. Attention, t n'est pas choisi arbitrairement, il faut anticiper ce dont on va avoir besoin.



Rq: Attention au vocabulaire, partager une structure signifie avoir deux pointeurs sur la même structure, hauteur, ...



Rq: Vous parlez de la compression de Huffman, on peut vous demander ce dont il s'agit. Pareil pour les deux problèmes NP-complets qui sont évoqués.  Général : Si vous parlez de quelque chose -> Soyez sûre de pouvoir répondre à des questions dessus.





### Sur le plan ###



Rq: Si on prend beaucoup d'espace dans le plan pour un sujet, c'est tentant pour le jury de poser des questions dessus !



### Générales ###



Rq: Attention à l'organisation du tableau. Essayer de commencer par séparer le tableau en colonnes.



Rq: Attention a écrire très proprement sur le brouillon, les choses qu'on veut écrire au tableau !
