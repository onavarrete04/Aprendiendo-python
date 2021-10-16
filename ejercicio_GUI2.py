from tkinter import *
import sys
import datetime


class Aplicacion:
    
    def __init__(self):

        fecha_creacion = datetime.datetime.now()
        self.root = Tk()
        self.root.title("Ejercicio_GUI2")
        self.label_1 = Label(self.root, text= "Sistema de Oscar Creado:")
        self.label_1.grid(column = 0, row = 0)
        self.label_2 = Label(self.root, text = fecha_creacion)
        self.label_2.grid(column = 0, row = 1)

        # Boton
        self.boton = Button(self.root, text = "FINALIZAR PROGRAMA", command = self.terminar_programa)
        self.boton.grid(column = 0, row = 3)

        # no dejar ampliar la ventana ni redimensionar
        self.root.resizable(0,0)
        
        self.root.mainloop()

    def terminar_programa(self):
            
        sys.exit(0) # de la libreria sys, el metodo exit(0) significa que se cierra python con normalidad, si es otro numero, significa que pudo ser anormal

aplicacion1 = Aplicacion()