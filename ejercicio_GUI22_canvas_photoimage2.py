from tkinter import *
import random 



class Ejercicio:
    def __init__(self):
        self.root = Tk()
        self.boton1 = Button(self.root, text = "sortear", command = self.sort)
        self.boton1.grid(column=0,row=0,padx=5,pady=5, sticky="w")
        self.boton2 = Button(self.root, text = "limpiar pantalla", command = self.borrar)
        self.boton2.grid(column=0,row=1,padx=5,pady=5,sticky="w")
        self.etiqueta1 = Label(self.root, text= "Mostrar Carta: ")
        self.etiqueta1.grid(column=0, row=2, sticky="w")
        

        self.canvas1 = Canvas(self.root,width=700, height=500, background="black")
        self.canvas1.grid(column=0, row=3)
        self.archi1 = PhotoImage(file="carta1.png") #
        
        self.archi2 = PhotoImage(file="carta2.png")
        
        self.archi3 = PhotoImage(file="carta3.png")
        
        self.root.mainloop()
    def sort(self):
        a = random.randint(1,3)
        if a == 1:
            self.canvas1.create_image(30,100, image = self.archi1, anchor="nw")
            self.etiqueta1.config(text="Mostrar Carta: 1")
        if a == 2:
            self.canvas1.create_image(240,100, image = self.archi2, anchor = "nw")
            self.etiqueta1.config(text="Mostrar Carta: 2")
        if a == 3:
            self.canvas1.create_image(450,100, image = self.archi3, anchor = "nw")
            self.etiqueta1.config(text="Mostrar Carta: 3")
        
    def borrar(self):
        self.canvas1.delete(ALL)
        


ejercicio1 = Ejercicio()