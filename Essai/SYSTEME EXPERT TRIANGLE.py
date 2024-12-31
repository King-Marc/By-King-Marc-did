# SYSTEME EXPERT RECONNAISSANCE DES FIGURES GEOMETRIQUES

angleDroit = 0
deuxCoteId = True


base_des_regles = [
        {"nom" :"triangle",
         "angleDroit": 0,
         "ordre": 3},
         "deuxCoteId": False,
        {"nom" :"rectangle",
         "angleDroit": 4,
         "ordre": 4},
        {"nom" :"rectangle",
         "angleDroit": 4,
         "ordre": 4,
         "deuxCoteId" = True},
        {"nom" :"triangleRectangleQuelconque",
         "angleDroit": 1,
         "ordre": 3,
         "deuxCoteId" = False,
         
         },
        {"nom" :"triangleIsoceleQuelconque",
         "angleDroit": 0,
         "ordre": 3,
         "deuxCoteId" = True},
    
    ]
angleD = int(input("ENTRER LE NOMBRE D'ANGLE DROIT:"))
Ordre = int(input("ENTRER L'ORDRE DE VOTRE FIGURE:"))
count = 0
for item in base_des_regles:
    if angleD == item["angleDroit"] and Ordre == item["ordre"]:
        print("VOTRE FIGURE S'APPELLE:",item["nom"])
        count = count + 1
    if base_des_regles.index(item) == len(base_des_regles) - 1 and count == 0:
        print("CECI N'EST PAS UNE FIGURE GEOMETRIQUE")
