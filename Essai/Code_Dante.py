
nombre = int(input("ENTREZ LE N:"))
ma_liste = list()
matrice = list()

for i in range(nombre):
    if i == 0:
            for i in range(nombre):
                ma_liste.append(i+1)
            matrice.append(ma_liste)
            ma_liste = list()
    else:
        for i in range(nombre):
            ma_liste.append(0)
        matrice.append(ma_liste)
        ma_liste = list()

entry = nombre
for i in range(1,nombre):
    for j in range(nombre):
        if j+1 < len(matrice[i]) and matrice[i][j] == 0:
                 matrice[i][j] = entry
        elif j+1 == len(matrice[i]) and matrice[i][j] == 0:
            for k in range(nombre):
                matrice[k][nombre-1] = entry
                entry = entry
                
        entry = entry + 1
    ma_liste = list()
for item in matrice:
    print(item)
