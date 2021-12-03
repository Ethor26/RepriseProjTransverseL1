# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : pour le 24 mai 2021
# Fichier F04 = "RESULTATS DU JEUX"
# ======================================================

# =====================
# Bibliothèques et importations :
import os  # Sert pour simplifier l'écriture du chemin d'accès d'un fichier (voir os.getcwd()).
from tkinter import *  # Attention, TKinter doit être importé pour utiliser image de fond, pas remplacable par import de
# fichier wF0... De plus, ordre des import important !
import wF01  # Import de F02 pour pouvoir l'ouvrir
from Tools import *  # Import de Tools pour pouvoir utiliser ses fonctions
from PIL import Image
from PIL.ImageTk import PhotoImage  # Ces deux liens servent pour amener les fonctions fixant les images de fond.
import wF02  # Import de F02 pour pouvoir l'ouvrir


# ====================
# Programme :
class F04(Tk):
    # **************************************
    # Constructeur de l'objet F04 : ne pas supprimer !!!
    def __init__(self, Score, IdJoueur, AncienMeilScore):  # Importation du paramètre score de F02.
        Tk.__init__(self)
        self.title("F04")  # Le titre de la fenêtre.
        self.minsize(1200, 700)  # taille de fenêtre.
        self.Largeur = 1200  # Largeur de la zone de résultat.
        self.Hauteur = 700  # Hauteur de la zone de résultat.
        # Paramètres plein écran.
        self.fullScreenState = True  # On attribue Vrai en disant que la fenêtre est en pleine écran.
        self.attributes("-fullscreen",
                        self.fullScreenState)  # On spécifie si la fenêtre est en mode plaine écran ou non.
        self.bind("<F11>", self.toggleFullScreen)  # On choisit une touche pour activer le pleine écran.
        self.bind("<Escape>", self.quitFullScreen)  # On choisit une touche pour quitter le pleine écran.
        self.ScoreRec = Score  # On attribue une variable dans l'objet à la valeur importée.
        self.IDJoueur = IdJoueur  # On attribue une variable dans l'objet à la valeur importée.
        self.OldBestScore = AncienMeilScore  # On attribue une variable dans l'objet à la valeur importée.
        # Une méthode séparée pour construire le contenu de la fenêtre.
        self.createWidgets()

    # **************************************
    # Fonction/Méthode de création des widgets.
    def createWidgets(self):
        # Création des widgets (boutons, labels, etc...)
        self.grid()  # Choix du mode d'arrangement des elements
        # ==================================================
        # FONCTIONS WIDGETS::::::::

        # ==================================================
        # ELEMENTS GRAPHIQUES::::::::

        # ...........< I M A G E S >.........................
        # ELEMENT GRAPHIQUE : <ImageDeFond> = [Image I09] : fond d'écran de F04 (fenêtre de résultat).
        # Fond d'écran :
        self.PhotofondInfo = Image.open(
            os.getcwd() + "/IMAGES/ImageF04/ImageConflitSpace.jpg")  # On importe l'image I09
        self.PhotofondInfo = self.PhotofondInfo.resize((self.Largeur, self.Hauteur), Image.ANTIALIAS)  # resize permet
        # de mettre les photos au bon format pour les inclure dans le canevas. Antialias = inconnu, permet à resize de
        # fonctionner
        self.FondF04 = PhotoImage(self.PhotofondInfo)  # On attribue l'image
        self.CanvasResult = Canvas(self, width=self.Largeur,
                                   height=self.Hauteur)  # Création d'un canevas, un nouvel espace d'écriture.
        self.ImgFondF04 = self.CanvasResult.create_image(self.Largeur // 2, self.Hauteur // 2, image=self.FondF04)
        # On met les paramètres de longueur et largeur de l'image de fond
        self.CanvasResult.pack(padx=5, pady=5)  # .pack sert à placer les éléments
        self.CanvasResult.tag_lower(self.ImgFondF04)  # Met l'objet à l'arrière plan

        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [Texte T09] : Afficher Score, nom, ...
        self.CanvasResult.create_text(600, 100,
                                      text="Résultat de la partie :", font='Gabriola 32 bold',
                                      fill='white')  # Création de la partie du texte qui sera toujours la
        Depasse, BestScore = self.VictoireJeu()  # Attribution des 2 variables de la fonction VictoireJeu, le booléen
        # qui indique si dépassé et le meilleur score du joueur.

        # ELEMENT GRAPHIQUE : <Labels> = [Texte T10] + [AffichageVariable A01 et A02] : Message d'encouragement.
        # A01 = affichage de la variable du score de la partie.
        # A01 = affichage de la variable du meilleur score du joueur.
        if Depasse:  # Condition pour afficher 2 textes différents : si le meilleur score est dépassé dans cette partie.
            self.CanvasResult.create_text(300, 300,
                                          text="Bravo, vous avez battu votre record !\nVotre score est : {}\n"  # T10 et A01
                                               "Votre ancien meilleur score était : {}".format(  # A02
                                              int(self.ScoreRec), self.OldBestScore), font='Gabriola 26',
                                          fill='cyan')  # Si le nouveau score est le meilleur score on affiche un
            # message de félicitation.
        else:  # Si le meilleur score n'a pas été dépassé :
            # ELEMENT GRAPHIQUE : <Labels> = [Texte T11] + [AffichageVariable A01 et A02] : Message d'encouragement.
            self.CanvasResult.create_text(300, 300,
                                          text="Dommage, vous ferez mieux la prochaine fois !\n Votre score est : {}\n"  # T11 et A01
                                               "Votre meilleur score reste à : {}".format(  # A02
                                              int(self.ScoreRec), BestScore), font='Gabriola 26',
                                          fill='cyan')  # Sinon on afficher le texte d'encouragement pour la prochaine
            # fois.

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T03] : Nom du jeu.
        Label1 = Label(self, text=" Un Heros contre Galacticov ", font=('Arial', 20),  # T01
                       fg='blue')  # On personnalise le label, du titre.
        # Label1.pack(padx=1, pady=1)
        Label1.place(x=900, y=750)  # On place le label.

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B05] : Retour au menu (Retour F01)
        self.RetourMenu = Button(self, text="Rejouer",
                                 command=self.commandeOuvreF02)  # Creation du bouton et de ce qu'il fait
        self.RetourMenu.place(x=250, y=600)  # On place ce bouton

        # ELEMENT GRAPHIQUE : <Button> = [B09] : Un bouton pour retourner au menu.
        self.quitButton = Button(self, text="Retourner au Menu",
                                 command=self.commandeOuvreF01)  # Création d'un bouton et de ce qu'il fait
        self.quitButton.place(x=350, y=600)  # Placement du bouton dans la fenêtre
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B06] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)  # Création d'un bouton et de sa fonction
        self.quitButton.place(x=550, y=600)  # Placement du bouton

    # ==================================================
    # AUTRES FONCTIONS::::::::

    # ---------------------------
    # FONCTIONS statuant si le meilleur score est dépassé (en cours).
    def VictoireJeu(self):  # On crée les fonctions qu'on utilise
        tab, nbLignes = open_score_file2()  # On prend des variables du fichier Tools
        if self.ScoreRec >= int(tab[self.IDJoueur + 1][3]):  # Ouverture d'une boucle
            print("Meilleur score dépassé")  # Pour controle
            return True, int(
                tab[self.IDJoueur + 1][3])  # On retourne Vrai si le score a été dépasé, et l'ancien meilleur score du
            # joueur
        else:
            print("Meilleur score non atteint")  # Pour controle
            return False, int(
                tab[self.IDJoueur + 1][3])  # On retourne faux si le score n'a pas été dépassé, et le meilleur score du
            # joueur.

    # Fonctions de l'activation du pleine écran : détailler dans F00.
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F04
        # ouvre F01
        app = wF01.F01(self.IDJoueur)
        app.focus_force()  # Force le focus sur la fenetre
        app.mainloop()  # Ouverture de F01

    # COMMANDE : ouvre F02 (Jouer)
    def commandeOuvreF02(self):
        self.destroy()  # ferme F01
        # ouvre F02
        app = wF02.F02(self.IDJoueur)  # implémente l'objet app
        app.focus_force()  # Force le focus sur la fenetre
        app.mainloop()  # Ouverture de F02
