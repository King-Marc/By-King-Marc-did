nombre = int(input("ENTREZ LE N:"))
ma_liste = list()
matrice = list()
debut = 4*nombre - 4
fin = nombre + 1
counter = 0 
for j in range(nombre):
    if j == 0:
            for i in range(nombre):
                ma_liste.append(i+1)
            matrice.append(ma_liste)
            ma_liste = list()
            
    else:
        counter1 = nombre*nombre - (nombre - 1)//2 + 1
        counter2 = nombre*nombre - nombre
        counter = debut + 1
        if j < (nombre - 1)//2:
                counter = debut + 1
        else :
                counter = debut - 1
        for i in range(nombre):
            if i == 0 :
                ma_liste.append(debut)
                    
                
            elif i == nombre - 1:
                ma_liste.append(fin)
                fin = fin + 1 
            else :
                
                
                if j < (nombre - 1)//2:
                    ma_liste.append(counter)
                    counter = counter + 1
                elif j == (nombre - 1)//2 :
                    if i == (nombre - 1)//2:
                       ma_liste.append(nombre*nombre)
                    elif i < (nombre - 1)//2:
                        ma_liste.append(counter1)
                        counter1 = counter1 + 1
                    else:
                        ma_liste.append(counter2)
                        counter2 = counter2 + 1
                else:
                    ma_liste.append(counter)
                    counter = counter - 1
    
                
        matrice.append(ma_liste)
        ma_liste = list()
        debut = debut - 1
for chose in matrice:
    print(chose)
