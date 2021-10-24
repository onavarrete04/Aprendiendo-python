from tkinter import *

class Sumar_Restar:

    def __init__(self):

        self.root = Tk()
        self.root.title("Sumar o Restar")

        self.etiqueta_1 = Label(self.root, text="Ingrese primer valor")
        self.etiqueta_1.grid(column = 0, row = 0)
        
        self.dato_a = IntVar()
        self.dato_b = IntVar()
        
        self.entry_1 = Entry(self.root, width = 10, textvariable = self.dato_a)
        self.entry_1.grid(column = 0, row = 1)

        self.etiqueta_2 = Label(self.root, text="Ingrese segundo valor")
        self.etiqueta_2.grid(column = 0, row = 3)

        self.entry_2 = Entry(self.root, width = 10, textvariable = self.dato_b)
        self.entry_2.grid(column = 0, row = 4)

        self.dato_seleccion = IntVar()
        self.dato_seleccion.set(2)

        self.radio1 = Radiobutton(self.root, text = "Sumar", variable = self.dato_seleccion, value = 1 )
        self.radio1.grid(column = 0, row = 5)
        self.radio2 = Radiobutton(self.root, text = "Restar", variable = self.dato_seleccion, value = 2 )
        self.radio2.grid(column = 0, row = 6)
        
        self.boton = Button(self.root, text = "Procesar", command = self.suma_resta)
        self.boton.grid(column = 0, row = 7)
        
        self.etiqueta_resultado = Label(self.root, text = "RESULTADO") 
        self.etiqueta_resultado.grid(column = 0, row = 8)

        self.root.mainloop()

    def suma_resta(self):

        if self.dato_seleccion.get() == 1:
            suma = self.dato_a.get() + self.dato_b.get()
            self.etiqueta_resultado.config(text= suma)
        if self.dato_seleccion.get() == 2:
            resta = self.dato_a.get() - self.dato_b.get()
            self.etiqueta_resultado.config(text = resta)

probando = Sumar_Restar()