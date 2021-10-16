from tkinter import *
import sys

class Mujer_Hombre:

    def __init__(self):
        self.root = Tk()
        self.root.title("Programa Mujer - Hombre")
        self.boton_f = Button(self.root, text = "MUJER", command = self.eleccion_f)
        self.boton_f.grid(column = 0, row = 0)
        self.boton_m = Button(self.root,text = "HOMBRE", command = self.eleccion_m)
        self.boton_m.grid(column = 0, row = 1)
        
        self.boton_finalizar = Button(self.root, text = "FINALIZAR PROGRAMA", command = self.finalizar)
        self.boton_finalizar.grid(column = 0, row = 3)

        self.root.mainloop()

    def eleccion_f(self):
        
        self.root.title("ELECCIÓN MUJER")
    def eleccion_m(self):
        self.root.title("ELECCION HOMBRE")
        
    def finalizar(self):
        sys.exit(0)

aplicacion1 = Mujer_Hombre() 