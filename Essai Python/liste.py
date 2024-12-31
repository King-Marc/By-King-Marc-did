L = []

for i in range(1,11):
    print('L[',i,']=', end='')
    L.append(int(input()))
L.sort(reverse= True)
print(L[1])