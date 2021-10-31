# ------------------ Combobox -------------------

# permite seleccionar un string de un conjunto de items desplegables

# current() -> puede indicarse el elemento por defecto


from tkinter import *
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.etiqueta_1 = Label(self.root, text = "Hola")
        self.etiqueta_1.grid(column = 0, row = 0)
        
        self.dato = StringVar()

        d_semana = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
        self.combobox1 = ttk.Combobox(self.root, width = 10, textvariable = self.dato, values = d_semana)

        #Current  ()
        self.combobox1.current(0) # dice cual es por defecto el string señalado
        self.combobox1.grid(column = 0, row = 1)
        self.boton = Button(self.root, text = "Actualizar", command = self.actualizar)
        self.boton.grid(column = 0, row = 2)
        self.etiqueta_2 = Label(self.root, text = " Día seleccionada: ")
        self.etiqueta_2.grid(column = 0, row = 3)

        self.root.mainloop()
    def actualizar (self):
        self.etiqueta_2.configure(text=self.dato.get())

ejercicio = Aplicacion()