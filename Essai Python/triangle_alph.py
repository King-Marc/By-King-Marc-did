L = int(input('Nombre de lignes: '))

for i in range (1, L+1):
    for j in range(i):
        n=65
        for j in range(i):
            print(chr(n),end='\t')
            n +=1
        print()