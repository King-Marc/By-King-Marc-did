import click

@click.command()

def main():
    print('Hello')
if __name__ == '__main__':
    main()

'''
class King_Marc:
    def __init__(self,nom,age,numero):
        self.nom = nom
        self.age = age
        self.numero = numero
    def classement(self):
        if self.age < 18:
            print("Vous etes mineur(e)")
        else:
            print("Vous etes majeur(e)")

h = King_Marc(input("Nom : "),int(input("Age : ")),input("Numero : "))
h.classement()

'''
