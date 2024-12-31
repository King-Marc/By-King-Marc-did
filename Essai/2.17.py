
x=input("Prix HT d'un kilo de tomates: ")
y=input("Quantite voulue: ")
z=input("TVA est= ")

x=float(x)
y=int(y)
z=float(z)

prix_ttc=x*y*(1+z)

print("Le prix total est: ",prix_ttc )

input()
