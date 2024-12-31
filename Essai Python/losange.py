L = int(input('Nombre de lignes: '))

for i in range (1, L+1):
    for j in range(1,L-i+1):
        print(' ',end='')
    for j in range(1,L+1):
        print('* ',end='')
    print()