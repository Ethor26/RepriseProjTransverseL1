from tkinter import *
import tkinter as tk
import time


def F04(score, t4):
    personal_best = 150
    self = Tk()
    self.title("F04")
    canvas = Canvas(self, width=500, height=300)
    canvas.configure(background='black')
    canvas.pack()
    if (score>personal_best):
        Bravo = canvas.create_text(250, 150, text="Bravo, vous avez battu votre record !\nVotre score est : {}\nVotre ancien meilleur score était : {}\nVous avez tenu : {} secondes".format(score, personal_best,t4), font='Gabriola 17', fill='white')
    else:
        Dommage = canvas.create_text(250, 150, text="Dommage, vous ferez mieux la prochaine fois !\n Votre score est : {}\nVotre meilleur score est : {}\nVous avez tenu : {} secondes".format(score, personal_best,t4), font='Gabriola 17', fill='white')
    b1 = Button(self, text="Quitter", command=self.destroy).place(x=10, y=270)
    b2 = Button(self, text="Rejouer", command=self).place(x=60, y=270)
    self.mainloop()



def Score():
#Augmente le score toutes les X millisecondes
    global CompteurScore
    CompteurScore += 15
    compteur_lbl['text'] = str(CompteurScore)
    app.after(1000, Score)


app = tk.Tk()
canvas = Canvas(app, width = 1200, height = 700)
canvas.configure(background='black')
canvas.pack()
CompteurScore = 0
compteur_lbl = tk.Label(app, text=str(CompteurScore), font=("", 16))
compteur_lbl.place(x=8,y=8)

app.after(1000, Score)
app.mainloop()