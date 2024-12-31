note1=input("Entrer la note1: ")
note2=input("Entrer la note2: ")
note3=input("Entrer la note3: ")
note4=input("Entrer la note4: ")
note5=input("Entrer la note5: ")


note1=int(note1)
note2=int(note2)
note3=int(note3)
note4=int(note4)
note5=int(note5)
moy=(note1+note2+note3+note4+note5)/5

if moy>=16:

    moy=(note1+note2+note3+note4+note5)/5
    print("Mention Tres bien", moy)
    input()

elif moy>=14:

    moy=(note1+note2+note3+note4+note5)/5
    print("Mention Bien", moy)
    input()

elif moy>=12:

    moy=(note1+note2+note3+note4+note5)/5
    print("Mention Assez bien", moy)
    input()

elif moy>=10:

    moy=(note1+note2+note3+note4+note5)/5
    print("Mention Passable", moy)
    input()

elif moy>=8:

    moy=(note1+note2+note3+note4+note5)/5
    print("Admis oral du deuxieme groupe", moy)
    input()

else:
    print("Recaler")
    