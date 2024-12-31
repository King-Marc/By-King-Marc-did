from tkinter import *
import sqlite3

root = Tk()
root.title('Agenda')
root.geometry('450×450')
matricule = Label(root, text = 'Matricule : ')
prenom = Label(root, text = 'Prenom : ')
nom = Label(root, text = 'Nom : ')
email = Label(root, text = 'Mail : ')
tel = Label(root, text = 'Telephone : ')

e_matricule = Entry(root, width = 35)
e_prenom = Entry(root, width = 35)
e_nom = Entry(root, width = 35)
e_email = Entry(root, width = 35)
e_tel = Entry(root, width = 35)

matricule.grid(row = 0, column = 0)
e_matricule.grid(row = 0, column = 0)
prenom.grid(row = 0, column = 0)
e_prenom.grid(row = 0, column = 0)
nom.grid(row = 0, column = 0)
e_nom.grid(row = 0, column = 0)
email.grid(row = 0, column = 0)
e_email.grid(row = 0, column = 0)
tel.grid(row = 0, column = 0)
e_tel.grid(row = 0, column = 0)

root.mainloop()