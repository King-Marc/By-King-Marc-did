t = int(input ('La seconde est: '))

h = t // 3600
r = t % 3600
m = r // 60
s = r % 60
print(h,'H:',m,'M:',s,'S')