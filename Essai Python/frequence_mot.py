f = open ('lire.txt', 'r')

list_unique = []
content = f.read()
list_mot = content.split()
f.close()

for mot in list_mot:
    if mot not in list_unique:
        list_unique.append(mot)
        print('Frequence d"apparition de:'+mot,list_mot.count(mot))