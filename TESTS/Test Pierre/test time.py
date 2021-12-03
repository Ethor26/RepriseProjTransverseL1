import time
from tkinter import *
import tkinter as tk


def Chrono():
    global score
    montemps = time.time()
    time.time()-montemps
    x = True
    while x == True:
        time.sleep(1)
        print(time.strftime('%M # %S ', time.localtime()))
        score += 25
        score_variable.set(f'score: {score}')
        canvas.update()


def ChangeX():
    time.sleep(2)


x = True
self = Tk()
self.title("score update")
canvas = Canvas(self, width=400, height=400)
canvas.pack()
score = 0
b1 = Button(self, text="Update le score", command=Chrono).pack(side=RIGHT, padx=5, pady=5)
b2 = Button(self, text="Stop le chrono", command=ChangeX).pack(side=LEFT, padx=5, pady=5)
score_variable = tk.StringVar(self, f'score: {score}')
score_lbl = tk.Label(self, textvariable=score_variable).pack()
self.mainloop()


# FONCTION OUTIL : Lance un chrono lorsqu'on lance la partie, score augmente en fonction.
# Renvoie un chiffre, généré par la fonction qui sera utilisé comme score
# Auteur : Pierre REY - Terminé
def Chrono(self):
    global score
    montemps = time.time()
    time.time() - montemps
    score = 0
    score_variable = 0
    x = True
    while x == True:
        time.sleep(1)
        print(time.strftime('%M # %S ', time.localtime()))
        score += 25
        score_variable.set(f'score: {score}')
        self.update()


def ChangeX(self):
    time.sleep(2)

