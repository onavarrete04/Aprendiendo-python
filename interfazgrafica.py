# INTERFACES GRAFICAS DE PYTHON

# tambien conocidas como GUI -grafical user interface
# la libreria tkinter esta codificada con la metodologia POO. la clase Tk() repsenta una ventana
import tkinter as tk # se utiliza el as para darle un alias
# tambien se puede importar asi:
# from tkinter import *


ventana1 = tk.Tk() # por convencion se deberia llamar raiz la variable (ventana1)
ventana1.title("Hola Mundo!")
ventana1.mainloop() # -> es un bucle infinito

class Aplicacion:
    
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Hola Mundo") # metodo title()
        self.ventana1.mainloop() # siempre debe estar al final esta instrucción

aplicacion1 = Aplicacion()

# Una interfaz grafica es una ventana con la que podemos interactuar
# es básicamente una intermedio entre el usuario y el programa.

# interfaces -> tkinter - wxpython -pyqt -pygtk

# La raiz es la (ventana) 
# frame (aglutinador de elementos elementos (widgets))


