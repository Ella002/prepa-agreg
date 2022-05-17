# 02/02 - 18. Stockage et manipulation de données, des fichiers aux bases de données. - Axel #



## Plan ##



Leçon pour public lycée, terminale. But: permettre aux élèves d'appréhender en pratique comment on interagit avec des données



Présentation de deux paradigmes de représentation des données

- système fichiers Linux

- stockage données relationnelles = BDD



### Linux ###

Description fichiers, principe arborescence fichiers, dossiers vs fichiers

Représentation machine, blocs de données, inode (représentation fichier pour OS)

Côté pratique: comment interagir avec? Descripteur de fichier, exemples Python et C (ouverture/lecture/écriture)

Autres représentations: archives (.zip, etc), gestion de version (git! **Développement 1**)



### Base de données ###

Description schéma relationnel, formé tables (relations), avec attributs. Données représentées sous forme de tuple.

Exemple fil rouge: :(

Manipulation données (structurées) via opérations complexes => plus d'opérations possibles (que ouverture/lecture), mais concepts plus difficiles à appréhender

   * - Créature table
   * - Lecture données -> requête SELECT * FROM table + opérations pour filtrer résultats
=> TP



Algèbre relationnelle

Définition dépendances fonctionnelles

Pb redondance données, mise à jour complexifiée

=> notions forme normale, BCNF et 3NF (???). **Développement 2**





Développements

   * **Représentation d'une arborescence dans git <- choisi par le jury (plus proche du sujet)**
   * Algorithme de décomposition en 3NF




## Développement (au tableau) ##



Développement = projet pour élèves classe Tale. But = coder un `minigit`. Ici, introduction du projet



Présentation des commandes :

   * `init` = initialise répertoire et la structure du `minigit`
   * `add` = ajoute des fichiers à l'arborescence courante
   * `commit` = écrire les changements apportés comme une nouvelle version de l'arborescence
   * `branch` = permet de développer l'application sur deux axes différents en gardant deux versions indépendantes de l'arborescence, dont aucune n'est plus récente que l'autre
   * `checkout` = permet de :
       * revenir à un commit précédent
       * changer de branche


`minigit` s'appuie sur système de fichiers => données sont stockées dans le système de fichiers, dans `.minigit`:

```

.minigit

├── HEAD : contient le nom de la branche courante

├── index : liste des fichiers suivis

├── objects : dossier contenant les fichiers suivis

└── refs

    └── heads : contient les références vers les têtes de branche

        └── main (branche quelconque qui existe)

```



Init: initialise tout ça:

   * HEAD = main
   * ajoute main dans refs/heads


Quels sont les objets stockés?

Trois types:

   * blob: représente un fichier
   * tree: représente une arborescence
   * commit: représente une sauvegarde de l'arborescence
En pratique -> chaque objet est représenté par un fichier.

Data :

   * type
   * données :
       * blob : contenu du fichier
       * tree : liste de noms d'objets
       * commit : métadonnées (date, auteur, ...) + un objet tree (l'état de l'arborescence) + un objet commit (le précédent dans l'arborescence)
Nom: hash(data)



Dynamiquement, il se passe quoi?

   * `init` -> initialisation
   * `add` -> mise à jour de l'index. /!\ pas de sauvegarde tant que pas de commit
   * `commit` -> sauvegarde état courant
       * parcours de l'index et création des objets nécessaires (qui n'existent pas déjà)
       * création d'un objet de type commit
       * mise à jour de refs/heads/main


On peut sauvegarder des versions \o/

Mais comment on change de version?



   * `branch` -> création nouvelle branche à partir de dernier commit
       * changement HEAD
       * ajout fichier dans refs/heads
   * `checkout` -> changement de branche.
       * Argument = hash d'un commit
           * reconstruction d'arborescence (le tree est stocké dans le commit)
       * Argument = nom branche
           * récupération commit associé
           * mise à jour HEAD
           * retour à l'autre cas


## Questions ##



### Sur le plan ###



Q (JL) : Lien entre SGBD et SGF ?

R : En pratique, les SGDB manipulent des fichiers, mais de manière plus spécifique.



Q (JL) : Fichier = représentation de données sous formes de suite de bits : il manque un (ou deux) terme(s) essentiel(s) pour la leçon. Un tableau n'est pas un fichier, qu'est-ce qui les différencie ?

R : Fichier stocké sur le disque (mémoire persistante) + accès par blocs, et pas randomisé (jules : je suis pas sûr d'avoir compris ce 2e point) (~~en gros en RAM on peut accéder directement à une case du tableau, alors que sur le disque le fichier est une liste chaînée de blocs donc c'est galère d'accès. Je crois.~~ Ah bah non du coup j'ai pas compris non plus (cf dernière question du bloc))



Q (JL) : Développer le lien entre réprésentations logiques et physiques. Intérêt de la représentation logique (= arborescence).

R : Représentation physique = inode et donc peut imaginer comment stocker dans le disque, par ex endroit fixe (car inode taille fixe) : lien entre adresse inode et les données représentées

Représentation arborescente : plus simple pour compartimenter, interaction entre fichiers plus simple



Q (JL) : *bruits confus* Quelle est la différence entre git et un SGBD?

R : Euuuuuuh. Dans git on sauvegarde des versions..?



Q (HN) : Est-ce qu'on peut résoudre ça avec un SGBD?

R : Oui : le SGBD traite les écritures de manière atomique

Q : Vous êtes sûr que c'est pas plutôt "isolation" le terme ?

R : Pour maintenir l'isolation, on peut garantir l'atomicité des opérations



Q (HN) : Vous parlez de paradigme : qu'entendez vous par là (NDJ: quelle question de pinailleur)

R : par paradigme, on suppose différentes choses sur données, du coup on les stocke de façon différente.

Pour les BDD, on suppose qu'on a cette structure sous forme de table, donc ça change qu'on va interagir de façon différente, par exemple via SQL



Q (HN) : Il peut arriver que la structure de fichiers soit abîmée (par une extinction brutale, etc). Au redémarrage il y a un programme qui essaye de réparer ça. Qu'est-ce qu'elle fait.

R : Plusieurs manières d'aborder le problème. On écrit dans un log ce qu'on veut faire. Si le log n'est pas vide au démarrage alors on s'est arrêté avant d'avoir fini les opérations en cours

Q : Quelle serait la complexité de ce genre d'opération ?

R : Pour les grosses réparations, j'imagine qu'il faudrait parcourir tout le disque pour trouver les objets non-référencés ?



Q : Supposons que j'aie une vidéo et que je souhaite retrouver les images qui correspondent à un timestamp. Est-ce que je peux retrouver ça ?

R : A priori oui, vu que j'ai une liste de liste de blocs, je n'ai pas besoin de tout parcourir



Q : ceux qui ont conçu Git auraient-ils pu utiliser git?

R :  (TL,DR [https://github.com/git/git)](https://github.com/git/git))



### Sur le développement ###



Q (HN) : Sur l'aspect multi-utilisateur de minigit, est-ce qu'on peut avoir deux programmes / utilisateurs qui lisent le même fichier?

R : Lire le même fichier c'est possible. Chaque programme a un descripteur de fichier qui lui est propre : lecture indépendante.



Q (HN) : Écriture par deux personnes? [NDJ: "vous et votre ami·e", c'est choupi je trouve ^^]

R : les deux écrivent indépendamment, sans se rendre compte, et écrasent le contenu de l'autre



Q (HN) : le git c'est une application, ça pourrait être aussi un exercice qu'on demande de modéliser. Est-ce qu'on pourrait modéliser avec un SGBD, et quels seraient avantages/inconvénients)

R : on pourrait avoir une table pour chaque type d'objet qui permette de décrire les objets, les arborescences, etc.



Q (HN) : Est-ce qu'il y aurait des choses qui ne sont pas très adaptées pour ça ?

R : une arborescence, typiquement, ça se stocke assez bien dans une tête -> attribut qui est parent dans l'arborescence [NDY : oui, comme le graphe dans l'exam è\_é]

Fichiers par contre pas forcèment adapté à stocker dans un SGBD. Typiquement stocker des fichiers volumineux ce serait pas pratique, il vaut mieux stocker un lien vers un fichier stocké en-dehors, indépendamment.



Q (HN) : Checkout permet de restaurer sauvegarde faite precedemment à l'aide d'un commit. Ça se fait comment par rapport aux fichiers?

R : dossier `.minigit` dont le contenu n'est pas modifié (non) par un checkout, par contre on restaure dans l'espace de travail.

Q (HN) : Contenu des fichiers, données proprement dites, où?

R : Fichiers courants -> hors du `.minigit`. Par contre à chaque commit on copie les infos dans le dossiers `objects`. En pratique c'est compressé, contrairement à `minigit`. Mais on veut garder une copie pour par exemple revert une suppression de fichier



Q : ?

R : Alors une fonctionnalité de git assez fondamentale c'est de fusionner des branches, voire de fusionner des fichiers textes.

Q : en quoi le fait que c'est un fichier texte permet la fusion? Quel algorithme?

R : on peut faire la différence entre deux fichiers en les parcourant. Problème: identifier différence? Quand est-ce que ça finit?

-> c'est pénible à faire au sein du développement d'un programme

HN : la notion de lignes est importante, c'est une comparaison ligne à ligne. Est-ce que l'exemple de fichier contenant du code est un bon exemple?

R : Pour du code, on pourrait vouloir trouver les fonctions et les comparer entre elles, mais c'est première approximation assez efficace

[ NDY : mouais, des fois il est quand même très à la ramasse quand on insère / supprime des fonctions ]



(Axel va avoir des notes marrantes à relire, avec nous qui disons des bêtises au milieu xD)



Q (JL) : comment on fait quand on a deux développeurs sur deux machines différentes?

R : Représentation logique des fichiers similaire, représentation physique géré sur chaque machine



## Remarques ##

(fanny : je trouve que tu écris un peu petit au tableau +1, Y) (cela dit j'aime bien l'organisation pour l'instant) (voui. La preuve on galère à recopier sur le pad, c'est que le tableau est bien utilisé) (Yaëlle qui change en live la concordance des temps, ah bah bravo le travail éditorial) (c'est même pas les temps, c'est la cohérence verbe / nom. Comme dans une recette de cuisine!)



HN: ce qui a manqué au début c'est d'utiliser le tableau pour écrire les parties du plan

oui, mais dans la vraie vie de l'agreg le jury a le plan sous les yeux, et personne a écrit son plan au tableau ([NDJS = Juge Salé <3 XD] des fois j'aimerais bien que le jury sache à quoi ressemble une leçon, en lisant ce document par exemple : <[https://agreg-info.org/files/2021/12/descriptionLecon.pdf](https://agreg-info.org/files/2021/12/descriptionLecon.pdf)>)



HN: gestion tableau -> il faudrait rappeler ce qu'on met au tableau, genre titre, pour garder de la structure



HN: leçon s'adresse au jury ou à des élèves?

l'exercice est plus de présenter les connaissances de façon organisée, sans forcément être pédagogique [NDY : sadness]



HN : donner un exemple dans la partie motivation, ça pourrait aider à démarrer la leçon



HN : manque d'articulation entre les deux



JL : En vrai il manquait peut-être une articulation plus forte entre les deux parties



HN : Aussi, peut-être préciser comment les données d'un SGBD sont stockées dans des fichiers. Par exemple, SQLite met tout dans un seul fichier, mais pas les systèmes plus avancés, pourquoi ?

-> c'est pour des raisons de mise à jour, modification des données et maintien encodage (dans même fichier) plus complexe qu'un fichier par table

JL : autre aspect?

-> indexation plus facile avec des fichiers (qui sont sérialisés) que un seul



HN : il vaut mieux diviser verticalement, c'est écrit un peu petit



[ NDYS : "quand je vous ai eu en cours" ... quand on s'est eu en cours et que vous avez regardé, vous voulez dire? +1]



JL : Pourquoi git ? Pourquoi pas un truc plus simple ? Surtout qu'on montre juste arborescence / gestion de fichiers

JL : Une idée d'autre développement serait de montrer l'implémentation concrète d'un SGBD



HN : Lister les pré-requis au début de la leçon



Jules : exemples en Python et C, possible question = et en OCaml?



Développement 2 un peu HS

Truc intéressant -> regarder fonctionnement interne SGBD, indexation, parcours d'arbre sous-jacent, etc



Truc manquant dans le plan d'après JL : la notion de clé (primaire, étrangère, etc)



Expression orale = bien, phrases claires, Axel posé [Je sais, j'ai la classe]



JL : n'hésitez pas à faire des schémas au tableau
