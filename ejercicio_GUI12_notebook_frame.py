###### Notebook

# Permite crear un cuaderno con una serie de pestañas en la parte superior
# para lo cual se asocian objetos de la clase Frame y otros botones visuales.

from tkinter import *
from tkinter import ttk
class Aplicacion:

    def  __init__(self):
        self.root = Tk()
        self.a = Label(self.root, text="aaaa")
        self.a.grid(column=0,row=0)
        self.root.title("Prueba de Notebook")
        self.cuaderno = ttk.Notebook(self.root) # Notebook es de el modulo ttk

        # se creara un Frame
        self.frame1 = Frame(self.root)
        self.cuaderno.add(self.frame1, text="Button")
        self.etiqueta = Label(self.frame1, text="la clase button permite capturar el click y lanzar metodo")
        self.etiqueta.grid(column=0,row=0)
        self.boton1 = Button(self.frame1, text= "Ejemplo de boton")
        self.boton1.grid(column=0,row = 1)
        self.boton2 = Button(self.frame1,text="Boton inactivo", state="disable")
        self.boton2.grid(column=0,row = 2)

        self.frame2 = Frame(self.cuaderno)
        self.cuaderno.add(self.frame2,text="Label") # text = label permite mostrar un mensaje
        self.etiqueta_2 = Label(self.frame2, text="Label permite mostrar un mensaje")
        self.etiqueta_2.grid(column=0, row= 0)
        self.etiqueta_3 = Label(self.frame2, text="con los caracteres \\n podemos hacer un salto de línea dentro de la Label")
        self.etiqueta_3.grid(column= 0, row= 1)

        self.frame3 = Frame(self.cuaderno)
        self.cuaderno.add(self.frame3, text = "Entry" )
        self.etiqueta_4 = Label(self.frame3, text= "veremos el entry")
        self.etiqueta_4.grid(column=0, row=0)
        self.entry = Entry(self.frame3,width=30)
        self.entry.grid(column=0,row=1)

        self.cuaderno.grid(column=0,row=1)

        self.root.mainloop()

aplicacion1 = Aplicacion()

