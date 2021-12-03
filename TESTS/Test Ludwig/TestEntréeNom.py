from tkinter import *

# from tkinter.messagebox import *

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Identification requise')


# enregistrer nom
def RecupName():
    "Enregistrer le ,nom"
    Name = EntreeNom.get()
    print("Nom :", Name)
    Mafenetre.destroy()


# Création d'un widget Label (texte 'Nom')
Label1 = Label(Mafenetre, text='Quel est ton nom jeune protecteur de la Galaxie? ', font=("Arial", 20))
Label1.pack(padx=100, pady=100)
# Création d'un widget Entry (champ de saisie)
Nom = StringVar()
EntreeNom = Entry(Mafenetre, textvariable=Nom, bg='bisque', fg='red', font=("Arial", 20), )
EntreeNom.focus_set()  # : nécessaire ?
EntreeNom.pack(padx=1, pady=1)
# Création d'un widget Button (bouton Valider)
BoutonValidNom = Button(Mafenetre, text='Valider', font=("Arial", 15), command=RecupName)
BoutonValidNom.pack(padx=95, pady=95)

Mafenetre.mainloop()
