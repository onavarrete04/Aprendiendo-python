from tkinter import *

class Ejercicio:
    def __init__(self):
        self.root = Tk()
        self.canvas1 = Canvas(self.root, width=900, height=500, background="black")
        self.canvas1.grid(column=0,row=0)
        self.archivo1 = PhotoImage(file="carta1.png")
        self.canvas1.create_image(30,100, image = self.archivo1, anchor = "nw", tags = "movil")
        self.archivo2 = PhotoImage(file="carta2.png")
        self.canvas1.create_image(240,100, image = self.archivo2, anchor = "nw", tags = "movil")
        self.canvas1.tag_bind("movil", "<ButtonPress-1>",self.presion_boton)#
        self.canvas1.tag_bind("movil", "<Button1-Motion>",self.moviendo)
        self.carta_seleccionada = None
        self.root.mainloop()
    def presion_boton(self, evento):
        carta = self.canvas1.find_withtag(CURRENT) #
        self.carta_seleccionada = (carta, evento.x, evento.y)
        #
    def moviendo(self,evento):
        x, y = evento.x, evento.y
        carta, x1, y1 = self.carta_seleccionada
        self.canvas1.move(carta, x-x1, y - y1)
        self.carta_seleccionada = (carta, x, y)


ejercicio1 = Ejercicio()