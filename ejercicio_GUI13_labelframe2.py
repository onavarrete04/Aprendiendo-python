from tkinter import *
from tkinter import ttk

class Ejercicio:

    def __init__(self):

        self.root = Tk()
        
        self.label_frame1 = ttk.LabelFrame(self.root, text= "Artículo")
        self.label_frame1.grid(column= 0, row= 0, padx= 5, pady= 10)
        self.articulo()
        self.label_frame2 = ttk.LabelFrame(self.root, text= "Operaciones")
        self.label_frame2.grid(column=0, row=1, padx=5, pady=10)
        self.operaciones()
        self.root.mainloop()
    def articulo(self):
        self.etiqueta1 = Label(self.label_frame1,text = "Código de artículo:")
        self.etiqueta1.grid(column=0,row=0, padx = 4, pady = 4)
        self.entry_1 = Entry(self.label_frame1)
        self.entry_1.grid(column=1,row= 0, padx= 4, pady= 4)
        self.etiqueta2 = Label(self.label_frame1,text = "Descripción:")
        self.etiqueta2.grid(column=0,row=1, padx = 4, pady = 4)
        self.entry_1 = Entry(self.label_frame1)
        self.entry_1.grid(column=1,row= 1, padx= 4, pady= 4)
        self.etiqueta3 = Label(self.label_frame1,text = "Precio:")
        self.etiqueta3.grid(column=0,row=2, padx = 4, pady = 4)
        self.entry_1 = Entry(self.label_frame1)
        self.entry_1.grid(column=1,row= 2, padx= 4, pady= 4)
    def operaciones(self):
        self.boton1 = Button(self.label_frame2, text="Alta")
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.boton2 = Button(self.label_frame2, text="Baja")
        self.boton2.grid(column=1, row=0, padx=4, pady=4)
        self.boton3 = Button(self.label_frame2, text="Modificación")
        self.boton3.grid(column=2, row=0, padx=4, pady=4)
ejercicio1 = Ejercicio()