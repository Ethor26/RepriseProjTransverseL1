import math
# import os

# from pygame import event

print("Welcome to testEthan")

from tkinter import *
# from Tools import *
from math import *


# Version fonction
def ComClav2(event2):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX, PosY
    touche = event2.keysym  # Un événement (event) est la survenue d’une action (clavier, souris) dont votre application a besoin d’être informée
    print(touche)
    VarX = 4
    angle = ValeurAngle()
    # déplacement programmable

    if touche == 'p':
        # for i in range(5): # Pour déplacement progressif
        PosY -= int(CalcProg(angle, VarX))
        PosX += VarX
    print(PosY)
    print(PosX)
    print(Pion)
    Canevas.coords(Pion, PosX - 10, PosY - 10, PosX + 10, PosY + 10)
    # on dessine le pion à sa nouvelle position


# =============================================================================
# FONCTION OUTIL: Calcul de la commande programmable. Auteur : Ethan SUISSA - En cours
def CalcProg(angle, VarX):
    v0 = 10 ** 2
    g = 9.81
    Eqmouv = (-1 / 2) * ((g * VarX ** 2) / (v0 * cos(angle)) ** 2) + tan(angle) * VarX
    return (Eqmouv)


def ValeurAngle():
    # codage à faire
    angle = math.radians(45)
    return angle


def PosInit():
    PosX = 230
    PosY = 150
    return (PosX, PosY)


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Pion')


# position initiale du pion
PosX = 230
PosY = 150
# Paramètre commande programmables
angle = 45

# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width=Largeur, height=Hauteur, bg='white')
Pion = Canevas.create_oval(PosX - 10, PosY - 10, PosX + 10, PosY + 10, width=2, outline='black', fill='red')
Canevas.focus_set()  # crée un cadre autour du canvas et permet l'activation de bind
Canevas.bind('<Key>', ComClav2)
Canevas.pack(padx=5, pady=5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text='Quitter', command=Mafenetre.destroy).pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()
