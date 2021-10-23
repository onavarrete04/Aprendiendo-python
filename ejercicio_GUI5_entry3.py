from tkinter import *

class Sumar:

    def __init__(self):

        self.root = Tk()
        self.root.title("Nombres")

        self.dato_capturado_1 = IntVar() # dato

        self.etiqueta = Label(self.root, text = "Ingrese primer dato")
        self.etiqueta.grid(column = 0 , row = 0)

        self.entry_1 = Entry(self.root, width = 10, textvariable = self.dato_capturado_1)
        self.entry_1.grid(column = 0, row = 2)

        self.dato_capturado_2 = IntVar() # dato

        self.etiqueta_2 = Label(self.root, text = "Ingrese primer dato")
        self.etiqueta_2.grid(column = 0 , row = 3)

        self.entry_2 = Entry(self.root, width = 10, textvariable = self.dato_capturado_2)
        self.entry_2.grid(column = 0, row = 4)

        self.boton = Button(self.root, text = "Procesar", command = self.suma)
        self.boton.grid(column = 0, row = 5)

        # RESULTADO
        self.etiqueta_3 = Label(self.root, text = "RESULTADO")
        self.etiqueta_3.grid(column = 0 , row = 6)

        self.root.mainloop()

    def suma(self):
        
        a = int(self.dato_capturado_1.get())
        b = int(self.dato_capturado_2.get())

        sumando = a + b
       
        self.etiqueta_3.config(text = sumando)

sumar1 = Sumar()