from tkinter import *
from tkinter import ttk

class Ejemplo:
    def __init__(self):
        self.root = Tk()

        self.boton1 = Button(self.root, text="Boton 1")
        self.boton1.grid(column=0,row=0)
        self.boton2 = Button(self.root, text="Boton 2")
        self.boton2.grid(column=1,row=0)
        self.boton3 = Button(self.root, text="Boton 3")
        self.boton3.grid(column=2,row=0, rowspan=2, sticky="ns") # rowspan expande y stick le da la orientacion North and South
        self.boton4 = Button(self.root, text="Boton 4")     # el sticky es para que no quede centrado el boton, sino que lo ocupe completamente
        self.boton4.grid(column=0,row=1)
        self.boton5 = Button(self.root, text="Boton 5")
        self.boton5.grid(column=1,row=1)
        self.boton6 = Button(self.root, text="Boton 6")
        self.boton6.grid(column=0,row=2, columnspan=3, sticky="we") # columnpasn, añade más columnas a utilizar
        
        self.root.mainloop()
        
ejercicio1 = Ejemplo()