# 21/04 - 15. Hiérarchie mémoire : Structure et applications - Thomas

Developpements :

- Protocole MESI

- **Attaque Spectre** <- Choisi par le jury



## Développement



Le problème est dans la prédiction de branchement, plus que dans la hiérarchie elle-même.



Principe de la prédiction de branchement :

- Avant un branchement, on sauvegarde l'état du processeur.

- Tant qu'on ne peut pas établir la condition, éxecuter une des branches

- A l'évaluation de la condition, si elle correspond, on a gagné du temps, sinon on restore l'état du processeur sauvegardé.



Attaque SPECTRE (principe) (svp formattez)

Etat de la mémoire :
```
        [x

         x

         x

         x

         x]

        ...

        [secret]

        ...

        [y

         y

         y

         y]
```

```
f(a):

   * if a<length(x):
   *     b = y[x[a]*taille_bloc]


mechant_a = dist(x,secret)

f(mechant_x)
```


Dans le cache, on va sauvegarder l'adresse de `y[contenu du secret]`


```
p=random

time(y[p]) -> environ accès cache si p=contenu du secret

           -> environ temps d'accès mémoire si p!=contenu du secret.
```

## Questions/Remarques



### Développement

Rq : Un peu court. Vous auriez pu détailler un peu plus, d'abord les deux protocoles, puis l'attaque elle-même, avec des dessins, les deux processus...



Q : Vous savez si il y a des protections logicielles dans ce type d'attaque ?

R : J'en ai vu quelques unes dans des bouquins, mais je ne savais pas ce qui traitait de SPECTRE et MELTDOWN.

Rq : Dans l'exemple donné, on peut remplacer sur f par pas de test, et `y[x[a%taille\_x]].`









Q : Est-ce que vous avez regardé le MELTDOWN ?

R : Pas vraiment non





### Plan

Q : Taille de  L1, L2, L3  ?

R : L1 quelques kilos à quelques dizaines, L2 [...]

L3 plusieurs méga



 Q : Quid des temps d'accès ?

 R : L1 : 2-5, L2 : 30-50, L3 : 100-300, RAM : 400-1000

 Q : Et le DD/SSD ?

 R : Stockage environ 1ms, donc 1 million de cycle.



Q : Vous ne parlez pas de stockage, vous ne l'incluez pas dans la hiérarchie mémoire ?

R : [Nan mais j'aurais pu ?]

Rq : parler de la granularité des accès



Q : La séparation en cache de données (instructions/données) se fait comment selon les tailles ?

R : Les caches L1 et L2 sont séparés en deux, L3 je sais pas

Q : Tailles égales ?

R : Je dirais plus en instruction

Rq : En fait ils sont de taille égale



Rq : On pourrait séparer les choix de structure, et des politiques d'implémentation (write-through, etc...)

RqAxel : perso je pense que comme rien n'est implanté en ligne de code, c'est une mauvaise idée de séparer, parce que les politiques d'implémentation, c'est aussi la structure des circuits



Q : En quoi la permutation de boucle est intéressante ?

R :
```
    for x = 0; x< 100; x ++ {

        for y = 0; y<100; y++{

            tab [100y + x]}}
```
   * Il vaut mieux inverser les boucles ici pour profiter de la localité spatiale.




Q : (Je sais pas trop la question --- Thomas. Nous non plus t'inquiètes pas !)

R : En cas de write-allocate, on va évincer plus de lignes



Rq : vraïte



Q : Vous avez assez peu parlé de la localité spatiale et temporelle, et de comment ça influe le code. Est-ce que vous pouvez développer ?

R : Localité temporelle : on a une bonne chance de réutiliser une variable.

   * Localité spatiale : justifie le chargement par bloc. Lorsqu'on charge une donnée (structure, objet, ...) on va avoir besoin des adresses suiva.ntes.


Q : est ce que vous avez parler de l'inclusivité ? entre L1 et L2 ? avantage inconvénient

R : pas trop d'idées



Q: [lien avec les caches pour autre chose que la RAM]

R : [oui par exemple la traduction des adresses de bloc en lecture de fichiers sur disque]



Q : Lien entre la cohérence de cache et la cohérence des TLB (je crois que c'est trop pointu)

R : Non



Q : Vous avez pas parlé de swap.

R : J'ai pas parlé de swap.



Q : Si vous devez refaire un ordinateur de zéro, et que vous vouliez tout mettre en registres parce que c'est plus rapide. C'est quoi la limite à cette approche ?

R :

Physiquement les registre c'est beaucoup plus chère (je crois que c'est 100 fois plus cher que de la SRAM [NDJury plutôt 2-3 fois])

Q : Ok mais entre 256 et 1024 registres pourquoi on prend le premier ?

R : Temps d'accès ?

RJury : En fait les problèmes c'est le décodage des adresses, et les bus ?





Q : En quoi cette connaissance est utile à un utilisateur lambda [NDJury qui s'appellerait par exemple Stef Graillat] qui veut faire des calculs de matrices pour être plus performant à algorithme donné (multiplication en O(n^3)

R : On peut profiter de la localité. On a besoin de savoir comment la matrice est stocké dans la mémoire (par ligne, colonne ...)

Q : Si j'ai vraiment des grosses grosses matrices [toujours le même lambda], quelle technique je pourrais essayer d'utiliser ?



Rq : On peut faire du calcul par bloc, ca permet de gagner énormément d'argent [corrigé par le reste du jury en gagner du temps]





## Remarques

### Plan

Peut-être mettre quelque chose sur les stratégies de remplacement ?



Q : Sur quels ouvrages ?

R : "Tout ce qu'un développeur devrait savoir sur la mémoire"

RqJ : Ouais, le NSI Paterson c'est la bible mais il est touffu, il faut savoir où chercher.



### Développement
