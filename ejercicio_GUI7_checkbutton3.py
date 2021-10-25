from tkinter import *

class Ejercicio:

    def __init__(self):
        self.root = Tk()
        self.root.title("Hola")

        # datos selectores
        self.dato_selector1 = IntVar()
        self.dato_selector2 = IntVar()
        self.dato_selector3 = IntVar()
        self.dato_selector4 = IntVar()

        self.check1 = Checkbutton(self.root, text = "Chrome   ", variable = self.dato_selector1)
        self.check1.grid(column = 0, row = 0)
        self.check2 = Checkbutton(self.root, text = "Explorer  ", variable = self.dato_selector2)
        self.check2.grid(column = 0, row = 1)
        self.check3 = Checkbutton(self.root, text = "Goodpack", variable = self.dato_selector3)
        self.check3.grid(column = 0, row = 2)
        self.check4 = Checkbutton(self.root, text = "Mozilla  ",variable = self.dato_selector4)
        self.check4.grid(column = 0, row = 3)

        self.boton = Button(self.root, text = "añadir", command = self.añadir)
        self.boton.grid(column = 0, row = 4)
        self.root.mainloop()
    
    def añadir(self):
        contador = ""
        if self.dato_selector1.get() == 1:
            contador = contador + "Chrome "
            
        if self.dato_selector2.get() == 1:
            contador = contador + "Explorer "
            
        if self.dato_selector3.get() == 1:
            contador = contador + "Goodpack "
            
        if self.dato_selector4.get() == 1:
            contador = contador + "Mozilla "
            
        
        self.root.title(contador)
ejercicio1 = Ejercicio()