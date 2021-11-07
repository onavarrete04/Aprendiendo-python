### Layoud Manager

# es una herramienta para armar la interfaz y definir una metodologia
# en tkinter hay 3 layout manager (grid, pack, place)

# ------------------ PACK --------------------------------<
from tkinter import *
from tkinter import ttk


class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.boton1 = Button(self.root, text = "Boton 1")
        self.boton1.pack(side = TOP, fill = BOTH) # top para ubicar en la parte superior y both para que el boton abarque todo el espacio
        self.boton2 = Button(self.root, text = "Boton 2")
        self.boton2.pack(side = TOP, fill = BOTH) 
        self.boton3 = Button(self.root, text = "Boton 3")
        self.boton3.pack(side = TOP, fill = BOTH) 
        self.boton4 = Button(self.root, text = "Boton 4")
        self.boton4.pack(side = LEFT) # se ubica el boton a la izquier
        self.boton5 = Button(self.root, text = "Boton 5")
        self.boton5.pack(side = RIGHT) # se ubica a la derecha
        self.boton6 = Button(self.root, text = "Boton 6")
        self.boton6.pack(side = RIGHT) 
        self.boton7 = Button(self.root, text = "Boton 7")
        self.boton7.pack(side = RIGHT) 
        self.root.mainloop()
aplicacion1 = Aplicacion()
        

