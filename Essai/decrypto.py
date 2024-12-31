phrase = input("Entrez votre phrase: ")
alpha = "abcdefghijklmnopqrstuvwxyz"
reponse = ""
lettre = "z"
espace = " "
position = 0
for i in range(len(phrase)):
    if phrase[i] != "a":
        if phrase[i] != " ":
            position = alpha.find(phrase[i])
            reponse = "{}{}".format(reponse, alpha[position -1])
        else :
            reponse = "{}{}".format(reponse,espace)
    else :
        reponse = "{}{}".format(reponse,lettre)
print(reponse)
