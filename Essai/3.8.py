
note=input("Entrer la note obtenue: ")

note=int(note)

if note>=16:
    print("Mention TB ")
    input()
elif note>=14:
    print("Mention B")
    input()
elif note>=12:
    print("Mention AB")
    input()
elif note>=10:
    print("Mention Passable")
    input()
else: 
    print("Mention Insuffisant")
    input()