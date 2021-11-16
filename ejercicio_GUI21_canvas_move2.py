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
        x1, y1, x2, y2 = self.canvas1.coords(self.cuadrado)
        # con el comando coords podemos obtener las coordenadas del canvas
        if evento.keysym == "Right":
            if  x2 < 600: # como ya sabemos cada punto cardinal, podemos limitarlo a los pixeles del canvas y no permitir que la figura salga de este parametro
                self.canvas1.move(self.cuadrado, 4, 0)
        if evento.keysym == "Left":
            if x1 > 0:
                self.canvas1.move(self.cuadrado,-4,0)
        if evento.keysym == "Down":
            if y2 < 400:
                self.canvas1.move(self.cuadrado, 0,4 )
        if evento.keysym == "Up":
            if y1 > 0:
                self.canvas1.move(self.cuadrado, 0, -4)

aplicacion1 = Aplicacion()