try:
    with open ("ordre.txt","r") as fic2: 
        carnet = fic2.readlines()
    del carnet[0]
except FileNotFoundError:
    fic2 = open ("ordre.txt","w")
    carnet = list()

nouveau = list()

Nom = input("Nom : ")
Nom = Nom.lower()
Nom = Nom.title()
nouveau.append(Nom)

Prenom = input("Prenom : ")
Prenom = Prenom.lower()
Prenom = Prenom.title()
nouveau.append(Prenom)

nouveau.append(input("Numero : "))

Email = input("Email : ")
Email = Email.lower()
Email+="\n"
nouveau.append(Email)

carnet.append("|".join(nouveau))
carnet.sort()

with open ("ordre.txt","w") as fic1:
    fic1.write("Nom|Prenom|Numero|Email\n")
    for contact in carnet:     
        fic1.write(contact)
