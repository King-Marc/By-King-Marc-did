from math import*
from itertools import*    

contenu = list()
cardinal_classe = list()
les_classes = list()
classe = list()
zero = 0
fic = open("lesdonnees.txt","r")
contenu = list()
contenus = list()
contenu = fic.readline()
elements = list()
contenus = contenu.split(",")
contenus1 = list()
for item in contenus:
     zero = int(item)
     contenus1.append(zero)
contenus1.sort()
cardinal3 = len(contenus1)

step = int(input("entrez le pas:"))
transit = 0
inf = min(contenus1)
sup = inf + step 
while inf < max(contenus1):
    classe.append(inf)
    classe.append(sup)
    les_classes.append(classe)
    classe = list()
    count = 0
    for nombre in contenus1:
        if inf <= nombre < sup:
            count = count + 1
    cardinal_classe.append(count)
    inf = sup
    sup = sup + step
print("¦¦=========¦¦=====================¦¦==================¦¦============") 
print("¦¦ CLASSES ¦¦  ","EFFECTIF ABSOLU  ","¦¦ EFFECTIF RELATIF ¦¦")
for cls in les_classes:
     
    print("¦¦=========¦¦=====================¦¦==================¦¦============") 
    print("¦¦",cls,"¦¦",cardinal_classe[les_classes.index(cls)],"¦¦",cardinal_classe[les_classes.index(cls)]/len(contenus1))
    

            
    






    

