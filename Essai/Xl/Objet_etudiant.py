class Etudiant:
    def __init__(self, nom, admissibilite):
        self.nom = nom
        self.admissibilite = admissibilite
try:
    with open ("fichier_etudiants.txt","r") as fic:
        fichier = list()
        noms = list()
        cotes = list()
        for ligne in fic:
            fichier.append(ligne)
        for i in fichier:
            i.split()
        for j in range(len(fichier)):
            nombre = 0
            index = 0
            debut_nom = 0
            fin_nom = 0
            debut_cote1 = 0
            fin_cote1 = 0
            debut_cote2 = 0
            fin_cote2 = 0
            debut_cote3 = 0
            fin_cote3 = len(fichier[j])
            for k in range(len(fichier[j])):
                index = index+1
                if fichier[j][k] == "|":
                    nombre = nombre+1
                    if nombre == 1:
                        fin_nom = (index)-1
                        debut_cote1 = (index)
                    elif nombre == 2:
                        fin_cote1 = (index)-1
                        debut_cote2 = (index)  
                    elif nombre == 3:
                        fin_cote2 = (index)-1
                        debut_cote3 = (index)
            noms.append(fichier[j][debut_nom:fin_nom])
            cotes.append(list())
            cotes[j].append(int(fichier[j][debut_cote1:fin_cote1]))
            cotes[j].append(int(fichier[j][debut_cote2:fin_cote2]))
            cotes[j].append(int(fichier[j][debut_cote3:fin_cote3]))
    etudiant = list()
    
    admissibilite = ""
    for i in range(len(noms)):
        somme = 0
        for j in range(3):
            somme = somme + cotes[i][j]
        moyenne = somme/3
        if moyenne < 10:
            admissibilite = "N"
        elif moyenne >= 10 and moyenne < 12:
            admissibilite = "P"
        elif moyenne >= 12 and moyenne < 14:
            admissibilite = "AB"
        elif moyenne >= 14 and moyenne < 16:
            admissibilite = "B"
        else:
            admissibilite = "TB"
        etudiant.append(Etudiant(noms[i],admissibilite))
    for objet in etudiant:
        print("{} : {}".format(objet.nom,objet.admissibilite))
                 
except FileNotFoundError:
    print("Le fichier n\'existe pas!")
    with open ("fichier_etudiants.txt", "w") as fic:
        pass
