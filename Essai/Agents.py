try :
    with open ("fichier_agents.txt", "a") as fic:
        option = input("Ajouter un agent (1/0) : ")
        while option == "1":
            fic.write(input("Matricule : "))
            fic.write("|")
            fic.write(input("Nom : "))
            fic.write("|")
            fic.write(input("Grade : "))
            fic.write("|")
            fic.write(input("Salaire base : "))
            fic.write("|")
            fic.write(input("Prime : "))
            fic.write("\n")
            option = input("Ajouter un agent (1/0) : ")
    with open ("fichier_agents.txt", "r") as fic:
        fichier = list()
        salaire = list()
        prime = list()
        for ligne in fic:
            fichier.append(ligne)
        for i in fichier:
            i.split()
        for j in range(len(fichier)):
            nombre = 0
            index = 0
            debut = 0
            fin = 0
            for k in range(len(fichier[j])):
                index = index+1
                if fichier[j][k] == "|" and j != 0:
                    nombre = nombre+1
                    if nombre == 3:
                        debut = (index)
                    if nombre == 4:
                        fin = (index)-1
            if j != 0:
                prime.append(int(fichier[j][fin+1:len(fichier[j])]))
                salaire.append(int(fichier[j][debut:fin]))
        print(prime[:])
        taux = list()
        for i in range(len(salaire)):
            if salaire[i] < 1000:
                taux.append(10)
            elif salaire[i] >= 1000 and salaire[i] < 2500:
                taux.append(15)
            elif salaire[i] >= 2500 and salaire[i] < 5000:
                taux.append(30)
            else:
                taux.append(50)
        print("Matricule|Nom|Grade|Salaire base|Prime|Salaire brut|impot|Salaire net")
        for i in range(len(fichier)):
            if i != 0:
                print("{}|{}|{}|{}".format(fichier[i][:-1],salaire[i-1]-(salaire[i-1]*(taux[i-1]/100)),(salaire[i-1]*(taux[i-1]/100)),(salaire[i-1]-(salaire[i-1]*(taux[i-1]/100)))+prime[i-1]))
        print("Nombre d'agents : {}".format(len(salaire)))
        total_salaire = 0
        total_prime = 0
        total_salaire_brut = 0
        total_impot = 0
        total_salaire_net = 0
        for i in range(len(salaire)):
            total_salaire = total_salaire+salaire[i]
            total_prime = total_prime+prime[i]
            total_salaire_brut = total_salaire_brut+salaire[i-1]-(salaire[i-1]*(taux[i-1]/100))
            total_impot = total_impot + (salaire[i-1]*(taux[i-1]/100))
            total_salaire_net = total_salaire_net + (salaire[i-1]-(salaire[i-1]*(taux[i-1]/100)))+prime[i-1]
            
        print("Total salaire de base : {}".format(total_salaire))
        print("Total prime : {}".format(total_prime))
        print("Total salaire brut : {}".format(total_salaire_brut))
        print("Total impot : {}".format(total_impot))
        print("Total salaire net : {}".format(total_salaire_net))
        
            
        
            
except FileNotFoundError:
    print("Le fichier n\'existe pas!")
    with open ("fichier_agents.txt", "w") as fic:
        fic.write("Matricule")
        fic.write("|")
        fic.write("Nom")
        fic.write("|")
        fic.write("Grade")
        fic.write("|")
        fic.write("Salaire base")
        fic.write("|")
        fic.write("Prime")
        fic.write("\n")
