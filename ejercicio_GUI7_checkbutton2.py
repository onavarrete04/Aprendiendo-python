from tkinter import *

class Ejercicio:

    def __init__(self):
        self.root = Tk()
        self.dato_selector = IntVar()

        
        self.check = Checkbutton(self.root, text= "¿Esta de acuerdo con los términos y condiciones?", variable = self.dato_selector, command = self.cambiar_estado)
        self.check.grid(column = 0, row = 0)
        
        # el atributo state
        # se crea el atributo state (estado) el cual se inicia como desactivado
        # y luego pasa a estado normal
        self.boton1 = Button(self.root, text = "Ingresar", state = "disable", command = self.ingresar)
        self.boton1.grid(column = 0, row = 1)

        self.root.mainloop()
    
    def cambiar_estado(self):
        if self.dato_selector.get() == 1:
            self.boton1.config(state="normal")
        if self.dato_selector.get() == 0:
            self.boton1.config(state = "disable")
    def ingresar(self):
        self.root.title("ingresando ...")

ejemplo1 = Ejercicio()