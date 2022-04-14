# Fanny #

## Présentation ##

### Plan ###



   1. Présentation du modèle
   1. Caractérisation des mots jonglables [Code]
   1. Extension du modèle




### I — Présentation du modèle ###



   * Δt = 1 (temps discret)
   * Jongle à une main
   * Patate chaude
   * Une seule action par instant


Modélisation

   * m = a<sub>0</sub>a<sub>1</sub>...a<sub>p+1</sub> (Σ = { 0, 1, ..., 9 }
   * [exemple faux :'( Ui oups]
   * cascade : bb...b -> bp
   * certains mots ne sont pas jonglables : 32 non jonglable




### II — Caractérisation des mots jonglables ###



Outils de modification des mots jonglables

   * Échange de lancers (dessin représentant l'échange) cf Figure 1
       * i != j, on pose e = (j-i) mod p
       * 1 <= e <= a<sub>i</sub> <= a<sub>j</sub> + e
       * a<sub>j</sub> <= a<sub>i</sub> - 2
       * [propose aussi l'échange inverse]


Figure 1 :

```
       ____________      ____________

    /                               \ /                              \

  /                                 /\                                  \

/                                /      \                                  \

                                j
```
↓                              devient :                                ↑
```
       __________________________

    /                                                                  \

  /                                 __                                 \

/                                /      \                                  \

                                j
```




Test par moyenne : nécessaire (pas suffisant) cf Figure 2

Test par permutation : CNF

   * "preuve" (avec les mêmes réserves que pour Thomas)
Test par réécriture : CNF

   * preuve / algo :
       * si m = bp, ok
       * sinon, on a une lettre maximale


Figure 2 :


```
                 ___________

                /           \

               /             \

    ----------+----------+----------+----------

              i               j



    <-------- p -------->
```


### III — Extension du modèle ###



A- Une main

   * Sans patate chaude
   * -> test : permutation
   * Sans compter a<sub>i</sub>i = 0

   * Plusieurs actions
   * "+" u ∑
   * 522+1+0 (?)


B- Plusieurs mains

```
     ←    🏐   ←

 ↓                       ↑

    🏐         🏐

     → 🖐 → 🖐 →
```


   * mg(n+1) md md1 mg


```
    -+-+-+-+-+-+-+-+-+-

      \   \ / \ / \ / \

       \   X   X   X

        \ / \ / \ / \ /

         X   X   X   X

        / \ / \ / \ / \

    -+-+-+-+-+-+-+-+-+-
```



## Remarques ##

NDY: trop bien la phrase d'intro!



MJ : Très bien

TC : Bien



TC : petit pb (même que Thomas), la "preuve" de la caractérisation est en fait une définition



Rq: Bien de mettre un contre-exemple aussi ! :)



TC : la preuve de test par réécriture est cool, mais [essaye de trouver un truc à redire mais n'en trouve pas et finalement se rétracte]

Peut-être rajouter une seconde preuve (rapide, ici test par permutation) ?



TC : pour les extensions, ça fait un peu catalogue
