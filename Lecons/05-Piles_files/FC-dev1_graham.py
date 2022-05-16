from typing import List, Tuple
from mypy import *
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import random as rd

TAILLE_MAX = 100
NB_POINTS = 20
LARG_MIN = 0
LARG_MAX = 100
HAUT_MIN = 0
HAUT_MAX = 100

## Structure de pile

class Pile:
    iTete : int
    contenu : List[Tuple[int,int]]
    
    def __init__(self, tailleMax : int) -> None:
        self.iTete = -1
        self.contenu = [(0, 0) for i in range(tailleMax)]
        
    def est_vide(self) -> bool:
        return self.iTete < 0
    
    def est_plein(self) -> bool:
        return self.iTete == len(self.contenu)-1
    
    def sommet(self) -> Tuple[int, int]:
        assert not self.est_vide()
        return self.contenu[self.iTete]
    
    def empile(self, elt : Tuple[int, int]) -> None:
        assert not self.est_plein()
        self.iTete += 1
        self.contenu[self.iTete] = elt
    
    def depile(self) -> Tuple[int, int]:
        assert not self.est_vide()
        res : Tuple[int, int] = self.contenu[self.iTete]
        self.iTete -= 1
        return res
    

def sous_sommet(p : Pile):
    """Prend une pile en entrée, 
    renvoie la valeur du 2e element de la pile, sans modifier la pile""" 
    s : Tuple[int, int] = p.depile()
    res : Tuple[int, int] = p.sommet()
    p.empile(s)
    return res
    
## Fonctions auxiliaires de calcul

def trouve_min(lp : List[Tuple[int, int]]) -> Tuple[int, int] :
    """Prend une liste de points du plan,
    renvoie le point le plus bas (y minimal), et le plus à gauche si égalité"""
    iMin : int = 0
    for i in range(len(lp)):
        if lp[i][0] < lp[iMin][0]:
            iMin = i
        elif lp[i][0] == lp[iMin][0] and lp[i][1] < lp[iMin][1]:
            iMin = i
    return lp[iMin]

def calcule_angle(p0 : Tuple[int, int], p1  : Tuple[int, int], p2 : Tuple[int, int]) -> float:
    """Prend trois points du plan, 
    renvoie la valeur de l'angle formé par les trois points"""
    v1 = (p0[0] - p1[0], p0[1] - p1[1])
    v2 = (p2[0] - p1[0], p2[1] - p1[1])
    
    return np.arctan2(v2[0], v2[1]) - np.arctan2(v1[0], v1[1])

def ordonner_points(lp : List[Tuple[int, int]], min_p : Tuple[int, int]) -> List[Tuple[int,  int]]:
    """Prend une liste de points du plan, et le premier point (bas à gauche)
    renvoie la liste triée dans le sens trigonométrique"""
    # On commence par calculer l'angle pour chaque point
    p_ref = (min_p[0]+1, min_p[1]) # pour avoir une base horizontale
    inter_list : List[Tuple[float, int, int]] = []
    for (i, j) in lp:
        inter_list.append((calcule_angle(p_ref, min_p, (i, j)), i, j))
    
    inter_list.sort() # enfin on trie la liste obtenue
    
    res : List[Tuple[int, int]] = []
    
    for (_, i, j) in inter_list:
        res.append((i, j))
    
    return res[1::] # on enlève le plus petit point, qui est déjà considéré
    


## Générations de l'ensemble de points

def creer_nuage(nb_points : int = NB_POINTS) -> List[Tuple[int, int]]:
    res : List[Tuple[int, int]] = []
    for i in range(nb_points):
        res.append((rd.randint(LARG_MIN, LARG_MAX), rd.randint(HAUT_MIN, HAUT_MAX)))
    
    return res


## Fonctions d'affichage
def affiche_points(lp : List[Tuple[int, int]], p : Pile) -> None:
    """Prend en entrée la liste de tous les points, et la pile donnant les arêtes de l'enveloppe convexe construite pour le moment et fait un affichage des données"""
    X : List[int] = []
    X_p : List[int] = []
    Y : List[int] = []
    Y_p : List[int] = []
    
    for (i, j) in lp:
        Y.append(i)
        X.append(j)
        
    while not p.est_vide():
        (i, j) =  p.depile()
        Y_p.append(i)
        X_p.append(j)
    
    # Attention il faut rétablir la pile !
    for i in range(len(X_p)-1, -1, -1):
        p.empile((Y_p[i], X_p[i]))
    
    plt.plot(X, Y, '+', linestyle="dotted")
    plt.plot(X_p, Y_p)
    plt.show()
    plt.pause(1)
    plt.close()
    
def affichage_en_cours(a : bool, p : Pile, lp_ord : List[Tuple[Int, Int], i : int):
    if a :
        p.empile(lp_ord[i])
        affiche_points(lp_ord, p)
        p.depile()              



## Algorithme de Graham

def balayage_graham(lp : List[Tuple[int, int]], affichage : bool = True) -> Pile:
    """prend une liste de points du plan en entrée,
    retourne une pile dont les éléments forment une enveloppe convexe
    de l'ensemble de points donné en entrée.
    L'argument facultatif permet un affichage graphique de l'exécution de l'algorithme"""
    
    p0 : Tuple[int, int] = trouve_min(lp) # on prend le point le plus bas
    lp_ord : List[Tuple[int, int]] = ordonner_points(lp, p0) # on ordonne les points dans l'ordre trigonométrique, selon p0
    s : Pile = Pile(TAILLE_MAX)
    
    s.empile(p0)
    s.empile(lp_ord[0]) # initialisation de la pile
    
    plt.ion() # pour l'affichage
    
    for i in range(1, len(lp_ord)): # parcours des points
        
        c = calcule_angle(sous_sommet(s), s.sommet(), lp_ord[i])
        while (np.pi > c > 0 or c < -np.pi):
            # si le point ajouté va "vers l'extérieur"
            # on enlève le point intermédiaire
            affichage_en_cours(affichage, s, lp_ord[i])  
            s.depile()
            c = calcule_angle(sous_sommet(s), s.sommet(), lp_ord[i])
        s.empile(lp_ord[i])
        
        if affichage :
            affiche_points(lp_ord, s)
            
    plt.pause(20) # encore pour l'affichage
    
    return s
    