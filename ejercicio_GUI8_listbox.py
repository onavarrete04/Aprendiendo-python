# -------------------- Listbox ------------
# se emplea para mostrar una lista de items, el usuario puede
# seleccionar uno o mas elementos de la lista segun como se lo configure a crearlo

from tkinter import *

class Aplicacion:

    def __init__(self):
        self.root = Tk()
        self.listbox1 = Listbox(self.root) # por defecto solo puede seleccionar un unico elemento, para poner opciones sectmode
        self.listbox1.grid(column = 0, row = 0)
        
        #metodo insert
        self.listbox1.insert(0, "papa") # primer valor es la posicion y el segundo el valor
        self.listbox1.insert(1, "manzana")
        self.listbox1.insert(2, "pera")
        self.listbox1.insert(3, "sandia")
        self.listbox1.insert(4, "naranja")
        self.listbox1.insert(5, "melon")

        self.boton1 = Button(self.root, text = "Recuperar", command = self.recuperar)
        self.boton1.grid(column = 0, row = 1)
        self.etiqueta = Label(self.root, text = "seleccionado -> ")
        self.etiqueta.grid(column = 0, row = 2)
        self.root.mainloop()
    
    def recuperar(self):
        if len(self.listbox1.curselection()) != False: # tambien puede ponerse 0 como false
            self.etiqueta.config(text = self.listbox1.get(self.listbox1.curselection()[0])) # pareciera ser que no necesita que se especifique el [0]
            # curselection retorna una tupla con todas las posiciones seleccionadas del listbox
            # como se pretende seleccionar un unico item, accedemos al item [0] del index de la tupla

aplicacion1 = Aplicacion()