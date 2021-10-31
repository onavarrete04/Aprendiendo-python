
from tkinter import *
from tkinter import ttk
class Ejercicio:

    def __init__(self):
        self.root = Tk()
        self.etiqueta_1 = Label(self.root, text="Nombre")
        self.etiqueta_1.grid(column = 0, row = 0)

        self.captura_dato_entry = StringVar()
        self.dato_combobox = StringVar()
        self.entry = Entry(self.root, width = 10, textvariable = self.captura_dato_entry)
        self.entry.grid(column = 0, row = 1)
        
        paises = ("Angentina","Angola","Chile","Colombia","brazil","belorusia")

        self.combobox1 = ttk.Combobox(self.root, textvariable = self.dato_combobox, value = paises)
        self.combobox1.current(0)
        self.combobox1.grid(column = 0, row = 2)
        self.boton = ttk.Button(self.root, text = "Actualizar", command = self.actualizar)
        self.boton.grid(column = 0, row = 3)
        self.root.mainloop()
    def actualizar(self):
        a = self.captura_dato_entry.get()
        b = self.combobox1.get()
        cadena = "Nombre: "+ a + " pais " + b
         
            
        
        self.root.title(cadena)

ejercicio1 = Ejercicio()