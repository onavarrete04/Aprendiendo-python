# se agregara una barra espaciadora o de scroll

from tkinter import *

class Ejercicio:

    def __init__(self):
        self.root = Tk()

        # se crea la barra scroll
        self.scroll1 = Scrollbar(self.root, orient = VERTICAL) #scrollbar es un metodo y orient es una opcion, vertical u horizontal
        self.listbox1 = Listbox(self.root, selectmode = MULTIPLE, yscrollcommand =  self.scroll1.set) # en el listbox1 se crea un atributo (una opcion de tk) yscrollcommand
        self.listbox1.grid(column = 0, row = 0)                                                         # que a la final va a conectarse con el widget scroll

        # configuracion barra scrollbar
        self.scroll1.config(command = self.listbox1.yview) # nuevamente llamamos el atributo con la referencia yview 
        self.scroll1.grid(column = 1, row = 0, sticky = "NS") # le indicamos que se expanda de "NS" north a south con el atributo sticky

        # metodo insert

        self.listbox1.insert(0, "Patilla")
        self.listbox1.insert(1, "Papaya")
        self.listbox1.insert(2, "Melon")
        self.listbox1.insert(3, "Banano")
        self.listbox1.insert(4, "Sandia")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(4, "Sandia")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")
        self.listbox1.insert(5, "naranja")

        self.boton = Button(self.root, text = "Restaurar", command = self.restaurar)
        self.boton.grid(column = 0, row = 1)
        self.etiqueta = Label(self.root, text= "Retornados -> ")
        self.etiqueta.grid(column = 0, row = 2)


        self.root.mainloop()
    
    def restaurar(self):
        if len(self.listbox1.curselection()) != 0: # aqui se esta preguntando, si contadas las selecciones curselecor alguna es diferente a falsa ingrese
            todas = "" # se crea una variable str vacia
            for posicion in self.listbox1.curselection(): # aqui se esta diciendo que habra un ciclo por cada opcion seleccionada por el cursor
                todas +=self.listbox1.get(posicion) + "\n" # se suma los valores oprimidos por el cursor
            self.etiqueta.config(text=todas) # se modifica la etiqueta 

ejemplo = Ejercicio()