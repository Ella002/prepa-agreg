from random import randint
from math import log2,floor
from  typing import *
from time import sleep
from shellsort import *

taille:int= 250


def  test_pratt()->None:
	#fonction de test avec les pas de Pratt
	for i in range(100):
		liste:List[int]=random_list(taille,borne)
		liste_pas:List[int]=gap_pratt(taille)
		shellsort(liste,liste_pas)
		liste_test:List[int]= sorted(liste)
		assert liste==liste_test

def  test_shell()->None:
	#fonction de test avec les pas de Shell
	for i in range(100):
		liste:List[int]=random_list(taille,borne)
		liste_pas:List[int]=gap_pratt(taille)
		shellsort(liste,liste_pas)
		liste_test:List[int]= sorted(liste)
		assert liste==liste_test

