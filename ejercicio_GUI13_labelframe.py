############### Labelframe

# tiene una funcionalidad casi identica al frame
# agrega texto en la parte superior y agrega un recuadro

# contenedor widget -> button, label, entrey, radiobbutton, etc


from tkinter import *
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.root = Tk()
        
        self.label_frame = LabelFrame(self.root, text="Login: ")
        self.label_frame.grid(column=0, row=0, padx=5, pady = 10 ) # padx y pady permiten dar un espacio entre lineas vertical y horizontal
        self.login()
        self.label_frame2 = LabelFrame(self.root, text="Operaciones")
        self.label_frame2.grid(column=0, row= 1, padx= 5, pady= 20)
        self.operaciones()
        self.root.mainloop()
    def login(self):
        self.etiqueta_1 = Label(self.label_frame, text="Nombre de Usuario")
        self.etiqueta_1.grid(column=0, row=0, padx= 4, pady= 4)
        self.entry1 = Entry(self.label_frame)
        self.entry1.grid(column=1,row= 0, padx= 4, pady= 4)
        self.etiqueta_2 = Label(self.label_frame, text="Contraseña")
        self.etiqueta_2.grid(column=0, row=2, padx=4, pady=4)
        self.entry2 = Entry(self.label_frame)
        self.entry2.grid(column = 1, row= 2,padx=4,pady=4)
        self.boton1 = Button(self.label_frame, text="Soy el Boton")
        self.boton1.grid(column=1,row=3,padx=4,pady=4)
    def operaciones(self):
        
        self.boton2 = Button(self.label_frame2, text = "Agregar Usuario")
        self.boton2.grid(column=0,row=0,padx=4,pady=4)
        self.boton3 = Button(self.label_frame2, text = "Modificar Usuario")
        self.boton3.grid(column=1,row=0,padx=4,pady=4)
        self.boton4 = Button(self.label_frame2, text = "Borrar Usuario" )
        self.boton4.grid(column=2,row=0,padx=4,pady=4)
aplicacion1 = Aplicacion()