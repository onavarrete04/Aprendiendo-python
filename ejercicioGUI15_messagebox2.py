# Varios botones u opciones:
from tkinter import *
from tkinter import messagebox
import sys

class Aplicacion:
    def __init__(self):

        self.root = Tk()
        self.agregar_menu()
        self.root.mainloop()

    def agregar_menu(self):
        # crear un Menu

        self.menu_bar = Menu(self.root)
        self.root.config(menu = self.menu_bar)
        self.opciones1 = Menu(self.menu_bar, tearoff= False)
        self.opciones1.add_command(label = "Salir", command= self.salir)
        self.menu_bar.add_cascade(label="Opciones", menu=self.opciones1)
    def salir(self):
        # metodo askyesno muestra un boton de si y uno de no
        # segun el boton que se presione es false or true
        respuesta = messagebox.askyesno("Cuidado","Quiere salir del programa")
        if respuesta == True:
            sys.exit(0)


aplicacion = Aplicacion()