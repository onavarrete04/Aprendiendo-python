from tkinter import *

class Usuario:

    def __init__(self):
        self.root = Tk()
        self.root.title("GUI ENTRY- 4")

        self.etiqueta_usuario = Label(self.root, text= "Ingrese el usuario")
        self.etiqueta_usuario.grid(column = 0, row = 0)

        self.dato_usuario = StringVar()
        self.dato_clave = StringVar()

        self.entry_usuario = Entry(self.root, width = 10, textvariable = self.dato_usuario)
        self.entry_usuario.grid(column = 0, row = 1)

        self.etiqueta_clave = Label(self.root, text = "Ingrese clave")
        self.etiqueta_clave.grid(column = 0, row = 2)
        
        self.entry_usuario_1 = Entry(self.root, width = 10, textvariable = self.dato_clave, show ="*")
        self.entry_usuario_1.grid(column = 0, row = 3)

        self.boton_ingreso = Button(self.root, text = "Ingresar", command = self.autenticar)
        self.boton_ingreso.grid(column = 0, row = 4)

        self.root.mainloop()

    def autenticar(self):
        
        usuario = self.dato_usuario.get()
        clave = self.dato_clave.get()

        if usuario == "juan" and clave == "abc123":
            self.root.title("CLAVE CORRECTA")
        else:
            self.root.title("INGRESO INCORRECTO")

camila = Usuario()