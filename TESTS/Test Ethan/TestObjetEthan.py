# Version objet
from Tools import *

class ProgCommandParam():
    # Constructeur de l'objet F01 : ne pas supprimer !!!
    def __init__(self, event2, angle, Canvas, Pion):
        """ Gestion de l'événement Appui sur une touche du clavier """
        global PosX, PosY
        touche = event2.keysym
        print(touche)
        VarX = 4
        # déplacement programmable
        if touche == 'p':
            for i in range(5): # Pour déplacement progressif
                # PosY += int(CalcProg(angle, VarX))
                PosX += 4

        # on dessine le pion à sa nouvelle position
        Canvas.coords(Pion, PosX - 10, PosY - 10, PosX + 10, PosY + 10)

from random import *

print(randint(1, 1000))
Liste = [100, 200, 300, 400, 500]
# position initiale aleatoire
listposX = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475,500,
                        525, 550, 575, 600, 625, 650, 675]

listposY = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475,500,
                        525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975,
                        1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175]
print("Longeur liste X", len(listposX),"Longeur liste Y", len(listposY), )
print(Liste[randint(0, 4)])

# print("Listes Collisions", ListCollisions, "\nNumImagePerso =", self.ImgPerso, "NumImageEcran =",
        # self.objImgFondEcran, "NumImageV4 =", self.objImgV4, "NumImageV3 =", self.objImgV3, "\nNumImageV2 =",
        # self.objImgV2, "NumImageV1 =", self.objImgV1, "\nNumBalleDroite =", self.balls[0], "NumBallebas =",
        # self.balls[3], "NumBalleGauche =", self.balls[2], "NumBalleHaut =", self.balls[1])  # Pour control de
        # collision : affiche identité des objets en collisions.
