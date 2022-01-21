import tkinter as tk
from tkinter import ttk

import formularios.login
import formularios.mensaje

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Hola Mundo")        
        self.boton1=ttk.Button(self.ventana1, text="Mostrar Mensaje", command=self.mostrar_mensaje)
        self.boton1.grid(column=0, row=0)
        self.boton2=ttk.Button(self.ventana1, text="Mostrar formulario de login", command=self.mostrar_login)
        self.boton2.grid(column=0, row=1)
        self.ventana1.mainloop()

    def mostrar_mensaje(self):
        formularios.mensaje.mostrar("Es una prueba de acceder a módulos de un paquete")

    def mostrar_login(self):
        formularios.login.mostrar()

aplicacion1=Aplicacion()