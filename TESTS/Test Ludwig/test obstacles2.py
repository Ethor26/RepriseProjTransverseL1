from tkinter import *
from random import randrange as rr
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
            can.delete(ball2)   # Pour supprimer obstacle, ici ball2, du canvas "can"
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

ListPosYDepart = [100, 200, 300, 400, 500]


balle1 = {'x': 100,
          'y': ListPosYDepart[randint(0, 4)],
          'ray': ray,
          'dx': 8,
          'dy': 8}

balle2 = {'x': rr(canW - 2 * ray) + ray,
          'y': rr(canH - 2 * ray) + ray,
          'ray': ray,
          'dx': rr(-5, 5),
          'dy': rr(-5, 5)}

balle3 = {'x': rr(canW - 2 * ray) + ray,
          'y': rr(canH - 2 * ray) + ray,
          'ray': ray,
          'dx': rr(-5, 5),
          'dy': rr(-5, 5)}

balle4 = {'x': rr(canW - 2 * ray) + ray,
          'y': rr(canH - 2 * ray) + ray,
          'ray': ray,
          'dx': rr(-5, 5),
          'dy': rr(-5, 5)}

balles = (balle1, balle2, balle3, balle4)

ball1 = can.create_oval(balle1['x'] - balle1['ray'],
                        balle1['y'] - balle1['ray'],
                        balle1['x'] + balle1['ray'],
                        balle1['y'] + balle1['ray'],
                        fill='red')

ball2 = can.create_oval(balle2['x'] - balle2['ray'],
                        balle2['y'] - balle2['ray'],
                        balle2['x'] + balle2['ray'],
                        balle2['y'] + balle2['ray'],
                        fill='green')

ball3 = can.create_oval(balle3['x'] - balle3['ray'],
                        balle3['y'] - balle3['ray'],
                        balle3['x'] + balle3['ray'],
                        balle3['y'] + balle3['ray'],
                        fill='blue')

ball4 = can.create_oval(balle4['x'] - balle4['ray'],
                        balle4['y'] - balle4['ray'],
                        balle4['x'] + balle4['ray'],
                        balle4['y'] + balle4['ray'],
                        fill='yellow')

balls = (ball1, ball2, ball3, ball4)

Button(fen, text="Quitter", command=fen.quit).pack()

action()
fen.mainloop()

# Test de la collision avec la raquette : utilisation d'une fonction qui vérifie s'il y a un chevauchement avec un
# rectangle
#   if len(canvas.find_overlapping(canvas.coords(raquette)[0], canvas.coords(raquette)[1], canvas.coords(raquette)[2],
                              # canvas.coords(raquette)[3])) > 1:
# Adaptation:
# print("Collision",
#                   self.CanevasJeu.find_overlapping(self.PosX - self.Perso_Largeur//2, self.PosY - self.Perso_Hauteur//2,
#                                                    self.PosX + self.Perso_Largeur//2,
#                                                    self.PosY + self.Perso_Hauteur//2))
#             print("NumImage =", self.ImgPerso, self.objImgFondEcran, self.raquette, self.objImgV4, self.objImgV3,
#                   self.objImgV2, self.objImgV1)

