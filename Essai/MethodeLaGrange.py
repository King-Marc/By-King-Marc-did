
def f(x):
    return x**2-4

# Implémentation de la méthode de fausse position 
def fausseposition(x0,x1,e):
    pas = 1
    print('\n\n*** IMPLEMENTATION DE LA METHODE DE LAGRANGE ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.6f et f(x2) = %0.6f' % (pas, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        pas = pas + 1
        condition = abs(f(x2)) > e

    print('\nLa racine recherchée est: %0.5f' % x2)


# Estimations en entrées

x0 = float(input("Première estimation: "))
x1 = float(input("Deuxième estimation: "))
e = float(input('Erreur Tolérable : '))
z = 5/x0

    
# Verification de la validite des valeurs des estimations et du faux positionnement
if f(x0) * f(x1) > 0.0:
    print("Les estimations fournies n'encadrent pas la racine")
    print("Réessayez avec des valeurs différentes")
else:
    fausseposition(x0,x1,e)
