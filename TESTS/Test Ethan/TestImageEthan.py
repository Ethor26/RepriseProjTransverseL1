import tkinter as Tk

from PIL import Image
from PIL.ImageTk import PhotoImage

print("Welcome to testImageEthan")


class Interface(Tk.Frame):
    def __init__(self, path_image, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.img = Image.open(path_image)
        self.image = PhotoImage(self.img)  # utiliser os.getcwd() ?
        self.w, self.h = self.image.width(), self.image.height()

        self.canvas = Tk.Canvas(self.master, width=self.w, height=self.h)
        self.canvas.pack()
        self.canvas.create_image((self.w // 2, self.h // 2), image=self.image)

        self.mainloop()


Interface(
    "/IMAGES/ImagesF02/ImageFondEtoile.jpg")  # Double slash pour la fin

# image2 = Image.open("D:\Pictures\god0a.jpg")
# #image2.show()
# image1 = ImageTk.PhotoImage(image2)
# background_label = tk.Label(master, image=image1)
# background_label.image1=image1
# background_label.place(x=0, y=0, height=250, width=350)
