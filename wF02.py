# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : pour le 24 mai 2021
# Fichier F02 = "JEUX EN ACTION"
# ======================================================

# =====================
# Bibliothèques et importations :

import os
import time
from random import *
from tkinter import *
from math import *
from PIL import Image
from PIL.ImageTk import PhotoImage
from Tools import *
import wF01  # Modification de l'import pour éviter les "circular import", en général rajoute des "wF01.Tk"
from wF04 import F04


# ====================
# Programme :
class F02(Tk):

    # ************************************
    # Constructeur de l'objet F02 : ne pas supprimer !!!
    def __init__(self, IDJoueur):
        Tk.__init__(self)
        self.title("F02")  # Le titre de la fenêtre
        self.IdJoueur = IDJoueur  # Transmission de l'ID du joueur

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.Largeur = 1200  # Largeur de la zone de jeu
        self.Hauteur = 680  # Hauteur de la zone de jeu

        # Reglage du plein écran
        self.fullScreenState = True
        self.attributes("-fullscreen", self.fullScreenState)
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        # Dimension de l'image du vaisseau : Hauteur = 45, largeur = 30.
        self.Perso_Hauteur = 45
        self.Perso_Largeur = 30

        # Dimension du rayon des obstacles.
        self.RayonObstacles = 20

        # position initiale du perso, respectivement X et Y
        self.PosX = 600
        self.PosY = 400

        # Declaration des variables d'actualisation des fenêtres pour l'arrêt (même si ce ne sont pas des entiers).
        self.idAfterD = 1
        self.idAfterP = 2
        self.idAfterQ = 3
        self.idAfterZ = 4
        self.idAfterS = 5

        # Temps initiaux
        self.Temps = 0  # le compteur temps de la commande programmable
        self.cpTemps = 2  # le compteur temps des commandes figées
        self.LimiteTpsDepl = 5  # la limite de l'incrémentation du compteur de temps des commandes figées

        # Nombre de Pas de déplacement pour les commandes figées.
        self.NbPas = 20

        # Déclaration du booléen FinAttente qui permet de réguler le bouton de pause : démarre à true car le jeu se
        # lance directement (sans pause préalable).
        self.FinAttente = True

        # Déclaration du score initial
        self.CompteurScore = 0

        # Déclaration d'ancien meilleur score initial
        self.Old_best_score = 0

        # Déclaration du nombre de vies initial
        self.CompteurVies = 3

        # Déclaration du booléen montrant s'il y a explosion, sert pour le placement de l'image.
        self.Explosion = False  # Pas d'explosion au début
        # 1ere position finale du personnage (confondue avec initiale).
        self.valY_Final = 0
        self.valX_Final = 0

        # Creation des elements graphiques
        self.createWidgets()

    # ************************************
    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # ==================================================
        # FONCTIONS WIDGET ::::::::

        # =============================================================================
        # FONCTION qui crée un déplacment lorsque l'on actionne une touche
        def CommandeClavier(event):
            self.touche = event.keysym  # Un événement (event) est la survenue d’une action (clavier, souris) dont votre
            # application a besoin d’être informée (trouvé sur internet).

            # Si touche d => deplt a droite
            if self.touche == 'd':
                print("Info:  touche d activée ***")
                if self.FinAttente:  # Si Pause n'est pas activé :
                    deplacement_D()  # Active la fonction de déplacement à droite.
                    self.Explosion = False  # Replace l'image d'explosion à l'arrière plan, en attendant la prochaine...

            # Si touche q => deplt a Gauche
            if self.touche == 'q':
                print("Info:  touche q activée ***")
                if self.FinAttente:  # Si Pause n'est pas activé:
                    deplacement_Q()  # Active la fonction de déplacement à gauche.
                    self.Explosion = False

            # Si touche s => deplt a bas
            if self.touche == 's':
                print("Info:  touche s activée ***")
                if self.FinAttente:  # Si Pause n'est pas activé:
                    deplacement_S()  # Active la fonction de déplacement en bas.
                    self.Explosion = False

            # Si touche z => deplt a Haut
            if self.touche == 'z':
                print("Info:  touche z activée ***")
                if self.FinAttente:  # Si Pause n'est pas activé:
                    deplacement_Z()  # Active la fonction de déplacement en haut.
                    self.Explosion = False

            # Si touche p => déplacement selon equation de mouvement
            if self.touche == 'p':
                print("Info:  touche p activée ***")
                if self.FinAttente:  # Si Pause n'est pas activé
                    deplacement_P()
                    self.Explosion = False

        # =============================================================================
        # FONCTION de déplacement de la touche P. Auteur : Ethan SUISSA - Terminé
        # COMMANDE : <Deplacement Programmable> = [Libellé C01]
        def deplacement_P():
            if self.FinAttente:  # Sert pour éviter les interruptions brutales
                nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement
                self.Temps += 0.0002  # Augmentation d'une variable de temps pour calcul Position Y (de commande
                # programmable) et permet de définir la limite du mouvement.
                # Récupération des nouvelles position
                self.PosX, self.PosY, self.siRebond, Temps = self.ValeurPosXY_P(self.PosX, self.PosY, self.Temps)

                print("posY = ", self.PosY)  # pour contrôle.
                print("posX = ", self.PosX)  # pour contrôle.
                print("Pion = ", self.PersoImgVaisseau)  # pour contrôle.
                print("Temps = ", Temps)  # pour contrôle.

                if self.FinAttente:  # Sert pour éviter les interruptions brutales
                    # Repositionnne le personnage en le redessinant à sa position avec "Canevas.coord()"
                    self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

                    # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
                    if self.siRebond:
                        nbRebond = nbRebond + 1
                        print("Nombre de rebond = ", nbRebond)  # pour contrôle.

                    # On déclenche le déplacement toute les 1 ms, réactualisation de la fenêtre
                    if self.FinAttente:  # Sert pour éviter les interruptions brutales (pas au point pour P)
                        self.idAfterP = self.after(1, deplacement_P)
                        print("idAfterP", self.idAfterP)
                        # On arrête le déplacement s'il y a un rebond ou si le facteur temps est supérieur à 0.05
                        if nbRebond > 0 or self.Temps > 0.065:  # 0.07 pour courbe complète
                            self.after_cancel(self.idAfterP)  # arrête la réactualisation de la fenêtre
                            # (et le déplacement)
                            self.Temps = 0  # Réinitialisation du compteur de temps de déplacement.

        # =============================================================================
        # FONCTION de déplacement de la touche D. Auteur : Lilandra ALBERT-LAVAUX - Terminé
        # COMMANDE : <Deplacement Droite> = [Libellé C05]
        def deplacement_D():  # ATTENTION : Pas de paramètres !
            if self.FinAttente:  # Sert pour éviter les interruptions brutales
                nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement

                # Récupération de la nouvelle position de X et renvoie siRebond=true si on touche le bord
                self.PosX, self.siRebond = self.ValeurPosX(self.PosX, self.NbPas)

                print("Deplacement Droite : posY = ", self.PosY)  # pour contrôle.
                print("Deplacement Droite : posX = ", self.PosX)  # pour contrôle.

                # Repositionnne le personnage
                if self.FinAttente:  # Sert pour éviter les interruptions brutales
                    self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

                    # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
                    if self.siRebond:
                        nbRebond = nbRebond + 1
                        print("Nombre de rebond = ", nbRebond)  # pour contrôle.

                    # On déclenche le déplacement toute les 40 ms, réactualisation de la fenêtre
                    self.idAfterD = self.after(40, deplacement_D)

                    # On arrête le dépldacement s'il y a un rebond ou si on arrive à la limite du temps de déplacement
                    self.cpTemps += 1

                    if nbRebond > 0 or self.cpTemps > self.LimiteTpsDepl:
                        self.after_cancel(self.idAfterD)  # arrête la réactualisation de la fenêtre
                        # (et le déplacement)
                        self.cpTemps = 0  # Réinitialisation du compteur de temps de déplacement.

        # =============================================================================
        # FONCTION de déplacement de la touche Q. Auteur : Lilandra ALBERT-LAVAUX - Terminé
        # COMMANDE : <Deplacement Gauche> = [Libellé C02]
        def deplacement_Q():  # ATTENTION : Pas de paramètres !
            if self.FinAttente:  # Sert pour éviter les interruptions brutales
                nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement

                # Récupération de la nouvelle position de X et renvoie siRebond=true si on touche le bord
                self.PosX, self.siRebond = self.ValeurPosX(self.PosX, -self.NbPas)
                print("Deplacement Gauche : posY = ", self.PosY)  # pour contrôle.
                print("Deplacement Gauche : posX = ", self.PosX)  # pour contrôle.

                # Repositionnne le personnage
                if self.FinAttente:  # Sert pour éviter les interruptions brutales
                    self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

                    # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
                    if self.siRebond:
                        nbRebond = nbRebond + 1
                        print("Nombre de rebond = ", nbRebond)

                    # On déclenche le déplacement toute les 40 ms, réactualisation de la fenêtre
                    self.idAfterQ = self.after(40, deplacement_Q)

                    # On arrête le dépldacement s'il y a un rebond ou si on arrive à la limite du temps de déplacement
                    self.cpTemps += 1

                    if nbRebond > 0 or self.cpTemps > self.LimiteTpsDepl:
                        self.after_cancel(self.idAfterQ)  # arrête la réactualisation de la fenêtre
                        # (et le déplacement)
                        self.cpTemps = 0  # Réinitialisation du compteur de temps de déplacement.

        # =============================================================================
        # FONCTION de déplacement de la touche Z. Auteur : Lilandra ALBERT-LAVAUX - Terminé
        # COMMANDE : <Deplacement Haut> = [Libellé C03]
        def deplacement_Z():  # ATTENTION : Pas de paramètres !
            if self.FinAttente:  # Sert pour éviter les interruptions brutales
                nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement

                # Récupération de la nouvelle position de X et renvoie siRebond=true si on touche le bord
                self.PosY, self.siRebond = self.ValeurPosY(self.PosY, -self.NbPas)

                print("Deplacement Haut : posY = ", self.PosY)  # pour contrôle.
                print("Deplacement Haut : posX = ", self.PosX)  # pour contrôle.

                if self.FinAttente:  # Sert pour éviter les interruptions brutales
                    # Repositionnne le personnage
                    self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

                    # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
                    if self.siRebond:
                        nbRebond = nbRebond + 1
                        print("Nombre de rebond = ", nbRebond)

                    # On déclenche le déplacement toute les 40 ms, réactualisation de la fenêtre
                    self.idAfterZ = self.after(40, deplacement_Z)

                    # On arrête le dépldacement s'il y a un rebond ou si on arrive à la limite du temps de déplacement
                    self.cpTemps += 1

                    if nbRebond > 0 or self.cpTemps > self.LimiteTpsDepl:
                        self.after_cancel(self.idAfterZ)  # arrête la réactualisation de la fenêtre
                        # (et le déplacement)
                        self.cpTemps = 0  # Réinitialisation du compteur de temps de déplacement.

        # =============================================================================
        # FONCTION de déplacement de la touche S. Auteur : Lilandra ALBERT-LAVAUX - Terminé
        # COMMANDE : <Deplacement Bas> = [Libellé C04]
        def deplacement_S():  # ATTENTION : Pas de paramètres !
            if self.FinAttente:  # Sert pour éviter les interruptions brutales
                nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement

                # Récupération de la nouvelle position de X et renvoie siRebond=true si on touche le bord
                self.PosY, self.siRebond = self.ValeurPosY(self.PosY, self.NbPas)

                print("Deplacement Bas : posY = ", self.PosY)  # pour contrôle.
                print("Deplacement Bas : posX = ", self.PosX)  # pour contrôle.

                if self.FinAttente:  # Sert pour éviter les interruptions brutales
                    # Repositionnne le personnage
                    self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

                    # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
                    if self.siRebond:
                        nbRebond = nbRebond + 1
                        print("Nombre de rebond = ", nbRebond)

                    # On déclenche le déplacement toute les 40 ms, réactualisation de la fenêtre
                    self.idAfterS = self.after(40, deplacement_S)

                    # On arrête le dépldacement s'il y a un rebond ou si on arrive à la limite du temps de déplacement
                    self.cpTemps += 1

                    if nbRebond > 0 or self.cpTemps > self.LimiteTpsDepl:
                        self.after_cancel(self.idAfterS)  # arrête la réactualisation de la fenêtre
                        # (et le déplacement)
                        self.cpTemps = 0

        # ==================================================
        # ELEMENTS GRAPHIQUES::::::::

        # ...........< I M A G E S >........................

        # ELEMENT GRAPHIQUE : <Image en FOND> = [Libellé I03] + <Canevas> = [Libellé G02] : Canevas imagé ou se déroule
        # le jeu.
        # Etape 1 : Création d'un Canevas noir
        self.CanevasJeu = Canvas(self, width=self.Largeur, height=self.Hauteur)
        self.CanevasJeu.pack(side=TOP, padx=5, pady=5)  # .pack est aussi une méthode de placement des objets tkinter.

        # Etape2 : Ajout d'un Fond d'ecran sur le Canevas
        self.imageFond = Image.open(os.getcwd() + "/IMAGES/ImagesF02/fondSpatial-1.jpeg")
        # Slash doivent être ajoutés à coté de D: et juste avant le nom de l'image pour le chemin absolue, sinon on peut
        # importer une partie du chemin (celle où est wF02) avec la fonction os.getcwd().
        self.imgfondEcran = PhotoImage(self.imageFond)  # importe la photo du fond dans le fichier
        self.objImgFondEcran = self.CanevasJeu.create_image(self.Largeur // 2, self.Hauteur // 2,
                                                            image=self.imgfondEcran)  # Implémentation de l'image dans
        # le Canevas du jeu.

        self.CanevasJeu.focus_set()  # crée un cadre autour du canvas et permet l'activation de bind
        self.CanevasJeu.bind('<Key>', CommandeClavier)  # Met en relation les touches du clavier et les commandes.
        self.CanevasJeu.tag_lower(self.objImgFondEcran)  # placement à l'arriere plan, tag_raise pour premier plan.

        # ELEMENT GRAPHIQUE : <PointesVaisseaux> : Eléments graphiques du fond.
        #   Vaisseau pointe Bas. Libellé : I04.
        self.imageV1 = Image.open(os.getcwd() + "/IMAGES/ImagesF02/image-DestoyerImperial-3 Bas.png")
        self.imageV1 = self.imageV1.resize((150, 180), Image.ANTIALIAS)  # resize permet de mettre les photos au bon
        # format pour les inclure dans le canevas. Antialias = inconnu, permet à resize de fonctionner
        self.imgV1 = PhotoImage(self.imageV1)  # Même principe que fond d'écran
        self.objImgV1 = self.CanevasJeu.create_image(self.Largeur // 2, self.Hauteur, image=self.imgV1)

        #   Vaisseau pointe Haut : Libellé : I06.
        # Même principe que pointe bas, valable pour toutes les pointes de vaisseaux
        self.imageV2 = Image.open(os.getcwd() + "/IMAGES/ImagesF02/image-DestoyerImperial-3 Haut.png")
        self.imageV2 = self.imageV2.resize((150, 180), Image.ANTIALIAS)
        self.imgV2 = PhotoImage(self.imageV2)
        self.objImgV2 = self.CanevasJeu.create_image(self.Largeur // 2, 0, image=self.imgV2)

        #   Vaisseau pointe Droite. Libellé : I05.
        self.imageV3 = Image.open(os.getcwd() + "/IMAGES/ImagesF02/image-DestoyerImperial-3 Droite.png")
        self.imageV3 = self.imageV3.resize((150, 180), Image.ANTIALIAS)
        self.imgV3 = PhotoImage(self.imageV3)
        self.objImgV3 = self.CanevasJeu.create_image(self.Largeur, self.Hauteur // 2, image=self.imgV3)

        #   Vaisseau pointe Gauche. Libellé : I07.
        self.imageV4 = Image.open(os.getcwd() + "/IMAGES/ImagesF02/image-DestoyerImperial-3 Gauche.png")
        self.imageV4 = self.imageV4.resize((150, 180), Image.ANTIALIAS)
        self.imgV4 = PhotoImage(self.imageV4)
        self.objImgV4 = self.CanevasJeu.create_image(0, self.Hauteur // 2, image=self.imgV4)

        #   Image Personnage : faucon millenium. Libellé : P01.
        self.PersoImgVaisseau = Image.open(os.getcwd() + "/IMAGES/ImagesF02/faucon millenium-3.png")
        self.PersoImgVaisseau = self.PersoImgVaisseau.resize((self.Perso_Largeur, self.Perso_Hauteur), Image.ANTIALIAS)
        self.logo = PhotoImage(self.PersoImgVaisseau)
        self.ImgPerso = self.CanevasJeu.create_image(self.PosX, self.PosY, image=self.logo)  # Placement à PosX et PosY
        # pour le déplacement de l'image comme personnage.

        # ELEMENT GRAPHIQUE : <ImageExplosion> : [Libellé I10]. appliquée à l'endroit du perso.
        self.imageExpl = Image.open(os.getcwd() + "/IMAGES/ImagesF02/ImageExplosion.png")
        self.imageExpl = self.imageExpl.resize((100, 60), Image.ANTIALIAS)
        self.imgExpl = PhotoImage(self.imageExpl)
        self.objImgExpl = self.CanevasJeu.create_image(self.PosX, self.PosY, image=self.imgExpl)
        self.CanevasJeu.tag_lower(self.objImgExpl)

        # ELEMENT GRAPHIQUE : <ImageBouleDeFeu> : Image constituant les obstacles. Libellé associé à ceux des
        # dictionnaires déclaré juste après (exemple : CoordObstHaut a le libellé Ob02, l'image associée aura donc le
        # même). En effet, l'image est juste importée ici mais les véritables "objets image mobile" sont crées dans la
        # Partie "obstacle".
        self.imageBoulFeu = Image.open(os.getcwd() + "/IMAGES/ImagesF02/ImageBouledefeu.png")
        self.imageBoulFeu = self.imageBoulFeu.resize((40, 40), Image.ANTIALIAS)
        self.imgBoulFeu = PhotoImage(self.imageBoulFeu)

        # ...........< O B S T A C L E S >........................

        # Listes des positions initiales aleatoires, d'où pourront partir les balles
        # Listes des ordonnées de départ possible (pour balles avec déplacement horizontale).
        self.listposY = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475,
                         500,
                         525, 550, 575, 600, 625, 650, 675]  # longueur = 27

        # Listes des abcisses de départ possible (pour balles avec déplacement verticales).
        self.listposX = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475,
                         500,
                         525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975,
                         1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175]  # Longueur = 47

        # Liste des vitesses initiales aléatoires.
        self.Listvitesse = []
        for i in range(4):
            self.Listvitesse.append(uniform(2, 2.5) * 4)  # Création d'une liste de vitesses de déplacement différentes,
            # choix d'une de ces vitesses au hasard pour chaque balle.

        # Liste des angles de déplacement possible des obstacles (4 directions possibles : en haut, en bas, à droite ou
        # à gauche).
        self.Listangle = []
        AngleRadianBalle = 0
        for i in range(4):
            self.Listangle.append(AngleRadianBalle)
            AngleRadianBalle += pi / 2

        # Declaration de 4 obstacles distincts, chacun allant dans une direction différente. La déclaration se fait en
        # 2 temps. Tout d'abord, une variables de type dictionnaire contient leurs coordonnées x et y à chaque instant,
        # leurs rayon,
        # et leurs déplacement instantannée dx et dy (additionné aux variables de positions à chaque instant).

        # ATTENTION: Les directions des obstacles dans le nom représentent l'endroit d'où ils partent, et non leurs
        # trajectoires. De plus, l'orientation des axes x et y est différentes sur un écran : l'origine est le point en
        # haut à gauche de l'écran, l'axe x va bien vers la droite mais l'axe y vas vers le bas : plus il augmente, plus
        # l'objet descend.

        # ELEMENT GRAPHIQUE ASSOCIE : <ImageBouleDeFeu> : [Libellé Ob01].
        # Coordonnées de l'obstacles partant de la gauche vers la droite.
        CoordObstacleGauche = {'x': 50,  # Equivalent du 0 en abscisse, 50 pour compenser le rayon
                               'y': self.listposY[randint(0, 26)],  # 26 et 46 car le rang d'une liste a un décalage de
                               # position de -1. Randint choisit un nombre dans une liste d'entier, une position de la
                               # liste à un rang aléatoire est choisie.
                               'ray': self.RayonObstacles,  # Définie le rayon de l'obstacle (c'est un cercle), sert
                               # principalement pour les collisions.
                               'dx': self.Listvitesse[0] * cos(self.Listangle[0]),  # L'obstacle additionne à chaque
                               # unité de temps la première vitesse de la liste des vitesse aléatoire
                               # (vitesse instantannée), multipliée par l'angle de la direction de sa trajectoire (ici 0
                               # car il part de la gauche pour aller à droite). Le cosinus est pour le déplacement de x.
                               'dy': self.Listvitesse[0] * sin(self.Listangle[0])}
        #                       Le sinus est pour le déplacement de x.

        # ELEMENT GRAPHIQUE ASSOCIE : <ImageBouleDeFeu> : [Libellé Ob02].
        # Coordonnées de l'obstacles partant du haut vers le bas.
        CoordObstacleHaut = {'x': self.listposX[randint(0, 46)],
                             'y': 50,
                             'ray': self.RayonObstacles,
                             'dx': self.Listvitesse[1] * cos(self.Listangle[1]),  # Même principe que
                             # CoordObstacleGauche avec l'angle à 90°.
                             'dy': self.Listvitesse[1] * sin(self.Listangle[1])}

        # ELEMENT GRAPHIQUE ASSOCIE : <ImageBouleDeFeu> : [Libellé Ob04].
        # Coordonnées de l'obstacles partant de la droite vers la gauche.
        CoordObstacleDroite = {'x': self.Largeur - self.RayonObstacles - 1,  # l'obstacle part de la droite de l'écran
                               'y': self.listposY[randint(0, 26)],
                               'ray': self.RayonObstacles,
                               'dx': self.Listvitesse[2] * cos(self.Listangle[2]),  # Même principe avec l'angle à 180°
                               'dy': self.Listvitesse[2] * sin(self.Listangle[2])}

        # ELEMENT GRAPHIQUE ASSOCIE : <ImageBouleDeFeu> : [Libellé Ob03].
        # Coordonnées de l'obstacles partant du bas vers le haut.
        CoordObstacleBas = {'x': self.listposX[randint(0, 46)],
                            'y': self.Hauteur - self.RayonObstacles - 1,  # L'obstacle part du bas de l'écran.
                            'ray': self.RayonObstacles,
                            'dx': self.Listvitesse[3] * cos(self.Listangle[3]),  # Même principe avec l'angle à 270°
                            'dy': self.Listvitesse[3] * sin(self.Listangle[3])}

        # La liste "balles" prend l'ensemble des dictionnaires de coordonnées des obstacles, elle sera lue par les
        # fonction de déplacement.
        self.balles = [CoordObstacleDroite, CoordObstacleHaut, CoordObstacleGauche, CoordObstacleBas]

        # Cette liste stocke les positions initiales des balles pour pouvoir les réinitialiser à chaque collision et
        # perte de vie. Il s'agit d'une liste de dictionnaires avec comme clée le nom de ces positions et comme valeur
        # lesdites positions.
        self.ListPosInitBalles = []
        for i in range(4):
            DictPos = {'x0': self.balles[i]['x'], 'y0': self.balles[i]['y']}  # x0 et y0 représentent les positions
            # initiales x et y de chaque balles.
            self.ListPosInitBalles.append(DictPos)  # Ajout du dictionnaire de coordonnée initiales d'une balle dans la
            # liste, et ce pour chaque balles.

        # Dans un 2e temps : on crée les objets tkinter avec la fonction Canevas.create_image : on crée donc des images
        # mobiles. L'emplacement de cette déclaration est important : il doit être après la creation de self.balles pour
        # que chaque image recoive les coordonnées de son type d'obstacles associée : la première prend celles de
        # l'obstacle de gauche, la 2e celle de celui du haut et ainsi de suite pour les 2 autres..
        self.ListImgBoulFeu = []  # Creation de la listes stockant les 4 images
        for elt in self.balles:
            self.objImgBoulFeu = self.CanevasJeu.create_image(elt['x'], elt['y'], image=self.imgBoulFeu)
            self.ListImgBoulFeu.append(self.objImgBoulFeu)  # Creation des 4 images avec leur coordonnées de départ,
            # ajout dans une liste. Donc creation des 4 :
            #   ELEMENT GRAPHIQUE ASSOCIE : <ImageBouleDeFeu> : [Libellé Ob...].

        # ...........< L A B E L S >........................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T01] : Titre du jeu
        LabelTitre = Label(self, text=" Un Heros contre Galacticov ", font=('Arial', 20), fg='blue')
        LabelTitre.place(x=900, y=700)

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T07] : Texte Score
        LabelScore = Label(self, text=" Score: ", font=('Arial', 20), fg='blue')
        LabelScore.place(x=20, y=100)

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T12] : Texte Vies
        LabelVies = Label(self, text="Vies: ", font=('Arial', 20), fg='blue')
        LabelVies.place(x=20, y=300)

        # ...........< L A B E L S  V A R I A B L E S > .........................

        # ELEMENT GRAPHIQUE : <Label> = [StringVar Sv03] : Affichage Score
        self.TextScore = StringVar()  # Explication dans ceux de F01
        self.TextScore.set(str(int(self.CompteurScore)))  # Affiche l'entier correspondant au score (un réel au départ),
        # lui-même sous forme d'un caractère pour l'affichage avec le StringVar.
        self.compteurScore_lbl = Label(self, textvariable=self.TextScore, font=("", 16))
        self.compteurScore_lbl.place(x=120, y=100)

        # ELEMENT GRAPHIQUE : <Label> = [StringVar Sv04] : Affichage vies restantes.
        self.TextVies = StringVar()
        self.TextVies.set(str(self.CompteurVies))  # Affiche l'entier correspondant au nombre de vies restantes,
        # lui-même sous forme d'un caractère pour l'affichage avec le StringVar.
        self.compteurVies_lbl = Label(self, textvariable=self.TextVies, font=("", 16))
        self.compteurVies_lbl.place(x=120, y=300)

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B09] : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=190, y=700)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B06] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=300, y=700)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B08] : Un bouton pour mettre le jeu en pause.
        self.PauseButton = Button(self, text="Pause", command=self.Pause)
        self.PauseButton.place(x=500, y=700)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B10] : Fin de la partie et ouvre F04, activable si bouton Pause pressé
        # avant. Modalités d'activation : voir fonction self.Pause().
        self.B0_FinPartie = Button(self, text="Fin de partie", command=self.Fin_Partie, state=DISABLED)
        self.B0_FinPartie.place(x=400, y=700)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07] : Redémarre les obstacles et les commandes
        self.BoutonReprise = Button(self, text="Reprendre", command=self.Reprendre, state=DISABLED)
        self.BoutonReprise.place(x=550, y=700)  # Le clic de "Pause" crée le bouton reprendre

        # *********************** Appel des fonctions
        self.AjoutBalles()  # Démarrage de la fonction qui ajoute des balles au cour du temps.
        self.action()  # Démarrage de la fonction qui fait bouger les obstacles, gère le score et les collisions.

    # ********************* FONTIONS DE L'OBJET

    # ========================
    # FONCTION OUTILS : Récupérant l'angle du fichier score.txt et le retournant en radian. Auteur : Ethan SUISSA - Terminé
    def ValeurAngleParametreEnRadian(self):
        # Etape 1 : Récupération angle du fichier Score.txt.
        tab, nbLignes = open_score_file2()  # Lecture du fichier score.txt, voir Tools.
        VAngleEnDegree = int(tab[self.IdJoueur + 1][2])  # self.IdJoueur + 2 = Numéro de ligne, on enlève 1 car tableau.
        # Prend l'angle enregistré dans la BDD, soit l'angle utilisé par le joueur actuellement.

        # Etape 2 : Conversion et envoi pour calcul commande programmable
        # Angles à tester : 26, 45, 60, 120, 210, 300, extremes (89, 179, 269, 359)
        # Angle Temporaire
        # AngleEnDegree = 269
        # print("Angle en degree = ", AngleEnDegree)  # Pour controle
        # angleRadian = math.radians(AngleEnDegree)  # Conversion en radians pour calculs de com programmable
        # return angleRadian
        # Vrai Angle
        print("Angle en degree = ", VAngleEnDegree)
        VangleRadian = radians(VAngleEnDegree)
        return VangleRadian

    # ========================
    # FONCTION OUTIL : Utilise l'équation de mouvement pour calculer la postion finale en fonction de l'angle
    # Auteur : Ethan SUISSA - Terminé
    def CalcProg(self, AngleDeduitDegree, Temps):
        v0 = 1.2  # Choix de vitesse intiale : modélise celle avec laquelle on lance un objet.
        g = 9.81  # Constante de gravitation influencant la chute.
        Angle_Deduit_Radian = radians(AngleDeduitDegree)  # convertion en Radian de l'angle deduit, utiliser
        # math.radians si "import math"
        dx = v0 * cos(Angle_Deduit_Radian)  # modélise le déplacement horizontale avec les équations de mouvements :
        # utilisation de la dérivée de la position horizontale dx (vitesse).
        if Angle_Deduit_Radian == 0.0:  # Pour obtenir un déplacement horizontal d'un objet à la hauteur 0(pas de chute)
            g = 0
        dy = -g * Temps + v0 * sin(Angle_Deduit_Radian)  # modélise le déplacement verticale avec les équations de
        # mouvements : utilisation de la dérivée de la position horizontale dy (vitesse).
        # PRINCIPE GENERAL: dx et dy représentent les vitesses x et y de l'objet, c'est à dire son déplacement à un
        # temps donné, la fonction additionne donc à chaque étape de temps (elle est utilisée à chaque fois que le temps
        # augmente) la distance parcourue à la position.
        print("Angle radian:", Angle_Deduit_Radian)  # Test
        print("dx = :", dx, "dy = :", dy)  # Test
        return dx, dy

    # ========================
    # FONCTION OUTIL : Utilisé pour la touche programmable exclusivement.
    # Renvoie les valeurs de X et Y selon l'équation de mouvement et selon l'angle paramétré
    # Auteur : Ethan SUISSA - Terminé
    def ValeurPosXY_P(self, valX_Initial, valY_Initial, Temps):
        print("ValPosXY :  valXInitial =", valX_Initial)  # Pour controle
        print("ValPosXY :  valYInitial =", valY_Initial)  # Pour controle
        AngleEnDegree = degrees(self.ValeurAngleParametreEnRadian())  # Convertie l'angle retourné en radian en degrés

        # Ajustement de l'angle pour le quart de repère dans lequel on se trouve :
        # Bloc 1 = quart haut-droite
        if 0 <= AngleEnDegree <= 90:
            print("ValPosXY :  Bloc 1 ")  # pour controle
            Dx, Dy = self.CalcProg(AngleEnDegree, Temps)  # Retourne les déplacement de x et y
            self.valX_Final = valX_Initial + Dx
            self.valY_Final = valY_Initial - Dy  # Déplacement dans le sens du repère de l'écran : vers la droite pour X
            # avec l'addition et vers le haut pour Y avec la soustraction

        # Bloc 2 = quart haut-gauche
        if 90 < AngleEnDegree <= 180:
            print("ValPosX :  Bloc 2 ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 90  # Ajustement de l'angle pour celui des calculs de la trajectoire
            # dans le bloc 2.
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial - Dy  # Soustraction au lieu d'addition pour X car déplacement horizontal vers
            # la gauche, inversion X et Y pour changement de repère.
            self.valY_Final = valY_Initial - Dx

        # Bloc 3 = quart bas-gauche
        if 180 < AngleEnDegree <= 270:
            print("ValPosX :  Bloc 3 ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 180
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial - Dx  # Addition au lieu de soustraction pour X car déplacement horizontal
            # vers la gauche.
            self.valY_Final = valY_Initial + Dy  # Addition au lieu de soustraction pour Y car déplacement vertical
            # vers le bas.
            # inversion X et Y pour changement de repère.

        # Bloc 4 = quart bas-droite
        if 270 < AngleEnDegree <= 360:
            print("ValPosX :  Bloc 4  ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 270
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial + Dy
            self.valY_Final = valY_Initial + Dx  # Addition au lieu de soustraction pour Y car déplacement vertical vers
            # le bas inversion X et Y pour changement de repère.

        print("ValPosXY : ValXFinal avant correction = ", self.valX_Final)  # Pour contrôle.
        print("ValPosXY : ValYFinal avant correction = ", self.valY_Final)  # Pour contrôle.

        # Correction de la position X si on sort du cadre
        # Rebond à gauche ou à droite
        rebondL = self.RebondLargeur(valX_Initial)
        rebondH = self.RebondHauteur(valY_Initial)
        if rebondL or rebondH:  # Si un des deux types de rebond est repéré, on considère qu'il en a eu 1.
            rebond = True
        else:
            rebond = False
        return self.valX_Final, self.valY_Final, rebond, Temps

    # ========================
    # FONCTION OUTIL : Vérifient si il y a eu un rebond, si oui, envoient une confirmation avec un booléen. La première
    # gère ceux à gauche ou à droite, et la 2e ceux en haut ou en bas. Auteur : Ethan SUISSA - Terminé

    def RebondLargeur(self, valX_Initial):
        rebond = False  # On considère qu'il n'y a pas de rebond au début.
        # Rebond à droite
        if self.valX_Final > self.Largeur - self.Perso_Largeur + 20:  # -20 ou -20 Pour précision du rebond
            print("ValPosXY (posX):  Sortie du cadre à droite => Rebond ")
            self.valX_Final = valX_Initial - self.Perso_Largeur + 20  # Réajustement de la position X à celle juste avant
            rebond = True  # Marque le rebond pour ne pas rebondir indéfiniment (voir fonction "deplacement_P).

            # Rebond à gauche
        if self.valX_Final < self.Perso_Largeur - 20:
            print("ValPosXY (posX):  Sortie du cadre à gauche => Rebond ")
            self.valX_Final = valX_Initial + self.Perso_Largeur - 20
            rebond = True
        return rebond

    def RebondHauteur(self, valY_Initial):
        rebond = False  # On considère qu'il n'y a pas de rebond au début.
        # Rebond en bas
        if self.valY_Final < self.Perso_Hauteur - 30:  # -30 ou +30 Pour précision du rebond
            print("ValPosXY (posY):  Sortie en bas ==> Rebond")
            self.valY_Final = valY_Initial + self.Perso_Hauteur - 30
            rebond = True
            # Rebond en haut
        if self.valY_Final > self.Hauteur - self.Perso_Hauteur + 30:
            print("ValPosXY (posY):  Sortie en haut ==> Rebond")
            self.valY_Final = valY_Initial - self.Perso_Hauteur + 30
            rebond = True
        return rebond

    # ========================
    # FONCTION OUTIL : Renvoie les valeurs de X et Y pour commandes figées. Auteur : Lilandra ALBERT-LAVAUX - Terminé

    def ValeurPosX(self, valInit, VarX):
        self.valX_Final = valInit + VarX  # On crée la nouvelle position de X en aditionnant son ancienne position avec
        # le décalage sur les cotés (vers la droite ou la gauche).
        rebond = self.RebondLargeur(valInit)  # On teste le rebond sur les côtés avec la fonction RebondLargeur.
        return self.valX_Final, rebond  # Renvoie des paramètres aux fonctions de déplacement pour réutilisation.

    def ValeurPosY(self, valInit, VarY):
        self.valY_Final = valInit + VarY  # On crée la nouvelle position de Y en aditionnant son ancienne position avec
        # le décalage de hauteur (vers le haut ou le bas).
        rebond = self.RebondHauteur(valInit)  # On teste le rebond sur les côtés avec la fonction RebondHauteur.
        return self.valY_Final, rebond  # Renvoie des paramètres aux fonctions de déplacement pour réutilisation.

    # ========================
    # FONCTION de creation des obstacles : ajoute un obstacle de direction aléatoire toutes les 10 secondes environ.
    def AjoutBalles(self):
        # ATTENTION: Les directions des obstacles dans le nom représentent l'endroit d'où ils partent, et non leurs
        # trajectoires.
        # Declaration initiales (rappel)
        if self.FinAttente:  # Si Pause n'est pas activé, sert aussi pour éviter les interruptions brutales
            # Pré-déclaration pour "rassurer" Pycharm.
            CoordObstacleRandom = {}
            # L'obstacle crée prend un des 4 types d'obstacles (partant de : haut, bas, droite ou gauche) de mainère
            # aléatoire. Ce type est représenté par un numéro entre 0 et 3, choisi au hasard par randint.
            TypeObstacle = randint(0, 3)
            # La déclaration du nouvel obstacle est identique à celle des 4 obstacles initiaux.
            # Si le type est 0, l'obstacle partira de la gauche.
            if TypeObstacle == 0:
                CoordObstacleRandom = {'x': 50,
                                       'y': self.listposY[randint(0, 26)],  # 26 et 46 car liste a décalage de position
                                       'ray': self.RayonObstacles,
                                       'dx': self.Listvitesse[0] * cos(self.Listangle[0]),
                                       'dy': self.Listvitesse[0] * sin(self.Listangle[0])}
            # Si le type est 1, l'obstacle partira du Haut.
            if TypeObstacle == 1:
                CoordObstacleRandom = {'x': self.listposX[randint(0, 46)],
                                       'y': 50,
                                       'ray': self.RayonObstacles,
                                       'dx': self.Listvitesse[1] * cos(self.Listangle[1]),
                                       'dy': self.Listvitesse[1] * sin(self.Listangle[1])}

            # Si le type est 2, l'obstacle partira de la droite.
            if TypeObstacle == 2:
                CoordObstacleRandom = {'x': self.Largeur - self.RayonObstacles - 1,
                                       'y': self.listposY[randint(0, 26)],
                                       'ray': self.RayonObstacles,
                                       'dx': self.Listvitesse[2] * cos(self.Listangle[2]),
                                       'dy': self.Listvitesse[2] * sin(self.Listangle[2])}

            # Si le type est 3, l'obstacle partira du bas.
            if TypeObstacle == 3:
                CoordObstacleRandom = {'x': self.listposX[randint(0, 46)],
                                       'y': self.Hauteur - self.RayonObstacles - 1,
                                       'ray': self.RayonObstacles,
                                       'dx': self.Listvitesse[3] * cos(self.Listangle[3]),
                                       'dy': self.Listvitesse[3] * sin(self.Listangle[3])}

            # Creation de l'image mobile de la boule de feu.
            self.objImgBoulFeu = self.CanevasJeu.create_image(CoordObstacleRandom['x'], CoordObstacleRandom['y'],
                                                              image=self.imgBoulFeu)

            # Ajout des propriétés du nouvel obstacles dans chaque liste, de la même manière que pour les 4 premiers. Il
            # sera donc considéré comme un nouvel obstacles à gérer pour les fonctions de mouvements
            if len(self.balles) < 50 and self.FinAttente:  # S'il n'y a pas déjà 50 obstacles (pour éviter une génération infinie).
                self.ListPosInitBalles.append({'x0': CoordObstacleRandom['x'], 'y0': CoordObstacleRandom['y']})
                self.balles.append(CoordObstacleRandom)
                self.ListImgBoulFeu.append(self.objImgBoulFeu)
            # print("balles", self.balles, "balls", self.balls)  # Pour contrôle.
            if self.FinAttente:
                self.after(10000,
                           self.AjoutBalles)  # Réinitialisation de la fonction toutes les 10s pour créer un obstacle.

    # ========================
    # FONCTION concentrant toutes celles gérant le déplacement des obstacles, les conséquences en cas de collision
    # (impact sur les vies, réinitialisation des obstacles, création de l'image d'explosion), ainsi que celle sur le
    # compte du score.
    def action(self):
        if self.FinAttente:  # Si Pause n'est pas activé, sert aussi pour éviter les interruptions brutales :
            self.collide()  # Gère les collisions des obstacles avec le vaisseau ou les bords du canevas.
            self.ComptageScore()  # S'occupe du comptage du score et de son affichage au cours du temps.
            self.AnimExplos()  # Gère la création de l'image d'explosion au moment de l'impact avec les obstacles.
            self.move()  # Fait bouger les obstacles
            self.after(20, self.action)  # Réinitialisation de la fonction toute les 20 ms pour déplacement permanent.

    # ========================
    # FONCTION créant un déplacement d'obstacle bref en additionnant leurs déplacements instantanéee à leur coordonnée
    # initiales.
    def move(self):
        "Déplacement des balles"
        for i in range(len(self.balles)):  # Une boucle parcour la listes des dictionnaires de coordonnés
            # de chaque obstacles,
            self.balles[i]['x'] += self.balles[i]['dx']  # Chaque obstacle voit sa coordonné en abscisse additionnée
            # avec son déplacement instantanné en abscisse.
            self.balles[i]['y'] += self.balles[i]['dy']  # Chaque obstacle voit sa coordonné en ordonnée additionnée
            # avec son déplacement instantanné en ordonnée.
            if self.FinAttente:  # Sert pour éviter les interruptions brutales
                # Les obstacles sont redessinées à leur nouvelles positions.
                self.CanevasJeu.coords(self.ListImgBoulFeu[i], self.balles[i]['x'], self.balles[i]['y'])

    # ========================
    # FONCTION vérifiant si les obstacles sont en collision avec les bords du Canevas ou le vaisseau. Si oui, les
    # obstacles sont réinitialisés, avec perte d'une vie pour le vaisseau si collision avec celui-ci.
    def collide(self):
        "Test de collision des balles"

        # Si collision avec les parois, les obstacles retournent à leurs posisitons initiales :
        for i in self.balles:  # La boucle vérifie les collisions pour chaque balle.
            if i['x'] - i['ray'] <= 0:  # Si l'obstacle va trop à gauche, réinitialisation à droite
                i['x'] = self.Largeur - self.RayonObstacles - 1
                i['y'] = self.listposY[randint(0, 26)]

            if i['x'] + i['ray'] >= int(self.CanevasJeu['width']):  # Si l'obstacle va trop à droite, réinitialisation
                # à gauche
                i['x'] = 50
                i['y'] = self.listposY[randint(0, 26)]

            if (i['y'] - i['ray']) <= 0:  # Si l'obstacle va trop en haut, réinitialisation en bas
                i['x'] = self.listposX[randint(0, 46)]
                i['y'] = self.Hauteur - self.RayonObstacles - 1

            if (i['y'] + i['ray']) >= int(self.CanevasJeu['height']):  # Si l'obstacle va trop en bas, réinitialisation
                # en haut
                i['x'] = self.listposX[randint(0, 46)]
                i['y'] = 50

        # Si collision avec le vaisseau : déclenchement de la fonction associée.
        self.CollisionVaisseau()

    # ========================
    # FONCTION vérifiant si les obstacles sont en collision avec le vaisseau. Si oui, appliquation des conséquences.
    def CollisionVaisseau(self):
        ListCollisions = self.CanevasJeu.find_overlapping(self.PosX - self.Perso_Largeur // 2,
                                                          self.PosY - self.Perso_Hauteur // 2,
                                                          self.PosX + self.Perso_Largeur // 2,
                                                          self.PosY + self.Perso_Hauteur // 2)
        # Find-overlapping retourne la liste des objets débordant sur un rectangle dont les coordonnées sont envoyées en
        # paramètres (ici le rectangle représente le personnage). Les coordonnées du rectangle sont celles des deux
        # sommets de sa diagonale principale (celui du bas puis celui du haut). Elle les retourne sous forme d'un tuple
        # des nombres associés aux éléments graphiques crées.

        if len(ListCollisions) > 2:  # On vérifie si la liste du tuple de find.Overlapping excède 2, c'est à dire s'il y
            # a un objet supplémentaire en contact avec le vaisseau. En effet, deux objets sont toujours sur ce
            # rectangle: l'image du perso (représentée par 1) et celle du Canevas (représentée par 6).

            for i in range(len(ListCollisions)):
                for j in range(len(self.ListImgBoulFeu)):
                    if ListCollisions[i] == self.ListImgBoulFeu[j]:  # Si le nombre du
                        # tuple est celui associé à l'une des
                        # balles, mais pas celui des pointes de vaisseaux car ce sont des images de fond uniquement.
                        if self.FinAttente:  # Sert pour éviter les interruptions brutales
                            print("Collision balle avec :", i, "Fin de partie")
                            self.ActionsPerteVie()  # Declenchement la fonction de perte de vie et l'ensemble des
                            # évènements associés.

    # ========================
    # FONCTION organisant la perte d'une vie avec l'ensemble des évènements associés : baisse du compteur, modification
    # du StringVar associé, activation de l'image d'explosion, déclenche la fin de Partie si plus de vie.
    def ActionsPerteVie(self):
        for i in range(len(self.ListPosInitBalles)):  # Réinitialisation des balles à leurs positions initiales en
            # utilisant la liste des positions initiales, et ce pour chaque obstacle.
            self.balles[i]['x'] = self.ListPosInitBalles[i]['x0']  # La coordonnée x reprend sa position initiale.
            self.balles[i]['y'] = self.ListPosInitBalles[i]['y0']  # La coordonnée y reprend sa position initiale.
        self.Explosion = True  # Fait passer l'image d'explosion au premier plan, jusqu'au moment ou un déplacement sera
        # exécuté.
        self.CompteurVies -= 1  # Diminution du nombre de vies.
        self.TextVies.set(str(self.CompteurVies))  # Changement de l'affichage du nombre de vie en conséquence.
        if self.FinAttente and self.CompteurVies == 0:  # S'il ne reste plus de vie :
            time.sleep(0.3)  # Fige la fenêtre pendant quelques secondes pour marquer l'impact.
            self.Fin_Partie()  # Declenchement de la fin de partie.

    # ========================
    # FONCTION gérant l'affichage de l'image d'explosion à chaque perte d'une vie, ainsi que le fait de la repasser à
    # l'arrière plan quand le vaisseau se redéplace (s'il reste des vies).
    def AnimExplos(self):
        if self.FinAttente:  # Sert pour éviter les interruptions brutales.
            self.CanevasJeu.coords(self.objImgExpl, self.PosX, self.PosY)
            if self.Explosion:  # Si le booléen est à "True", l'image devient visible, sinon elle redevient invisible.
                self.CanevasJeu.tag_raise(self.objImgExpl)  # Passage de l'image au 1er plan.
            else:
                self.CanevasJeu.tag_lower(self.objImgExpl)  # Passage de l'image à l'arriere plan.

    # ========================
    # FONCTION s'occupant du compte du score en l'augmentant à chaque fois et en changeant l'affichage à l'écran.
    def ComptageScore(self):
        self.CompteurScore += 0.03  # L'augmentation de la variable de score est calculé avec l'actualisation de la
        # fonction "action" toutes les 20 ms pour qu'au final, le score augmente d'1 toute les secondes.
        if self.FinAttente:  # Si bouton pause non activé, évite les interruptions brutales.
            self.TextScore.set(str(int(self.CompteurScore)))  # Affichage de la nouvelle valeur de score

    # ========================
    # FONCTION créeant une pause du jeu : les commandes deviennent inutilisables et les obstacles sont figées. L'effet
    # se désactive en cliquant sur "Reprendre", la fonction en dessous redémarre alors l'ensemble des processus.
    def Pause(self):
        self.FinAttente = False  # Les fonctions de déplacement des objets et personnage ne s'active que si ce boléen
        # est à "True", donc blocage de ces actions. Quitter la fenêtre de jeu reste cependant possible (contrairement
        # à time.sleep()).

        self.B0_FinPartie['state'] = NORMAL  # Le bouton B10 qui n'était pas activable avec l'option "state = DISABLED"
        # le redevient en changeant l'état à "Normal". Ce bouton n'est activable en effet que si le bouton pause est
        # actif, et se désactive après le clic sur "Reprendre.

        self.BoutonReprise['state'] = NORMAL  # De même, le bouton reprendre n'est actif que si le Pause a été activé,
        # il se désactive ensuite lui-même jusqu'au prochain clic sur "Pause".

    # ========================
    # FONCTION Outil qui redémarre les processus et désactive les boutons "Fin de partie" et "Reprendre".
    def Reprendre(self):  # Si le bouton "Reprendre" est cliqué, le boléen change et tout redémarre
        self.FinAttente = True
        self.B0_FinPartie['state'] = DISABLED
        self.BoutonReprise['state'] = DISABLED  # Desactive de nouveau le bouton "Fin de partie" et le bouton
        # "Reprendre" jusqu'au prochain clic sur "Pause".
        self.AjoutBalles()
        self.action()  # Redémarre les balles car fonctions récursive, activée une fois seulement dans l'algorithme
        # principal.

    # Fonctions paramétrant le plein écran (déjà expliquée dans F00).
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    # ========================
    # COMMANDE = ouvre F01,  (retour au menu)
    # Auteur : Ethan SUISSA - En Cours
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F02
        # ouvre F01
        app = wF01.F01(self.IdJoueur)
        app.focus_force()  # Force le focus sur la fenetre
        app.mainloop()

    # ========================
    # COMMANDE = ouvre F04,  Fenêtre de résultat de la partie
    # Auteur : Ethan SUISSA - En Cours
    def commandeOuvreF04(self):
        # Ferme la fenetre
        F02.destroy(self)  # ferme F02, format donne même résultat
        # ouvre F01
        app = F04(self.CompteurScore, self.IdJoueur, self.Old_best_score)
        app.focus_force()  # Force le focus sur la fenetre
        app.mainloop()

    # ========================
    # FONCTION : Fonction de fin de partie, appelée si partie finie pour récupérer le meilleur score et ouvrir F04
    def Fin_Partie(self):
        self.FinAttente = False  # Arrêt de toutes les fonctions en cours exécutée par l'ordi.
        # Arrêt des actualisation de fenêtre par les fonctions pour éviter les problèmes d'arrêt brutal du script.
        self.after_cancel(self.action)
        self.after_cancel(self.AjoutBalles)
        self.after_cancel(self.idAfterD)
        self.after_cancel(self.idAfterP)
        self.after_cancel(self.idAfterQ)
        self.after_cancel(self.idAfterZ)
        self.after_cancel(self.idAfterS)
        BestScore, OldBestScore = score_comparaison(int(self.CompteurScore),
                                      self.IdJoueur)  # Ligne trouvée avec l'ID dans la fonction. Retourne le nouveau et
        # l'ancien meilleur score.
        self.Old_best_score = OldBestScore
        ModifPrecisFichier(self.IdJoueur + 2, 3, BestScore)  # self.IdJoueur +2 car c'est le numéro de ligne
        # correspondant, le meilleur score est à l'emplacement t[i][3] du tableau d'"open_score_file",
        # BestScore est ce qu'on écrit.
        self.commandeOuvreF04()
