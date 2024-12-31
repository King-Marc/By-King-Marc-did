import math 
N = int(input("La valeur de N: "))
S = 0

for i in range(1,N+1):
    S = S+ 1/i

print('La somme est: ',S)