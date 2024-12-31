f1= open('lire.txt','r')
f2= open('lire1.txt')

cont1=f1.read()
cont2=f2.read()
l1=cont1.split()
l2=cont2.split()
f1.close()
f2.close()

mot_commun = []
for mot in l1:
    if mot in l2 and mot not in mot_commun:
        mot_commun.append(mot)
print (mot_commun)