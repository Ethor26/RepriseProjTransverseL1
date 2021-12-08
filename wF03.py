# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : pour le 24 mai 2021
# Fichier F03 = "INFORMATIONS DU JEU"
# ======================================================

# =====================
# Bibliothèques et importations :
import wF01
import os
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage


# ====================
# Programme :
class F03(Tk):
    # Constructeur de l'objet F03 : ne pas supprimer !!!
    def __init__(self, IDJoueur):  # NomJoueur a ajouter en paramètre ?
        Tk.__init__(self)
        self.title("F03")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre
        self.IdJoueur = IDJoueur  # Transmission de l'ID du joueur
        self.Largeur = 1200  # Largeur de la zone de jeu
        self.Hauteur = 700  # Hauteur de la zone de jeu

        # Paramètres plein écran
        self.fullScreenState = True  # Met la fenêtre en plein écran
        self.attributes("-fullscreen", self.fullScreenState)  # la fonction crée un plein écran si self.FullscreenState
        # = "True", et en mode affichage simple si "False".
        self.bind("<F11>", self.toggleFullScreen)  # Fonction permet d'obtenir un plein écran avec la touche F11
        self.bind("<Escape>", self.quitFullScreen)  # Fonction permet d'enlever le plein écran avec la touche Echap

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

    # **************************************
    # Fonction/Méthode de création des widgets.
    def createWidgets(self):  # Création des widgets (boutons, labels, etc...)
        self.grid()  # Choix du mode d'arrangement des elements

        # =================================================
        # ELEMENTS GRAPHIQUES::::::::

        # ...........< I M A G E S >........................

        # ELEMENT GRAPHIQUE : <Image en FOND> = [Libellé I08] + <Canevas> = [Libellé G03]
        # Fond d'écran :
        self.PhotofondInfo = Image.open(os.getcwd() + "/IMAGES/ImageF03/ImageGuerreSatellite.jpg")  # Affichage de
        # l'image grâce au chemin d'accès de l'image : os.getcwd() est une chaine de caractère représentant
        # l'emplacement du fichier
        self.PhotofondInfo = self.PhotofondInfo.resize((self.Largeur, self.Hauteur), Image.ANTIALIAS)  # resize permet
        # de mettre les photos au bon format pour les inclure dans le canevas. Antialias = inconnu, permet à resize de
        # fonctionner
        self.FondF03 = PhotoImage(self.PhotofondInfo)  # Formatation de l'image en tant que image pour Canevas
        self.CanvasInfo = Canvas(self, width=self.Largeur, height=self.Hauteur)  # Creation du Canevas de F03
        self.ImgFondF03 = self.CanvasInfo.create_image(self.Largeur // 2, self.Hauteur // 2, image=self.FondF03)
        # Creation d'un emplacement d'image dans le canevas, où l'on place l'image de Fond sélectionnée.
        self.CanvasInfo.pack(padx=5, pady=5)  # .pack sert à placer le texte
        self.CanvasInfo.tag_lower(self.ImgFondF03)  # tag_lower sert à mettre l'image en arrière plan

        # ...........< T E X T E S > .......................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T09] : Texte explicatif du jeu
        self.CanvasInfo.create_text(600, 350, text="Bienvenue dans notre jeu ! \nLe but est simple :"
                                                   " esquivez les missiles qui vous arrivent dessus\n"
                                                   "Pour cela, deux options s'offrent à vous :\n"
                                                   "- La première est de se déplacer a l'aide des touches :\n "
                                                   "'z' : pour aller en haut\t"
                                                   "'q' : pour aller a gauche\n"
                                                   "'s' : pour aller en bas\t"
                                                   "'d' : pour aller à droite\n"
                                                   "- La seconde est d'utiliser une commande programmable qui vous fera bondir\n"
                                                   "avec un angle que vous pouvez choisir dans le menu, vous obtiendrez  \n"
                                                   " un déplacement parabolique avec cet angle.\n"
                                                   "La touche 'p' : vous permettra d'exécuter cette commande",
                                    font='Gabriola 23 italic', fill='cyan')
        # font sert à choisir la police, la taille. fill sert a donner une couleur au texte

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T08] : Titre de la fenêtre
        self.CanvasInfo.create_text(600, 50,
                                    text="Informations sur le jeu.", font='Gabriola 32 italic', fill='blue')
        # font sert à choisir la police, la taille. fill sert a donner une couleur au texte

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T03] : Nom du jeu
        Label1 = Label(self, text=" Un Heros contre Galacticov ", font=('Arial', 20), fg='blue')
        # font sert à choisir la police, la taille. fg sert a donner une couleur au texte du label
        Label1.place(x=900, y=750)  # .place sert à placer le label
        # ...........< E N T R Y ' S > .......................

        # ...........< B U T T O N S >........................

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B09] : Retour au menu (Retour F01)
        self.RetourMenu = Button(self, bg="Royalblue1", fg="white", font=("Arial", 15), text="Retourner au menu", command=self.commandeOuvreF01)
        self.RetourMenu.place(x=180, y=670)  # .place sert à placer le label

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B06] : Un bouton pour quitter l'application
        self.quitButton = Button(self, bg="Royalblue3", fg="white", font=("Arial", 15), text="Quitter", command=self.destroy)
        self.quitButton.place(x=330, y=670)  # .place sert à placer le label

    # ==================================================
    # AUTRES FONCTIONS DE LA CLASSE ::::::::
    # FONCTIONS réglant respectivement l'application du plein écran avec F11, et la fin du plein écran avec Echap.
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState  # Le paramètre prend True si False avant (ce qui est le cas
        # par défaut: la fenêtre ne s'affiche pas en plein écran)
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        self.destroy()  # ferme F03
        # ouvre F01
        app = wF01.F01(self.IdJoueur)
        app.focus_force()  # Force le focus sur la fenetre, pour ne pas avoir besoin de cliquer dessus
        # et risquer d'endommager le code
        app.mainloop()  # Maintiens la fenêtre ouverte tant qu'il n'y pas d'action pour la fermer
