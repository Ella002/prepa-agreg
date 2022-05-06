from typing import List, Callable

import random
import matplotlib.pyplot as plt

from strats import next_fit, fit_first, best_fit, waste
from strats import best_fit_decreasing, fit_first_decreasing

def generate(n: int, c: int) -> List[int]:
    ''' generate(n, c) génère une liste de n objets de taille aléatoire, au plus c
    '''
    res = []
    for _ in range(n):
        res.append(random.randint(1, c))
    return res

nb_simu = 500
global_c = 10
n_values = [ (i+1)*10 for i in range(10) ]

def simu_n_strat(n: int, strat: Callable[[List[int], int], int]) -> float :
    ''' simu_n_strat(n, strat) fait tourner la stratégie strat
    sur des listes d'objets aléatoires, de taille n,
    et renvoie la moyenne des pertes
    NB: le nombre de simulations et la taille des conteneurs sont des variables globales
    '''
    wastes : List[int] = []
    for _ in range(nb_simu):
        # on genere une liste aléatoire
        objects : List[int] = generate(n, global_c)
        # on calcule la perte et on l'ajoute à la liste
        wastes.append(waste(strat, objects, global_c))
    return sum(wastes)/len(wastes)

def simu():
    ''' simu() appelle simu_n_strat pour toutes les valeurs de n et toutes les stratégies,
    et affiche le résultat sous forme d'un graphe
    '''
    pertes_nf : List[float] = [ simu_n_strat(n, next_fit) for n in n_values ]
    pertes_ff : List[float] = [ simu_n_strat(n, fit_first) for n in n_values ]
    pertes_bf : List[float] = [ simu_n_strat(n, best_fit) for n in n_values ]
    pertes_bfd : List[float] = [ simu_n_strat(n, best_fit_decreasing) for n in n_values ]
    pertes_ffd : List[float] = [ simu_n_strat(n, fit_first_decreasing) for n in n_values ]

    fig, ax = plt.subplots()
    ax.plot(n_values, pertes_nf, label='next fit')
    ax.plot(n_values, pertes_ff, label='fit first')
    ax.plot(n_values, pertes_bf, label='best fit')
    ax.plot(n_values, pertes_bfd, label='best fit decreasing')
    ax.plot(n_values, pertes_ffd, label='fit first decreasing')
    ax.set_xlabel('n')
    ax.set_ylabel('pertes moyennes')
    ax.legend()
    plt.show()

simu()
