from tkinter import *
import math, random
# from random import randrange as rr
from random import randint


######
# Définitions de fonctions

def action():
    "Animation"
    collide()
    move()
    fen.after(20, action)


def move():
    "Déplacement des balles"
    for i in range(len(balles)):
        balles[i]['x'] += balles[i]['dx']
        balles[i]['y'] += balles[i]['dy']
        can.coords(balls[i],
                   balles[i]['x'] - balles[i]['ray'],
                   balles[i]['y'] - balles[i]['ray'],
                   balles[i]['x'] + balles[i]['ray'],
                   balles[i]['y'] + balles[i]['ray'])


def collide():
    "Test de collision des balles"
    # Collision avec les parois
    for i in balles:
        if (i['x'] - i['ray']) <= 0 or (i['x'] + i['ray']) >= int(can['width']):
            i['dx'] = -i['dx']
        if (i['y'] - i['ray']) <= 0 or (i['y'] + i['ray']) >= int(can['height']):
            i['dy'] = -i['dy']
    # Collision entre les balles
    # ordre = 1/2, 1/3, 1/4, 2/3, 2/4, 3/4
    for i in range(len(balles)):
        j = i + 1
        while j < len(balles):
            # Test si (ray1+ray2)² > dist(x1-x2)² + dist(y1-y2)²
            # et interverti les dx et dy
            if (balles[i]['ray'] + balles[j]['ray']) ** 2 > \
                    ((balles[i]['x'] - balles[j]['x']) ** 2 +  # \
                     (balles[i]['y'] - balles[j]['y']) ** 2):
                balles[i]['dx'], balles[j]['dx'] = balles[j]['dx'], balles[i]['dx']
                balles[i]['dy'], balles[j]['dy'] = balles[j]['dy'], balles[i]['dy']
            j += 1


#######################
# Programme principal #
#######################

######
# Widget principal
fen = Tk()
fen.title("Obstacles")

######
# Variables
canW, canH = 640, 480
ray = 15

######
# Widget enfants
can = Canvas(fen, width=canW, height=canH, bg='white')
can.pack(side=TOP, padx=5, pady=5)

# position initiale aleatoire
listpos= [50,100,150,200,250,300,350,400]

# direction initiale aléatoire
Listvitesse = []
for i in range(4):
    Listvitesse.append(random.uniform(1.8, 2) * 4)

Listangle = []
AngleRadianBalle = 0
for i in range(4):
    Listangle.append(AngleRadianBalle)
    AngleRadianBalle += math.pi/2


print("ListAngles:", Listangle, "ListeVitesses", Listvitesse)
# DX = vitesse * math.cos(angle)
# DY = vitesse * math.sin(angle)

CoordObstacleDroite = {'x': 50,
          'y': listpos[randint(0,5)],
          'ray': ray,
          'dx': Listvitesse[0] * math.cos(Listangle[0]),
          'dy': Listvitesse[0] * math.sin(Listangle[0])}

CoordObstacleBas = {'x': listpos[randint(0, 7)],
          'y': canH-ray+1,
          'ray': ray,
          'dx': Listvitesse[1] * math.cos(Listangle[1]),
          'dy': Listvitesse[1] * math.sin(Listangle[1])}

CoordObstacleGauche = {'x': canW - ray - 1,
          'y': listpos[randint(0,5)],
          'ray': ray,
          'dx': Listvitesse[2] * math.cos(Listangle[2]),
          'dy': Listvitesse[2] * math.sin(Listangle[2])}

CoordObstacleHaut = {'x': listpos[randint(0, 7)],
          'y': 50,
          'ray': ray,
          'dx': Listvitesse[3] * math.cos(Listangle[3]),
          'dy': Listvitesse[3] * math.sin(Listangle[3])}

balles = (CoordObstacleDroite, CoordObstacleBas, CoordObstacleGauche, CoordObstacleHaut)

ObjObstacleDroite = can.create_oval(CoordObstacleDroite['x'] - CoordObstacleDroite['ray'],
                                    CoordObstacleDroite['y'] - CoordObstacleDroite['ray'],
                                    CoordObstacleDroite['x'] + CoordObstacleDroite['ray'],
                                    CoordObstacleDroite['y'] + CoordObstacleDroite['ray'],
                                    fill='red')

ObjObstacleBas = can.create_oval(CoordObstacleBas['x'] - CoordObstacleBas['ray'],
                                 CoordObstacleBas['y'] - CoordObstacleBas['ray'],
                                 CoordObstacleBas['x'] + CoordObstacleBas['ray'],
                                 CoordObstacleBas['y'] + CoordObstacleBas['ray'],
                                 fill='green')

ObjObstacleGauche = can.create_oval(CoordObstacleGauche['x'] - CoordObstacleGauche['ray'],
                                    CoordObstacleGauche['y'] - CoordObstacleGauche['ray'],
                                    CoordObstacleGauche['x'] + CoordObstacleGauche['ray'],
                                    CoordObstacleGauche['y'] + CoordObstacleGauche['ray'],
                                    fill='blue')

ObjetObstacleHaut = can.create_oval(CoordObstacleHaut['x'] - CoordObstacleHaut['ray'],
                                    CoordObstacleHaut['y'] - CoordObstacleHaut['ray'],
                                    CoordObstacleHaut['x'] + CoordObstacleHaut['ray'],
                                    CoordObstacleHaut['y'] + CoordObstacleHaut['ray'],
                                    fill='yellow')

balls = (ObjObstacleDroite, ObjObstacleBas, ObjObstacleGauche, ObjetObstacleHaut)

Button(fen, text="Quitter", command=fen.quit).pack()

action()
fen.mainloop()
