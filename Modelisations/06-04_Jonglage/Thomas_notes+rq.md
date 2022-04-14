# Thomas #

## Présentation ##


### Plan ###

   1. Modèle
       * jonglage simple périodique
       * modèle par mot
       * modèle par diagramme
   1. Caractérisation
       * fonction d'ATERissage
       * caractérisation par permutation (code)
       * caractérisation par substitution
   1. Algorithme d'énumération (code)
   1. Automates de jonglage
   1. Modèles de jonglage plus large


### I — Modèle ###



Jonglage simple :

   * 1 seule main

Jonglage complexe :

   * 1 seule boule  ...
   * "Patate chaude" : on relance immédiatement les boules

   * Représenter le jonglage en mot sur N
   * durée `d` bornant des lancers
```
      ______________

     /   ________   \   _______

    /   /        \   \ /       \

    t  o          o  t+h        o
```

### II — Caractérisation ###

- fonction d'atterrissage: mot d<sub>0</sub> ... d<sub>p-1</sub>

σ : ⟦0, p-1⟧ -> ⟦0, p-1⟧

   *    k         -> k + σ k mod[p]

- caractérisation par permutation:

    Prop: σ est jonglable ssi sa fonction d'atterrissage est bijective



Preuve : Soit a<sub>0</sub>…a<sub>p-1</sub> un mot et σ sa fonction d'atterrissage





Si n'est pas bijective. On a l, k ∈ ⟦0, p-1⟧, l ≠ k et sigma(l) = sigma(k)



Soit t<sub>k</sub>, t<sub>l</sub> l'instant auquel atterrit la boule lancée à l'instant respectivement k et l.



**∃**n<sub>0</sub> ∈ ℤ, t<sub>k</sub> = t<sub>l</sub> + n<sub>0</sub> p

La boule lancée à l'instant k + n<sub>0</sub> p et l'instant l'atterrissent  ensemble





Si σ est bijective, soit n ∈ ℕ

Soit l<sub>0</sub>, l<sub>1</sub> 2 instants tels que la boule  la boule lancée à l'instant l<sub>0</sub> et celle lancée à l'instant l<sub>1</sub> atterrissent à l'instant  n



- Si l<sub>0</sub> ≡ l<sub>1</sub> mod[p]

	La durée du lancer à l'instant l<sub>0</sub> et l<sub>1</sub> sont les mêmes

	l<sub>0</sub> = l<sub>1</sub>



- Si l<sub>0</sub>  ≢ l<sub>1</sub> mod[p], σ-1(n mod[p]) contient (?) l<sub>0</sub> mod[p] et l<sub>1</sub> mod[p]



[Présentation d'un algo naïf vérifiant si un mot est jonglable en construisant tous les mots jonglables]



### III – Algorithme d'énumération ###



- exhaustion des mots

- "inverser le test de permutation"

   + on construit les bijections de ⟦0, p-1⟧
   + pour chacune on construit les a<sub>0</sub>…a<sub>p-1</sub> avec a<sub>i</sub> ≤ val tel que a<sub>i</sub> ≡ σ(i)- 1 [p]


### IV – Automates de jonglage ###



### V – Modèles de jonglage plus larges ###



Q = 2D

v<sub>1</sub>…v<sub>D</sub>  "à l'instant i, il y a v<sub>i</sub> boules qui atterrissent"



q = v<sub>1</sub>…v<sub>d</sub> ∈ Q



Si v<sub>1</sub> = 0                                                j

                                                            ↓

q ????? si v<sub>j+1</sub> = 0 avec q' = v<sub>2</sub>         1 v<sub>d-1</sub>


```
                              (0  1)

 __             |  →      🤲

 |   ↓            |             | ^

(0 0)   ___|          0 |  |2                    (1   1)

 🤲                          |  |                     🤲

                                ↓ |

                        _  (1  0)

                    1   | → 🤲
```


Quelles sont les boules en vol et qu'est ce que je peux lancer.



## Remarques ##

[NDManet : zoomer sur le code projeté]

Rq: Trop long, le jury a dû couper Thomas ✂️✂️, dans la situation réelle, ce n'est pas ouf.

Rq: Exposé bien préparé, ça fait plaisir au jury !

Rq : Éviter le "si j'ai le temps"

Rq : Modèle bien présenté, il manque des exemples sans doute

Rq : Si on traite partiellement une section, ne pas hésiter à l'annoncer au jury (pour pas qu'il s'attende à voir ce truc).

Rq : À TOUT MOMENT, LE JURY PEUT S'ENDORMIR 💤💤. Il ne faut pas qu'il soit perdu quand il se réveille. Du coup faut bien écrire les trucs clés 🔑 au tableau

Rq : ⚠️ GROSSE ERREUR ⚠️ "Mot jonglable" n'est pas défini. La "preuve" du critère de substitution n'est pas une preuve, c'est une définition argumentée.

Rq: Idéalement, on devrait montrer des tests.



Rq de Y: cloner l'écran pour faciliter le live coding   [ou alors coder sans regarder son clavier pour montrer qu'on est un·e programmeu·r·se hardcore]



Rq: Trop de temps passé sur la "preuve". Il aurait été intéressant d'y passer moins de temps, et plus sur l'autre caractérisation [Le jury a carrément lâché le mot "erreur" et a ajouté que le sujet incitait à faire cette "erreur", donc attention au sujet aussi !]



Rq: Bonne présentation du sujet.



Rq: Il faudrait regarder l'heure
