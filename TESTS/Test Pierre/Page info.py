from tkinter import *
#fonction qui affiche le tutoriel


def F0001():
    self = Tk()
    self.title("F0001")
    canvas = Canvas(self, width=1200, height=700)
    canvas.configure(background='black')
    canvas.pack()
    txt = canvas.create_text(600,350, text="Bienvenue dans notre jeu ! \nLe but est simple :\n"
                           "- esquivez les missiles qui vous arrivent dessus\n"
                           "Pour cela, deux options s'offrent à vous :\n"
                           "La première est de se déplacer a l'aide des touches :\n 'z' : pour aller en haut\n'q' : pour aller a gauche\n"
                           "'s' : pour aller en bas\n'd' : pour aller à droite\n"
                           "La seconde est d'utiliser une commande programmable qui vous fera bondir\n"
                           "avec un angle que vous pouvez choisir dans les paramètres \n"
                           " 'p' : vous permettra d'executer cette commande", font='Gabriola 20 italic', fill='white')
    b1 = Button(self, text="Revenir au menu principal", command=self).pack(side=LEFT, padx=5, pady=5)
    b2 = Button(self, text="Close", command=self.destroy).pack(side=RIGHT, padx=5, pady=5)
    self.mainloop()

F0001()

