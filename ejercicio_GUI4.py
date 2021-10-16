from tkinter import *
import sys

class Botones:
    
    def __init__(self):
        self.lista =  []   
        self.root = Tk()
        self.label = Label(self.root, text= "hola")
        self.label.grid(column = 0, row = 1)

        self.boton1 = Button(self.root, text = "1", command = self.eleccion_1 )
        self.boton1.grid(column = 0, row = 3)
        
        self.boton2 = Button(self.root, text = "2", command = self.eleccion_2 )
        self.boton2.grid(column = 0, row = 4)
        self.boton3 = Button(self.root, text = "3", command = self.eleccion_3 )
        self.boton3.grid(column = 0, row = 5)
        self.boton4 = Button(self.root, text = "4", command = self.eleccion_4 )
        self.boton4.grid(column = 0, row = 6)
        self.boton5 = Button(self.root, text = "5", command = self.eleccion_5 )
        self.boton5.grid(column = 0, row = 7)

        self.root.mainloop()
    
    def eleccion_1(self):

        self.lista.append(1)
        self.label.config(text = self.lista)
    def eleccion_2(self):

        self.lista.append(2)
        self.label.config(text = self.lista)
    def eleccion_3(self):

        self.lista.append(3)
        self.label.config(text = self.lista)
    def eleccion_4(self):

        self.lista.append(4)
        self.label.config(text = self.lista)
    def eleccion_5(self):

        self.lista.append(5)
        self.label.config(text = self.lista)
        

aplicacion1 = Botones()