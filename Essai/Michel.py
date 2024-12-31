from random import*


etage1 = int(input("entrez l'étage ou vous etes:"))
etageinf = list()
insist = int(input("insisteriez-vous?"))
immeuble = int(input("entrez le nombre total des etages de l'immeuble"))
persmont = list()
choix = 0
while choix == 0:
    count = 0
    num = ''
    for i in range(1,etage1):
        dee = randint(1,5)
        if dee == 1:
            count = count + 1
            persmont.append(i)
    if count == 0:
         print("l'assensceur est dispo du premier bord")
    else :
     if insist == 1 and count > 0:
        k = 0
        while k < len(persmont):
                val = randint(persmont[k]+1,immeuble)
                k = k+1
                if val < etage1:
                    for s in range(len(persmont)):
                            if val == persmont[s]:
                                if k < len(persmont)-1:
                                    k = persmont.index(val)
                                    print("passé par ici")
                                    break
                 
                            
                            
                        
            
                elif val == etage1:
                        print("wow l'ascensseur est dispo")
                        break

                else:
                    print("desolé vous ratez l'assenseur il va au dessus")
                    break

      else:
            print("vous avez raté l'ascensseur vous n'avez pas insisté")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        choix = int(input("Appuyer 0: "))
        
