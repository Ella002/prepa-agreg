# 07/04 - 13. Algorithmes d'ordonnancement et de gestion de ressources - Fanny



Développements :

   1. Optimalité et 2-approximation avec la règle de Smith (non-préparé)
   1. **Optimalité de l'ordonnancement de niveau** <- """choisi""" par le jury


## Développement



### Illustration sur un exemples



3 machines



16 tâches


```
J01 J02 J03 J04 J05 J06 J07 J08 J09 J10

   \  \  |  /  /     |   |    \  |  /

    \  | | |  /      \   /     | | |

     \ \ | / /        | |      \ | /

      \ ||| /         \ /       |||

       \\|//           |        \|/

        J11           J12       J13

          \           /          |

           \         /           |

            \       /            |

             \     /             |

              \   /              |

               J14              J15

                  \             /

                   \           /

                    \         /

                     \       /

                      \     /

                       \   /

                        J16
```


M3 J03 J06 J09 J12

M2 J02 J05 J08 J11 J14

M1 J01 J04 J07 J10 J13 J15 J16



### Lemmes



Je faisais le dessin j'ai pas noté les lemmes

huhu









### Preuve finale



Supposons par l'absurde que l'ordonnancement n'est pas optimal, soit n le plus petit entier tel qu'il existe n tâches telles que l'ordonnancement delta soit plus petit que l'ordonnancement optimal



D'après les lemmes, il existe une machine M\_i libre à delta - 2

On retire toutes les tâches de niveau 2, ce qui permet de rapprocher la dernière tâche d'un instant pour la solution par niveau ;

Et cela permet aussi de diminuer la solution optimale d'un instant.

On a donc un contre-exemple d'optimalité strictement plus petit, ce qui contredit l'hypothèse absurde.





## Questions







## Remarques

RqDManet : le "D(I(t)) descendants" écrit en 2cm sur le bas du tableau c'est tendu en vrai ^^

RqDManet : C'est bizzare que toutes les feuilles soient au même niveau

Rq : Les diagrammes de Gantt, je ne m'en sers pas dans la vie de tous les jours. Pourquoi avoir décider d'en parler si c'est si nul ?

Rq : Ordonnancement EDF incontournable

Rq : Lien avec le sac à dos (encore lui !)
