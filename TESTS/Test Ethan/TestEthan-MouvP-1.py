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
def CommandeClavier(event2):
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
def CalcProg(angle, VarX):
    v0 = 10 ** 2
    g = 9.81
    Eqmouv = (-1 / 2) * ((g * VarX ** 2) / (v0 * cos(angle)) ** 2) + tan(angle) * VarX
    return Eqmouv


def ValeurAngle():
    # codage à faire : Récupérer angle dans score.txt
    angle = math.radians(350)
    print(angle)
    return angle


def PosInit():
    PosX = 230
    PosY = 150
    return (PosX, PosY)


def ValeurPosX(valInit, VarX):
    ParametreAngle = ValeurAngle()
    VraiVarX = VarX
    if 90 < degrees(ParametreAngle) < 270:
        VraiVarX = -VraiVarX
    valPosX = valInit + VraiVarX
    # Verifie que l'on ne sort pas du cadre
    if valPosX > Largeur - Rayon:
        valPosX = valInit - Rayon
    if valPosX < Rayon:
        valPosX = valInit + Rayon
    return valPosX


def ValeurPosY(valInit, VarX):
    ParametreAngle = ValeurAngle()
    DeplProgY = int(CalcProg(ParametreAngle, VarX))
    if (90 < degrees(ParametreAngle) < 180) or (270 < degrees(ParametreAngle) < 360):
        DeplProgY = -DeplProgY   # Pour permettre les déplacements à gauche
    valPosY = valInit - DeplProgY
    # Rebond en bas
    if valPosY < Rayon:
        valPosY = valInit + Rayon
    # Rebond en haut
    if valPosY > Hauteur - Rayon:
        valPosY = valInit - Rayon
    return valPosY


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Pion')

# Paramètre commande programmables
# angle = 45

# Création d'un widget Canvas (zone graphique)

Canevas = Canvas(Mafenetre, width=Largeur, height=Hauteur, bg='white')
Pion = Canevas.create_oval(PosX - 10, PosY - 10, PosX + 10, PosY + 10, width=2, outline='black', fill='red')
Canevas.focus_set()

Canevas.bind('<Key>', CommandeClavier)
Canevas.pack(padx=5, pady=5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text='Quitter', command=Mafenetre.destroy).pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()
