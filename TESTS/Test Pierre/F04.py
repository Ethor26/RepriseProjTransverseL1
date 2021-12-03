from tkinter import *
import time

def F04():
    score = 1540
    personal_best = 1900
    self = Tk()
    self.title("F04")
    canvas = Canvas(self, width=500, height=300)
    canvas.configure(background='black')
    canvas.pack()
    if (score>personal_best):
        Bravo = canvas.create_text(250, 150, text="Bravo, vous avez battu votre record !\nVotre score est : {}\nVotre ancien meilleur score était : {}".format(score, personal_best), font='Gabriola 17', fill='white')
    else:
        Dommage = canvas.create_text(250, 150, text="Dommage, vous ferez mieux la prochaine fois !\n Votre score est : {}\nVotre meilleur score est : {}".format(score, personal_best), font='Gabriola 17', fill='white')
    b1 = Button(self, text="Quitter", command=self.destroy).place(x=10, y=270)
    b2 = Button(self, text="Rejouer", command=self).place(x=60, y=270)
    self.mainloop()


def Time(): #ca c'est l'idée que j'ai pour faire le temps d'affichage de la fenetre de jeu, a voir comment faire pour le mettre dans le code
    t1 = time.time()
    F04()
    t2 = time.time()
    t3 = t2-t1
    print(t3)


Time()
