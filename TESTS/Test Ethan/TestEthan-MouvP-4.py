# Bibliothèques
import math
from tkinter import *
from math import *
# import time

print("Welcome to TestEthan-MouvP-4")

Largeur = 1000  # Largeur Ecran Jeu
Hauteur = 500  # Hauteur Ecran Jeu
Rayon = 10  # rayon de l'objet

AngleEnDegree = 40
Temps = 0
# position initiale du pion
PosX = 230
PosY = 150


# Version fonction
def CommandeClavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    touche = event.keysym  # Un événement (event) est la survenue d’une action (clavier, souris) dont votre application
    # a besoin d’être informée

    # Si touche ? => deplt a droite
    # A CODER

    # Si touche ? => deplt a Gauche
    # A CODER

    # Si touche ? => deplt a bas
    # A CODER

    # Si touche ? => deplt a Haut
    # A CODER

    if touche == 'p':
        deplacement_P()


# =============================================================================
# Fonction de déplacement de la touche P
def deplacement_P():
    global PosX, PosY, Temps  # Pour qu'elles soient utilisables partout
    nbRebond = 0  # Initialise le nombre de rebond à 0 (pour programmer l'arrêt à 1 rebond)

    PosX, PosY, siRebond, Temps = ValeurPosXY(PosX, PosY, Temps)  # La fonction retourne les paramètres de position x et
    # y de l'objet, ainsi que la variable de temps et le nombre de rebonds du déplacement.
    Temps = Temps + 0.0001
    print("posY = ", PosY)  # pour controle
    print("posX = ", PosX)  # pour controle
    print("Pion = ", Pion)  # pour controle
    print("t = ", Temps)  # pour controle

    Canevas.coords(Pion, PosX - 10, PosY - 10, PosX + 10, PosY + 10)
    # On dessine le persoPion à sa nouvelle position

    if siRebond:  # S'il y a plus de 0 rebond, on augmente le compteur
        nbRebond = nbRebond + 1
        print("Nombre de rebond = ", nbRebond)  # Pour control

    idAfter = Mafenetre.after(3, deplacement_P)

    if nbRebond > 0 or Temps > 0.05:  # Au bout d'un certain temps ou au dela d'un rebond, le déplacement s'arrête.
        Mafenetre.after_cancel(idAfter)


# FONCTION OUTIL: Calcul de la commande programmable. Auteur : Ethan SUISSA - En cours
def ValeurAngleParametreEnRadian():
    # codage à faire : Récupérer angle dans score.txt
    print("Angle en degree = ", AngleEnDegree)  # Pour contrôle
    angleRadian = math.radians(AngleEnDegree)  # valeur par defaut
    return angleRadian


# Utilise l'équation de mouvement pour calculer la postion finale en fonction de l'angle
def CalcProg(AngleDeduitDegree, Temps):
    v0 = 0.9  # Choix de vitesse à ... en m/s
    g = 9.81  # Constante de gravitation terrestre en m/s
    Angle_Deduit_Radian = math.radians(AngleDeduitDegree)  # convertion en Radian de l'angle deduit
    dx = v0 * cos(Angle_Deduit_Radian)  # Calcul du déplacement horizontal du perso
    if Angle_Deduit_Radian == 0.0:  # Si l'angle est nul, le perso suit un mouvement rectiligne uniforme, pas de chute.
        g = 0
    dy = -g * Temps + v0 * sin(Angle_Deduit_Radian)  # Calcul du déplacement vertical du perso
    print("Angle radian:", Angle_Deduit_Radian)  # Test
    return dx, dy


def ValeurPosXY(valX_Initial, valY_Initial, Temps):
    global valY_Final, valX_Final, rebond
    print("ValPosXY :  valXInitial =", valX_Initial)
    print("ValPosXY :  valYInitial =", valY_Initial)
    rebond = False

    # Bloc 1
    if 0 <= AngleEnDegree <= 90:
        print("ValPosXY :  Bloc 1 ")  # pour controle
        Dx, Dy = CalcProg(AngleEnDegree, Temps)
        valX_Final = valX_Initial + Dx
        valY_Final = valY_Initial - Dy

    # Bloc 2
    if 90 < AngleEnDegree <= 180:
        print("ValPosX :  Bloc 2 ")  # pour controle
        Angle_Deduit_Degree = AngleEnDegree - 90
        Dx, Dy = CalcProg(Angle_Deduit_Degree, Temps)
        valX_Final = valX_Initial - Dy
        valY_Final = valY_Initial - Dx

    # Bloc 3
    if 180 < AngleEnDegree <= 270:
        print("ValPosX :  Bloc 3 ")  # pour controle
        Angle_Deduit_Degree = AngleEnDegree - 180
        Dx, Dy = CalcProg(Angle_Deduit_Degree, Temps)
        valX_Final = valX_Initial - Dx
        valY_Final = valY_Initial + Dy

    # Bloc 4
    if 270 < AngleEnDegree <= 360:
        print("ValPosX :  Bloc 4  ")  # pour controle
        Angle_Deduit_Degree = AngleEnDegree - 270
        Dx, Dy = CalcProg(Angle_Deduit_Degree, Temps)
        valX_Final = valX_Initial + Dy
        valY_Final = valY_Initial + Dx

    print("ValPosXY : ValXFinal avant correction = ", valX_Final)
    print("ValPosXY : ValYFinal avant correction = ", valY_Final)

    # Corrige la position X si on sort du cadre
    # Rebond à droite
    if valX_Final > Largeur - Rayon:
        print("ValPosXY (posX):  Sortie du cadre à droite => Rebond ")
        valX_Final = valX_Initial - Rayon
        rebond = True

    # Rebond à gauche
    if valX_Final < Rayon:
        print("ValPosXY (posX):  Sortie du cadre à gauche => Rebond ")
        valX_Final = valX_Initial + Rayon
        rebond = True

    # Rebond en bas
    if valY_Final < Rayon:
        print("ValPosXY (posY):  Sortie en bas ==> Rebond")
        valY_Final = valY_Initial + Rayon
        rebond = True

    # Rebond en haut
    if valY_Final > Hauteur - Rayon:
        print("ValPosXY (posY):  Sortie en haut ==> Rebond")
        valY_Final = valY_Initial - Rayon
        rebond = True

    return valX_Final, valY_Final, rebond, Temps


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Pion')

# Création d'un widget Canvas (zone graphique)
Canevas = Canvas(Mafenetre, width=Largeur, height=Hauteur, bg='white')
Pion = Canevas.create_oval(PosX - 10, PosY - 10, PosX + 10, PosY + 10, width=2, outline='black', fill='red')
Canevas.focus_set()

Canevas.bind('<Key>', CommandeClavier)
Canevas.pack(padx=5, pady=5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text='Quitter', command=Mafenetre.destroy).pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()

# GRAVITE = 9.8
# ANGLE = PI / 4
# V0 = 0.8

# def setup():
#     global largeur
#     global hauteur
#     global x
#     global y
#     global dx
#     global dy
#     global t
#     largeur = 1000
#     hauteur = 500
#     size(1000, 500)
#     x = 0
#     y = hauteur / 2
#     dy = 0
#     t = 0
#     frameRate(100)
#
#
# def draw():
#     global x, y, t
#     background(200)
#     noStroke()
#     fill(255, 0, 0)
#     ellipse(x, y, 10, 10)
#     dx = - V0 * cos(PI - ANGLE)
#     dy = GRAVITE * t - V0 * sin(PI - ANGLE)
#     x = x + dx
#     y = y + dy
#     t = t + 0.0001
