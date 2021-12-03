import tkinter as tk

from PIL import Image
from PIL.ImageTk import PhotoImage

Hauteur = 600
Largeur = 800

# position initiale du pion
PosX = 100
PosY = 100


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()  # taille de la fenetre
        self.create_widgets()

    def Clavier(self, event):
        """ Gestion de l'événement Appui sur une touche du clavier """
        global PosX, PosY
        touche = event.keysym
        print(touche)
        # déplacement vers le haut
        if touche == 'z':
            print("touche = z (monte)")
            PosY -= 45
        # déplacement vers le bas
        if touche == 's':
            print("touche = s (descend")
            PosY += 45
        # déplacement vers la droite
        if touche == 'd':
            print("touche = d (va à droite)")
            PosX += 30
        # déplacement vers la gauche
        if touche == 'q':
            print("touche = q (va à gauche) ")
            PosX -= 30
        # on dessine le pion à sa nouvelle position
        self.cnv.coords(self.objImg, PosX, PosY)

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.cnv = tk.Canvas(root, width=Largeur, height=Hauteur, bg="white")
        self.cnv.pack()

        self.image = Image.open(
            "/IMAGES/ImagesF02/faucon millenium-3.png")
        self.image = self.image.resize((30, 45), Image.ANTIALIAS)  # The (
        self.logo = PhotoImage(self.image)
        # self.logo = PhotoImage(file="IMAGES/fauconMillenium.png")
        self.objImg = self.cnv.create_image(PosX, PosY, image=self.logo)
        self.cnv.focus_set()
        self.cnv.bind('<Key>', self.Clavier)

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
