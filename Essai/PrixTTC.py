passer = False
while(1):
    try:
        prixHT = float(input("Saisir le prix hors taxe : "))
    except ValueError :
        print("Veuillez entrer un nombre")
    else:
        if prixHT < 0:
            print("Vous avez saisi un nombre negatif!")
        else:
            passer = True
    if passer:
        break
        
    
taux_taxe = 15
prixTTC = ((prixHT*taux_taxe)/100)+ prixHT

if prixTTC < 100 :
    remise = 0
elif prixTTC >= 100 and prixTTC < 500:
    remise = 1
elif prixTTC >= 500 and prixTTC < 1000:
    remise = 5
else:
    remise = 8

print("La remise est de",(remise*prixTTC)/100)
print("Le nouveau prix toutes taxes comprises est de",prixTTC-((remise*prixTTC)/100))
