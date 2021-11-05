from tkinter import *
import sys

class Ejercicio:

    def __init__(self):
        self.root = Tk()

        # recoger los datos
        self.dato_1 = StringVar()
        self.dato_2 = StringVar()

        #Entrys
         
        self.entry_1 = Entry(self.root, width=10,textvariable=self.dato_1)
        self.entry_1.grid(column=0,row=0)
        self.entry_2 = Entry(self.root, width=10, textvariable=self.dato_2)
        self.entry_2.grid(column=0,row=1)

        # Menu    
        menu_1 = Menu(self.root)
        self.root.config(menu=menu_1)
        eleccion1 = Menu(menu_1)
        eleccion2 = Menu(menu_1)

        # añadir al menu
        eleccion1.add_command(label="cambiar tamaño de pantalla", command = self.cambiartamaño)
        menu_1.add_cascade(label="Tamaño", menu=eleccion1)
        eleccion2.add_command(label="finalizar programa", command=self.finalizar)
        menu_1.add_cascade(label="Finalizar", menu = eleccion2)

        self.root.mainloop()

    def cambiartamaño(self):
        cadena = self.dato_1.get() + "x" + self.dato_2.get()

        self.root.geometry(cadena)
    def finalizar(self):
        
        sys.exit(0)

ejercicio  = Ejercicio()