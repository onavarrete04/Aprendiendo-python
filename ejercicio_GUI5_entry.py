# -------------------- ENTRY ----------------------

# Permite mostrar y solicitar datos al usuario

# Utilizarlo se debe declarar un StringVar o un IntVar (variables)
# las variables capturaran el texto ingresado para trabajar con el dato
"""
from tkinter import *

root = Tk()

campo_text_ejemplo = Entry()
campo_text_ejemplo.pack()
campo_text_ejemplo.get() # -> obtiene el dato del campo de texto y tambien actualiza el dato dato en un momento

#root.mainloop()

a = campo_text_ejemplo.get()

print(a) """

from tkinter import *

class Aplicacion:

    def __init__(self):
        self.root = Tk()
        self.root.title("Instrumento Al Cuadrado")

        self.etiqueta_1 = Label(self.root, text = "ingrese un numero")
        self.etiqueta_1.grid(column = 0 , row = 1)
        
        self.dato = StringVar()

        self.entry = Entry(self.root, width = 10, textvariable = self.dato ) # textvariable 
        self.entry.grid(column = 0, row = 2)

        self.boton1 = Button(self.root, text = "CALCULAR CUADRADO", command = self.cuadrado)
        self.boton1.grid(column = 0, row = 4)

        self.etiqueta_2 = Label(self.root, text = "Resultado")
        self.etiqueta_2.grid(column = 0, row = 6)
        
        self.root.mainloop()
    
    def cuadrado(self):
        
        # 1) se convierte el valor dato en un int

        valor = int(self.dato.get()) # get captura el valor y lo va actualizando

        # 2) se hace la operacion

        calcular_cuadrado = valor * valor

        # 3) se llama la etiqueta_2 para mostrar el valor

        self.etiqueta_2.config(text = calcular_cuadrado)

ejercicio = Aplicacion()
