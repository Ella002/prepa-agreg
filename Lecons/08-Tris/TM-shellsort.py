from random import randint
from math import log2,floor
from  typing import *



def random_list(longeur: int, borne_sup:int)->List[int]:
	"""génère une liste de longeur longeur d'entier aléatoires entre 0 et borne_sup"""
	i:int
	lst_res:List[int]=[]
	for i in range(longeur):
		lst_res.append(randint(0,borne_sup))
	return lst_res




def shellsort(lst:List[int],gaps:List[int], verbose:bool=False)->None:
	""" trie la liste lst par shell sort avec gaps pour liste des pas .
	Précondition: gaps est une liste décroissante d'entier finissant par 1. 
	La complexité dépends de gaps"""
	j:int
	temp:int
	for gap in gaps:
		#on fait le tri par insertion des sous-listes d'éléments d'indice congru modulo gap
		for j in range(gap,len(lst)):
			temp=lst[j]
			while ((j>=gap) and (lst[j]<lst[j-gap])):
				#on échange lst[j] et  lst[j-gap]
				lst[j]=lst[j-gap]
				lst[j-gap]=temp
				j= j-gap
		if verbose==True:
			#Si en mode verbose affiche la liste et on attends une entrée:
			print("pas:"+str(gap))
			print(lst)
			input()


#Construction de differentes listes de pas

def gap_shell(n:int)->List[int]:
	#liste  des pas [n/2,n/4,...,1]
	#induit une complexité O(n^2)
	return [n//(2**k) for k in range(1,floor(log2(n))+1)]

def gap_hibard(n:int)->List[int]:
	#liste  des pas de la forme 2**k -1
	#induit une complexité O(n^(3/2))
	return [(2**k)-1 for k in range(floor(log2(n+1)),0,-1)]

def gap_pratt(n:int)->List[int]:
	"""liste des entiers qui n'ont pas de diviseurs premier >3 (nombre 3-friable) entre 1 et n
	induit une complexité O(n(log(n))^2)
	algorithme fonctionnant en temps O(log^2(n)) car le nombre d'entiers 3 friable est dominé par log^2(n)"""
	liste_pas:List[int]=[1]
	indice_non_inclus_2:int=0
	indice_non_inclus_3:int=0
	valeur_non_inclus_2=2
	valeur_non_inclus_3=3
	fini_2:bool= False
	fini_3:bool= False
	while ((fini_3==False) or (fini_2==False)) :
		if (valeur_non_inclus_3<valeur_non_inclus_2):
			#Si le prochain entier friable est obtenu comme multiple de 3
			liste_pas.append(valeur_non_inclus_3)
			indice_non_inclus_3+=1
			valeur_non_inclus_3=3*liste_pas[indice_non_inclus_3]
			if valeur_non_inclus_3==valeur_non_inclus_2:
				indice_non_inclus_3+=1
				valeur_non_inclus_3= 3*liste_pas[indice_non_inclus_3]

			if valeur_non_inclus_3>=n:
				#si le prochain entier friable obtenu comme multiple de 3 est trop grand
				fini_3= True
		else:
			#Si le prochain entier friable est obtenu comme multiple de 2
			liste_pas.append(valeur_non_inclus_2)
			indice_non_inclus_2+=1
			valeur_non_inclus_2= 2*liste_pas[indice_non_inclus_2]
			if valeur_non_inclus_3==valeur_non_inclus_2:
				indice_non_inclus_2+=1
				valeur_non_inclus_2=2* liste_pas[indice_non_inclus_2]

			if valeur_non_inclus_2>=n:
				#si le prochain entier friable obtenu comme multiple de 2 est trop grand
				fini_2= True
	liste_pas.reverse()
	return liste_pas
#Remarque: cette fonction est correcte car on ne croisent les doublons que lorsque l'on cherche à les insérer tout les deux.et que l'ensemble des entiers 3-friables est l'ensemble defini par induction par {1} et les fonctions x->2x et x->3x.




taille:int= 250
borne:int=300

liste:List[int]=random_list(taille,borne)

#tri insertion
#liste_pas:List[int]=[1]

# pas de shell
#liste_pas:List[int]=gap_shell(taille)

# pas de hibard
liste_pas:List[int]=gap_hibard(taille)

#pas de pratt
#liste_pas:List[int]=gap_pratt(taille)


#shellsort(liste,liste_pas,True)

#print(liste)



