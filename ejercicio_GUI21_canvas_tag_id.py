# Cuando se crea un elemento en la clase canvas este devuelve
# un ID luego podemos trabajar con el

# además podemos asociar una marca TAG a varios elementos y aplicar 
# modificaciones a los mismos.
from tkinter import *

class Ejercicio:
    def __init__(self):
        self.root = Tk()
        self.crear_botones()
        self.canvas1 = Canvas(self.root, width=600, height=400, background="black")
        self.canvas1.grid(column=0,row=1)
        self.linea = self.canvas1.create_line(0,0,100,100, fill="white")
        self.rectangulo1 = self.canvas1.create_rectangle(130,20,300,150, fill="#aaaaaa")
        self.ovalo=self.canvas1.create_oval(400,20,500,150, fill="red")
        self.canvas1.create_rectangle(130,190,180,230, fill="#aaaaaa", tag="cuadrado")
        self.canvas1.create_rectangle(200,190,240,230, fill="#555555", tag="cuadrado")
        self.canvas1.create_rectangle(270,190,310,230, fill="#cccccc", tag="cuadrado")

        self.root.mainloop()
    
    def crear_botones(self):
        self.label_frame1 = LabelFrame(self.root, text="Opciones")
        self.label_frame1.grid(column=0,row=0)
        
        self.boton1 = Button(self.label_frame1, text="Borrar linea", command=self.borrar_linea)
        self.boton1.grid(column=0, row=0, padx=5, pady=5)

        self.boton2 = Button(self.label_frame1, text="Borrar rectángulo", command=self.borrar_rectangulo)
        self.boton2.grid(column=1, row=0, padx=5, pady=5)

        self.boton2 = Button(self.label_frame1, text="Borrar óvalo", command=self.borrar_ovalo)
        self.boton2.grid(column=2, row=0, padx=5, pady=5)

        self.boton2 = Button(self.label_frame1, text="Borrar todos los cuadros",command=self.borrar_cuadrados)
        self.boton2.grid(column=3, row=0, padx=5, pady=5)

        self.boton1 = Button(self.label_frame1, text="Borrar todos",command=self.borrar_todo)
        self.boton1.grid(column=4, row=0, padx=5, pady=5)
    def borrar_linea(self):
        self.canvas1.delete(self.linea)
    def borrar_rectangulo(self):
        self.canvas1.delete(self.rectangulo1)
    def borrar_ovalo(self):
        self.canvas1.delete(self.ovalo)
    def borrar_cuadrados(self):
        self.canvas1.delete("cuadrado")
    def borrar_todo(self):
        self.canvas1.delete(ALL)
    
ejercicio1 = Ejercicio()