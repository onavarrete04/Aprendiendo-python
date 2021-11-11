# ------------ Spinbox 

# seleccionado para seleccionar un valor de una lista, se dispone de un boton para subir y bajar
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.etiqueta = Label(self.root, text= "Seleccione la cantidad de bultos")
        self.etiqueta.grid(column=0,row=0,padx=5,pady=15)
        self.espinbox1 = ttk.Spinbox(self.root, from_=0,to=100,width=10,state="readonly") # debe ir referenciado con el metodo ttk
        # from_ "desde " -> 0, to " hasta" -> 100
        self.espinbox1.set(0) # es el valor que se muestra en el spinbox, en esta caso inicia en 0 y se va actualizando
         #
        self.espinbox1.grid(column=0,row=1,padx=5,pady=5)
        self.boton = Button(self.root, text="Sortear",command=self.sort)
        self.boton.grid(column=0,row=2,padx=5,pady=5)
        self.etiqueta2 = Label(self.root, text="",width=15)
        self.etiqueta2.grid(column=1,row=2,padx=5,pady=15)
        self.root.mainloop()
    
    def sort(self):
        if int(self.espinbox1.get()) == 0:
            messagebox.showerror("Cuidado","Debe seleccionar un valor distinto de cero")
        else:
            valor = random.randint(1,3)
            if valor == 1:
                self.etiqueta2.config(text="se debe revisar",background="red")
            else:
                self.etiqueta2.config(text="No se debe revisar",background="green")


aplicacion1 = Aplicacion()