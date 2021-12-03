import os
from random import *
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage
from Tools import *
import wF01  # Modification de l'import pour éviter les "circular import", en général rajoute des "wF01.Tk"
from wF04 import F04

self.raquette = self.CanevasJeu.create_rectangle(200, 380, 400, 390, fill='red')

# position initiale aleatoire
self.listpos = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525,
                550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025,
                1050, 1075, 1100, 1125, 1150, 1175, 1200]
# direction initiale aléatoire
Listvitesse = []
for i in range(4):
    Listvitesse.append(uniform(1.8, 2) * 4)

Listangle = []
AngleRadianBalle = 0
for i in range(4):
    Listangle.append(AngleRadianBalle)
    AngleRadianBalle += pi / 2

print("ListAngles:", Listangle, "ListeVitesses", Listvitesse)
# DX = vitesse * math.cos(angle)
# DY = vitesse * math.sin(angle)

# ATTENTION: Les directions des obstacles dans le nom représentent l'endroit d'où ils partent, et non leurs
# trajectoires.

CoordObstacleGauche = {'x': 50,
                       'y': self.listpos[randint(0, 5)],
                       'ray': self.RayonObstacles,
                       'dx': Listvitesse[0] * cos(Listangle[0]),
                       'dy': Listvitesse[0] * sin(Listangle[0])}

CoordObstacleHaut = {'x': self.listpos[randint(0, 7)],
                     'y': 50,
                     'ray': self.RayonObstacles,
                     'dx': Listvitesse[1] * cos(Listangle[1]),
                     'dy': Listvitesse[1] * sin(Listangle[1])}

CoordObstacleDroite = {'x': self.Largeur - self.RayonObstacles - 1,
                       'y': self.listpos[randint(0, 5)],
                       'ray': self.RayonObstacles,
                       'dx': Listvitesse[2] * cos(Listangle[2]),
                       'dy': Listvitesse[2] * sin(Listangle[2])}

CoordObstacleBas = {'x': self.listpos[randint(0, 7)],
                    'y': self.Hauteur - self.RayonObstacles - 1,
                    'ray': self.RayonObstacles,
                    'dx': Listvitesse[3] * cos(Listangle[3]),
                    'dy': Listvitesse[3] * sin(Listangle[3])}

self.balles = [CoordObstacleDroite, CoordObstacleHaut, CoordObstacleGauche, CoordObstacleBas]

ObjObstacleGauche = self.CanevasJeu.create_oval(CoordObstacleGauche['x'] - CoordObstacleGauche['ray'],
                                                CoordObstacleGauche['y'] - CoordObstacleGauche['ray'],
                                                CoordObstacleGauche['x'] + CoordObstacleGauche['ray'],
                                                CoordObstacleGauche['y'] + CoordObstacleGauche['ray'],
                                                fill='red')

ObjObstacleHaut = self.CanevasJeu.create_oval(CoordObstacleHaut['x'] - CoordObstacleHaut['ray'],
                                              CoordObstacleHaut['y'] - CoordObstacleHaut['ray'],
                                              CoordObstacleHaut['x'] + CoordObstacleHaut['ray'],
                                              CoordObstacleHaut['y'] + CoordObstacleHaut['ray'],
                                              fill='green')

ObjObstacleDroite = self.CanevasJeu.create_oval(CoordObstacleDroite['x'] - CoordObstacleDroite['ray'],
                                                CoordObstacleDroite['y'] - CoordObstacleDroite['ray'],
                                                CoordObstacleDroite['x'] + CoordObstacleDroite['ray'],
                                                CoordObstacleDroite['y'] + CoordObstacleDroite['ray'],
                                                fill='blue')

ObjetObstacleBas = self.CanevasJeu.create_oval(CoordObstacleBas['x'] - CoordObstacleBas['ray'],
                                               CoordObstacleBas['y'] - CoordObstacleBas['ray'],
                                               CoordObstacleBas['x'] + CoordObstacleBas['ray'],
                                               CoordObstacleBas['y'] + CoordObstacleBas['ray'],
                                               fill='yellow')


# FONCTION de déplacement des obstacles
def action(self):
    "Animation"
    print("Action balle !")
    self.collide()
    self.move()
    if self.FinAttente:  # Si Pause n'est pas activé
        self.after(20, self.action)


def move(self):
    "Déplacement des balles"
    for i in range(len(self.balles)):
        self.balles[i]['x'] += self.balles[i]['dx']
        self.balles[i]['y'] += self.balles[i]['dy']
        self.CanevasJeu.coords(self.balls[i],
                               self.balles[i]['x'] - self.balles[i]['ray'],
                               self.balles[i]['y'] - self.balles[i]['ray'],
                               self.balles[i]['x'] + self.balles[i]['ray'],
                               self.balles[i]['y'] + self.balles[i]['ray'])


def collide(self):
    "Test de collision des balles"

    # Collision avec les parois
    j = 0
    for i in self.balles:
        if (i['x'] - i['ray']) <= 0 or (i['x'] + i['ray']) >= int(self.CanevasJeu['width']) or \
                (i['y'] - i['ray']) <= 0 or (i['y'] + i['ray']) >= int(self.CanevasJeu['height']):
            # i['dx'] = -i['dx']
            # CopieObjBall = self.balls[j]
            # CopieCoordBall = self.balles[j]

            # Réinitialisation à droite
            if self.balls[j] == 10:
                i['x'] = self.Largeur - self.RayonObstacles - 1
                i['y'] = self.listpos[randint(0, 28)]

            # Réinitialisation en basd
            if self.balls[j] == 11:
                i['x'] = self.listpos[randint(0, 48)]
                i['y'] = self.Hauteur - self.RayonObstacles - 1

            # Réinitialisation à gauche
            if self.balls[j] == 8:
                i['x'] = 50
                i['y'] = self.listpos[randint(0, 28)]
            # Réinitialisation en haut
            if self.balls[j] == 9:
                i['x'] = self.listpos[randint(0, 48)]
                i['y'] = 50

            # Modif de balls, balles et des coordonnées de départ à faire
            # self.CanevasJeu.delete(self.balls[j])
        j += 1

        # di['dy'] = -i['dy']
    # Collision entre les balles
    # ordre = 1/2, 1/3, 1/4, 2/3, 2/4, 3/4
    #         for i in range(len(self.balles)):
    #             j = i + 1
    #             while j < len(self.balles):
    #                 # Test si (ray1+ray2)² > dist(x1-x2)² + dist(y1-y2)²
    #                 # et interverti les dx et dy
    #                 if (self.balles[i]['ray'] + self.balles[j]['ray']) ** 2 > \
    #                         ((self.balles[i]['x'] - self.balles[j]['x']) ** 2 +  # \
    #                          (self.balles[i]['y'] - self.balles[j]['y']) ** 2):
    #                     self.balles[i]['dx'], self.balles[j]['dx'] = self.balles[j]['dx'], self.balles[i]['dx']
    #                     self.balles[i]['dy'], self.balles[j]['dy'] = self.balles[j]['dy'], self.balles[i]['dy']
    #                 j += 1
