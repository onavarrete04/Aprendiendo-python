from tkinter import *

class Ejercicio:

    def __init__(self):
        self.root = Tk()
        self.scroll = Scrollbar(self.root, orient = VERTICAL)

        self.dato = StringVar()

        self.entry1 = Entry(self.root, width = 10, textvariable = self.dato)
        self.entry1.grid(column = 0, row = 0)

        
                
        self.listbox = Listbox(self.root, yscrollcommand = self.scroll.set)
        self.listbox.grid(column = 0, row = 1)

        # config scroll

        self.scroll.config(command = self.listbox.yview)
        self.scroll.grid(column = 1, row = 1, sticky = "NS")
        # insert listbox

        self.listbox.insert(0, "Argentina")
        self.listbox.insert(1, "Chile")
        self.listbox.insert(2, "Paraguay")
        self.listbox.insert(3, "Uruguay")
        self.listbox.insert(4, "Peru")
        self.listbox.insert(5, "Brasil")
        self.listbox.insert(6, "Bolivia")
        self.listbox.insert(7, "Venezuela")
        self.listbox.insert(8, "Colombia")
        self.listbox.insert(9, "Pánama")
        
        self.boton = Button(self.root, text = "Procesar", command = self.procesar)
        self.boton.grid(column = 0, row = 2)

        self.etiqueta = Label(self.root, text= "RESULTADO")
        self.etiqueta.grid(column = 0, row = 3)

        self.root.mainloop()
    def procesar(self):
        
        cadena = ""
        if len(self.listbox.curselection()) != 0:
            
            cadena += self.dato.get() +" - pais - "+ self.listbox.get(self.listbox.curselection()[0])
            
            self.etiqueta.config(text = cadena)

ejercio1 = Ejercicio()
