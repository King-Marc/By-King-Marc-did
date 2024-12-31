nombre = int(input("entrez votre nombre: "))
a = nombre
precision = nombre * 10

while a*a <= nombre - 1 or a*a >= nombre + 1:
    a = (a+nombre/a)/2
    print(a)

print("la racine carre de {} est {}".format(nombre,a))
