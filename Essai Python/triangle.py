L = int(input('Nombre de lignes: '))

for i in range(1, L+1):
    for j in range(1,L-i+1):
        print(' ',end='')
    for j in range(1,2*i-1+1):
            if j == 1 or j == 2*i-1 or i == L:
                print('* ', end='')
            else:
                 print(' ',end='')

            
    print()