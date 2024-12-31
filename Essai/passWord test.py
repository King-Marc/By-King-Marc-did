passWords = ["King_Marc","Regis","Christian","Amani","Mutahali","Davina","Betty"]
motDePasse = input("ENTREZ VOTRE MOT DE PASSE: ")
motDePasse = motDePasse.lower()
compteur = 0
i = 0
while i < len(passWords) :
    if motDePasse == passWords[i]:
        print("MOT DE PASSE CORRECT")
        break
    else:
        compteur = compteur + 1
        i = i+1 
        if compteur == len(passWords):
            compteur = 0
            motDePasse = input("MOT DE PASSE INCORRECTE! ENTREZ UN MOT DE PASSE VALIDE: ")
            i = 0

name = input("Entrez votre nom: ")
postname = input("Entrez votre postnom: ")
prename = input("Entrez votre prenom: ")
print("...................Va te faire voir.................!")
