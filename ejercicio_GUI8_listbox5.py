from tkinter import *

class Lbox:

    def __init__(self):

        self.root = Tk()
        self.etiqueta = Label(self.root, text = "Elija idiomas")
        self.etiqueta.grid(column = 0, row = 0)
        self.listbox = Listbox(self.root, selectmode = MULTIPLE)
        self.listbox.grid(column = 0 , row = 2) 
        # insert

        self.listbox.insert(0,"ingles")
        self.listbox.insert(1,"mandarin")
        self.listbox.insert(2,"español")
        self.listbox.insert(3,"frances")

        self.boton = Button(self.root, text = "PROCESAR", command = self.procesar)
        self.boton.grid(column = 0 , row = 3)
        self.etiqueta_2 = Label(self.root, text = "RESULTADO")
        self.etiqueta_2.grid(column = 0 , row = 4)
        self.root.mainloop()

    def procesar(self):
        cadena = ""
        if len(self.listbox.curselection() )!= 0:
            for i in self.listbox.curselection():
                cadena +=  self.listbox.get(i) + "\n"
            self.etiqueta_2.config(text = cadena)


ejercicio = Lbox()
