from tkinter import *

class Ejercicio:
    def __init__(self):
        self.root = Tk()
        self.canvas1 = Canvas(self.root, width=600, height=400, background="black")
        self.canvas1.bind("<ButtonPress-1>",self.boton_presion)#
        self.canvas1.bind("<Motion>", self.mover_mouse)#
        self.canvas1.bind("<ButtonRelease-1>",self.boton_soltar)#
        self.canvas1.grid(column=0,row=0)
        self.presionado = False
        self.root.mainloop()
# TODOS LOS EVENTOS tienen un atributo x y un atributo y, por eso se puede llamar haciendo el .x o .y
    def boton_presion(self,evento):
        self.presionado = True
        self.origen_x = evento.x 
        self.origen_y = evento.y
# en el evento presion se crean los eventos origen.x y origen.y que son los que indican desde donde se va a pintar la linea
    def mover_mouse(self,evento):
        if self.presionado:
            self.canvas1.create_line(self.origen_x,self.origen_y,evento.x,evento.y,fill="yellow")
# cuando se pinta la linea llamamos los atributos origen y nos llega el evento mover_mouse del Motion Y ASI SE PINTA LA LINEA
            self.origen_x = evento.x
            self.origen_y = evento.y
    def boton_soltar(self,evento):
        self.presionado = False



ejercicio1 = Ejercicio()