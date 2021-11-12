# ----------------------- Canvas

# Permite acceder a lines, rectangulos y otras formas para graficar.


from tkinter import *

class Ejercicio:
    
    def __init__(self):

        self.root = Tk()
        self.canvas1 = Canvas(self.root, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0)
# Formas
        self.canvas1.create_line(0,0,100,50, fill= "white")
# (0,0) -> "columna y fila" -> inicia linea -> (100,50) "columna, fila" ->finaliza la linea
        
        self.canvas1.create_rectangle(150,10,250,110, fill="white")
# (150,10) -> "columna y fila superior izquierdo" y (250,110) "columna y fila inferior derecho"
        self.canvas1.create_oval(300,10,400,150, fill="red")
# iguales que rectangulo
        self.canvas1.create_arc(420,10,550,110, fill = "yellow", start = 180, extent = 270)
# iguales que rectangulo pero - start -> grado donde debe iniciar el arco, y extent grados del trozo
        self.canvas1.create_rectangle(150,210,250,310, outline = "white")
# outline es para pintar solo la linea
        self.canvas1.create_oval(300, 210,400,350, outline="red")

        self.canvas1.create_arc(420,210,550,310, outline = "yellow", start = 180, extent = 90)
        self.root.mainloop()

ejercicio1 = Ejercicio()