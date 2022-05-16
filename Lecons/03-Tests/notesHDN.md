# 10/11 - Tests de programme et inspection de code [Hector]



2 développements : (1) mini-typeur en python et (2) logique de Hoare



Devt 2 était : donner les règles, puis pb avec non-terminaison, puis invariants, puis weakest preconditions



Note sur le devt 2 : il faudrait introduire dans le plan la logique de Hoare pour faire un développement qui prouve un résultat, soit dérouler entièrement un exemple en logique de Hoare après avoir présenté les règles (en 15-20 min)



#### Devt 1 : Typeur de Python

Exemples considérés :

   * -def f()->str:
       * return 1
   * -def g()->int:
       * return 1
   * 

expressions régulières utilisées pour parser, plus simple mais moins puissant que lexer -> parseur -> AST



H. présente (à l'oral) ses exemples pour montrer les objectifs de son typeur :

    - réaffectations uniquement avec le bon type

    - inférence de types (int et str)

    - types des paramètres dans les appels



Puis le fonctionnement du typeur:

   * H. présente le fonctionnement des expressions régulières
   * chaque fonction est représentée par un dictionnaire avec son corps, ses types d'entrée et son potentiel type de sortie.
   * 

En fin de développement, H montre les limites de son implémentation (branchements avec types option, affectations de variables de type non spécifié ?).



### Questions



#### Développement

Q : Qu'est ce que c'est un programme ?

H. donne une grammaire pour ce que son programme peut comprendre (les regex sont utilisées localement et plusieurs fois, donc c'est pas un truc régulier non plus)

Aller-retours entre H et le prof pour définir précisément la grammaire.



Q : Quel est le langage des types

H : str | int

Q : type de "def f(x): \n\t return 42" ? type de x dedans ?

H : x serait de type ?

Q : Il faut donc ajouter ? dans les types. Quid de f ? Parallèle avec le lambda calcul typé ? Y-a-til besoin de qqch de différent ?

H : Typage en 2 passes, 1 première définissant le type de fonctions, et une deuxième vérifiant que les appels sont corrects

Q : Quid de def g: \n\t return f(3)" ? C'est quelque chose que vous savez interpréter.

H : On n'infère pas le type des fonctions dans mon programme

Q : Et si on annote f ?

H : ce n'est pas utilisé, mais pour pouvoir maintenir les autres types pythons valides, je préfère ne pas l'utiliser (exemple sur les types option en retour, qui ne seraient plus pris en compte).



Q : "def k(x,y): \n\t return x" Que se passe-t-il niveau typage ?

H : Pas d'annotation, donc l'utilisation ne foire jamais. On type [?,?]->?

Q : Pas capable de voir que le type est le même que celui de x ?

H : Non en effet.

Q : Du coup vous voyez la diff avec les variables de type.



Q : Sur le premier exemple (du développement). Pourquoi on a problème dedans ?

H : mypy est pas content avec cette syntaxe avec trop d'annotations.

Q : Mais pourquoi ca pose problème ? Pour vous aider, écrivez cette fonction en Ocaml

    H : 

    let b = ref 0 in

    b := b;

    "a"

    

Q : Vous avez choisi les regexp, c'est courageux. Alternatives plus simples en Python ?

H : Je pense qu'il y a des modules créant les AST

Q : Le typeur généralement agit sur quoi

H : Un AST



Q : Question sur la limitation des branchements. Si c'est un 

    if false

on ne remarque rien. Ca vous convient ?

R : On peut vérifier si c'est false la condition, mais c'est beaucoup plus dur de si on a des variables

Q : est-ce que c'est possible de vérifier si du code est mort ?

H : C'est indécidable.

Q : Oui. Vous pouvez donner un argument ?

H : On va pouvoir créer un while qqch

Q: Oui la stratégie c'est de se ramener au problème de l'arret





Q : Vous pouvez justifier le choix de l'anglais dans votre code ?

H : Les messages d'erreur de python sont en anglais

Q : Donc vous voulez être cohérents avec les messages d'erreur

Q : On peut peut-être vous reprocher les chaines de caractère en anglais lors d'une leçon



Q : Vous avez choisi Python, est-ce qu'il y a des choses qui vous ont paru difficiles à traiter (dans la syntaxe, ...) ?

H : ...

Q : Par exemple, comment vous gérez la portée de vos variables ?

H : En python les variables sont définies au-delà du bloc de leur définition



Q : Rapport développement/cadre général de la leçon, par exemple avec la partie analyse statique ?

H : Oui c'est pas complètement typé, testé, documenté, les tests sont pas automatisés...

Q : Par exemple, votre première fonction, vous pourriez typer son résultat ? (actuellement dict() )

H : Dict[str, Tuple[int, List[Tuple[str]], str]]



#### Plan :



Q : Quelles sont les propriétés qu'on essaie d'exhiber dans les programmes que vous avez présenté comme exemple ? Je vous aide, ils sont relativement surs, performents et conséquents

H : Sûr : qui correspond à la spécification qu'on a donné, qui ne va pas planter

Conséquent : (c'est juste que le code est long)

Performant : temps d'exécution, espace occupé....



Q : Y a-t-il  un lien entre test et performance de programme ?

H : Il y a des tests de réactivité, et on peut améliorer le temps d'exécution par analyse statique.



Q : Dans les schémas de I.A, l'abscisse c'est le temps mais l'ordonnée c'est quoi ? Qu'est-ce que c'est la différence entre que descendre et descendre et remonter

H : C'est juste pour mettre en relation les différents types de tests avec la phase de conception



Q : Question sur I.B. Vous dites "cadre d'information", ca veut dire quoi ?

H : Quantité d'information on a accès.

Q : Pourquoi il y a trois types différents ?

H : C'est une grille de lecture pour certains tests, les tests unitaires se font en boite blanche,...

Q : Est-ce qu'il y a un avantage à faire un test en boîte noire, avec moins d'information ?

H : Ca retire des contraintes sur l'implémentation des tests, il ne seront pas dépendant de l'implémentation de la feature



Q : Sur "couverture de code", vous avez un exemple de code qui a une couverture complète au niveau lignes de code, mais non-complète au niveau du comportement ?

H :

    def f(a):

   * if a> print("a")
   * if a>1 print("b")
Le test avec a=2 on a pas de comportement où on affiche "a"

Q : En général, possible de couvrir tous les comportements ?

H : indécidable

Q : Vous auriez besoin de preuve si vous pouviez ?

H : non



Q : Comment vous faites pour assurer la clarté du code ? Est-ce que tout le monde doit se l'imposer ?

Q : Est-ce que c'est automatisable ? Est-ce que ça existe ?

H : Oui, il y a des outils qui existent. Auto-PEP8 en Python, plus ou moins paramétrables.



## Exercice(s)

Assez simple et classique.



"FizzBuzz" parcourir les 100 premiers entiers, écrire "Fizz" à la place des multiples de 3, écrire "Buzz" quand c'est un multiple de 5, écrire l'entier si aucun des deux.



------------------------------------------------------------------------------------------------------------------------------

Note du (plus jeune) secrétaire : test utilisé dans l'industrie pour évaluer la quelité du code produit. Il y a beaucoup de manières de coder ça, et la plupart utilisent des duplications de code ou ne sont pas modifiables facilement. Pour information, ci-dessous une version ok de l'implémentation (quoique un peu lourde, et n'effectue que des print et ne renvoie pas la liste)



    def fizzbuzz(n : int) -> None :

        l\_diviseur : List[int] = [3,5]

        l\_mots : List[string] = ["Fizz", "Buzz"]

        ecrire\_entier : bool

        

        for i in range(1,n+1):

            ecrire\_entier = true

            for index in range(len(l\_diviseur)):

                diviseur = l\_diviseur[index]

                if(i%diviseur == 0):

                    ecrire\_entier = false

                    print(l\_mots[index], end="")

            if(ecrire\_entier):

   *         print(i, end="")
           * print("") #saut à la ligne dans tous les cas
------------------------------------------------------------------------------------------------------------------------------



    def fizzbuzz\_un(n:int) -> str:

        """Procède sur un entier pour calculer ce qu'on est sensé afficher"""

        if n % 15 == 0:

        return "fizzbuzz"

        if n%5 == 0:

   *     return "fizz"
        if n%3 == 0:

   *     return "buzz"
        return str(int)

        l

        l





### Debat sur la structure de la lecon :



Il faut un cadre au début, et dès le début des définitions formelles.

Les processus de test : C'est au programme donc c'est bien, mais ça prend beaucoup de place alors que c'est pas très pratique



La suite arrive tard malheureusement, et vous passez trop de temps sur le processus de test (3/6 min)

Vous avez le droit d'utiliser une page d'annexe pour y faire apparaître les schémas



Sur la structure, c'est assez étonnant de voir des processus de développements apparaître dans l'analyse dynamique, alors que l'analyse statique est aussi classiquement dans ces processus 

(exemples : linters, typages, etc). Il faudrait donc faire une partie d'intro qui comprend ça, et motive les deux parties "intéressantes" d'après sur analyse statique et dynamique



Vous avez (comme R.D.) compris le titre comme "analyse statique / analyse dynamique" mais il manque, du coup, deux parties en plus de cette disjonction : une d'intro (cf paragraphe ci-dessus) qui replace le contexte, et une d'ouverture

Aussi, classiquement on met ça dans l'autre sens, mais pourquoi pas.



Alternative : 1 Pourquoi, 2 comment



Il faut plus d'exemples, et il faut mettre des petits exemples illustratifs sur les différentes parties. On peut entre autres ajouter un exemple récurrent dans les définition qui permet de les comparer. Il ne faut pas parler de cet exemple à l'oral, mais il explicite le plan.



Il faut considérer que le plan est là pour un cours entier, pas juste une présentation en 6 min au jury. Le jury devrait être convaincu que c'est de quoi tenir longtemps.



Point positif : couvre globalement le programme. Il faut insister plus sur la couverture de code avec des exemples, et en plus ça plaît au jury parce qu'il y a de l'algorithmique qui se fait bien dessus



pour la prog par contrat, vous voulez dire "gen automatique de code" (H : oui), c'est bien, il faut être prêt à répondre aux questions attenantes.



Partie analyse statique : bonne pratique à la main, c'est bien d'en parler, mais il manque des données, définitions et théorèmes sur l'analyse automatique, ce qui est disponible.

La partie optimisation ça rentre peu 



On s'attend plutôt en analyse statique à : linter, typage, analyse de code mort



La partie preuve de programme est pertinente, il faut parler de préconditions et postconditions, potentiellement d'invariants voire de logique de Hoare.



Plan à affiner, mais c'est normal, et c'est déjà pas mal.



Sur le papier, le devt 2 est assez parfait : analyser un fragment d'un langage, et c'est sympa.



Sur la manière dont c'est fait, quelque chose n'allait pas trop, car vous avez passé tout le temps à présenter du code, et en particulier les regexp.

Il faut montrer au jury que vous avez compris qu'il faut séparer la partie "extraction d'abstraction" et "travail sur l'abstraction". Comment faire du coup ?

Une solution : travailler directement sur l'AST, pas besoin de montrer le programme qui transforme le programme en AST.

ce qui compte c'est de montrer le travail sur l'AST, l'extraction d'information, les contraintes...

En python, module AST, ast.parse(str) donne l'AST python directement.



Nombre de ligne de code des fonctions trop élevé, il faut séparer en bouts spécialisés et commentés. Attention à respecter ce qu'on présente dans la leçon en terme de clarté de code.



Pour les regex : attention, 50 caractères non seulement c'est impossible à lire, mais c'est infernal à débugger surtout en situation de stress de j'ai-5-h-pour-préparer



Il ne faut pas oublier qu'il faut commencer par utiliser le tableau pour expliquer ce qu'on veut faire. Ici, présenter le langage à utiliser, puis le langage de types, avant de présenter du code



Typer un langage impératif c'est plus dur qu'un langage fonctionnel, attention





Développements possibles :

- analyseur de code mort (une fois que l'AST est produit par le bon module)

- mini-typeur (plutot fonctionnel, pas de ref à gérer)

-logique de Hoare

-programme impératif intéressant et flot de contrôle

-précondition/invariant/postcondition sur du code objet existant (vérifier la spec de classes)

-interprétation abstraite sur les intervalles

-fuzzing, coder un fuzzer qui fait de l'exploration aléatoire
