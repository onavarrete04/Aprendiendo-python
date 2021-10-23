
from tkinter import *

class Usuario:

    def __init__(self):

        self.root = Tk()
        self.root.title("Nombres")

        self.etiqueta = Label(self.root, text = "Ingrese el nombre del usuario")
        self.etiqueta.grid(column = 0 , row = 0)

        self.dato_capturado = StringVar()

        self.entry = Entry(self.root, width = 10, textvariable = self.dato_capturado)
        self.entry.grid(column = 0, row = 2)

        self.boton = Button(self.root, text = "Procesar", command = self.texto_ingresado)
        self.boton.grid(column = 0, row = 4)

        self.root.mainloop()

    def texto_ingresado(self):

       
        self.root.title(self.dato_capturado.get())

usuario1 = Usuario()