# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : pour le 24 mai 2021
# Fichier F00
# ======================================================

# =====================
# Bibliothèques et importations :
import os  # Sert pour simplifier l'écriture du chemin d'accès d'un fichier (voir os.getcwd()).
from tkinter import *  # Attention, TKinter doit être importé pour utiliser image de fond, pas remplacable par import de
# fichier wF0... De plus, ordre des import important !
from PIL import Image
from PIL.ImageTk import PhotoImage  # Ces deux liens servent pour amener les fonctions fixant les images de fond.

from wF01 import F01  # Import de F01 pour pouvoir l'ouvrir


# ====================
# Programme :
class F00(Tk):  # Declaration de l'objet F00
    # *****************************************
    # Constructeur de l'objet F01 : ne pas supprimer, sert pour mettre les paramètres et fonctions propres à l'objet.
    def __init__(self, message):  # Importation d'un message de test, ici "début" affiché en console
        # (pour vérifier l'importation de paramètres).
        Tk.__init__(self)
        print("*** F00 ***")  # Pour controle en console.
        self.title("F00")  # Le titre de la fenêtre.
        self.minsize(1200, 700)  # Initialisation de la taille de fenêtre.
        self.Largeur = 1200  # Paramètre représentant la largeur de la zone du Canevas.
        self.Hauteur = 700  # Hauteur de la zone du canevas.

        # Paramètres plein écran, réutilisés dans les autres fenêtres.
        self.fullScreenState = True
        self.attributes("-fullscreen", self.fullScreenState)  # la fonction crée un plein écran si self.FullscreenState
        # = "True", et en mode affichage simple si "False".
        self.bind("<F11>", self.toggleFullScreen)  # Fonction permet d'obtenir un plein écran avec la touche F11
        self.bind("<Escape>", self.quitFullScreen)  # Fonction permet d'enlever le plein écran avec la touche Echap

        # Une méthode séparée pour construire le contenu de la fenêtre : crée une sorte "d'algorithme principal" dans
        # l'objet
        self.createWidgets()

        print(message)  # A supprimer : controle/test de passage de valeur à la classe par son constructeur

    # **************************************
    # Fonction/Méthode de création des widgets.
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement des éléments de la fenêtre.

        # ...........< I M A G E S > .........................
        # ELEMENT GRAPHIQUE : <Image en FOND> = [Libellé I01] + <Canevas> = [Libellé G01] :
        # Affichage du fond d'écran de F00 dans son Canevas
        self.Photofond = Image.open(
            os.getcwd() + "/IMAGES/Image F00/image5.png")  # Ouverture de l'image en important le
        # chemin d'accès de l'image : os.getcwd() est une chaine de caractère représentant l'emplacement du fichier
        # wF00, le fichier image a donc ce chemin là avec celui du dossier IMAGES puis du dossier "Images F00".
        self.FondF00 = PhotoImage(self.Photofond)  # Formatation de l'image en tant que image pour Canevas

        self.CanvasPres = Canvas(self, width=self.Largeur, height=self.Hauteur)  # Creation du Canevas de F00
        self.ImgFondF00 = self.CanvasPres.create_image(self.Largeur // 2, self.Hauteur // 2, image=self.FondF00)
        # Creation d'un emplacement d'image dans le canevas, où l'on place l'image de Fond sélectionnée.
        self.CanvasPres.pack(padx=5, pady=5)  # .pack sert à placer un élément dans la fenêtre.
        self.CanvasPres.tag_lower(self.ImgFondF00)  # tag_lower place ses éléments en paramètres à l'arrière plan.

        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T01] : Titre du jeu
        self.CanvasPres.create_text(600, 50,
                                    text="Un heros Contre Galacticov.", font='Gabriola 32 italic', fill='cyan')

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T02] : Label anti-copie
        self.CanvasPres.create_text(1100, 650,
                                    text="© Touts droits réservés. ", font='Gabriola 15 italic', fill='cyan')

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T03] : Texte du scénario
        # Affichage du scénario : un label sur Tkinter permet d'afficher du texte, create_text met du texte dans un
        # canvas. Paramètre inutile ici car placement direct. fill = couleur du texte.
        self.CanvasPres.create_text(600, 300,
                                    text="Il y a bien longtemps, une galaxie lointaine était dirigée par un Conseil"
                                         " de sages qui s’efforçaient à ce que tous le monde vive une vie paisible.\n"
                                         "Malheureusement, ils virent bientôt apparaître une armée menée par un"
                                         " empereur infecté par un virus nommé Galacticov. Ce virus avait paralysé\n"
                                         "toutes les zones du cerveau de l’empereur qui lui permettait d’éprouver"
                                         " des émotions négatives et stimulé les connexions dans celles créant des\n"
                                         "émotions négatives. Un empereur juste et intègre devint alors cruel et "
                                         "implacable. Ce virus étant contrôlé à distance par un conseiller avide\n "
                                         " de pouvoir dans une centrale, le Conseil vous recruta avec d’autres héros"
                                         " pour atteindre et détruire cette centrale, en évitant les tirs des "
                                         "vaisseaux\n "
                                         "délégué par l’empereur. Vous devrez donc passer à travers "
                                         "cette armée, mais avec l’interdiction du Conseil de détruire les autres "
                                         "vaisseaux.\n "
                                         "En effet, ils sont contrôlés par des pilotes innocents mais manipulés. Ils "
                                         "ignorent "
                                         "vos objectifs et s’imaginent que vous venez détruire leur empire.\n "
                                         "Une quête ardue commence alors pour vous…\n", font='Gabriola 17 italic',
                                    fill='white')

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B01] : ouvrir menu (F01)
        self.ouvreF01 = Button(self, text="Start", command=self.commandeOuvreF01)  # Creation d'un bouton sur tkinter:
        # la fenêtre du bouton est l'objet représenté par self, le texte dans le bouton est "start" et le clic active la
        # fonction définie dans "command", ici self.commandeOuvreF01 (SANS PARAMETRES).
        self.ouvreF01.place(x=200, y=650)  # Place le bouton aux coordonnées x et y définies.

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B06] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=300, y=650)

    # **************************************
    # Autres Fonctions de l'objet:

    # -----------------------
    # FONCTIONS réglant respectivement l'application du plein écran avec F11, et la fin du plein écran avec Echap.
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState  # Le paramètre prend True si False avant (ce qui est le cas
        # par défaut: la fenêtre ne s'affiche pas en plein écran)
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    # COMMANDE = ouvre F01,  et ferme F00 (retour au menu)
    def commandeOuvreF01(self):
        self.destroy()  # ferme F00, destroy supprime aussi toute les modifications qu'aura recue un objet : si on
        # réouvre une fenêtre, elle sera à son état initial. Exemple : si on ferme la fenêtre de jeu F02 et qu'on la
        # réouvre, les obstacles, le nombre de vie, le score et le personnage reprendront leur état initial (score = 0,
        # nombre de vie = 3...).
        # ouvre F01
        app = F01(0)  # 0 représente un ID nul, sert pour que F01 puisse transmettre l'ID après
        app.focus_force()  # Force le focus sur la fenetre, pour ne pas avoir besoin de cliquer dessus et risquer
        # d'endommager le code.
        app.mainloop()  # Ouvre l'objet tkinter (fenêtre) F01.
