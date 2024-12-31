# -*- coding: utf-8 -*-
import itertools
import copy

n = input("Combien de nombres allez-vous entrez : ")
liste = list()
reference = list()
somme = list()
produit = list()
compare = list()

for i in range(int(n)):
    liste.append(int(input("Donner le nombre {}:".format(i+1))))
reference = copy.deepcopy(liste)
for j in range(len(liste)):  
    permute = itertools.permutations(liste,j)
    for item in permute:
        for element in item:
            reference.remove(element)          
    
for item in permute:
    print( item[:])
    