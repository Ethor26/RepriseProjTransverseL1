import math

print("Welcome to testEthan")

from tkinter import *
# from Tools import *
from math import *

Largeur = 480
Hauteur = 320
Rayon = 10  # rayon de l'objet

# position initiale du pion
PosX = 230
PosY = 150


# Version fonction
def CommandeClavier2(event2):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX, PosY
    touche = event2.keysym  # Un événement (event) est la survenue d’une action (clavier, souris) dont votre application a besoin d’être informée

    # Si touche ? => deplt a droite
    # A CODER

    # Si touche ? => deplt a Gauche
    # A CODER

    # Si touche ? => deplt a bas
    # A CODER

    # Si touche ? => deplt a Haut
    # A CODER

    if touche == 'p':
        PosY = ValeurPosY(PosY, 4)
        PosX = ValeurPosX(PosX, 4)

    print("posY = ", PosY)  # pour controle
    print("posX = ", PosX)  # pour controle
    print("Pion = ", Pion)  # pour controle
    Canevas.coords(Pion, PosX - 10, PosY - 10, PosX + 10, PosY + 10)
    # on dessine le pion à sa nouvelle position


# =============================================================================
# FONCTION OUTIL: Calcul de la commande programmable. Auteur : Ethan SUISSA - En cours
def ValeurAngle():
    # codage à faire : Récupérer angle dans score.txt
    angle = math.radians(179)
    print(angle) # Pour Test
    return angle

# Non utilisé
def PosInit():
    PosX = 230
    PosY = 150
    return (PosX, PosY)


def AdaptAngle(angle):
    MouvAngle = degrees(angle)
    if 90 < MouvAngle < 180:
        MouvAngle -= 90
    if 180 < MouvAngle < 270:
        MouvAngle -= 180
    if 270 < MouvAngle < 360:
        MouvAngle -= 270
    return MouvAngle

def CalcProg(angle, VarX):
    v0 = 5
    g = 9.81
    MouvAngle = math.radians(AdaptAngle(angle))
    Eqmouv = (-1 / 2) * ((g * VarX ** 2) / (v0 * cos(MouvAngle)) ** 2) + tan(MouvAngle) * VarX
    AdaptEqMouv = int(Eqmouv)
    return AdaptEqMouv



def ValeurPosX(valInitX, VarX):
    ParametreAngle = ValeurAngle()
    TVarX, TVarY, Angle = RenvRepere(VarX, ParametreAngle)
    valPosX = valInitX + TVarX
    # Test Axes

    # Verifie que l'on ne sort pas du cadre
    if valPosX > Largeur - Rayon:
        valPosX = valInitX - Rayon
    if valPosX < Rayon:
        valPosX = valInitX + Rayon
    return valPosX


def ValeurPosY(valInitY, VarX):
    ParametreAngle = ValeurAngle()
    TVarX, TVarY, Angle = RenvRepere(VarX, ParametreAngle)
    valPosY = valInitY + TVarY
    # Rebond en bas
    if valPosY < Rayon:
        valPosY = valInitY + Rayon
    # Rebond en haut
    if valPosY > Hauteur - Rayon:
        valPosY = valInitY - Rayon
    return valPosY

# CONFIGURATION RENVREPERE:
    # Configuration 1
def RenvRepere(VarX, angle):
    VarY = CalcProg(angle, VarX)
    TempX = VarX # Pour inversion
    TempY = VarY
    # Adaptation Angle et repères
    if 90 < degrees(angle) < 180:
        VarX = TempY
        VarY = VarX
    if 180 < degrees(angle) < 270:
        VarX = -VarX
        VarY = -VarY
    if 270 < degrees(angle) < 360:
        VarY = -VarY
    return VarX, VarY, angle

    # Configuration2
def RenvRepere2(VarX, VarY, angle):
    TempX = VarX # Pour inversion
    TempY = VarY
    MouvAngle = AdaptAngle(angle)
    # Adaptation Angle et repères
    if 90 < degrees(angle) < 180:
        VarX = -VarY
        VarY = TempX
    if 180 < degrees(angle) < 270:
        VarX = -VarX
        VarY = -VarY
    if 270 < degrees(angle) < 360:
        VarY = -VarX
        VarX = TempY
    return VarX, VarY, angle
# Pour Calcul de renversement de repère :
#     1: y = x, x = -y pour 90<angle<180 : division par 2 de l'angle
#     2: y = -y, x = -x pour 180<angle<270 : division par 4
#     3: y = -x, x = y pour 270<angle<360 : division par 8

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Pion')

# Paramètre commande programmables
# angle = 45

# Création d'un widget Canvas (zone graphique)

Canevas = Canvas(Mafenetre, width=Largeur, height=Hauteur, bg='white')
Pion = Canevas.create_oval(PosX - 10, PosY - 10, PosX + 10, PosY + 10, width=2, outline='black', fill='red')
Canevas.focus_set()

Canevas.bind('<Key>', CommandeClavier2)
Canevas.pack(padx=5, pady=5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text='Quitter', command=Mafenetre.destroy).pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()