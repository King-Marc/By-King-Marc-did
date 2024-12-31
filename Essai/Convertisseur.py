passer = False
while(1):
    try:
        secondes = int(input("Saisir le nombre de secondes : "))
    except ValueError :
        print("Veuillez entrer un entier")
    else:
        passer = True
    if passer:
        break
if secondes//(60*60*24*365) > 0:
    print("Nombre d'annees =",secondes//(60*60*24*365))
if (secondes%(60*60*24*365))//(60*60*24*30) > 0:
    print("Nombre de mois =",(secondes%(60*60*24*365))//(60*60*24*30))
if ((secondes%(60*60*24*365))%(60*60*24*30))//(60*60*24) > 0:
    print("Nombre de jours = ",((secondes%(60*60*24*365))%(60*60*24*30))//(60*60*24))
if (((secondes%(60*60*24*365))%(60*60*24*30))%(60*60*24))//(60*60) > 0:
    print("Nombre d'heures =",(((secondes%(60*60*24*365))%(60*60*24*30))%(60*60*24))//(60*60))
if ((((secondes%(60*60*24*365))%(60*60*24*30))%(60*60*24))%(60*60)//60) > 0:
    print("Nombre de minutes =",((((secondes%(60*60*24*365))%(60*60*24*30))%(60*60*24))%(60*60)//60))
if ((((secondes%(60*60*24*365))%(60*60*24*30))%(60*60*24))%(60*60))%60 > 0: 
    print("Nombre de secondes =",((((secondes%(60*60*24*365))%(60*60*24*30))%(60*60*24))%(60*60))%60)
