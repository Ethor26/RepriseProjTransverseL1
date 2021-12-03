# Ce fichier rescence les bouts de codes d'Harmonie musicale qui peuvent servir : il y a une partie graphique puis des
# fonctions

# PARTIE GRAPHIQUE :
import os
from tkinter import *
from tkinter.filedialog import askopenfile

# Déclaration de la fenetre Tkinter
wSaisieNouvellePartition = Tk()

# (TKINTER) LABEL : Libellés titre de la zone de saisie de k
lblEntrek = Label(wChoixTransformation, text="k=") # Nom de la fenêtre en rouge à déclarer comme au dessus (avec le nom
# de fenêtre qu'on veut
lblEntrek.place(x=430, y=50)

# (Tkinter)LISTBOX : Liste des titres des partitions de la base de données (déclaration & position )
lp = Listbox(wFenetrePrincipale)
lp.place(x=26, y=26, width=350, height=500)

# (TKINTER) ENTRY : Ligne de saisie de k
entrek = Entry(wChoixTransformation)
entrek.place(x=450, y=50, width=26)

# Bouton mettre à jour listbox
b6_1 = Button(wFenetrePrincipale, text='Mettre à jour la liste', command=commandBoutonMajListe) # Command = <fonction>
# mais sans paramètres
b6_1.place(x=410, y=550, width=150)

# (Tkinter)BUTTON   : Bouton Enregistrer
b9 = Button(wSaisieNouvellePartition, text='Enregistrer', command=commandBouton51)
b9.place(x=300, y=200, width=150)

# DEFINITION FENËTRE PRINCIPALE
def genererFenetrePrincipale(cheminAcces):
    print("genererFenetrePrincipale: cheminAcces= " + cheminAcces)  # Pour contrôle en console

    # (Tkinter)FENETRE:
    wFenetrePrincipale = Tk()  # Déclaration de l'objet wFenetrePRincipale
    wFenetrePrincipale.geometry('800x600')  # Taille de la fenêtre

    # (Tkinter)LABEL: Libellé titre (déclaration & position )
    lbl = Label(wFenetrePrincipale, text="HARMONIE MUSICALE")
    lbl.pack()  # Positionne le libellé sur la fenêtre (ou avec place pour position plus précise)

    # (Tkinter)LABEL: Libellé Auteurs (déclaration & position )
    lblautheurs = Label(wFenetrePrincipale, text="""EFREI - L1BN/2020-2021 : Ethan Suissa et Paul Galopin""")
    lblautheurs.place(x=11, y=550)

    # (Tkinter)LISTBOX : Liste des titres des partitions de la base de données (déclaration & position )
    lp = Listbox(wFenetrePrincipale)
    lp.place(x=26, y=26, width=350, height=500)

    # Variable(s) STRING
    messageUtilisateur = StringVar()  # Variable de message d'erreur de saisie type stringvar() pour maj Label
    messageUtilisateur.set('...')  # On initialise la variable

    # -----------------------*

    # FONCTION COMMUNE : Récupere le Numéro de la Ligne Sélectionné dans l'élément LISTBOX <lp>
    def recupereNoLigneSelectionne():
        noLigne = 0
        tupleSelectionne = lp.curselection()  # curselection() renvoie un tuple (n0 ligne, titre)
        if tupleSelectionne:
            noLigne = 1 + tupleSelectionne[0]  # No de ligne + 1
            print("numero de ligne selectionnee =" + str(noLigne))  # pour controle
            messageUtilisateur.set('...')  # On efface un message d'erreur utilisateur residuel, car OK
        return noLigne

    # FONCTION COMMANDE BOUTON : Alimentation de la liste par la base de donnees           *-------
    def commandBoutonMajListe():
        print("commandBoutonMajList appelle")  # pour contrôle
        lp.delete(0, END)  # Initialise la listBox nommé lp
        fichierBdd = open(cheminAcces, 'r')  # Ouverture de la base de donnees # r pour read
        lignes = fichierBdd.readlines()  # Lecture des lignes

        # insertion des lignes dans la listBox
        i = 0
        for ligne in lignes:
            if ligne.startswith("#"): # Choix d'inclure les lignes commencant par # dans la listbox
                i += 1
                lp.insert(i, ligne.upper())  # upper pour passer en majuscule

        fichierBdd.close()  # Fermeture du fichier base de donnees

    # FONCTION COMMANDE BOUTON : commande action du bouton 5-1 qui déclenche l'enregistrement des données de la fenetre
    # de saisie *-------
    def commandBouton51():

        # Récupération des données de la fenêtre
        titreAenregistrer = t1.get()  # Récupère donnée saisie dans t1 (Entry)
        partitionAenregistrer = t2.get("0.0", "end")
        # Récupère donnée saisie dans t2 (Text) de la position 0.0 jusqu'à la fin

        # Appel de la fonction qui met à jour la base de données
        message = AddInFile(titreAenregistrer, partitionAenregistrer, cheminAccesBdd)
        print(message)  # Pour contrôle en console

        if message == "OK":
            print(message)  # Pour contrôle en console
            wSaisieNouvellePartition.destroy()  # La partition a été enregistré dans la base de données. On ferme la
            # fenetre

        else:
            # La partition n'a pas été enregistré. on reste sur la fenetre de saisie et on affiche le message
            lblMessage = Label(wSaisieNouvellePartition, text=message)  # En cours de verification
            lblMessage.place(x=30, y=180, width=250)

# FONCTIONS UTILES :

# *******************************************************************************************
# FONCTION OUTIL: Renvoie la ligne choisie du fichier indiqué dans une chaine de caractère (équivalent de read_file_line
# avec le chemin d'accès en entrée)
# Auteur : Ethan SUISSA - Terminé
# Sortie : Chaine de caractère qui contient la ligne récupérée
def lireLaLignechoisie(chemin_acces, noLine):  # Entrée :  Chemin_acces = chemin d'acces du fichier, # noline = Numero
    # de la ligne
    line = ""
    # Vérifie si le chemin existe ou non
    import os.path
    if os.path.isfile(chemin_acces):
        print("Chemin ", chemin_acces, " existe")  # pour controle

        # Recupere le contenu de la ligne dans le fichier
        file = open(chemin_acces, 'r')
        for i in range(noLine):
            line = file.readline()
        file.close()
    else:
        print("Chemin ", chemin_acces, " n'existe pas")  # pour controle
    return line

# ***********************************************************************
# FONCTION OUTIL : Fonction qui ajoute une partition et son titre dans la base de données
# Auteur : Ethan SUISSA - Terminé
def AddInFile(titreChanson, partitionTexte, cheminAccesBdd):
    titreChanson = str(titreChanson).rstrip("\n")
    partitionTexte = str(partitionTexte).rstrip("\n")
    if titreChanson == "" or partitionTexte == "":
        message = "Les deux champs doivent être renseignés"
    else:
        message = "OK"  # Pour controle de retour
        file = open(cheminAccesBdd, 'a')  # 'a' ouvert en ecriture, ajoute à la fin du fichier
        file.write('\n')  # Ajoute un saut de ligne.
        file.write('#' + titreChanson)  # Ajoute le titre
        file.write('\n')  # Ajoute un saut de ligne. necessaire sinon ajoute à la suite du titre
        file.write(str(partitionTexte).replace('\n', ''))  # Ajoute la partition
        closeFile(file)  # Ferme le fichier

    return message


# ***********************************************************************
# FONCTION OUTIL : Fermer un fichier
# Auteur : Rédacteur de la consigne

def closeFile(f):
    f.close()

# ******************************************************************************************
# FONCTION OUTIL: fonction COMPLEMENTAIRE aux précédentes qui retourner la clé d'un dictionnaire avec en entrée
# celui-ci et une de ses valeurs.  Auteur : Ethan SUISSA - Terminé
def find_key(Dict, Val):
    for key, val in Dict.items():
        if Val == val:
            return key

# 01 : Fonction qui ouvre l'explorateur de fichier et renvoie le chemin d'acces du fichier
def cheminDaccesFichierSelectionne():
    # Ouverture de la boite de dialogue pour selection du fichier
    rep_file = askopenfile(title="Lire un fichier TEXTE", defaultextension=".txt",
                           filetypes=[("Fichiers Textes ", ".txt")], mode="r")

    if rep_file is None:  # Si appui sur Annuler
        pass
    else:
        # Récupération du nom complet du fichier avec l'attribut .name du module "os"
        cheminAccesSelection = os.path.abspath(rep_file.name)
        return cheminAccesSelection