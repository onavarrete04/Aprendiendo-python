from tkinter import *

class Aplicacion:
    def __init__(self):
        self.root = Tk()

        self.dato_seleccion = IntVar()
        self.dato_seleccion.set(2) # metodo set muy importante para cambiar un dato, se le indica que son dos numeros

        self.radio1 = Radiobutton(self.root, text="Varon", variable = self.dato_seleccion, value = 1)
        self.radio1.grid(column = 0, row = 0)
        self.radio2 = Radiobutton(self.root, text="Mujer", variable = self.dato_seleccion, value = 2)
        self.radio2.grid(column = 0, row = 1)
        # se le ingresa la propiedad variable a radio1
        self.boton1 = Button(self.root, text="Mostrar seleccionada", command = self.mostrar_seleccion)
        self.boton1.grid(column = 0, row = 2)

        self.etiqueta = Label(self.root, text = "opcion seleccionada")
        self.etiqueta.grid(column = 0, row = 3)

        self.root.mainloop()
    
    def mostrar_seleccion(self):
        if self.dato_seleccion.get() == 1:
            self.etiqueta.config(text= "opcion seleccionada = VARON")
        if self.dato_seleccion.get() == 2:
            self.etiqueta.config(text="opcion seleccionada = MUJER")

aplicacion = Aplicacion()



