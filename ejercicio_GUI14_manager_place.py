# PLACE

# Se da un valor y una posición con valor absoluto en pixeles, se debe cuidar
# este diseño porque si se agranda la pantalla los botones podrian quedar
# o controles queden fuera

from tkinter import *
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.resizable(0,0) # no permite que se agrande la pantalla
        self.boton = Button(self.root, text = "Confirmar")
        self.boton.place(x = 680, y = 550, width=90, height=30)
        self.boton2 = Button(self.root, text="Cancelar")
        self.boton2.place(x = 580, y =550, width=90,height=30)
        self.root.mainloop()
aplicacion1 = Aplicacion()

# conclusiones


# a) grid -> para un formato más de tabla o estructurado, utiliza styky y rowspan y columnspan que expande
# b) pack -> sirve para el mismo formato, pero se orienta según posiciones como TOP, LEFT, u otras.
# c) place -> por defecto ya se definen por pixeles elementos, y se realiza ubicación en el plano cartesiano