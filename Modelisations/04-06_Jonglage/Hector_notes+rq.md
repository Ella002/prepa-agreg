# Hector #



## Présentation ##



### Plan ###



   1. Modèle
   1. Caractérisation ~~Partie runjour 💯🔙 🎼🎤~~
   1. Énumération


### I — Modèle ###



Discrétisation du problème 🤫, durée d ∈ ℕ



Périodicité, période p ∈ ℕ



Exemple : motif "33"

```
__ __ __ __ __ __

      X  X  X  X  X

    \/ \/ \/ \/ \/ \/

    /\ /\ /\ /\ /\ /\

      3  3  3  3  3

```



Transition

```
        _____  ______

       /     \/      \

      /      /\       \

     /      /  \       \

    n    n+k    n+dn    n+(k+dn)

↓                    ↑

    ↓   _____________    ↑

    ↓  /             \   ↑

    ↓ /      __       \  ↑

    ↓/      /  \       \ ↑

    n    n+k    n+dn    n+(k+dn)
```



```
       ____________      ____________

    /                               \ /                              \

  /                                 /\                                  \

/                                /      \                                  \

n                            n+k    n+d\_n                          n+(k+d\_n)

↓                                                                                       ↑

↓     __________________________                  ↑

↓  /                                                                  \               X

↓/                                 __                                 \            ↑

/                                /      \                                  \         ↑

n                            n+k     d\_n - k                          n+(k+d\_n)
```




### II — Caractérisation ###



   * Test de la moyenne :
    d<sub>0</sub> … d<sub>p-1</sub>

    (1/p) ∑ d<sub>i</sub> = b



   * Tests  des permutations :
    a<sub>0</sub> … a<sub>p-1</sub>


```
                  a0                                    a1

       ____________      ____________

    /                               \ /                              \

  /                                 /\                                  \

/                                /      \                                  \



    a\_k + k[p]
```




   * Test de réécriture :
       * Un mot p est jonglable ssi on peut le construire à partir de transitions à partir de bp


[CODE]



### III — Énumération ###



A) Nombre de balles et période fixés

   * Énumération naïve
   * ???
   * Énumération par transitions


B) Nombre de balle et durée maximale d'un lancer fixés



## Remarques ##

Rq de Y : c'est beau du code avec des commentaires de doc 😍



Rq : Très improvisé, on voit que c'est bien compris, le programme est bien, mais effectivement la présentation est pas assez construite (on peut pas trop improviser une définition).



Rq (Jaume) : Présentation qui reste proche du texte, peu d'apports personnel.

Peut-être se concentrer sur des points plus précis, quitte à ne pas couvrir tout le sujet.



Rq: Faire le lien entre le problème et les noms de fonctions, il faut donner l'intention !
