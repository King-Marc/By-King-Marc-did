phrase = input("Entrez votre phrase: ")
alpha = "abcdefghijklmnopqrstuvwxyz"
reponse = ""
lettre = "a"
espace = " "
position = 0
signes = [",",";","?",'"',".","/","é","è","à","â","ê"]
for i in range(len(phrase)):
    count = 0
    if phrase[i] != "z":
        if phrase[i] != " ":
            position = alpha.find(phrase[i])
            reponse = "{}{}".format(reponse, alpha[position +1])
        else :
            reponse = "{}{}".format(reponse,espace)
    else :
        for l in signes:
            if phrase[i] == l:
                count = count + 1
               reponse = "{}{}".format(reponse,phrase[i])
        else:
            reponse = "{}{}".format(reponse,lettre)
print(reponse)
