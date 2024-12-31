

x=input("Cours 1: ")
y=input("Cours 2: ")
z=input("Cours 3: ")
r=input("Cours 4: ")
j=input("Cours 5: ")


x=int(x)
y=int(y)
z=int(z)
r=int(r)
j=int(j)
k=((x+y+z+r+j)*100)/100

if k<60:

    print(f'Echec avec {k}','%')

elif k>=60 and k<70:

    print(f'Passe avec {k}','%')

elif k>70:

    print(f'Disticntion avec {k}','%')
