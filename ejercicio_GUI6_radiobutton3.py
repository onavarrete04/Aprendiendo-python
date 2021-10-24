from tkinter import *

class Colores:

    def __init__(self):

        self.root = Tk()
        self.root.title("Colores")

        self.dato_selector = IntVar()
        self.dato_selector.set(3)

        self.radio_1 = Radiobutton(self.root, text = "Rojo", variable = self.dato_selector, value = 1)
        self.radio_1.grid(column = 0, row = 1)
        self.radio_2 = Radiobutton(self.root, text = "Verde", variable = self.dato_selector, value = 2)
        self.radio_2.grid(column = 0, row = 2)
        self.radio_3 = Radiobutton(self.root, text = "Azul", variable = self.dato_selector, value = 3)
        self.radio_3.grid(column = 0, row = 3)

        self.boton = Button(self.root, text = "Procesar", command = self.cambiar_color)
        self.boton.grid(column = 0, row = 4)

        self.root.mainloop()
    
    def cambiar_color(self):
        if self.dato_selector.get() == 1:
            self.root.config(bg = "red")
        if self.dato_selector.get() == 2:
            self.root.config(bg = "green")
        if self.dato_selector.get() == 3:
            self.root.configure(bg="blue")

color1 = Colores()