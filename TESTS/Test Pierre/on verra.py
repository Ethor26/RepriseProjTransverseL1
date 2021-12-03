import time
from tkinter import *
import tkinter as tk


def Chrono():
    score = 0
    montemps = time.time()
    if x == True:
        while True:
            y = time.time()-montemps
            time.sleep(1)
            print(time.strftime('%M # %S ', time.localtime()))
            score += 100
            canvas.update()
            score_variable.set(f'score: {score}')


x = 0
score = 0
self = Tk()
self.title("score update")
canvas = Canvas(self, width=400, height=400)
canvas.pack()
b1 = Button(self, text="Update le score", command=Chrono).pack(side=RIGHT, padx=5, pady=5)
b2 = Button(self, text="Stop le chrono", command=self.destroy).pack(side=LEFT, padx=5, pady=5)
score_variable = tk.StringVar(self, f'score: {score}')
score_lbl = tk.Label(self, textvariable=score_variable).pack()

self.mainloop()

