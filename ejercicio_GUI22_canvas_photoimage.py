# --------------------------- PhotoImage

# permite la lectura de una imagen, y luego con el metodo

# CREATE_IMAGE se puede visualizar

from tkinter import *

class Ejercicio:
    def __init__(self):
        self.root = Tk()
        self.canvas1 = Canvas(self.root,width=700, height=500, background="black")
        self.canvas1.grid(column=0, row=0)
        archi1 = PhotoImage(file="carta1.png") #
        self.canvas1.create_image(30,100, image = archi1, anchor="nw")
        archi2 = PhotoImage(file="carta2.png")
        self.canvas1.create_image(240,100, image = archi2, anchor = "nw")
        archi3 = PhotoImage(file="carta3.png")
        self.canvas1.create_image(450,100, image = archi3, anchor = "nw") # nort | west
        self.root.mainloop()

ejercicio1 = Ejercicio()