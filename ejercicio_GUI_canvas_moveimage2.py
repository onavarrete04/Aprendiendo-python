from tkinter import *
import random

class Ejercicio:
    def __init__(self):
        self.root = Tk()
        self.canvas1 = Canvas(self.root, width=800, height=600, background="black")
        self.canvas1.tag_bind("cuadrado", "<ButtonPress-1>",self.presion_boton)# # se presiona el boton derecho del mouse
        self.canvas1.tag_bind("cuadrado", "<Button1-Motion>",self.moviendo) # envia información cuando se pmantiene presionado el boton y se mueve
        self.canvas1.grid(column=0, row=0)
        for i in range(101): # se crean 100 cuadros
            x1 = random.randint(0,800)            
            y1 = random.randint(0,600)
            
            self.canvas1.create_rectangle(x1,y1,x1+20,y1+20 ,  fill="red",tags = "cuadrado")
        self.cuadrado_moviendo = None # se dice que no se mueven los cuadros

        self.root.mainloop()
    def presion_boton(self,evento): # se recibe si se estta presionando un cuadrado (evento)
        cuadrado = self.canvas1.find_withtag(CURRENT) # busca el cuadrado actual presionado
        self.cuadrado_moviendo = (cuadrado, evento.x, evento.y) #se indica que el cuadrado actual es el que esta en movimiento
    def moviendo(self,evento):
        x, y = evento.x, evento.y # se define variable x | y
        cuadrado, x1, y1 = self.cuadrado_moviendo # se guardan las coordenadas del cuadro en su posición previa
        self.canvas1.move(cuadrado, x-x1, y- y1) # se pasan las coordenadas para mover el cuadro
        self.cuadrado_moviendo=(cuadrado, x, y) # se guardan las nuevas coordenadas del ultimo movimiento del cuadrado
    

       
            
            

ejercicio1 = Ejercicio()