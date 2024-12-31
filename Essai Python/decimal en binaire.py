#Convertion du decimal en autre methode
decimal = int(input('Entrez la valeur decimale: \n'))
convert = int(input('Convertir en: [1] Binaire, [2] Octal, [3] Hexadecimal: \n'))   #les valeurs en listes c'est pour determiner en quoi doit se faire  la convertion

if convert == 1:
    print('La convertion de la valeur saisie en binaire est: \n', bin(decimal))
elif convert == 2:
    print(('La convertion de la valeur saisie en decimal est: \n', oct(decimal)))

elif convert == 3:
    print(('La convertion de la valeur saisie en hexadecimal est: \n', hex(decimal)))

