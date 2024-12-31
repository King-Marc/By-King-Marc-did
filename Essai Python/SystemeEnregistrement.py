import tkinter as tk
from tkinter import messagebox
#import sqlite3 

fenetre = tk.Tk()
fenetre.title('GestionT')

listbox = tk.Listbox(fenetre, font = ('Arial', 12), selectbackground= '#4286f4', selectforeground= 'white')
listbox.pack(pady= 10, padx= 10, fill= tk.BOTH, expand= True)

entry= tk.Entry(fenetre, font = ('Arial', 12))
entry.pack(pady= 5, padx= 10)

frame_boutons= tk.Frame(fenetre)
frame_boutons.pack(pady= 5)

def ajouter():

    tache= entry.get()
    if tache:
        listbox.insert(tk.END, tache)
        entry.delete(0, tk.END)

def supprimer():
    index= listbox.curselection(index)
    if index:
        Select= listbox.get(index)
        confirm= messagebox.askyesno('Confirmation', f'Voulez-vous vraiment supprimer', (Select))
        if confirm:
            listbox.delete(index)


bouton_add= tk.Button(frame_boutons, text= 'Ajouter', command= ajouter, font = ('Arial', 12),
bg= '#4286f4', fg= 'white', relief= 'flat', padx= 10)
bouton_add.pack(side= tk.LEFT, padx= 5)

bouton_supp= tk.Button(frame_boutons, text= 'Supprimer', command= supprimer, font = ('Arial', 12),
bg= '#f44336', fg= 'white', relief= 'flat', padx= 10)
bouton_supp.pack(side= tk.LEFT, padx= 5)

fenetre.mainloop()