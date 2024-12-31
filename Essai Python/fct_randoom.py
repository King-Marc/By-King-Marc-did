from random import randint


for i in range(0,10):
    x = randint(1,6)
    if  x == 2 or x == 5:
        print('Vous avez gagnez')
    else:
        print('Loser!')
n = 0
for i in range(0,100):
    x = randint(1,6)
    if  x == 2 or x == 5:
        n+=1
print('Tu as gagnee', n, 'fois')
