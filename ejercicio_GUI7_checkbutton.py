# ----------------- Checkbutton --------------------

"""
    Es como un control visual que permite implementar un boton en dos estados (boton de schrodinger) ajjajaja


"""

from tkinter import *

class Aplicacion:

    def __init__(self):
        
        self.root = Tk()

        # selectores
        self.dato_selector1 = IntVar()
        self.dato_selector2 = IntVar()
        self.dato_selector3 = IntVar()
        
        # checkbutton
        self.check_1 = Checkbutton(self.root, text = "Python", variable = self.dato_selector1)
        self.check_1.grid(column = 0, row = 0)
        self.check_2 = Checkbutton(self.root, text = "C++", variable = self.dato_selector2)
        self.check_2.grid(column = 0, row = 1)
        self.check_3 = Checkbutton(self.root, text = "JAVA", variable = self.dato_selector3)
        self.check_3.grid(column = 0, row = 2)

        # button
        self.boton = Button(self.root, text = "Verificar", command = self.verificar)
        self.boton.grid(column= 0, row = 3)

        # label
        self.etiqueta = Label(self.root, text = "cantidad: ")
        self.etiqueta.grid(column=0, row = 4)

        self.root.mainloop()

    def verificar(self):
        cantidad = 0

        # el dato selector inicia automaticamente en 0, su valor cambia a 1 si se elige
        if self.dato_selector1.get() == 1:
            cantidad += 1
        if self.dato_selector2.get() == 1:
            cantidad += 1
        if self.dato_selector3.get() == 1:
            cantidad += 1
        self.etiqueta.config(text = "Cantidad: " + str(cantidad))

ejercicio = Aplicacion()
        