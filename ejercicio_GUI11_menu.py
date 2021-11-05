#################### Menu ###################333

# Es un menu que permite ingresar la barra horizontal y se necesita crear
# para eso se declara el objeto menu de la libreria tk - ttk

from tkinter import *
import tkinter

import tkinter as tk

class Aplicacion:
    def __init__(self):
        
        self.root = Tk()
        menu_bar  = Menu(self.root) # se crea el menu con el metodo Menu
        self.root.config(menu=menu_bar) # atributo menu de ventana root
        opciones_1 = Menu(menu_bar) # se crean las opciones con el metodo Menu
        opciones_1.add_command(label = "Rojo", command = self.fijarrojo) # se añaden los elementos del menu que se desagregaran
        opciones_1.add_command(label="Verde", command=self.fijarverde)
        opciones_1.add_command(label="Azul", command=self.fijarazul)
        menu_bar.add_cascade(label="Colores",menu=opciones_1) # se muestra el titulo y como se van a mostrar
        opciones_2 = Menu(menu_bar)
        opciones_2.add_command(label = "640X480",command = self.ventanachica)
        opciones_2.add_command(label="1024X800", command = self.ventanagrande)
        menu_bar.add_cascade(label="Tamaños",menu = opciones_2)
        self.root.mainloop()
    def fijarrojo(self):
        self.root.config(bg="red")
    def fijarazul(self):
        self.root.config(background="blue")
    def fijarverde(self):
        self.root.config(background="green")
    def ventanachica(self):
        self.root.geometry("640x40")
    def ventanagrande(self):
        self.root.geometry("1024x800")

Ejemplo = Aplicacion()

# se  pueden crear lineas separadoras con

# opciones1.add_separator() -> add_separator()


# si se desea eliminar la opcion de que el menu pueda desprenderse del root o de la raiz se pasa
# opciones1 = Menu(menubar1, tearoff=0) - > taaroff = false o 0

#EJEMPLOS METODOS accelerator

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Rojo", command=self.fijarrojo, accelerator="Ctrl+R") # se utiliza el metodo accelerator y se le indica la opcion
        opciones1.add_command(label="Verde", command=self.fijarverde, accelerator="Ctrl+V")
        opciones1.add_separator()        
        opciones1.add_command(label="Azul", command=self.fijarazul, accelerator="Ctrl+A")
        self.ventana1.bind_all("<Control-r>", self.cambiar) # metodo bindall
        self.ventana1.bind_all("<Control-v>", self.cambiar)
        self.ventana1.bind_all("<Control-a>", self.cambiar)
        menubar1.add_cascade(label="Colores", menu=opciones1)        
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaños", menu=opciones2)        
        self.ventana1.mainloop()

    def cambiar(self, event):
        if event.keysym=="r": # se le indic que si preciona control r minustula haga el cambio y sucesivamente
            self.fijarrojo()
        if event.keysym=="v":
            self.fijarverde()
        if event.keysym=="a":
            self.fijarazul()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

aplicacion1=Aplicacion()