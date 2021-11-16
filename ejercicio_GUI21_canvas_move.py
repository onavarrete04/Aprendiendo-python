# desplazar un figura utilizando el ID

from tkinter import *

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.canvas1 = Canvas(self.root, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0)
        self.cuadrado = self.canvas1.create_rectangle(50,90,100,140, fill="red")
        self.root.bind("<KeyPress>", self.presion_tecla) # el metodo bind se aplica sobre la raiz
        self.root.mainloop()
    def presion_tecla(self,evento):
        if evento.keysym == "Right":
            self.canvas1.move(self.cuadrado, 4, 0)
        if evento.keysym == "Left":
            self.canvas1.move(self.cuadrado,-4,0)
        if evento.keysym == "Down":
            self.canvas1.move(self.cuadrado, 0,4 )
        if evento.keysym == "Up":
            self.canvas1.move(self.cuadrado, 0, -4)

aplicacion1 = Aplicacion()