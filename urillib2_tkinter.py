from cgitb import text
from tkinter import *
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
from urllib import request, error
from tkinter import messagebox


class Aplicacion:

    def __init__(self):
        self.root = Tk()
        self.dato = StringVar()
        self.etiqueta1 = Label(self.root, text="Ingrese URL del sitio web")
        self.etiqueta1.grid(column=0,row=2, padx=5, pady=5)
        self.entry1 = Entry(self.root, textvariable=self.dato)
        self.entry1.grid(column=0, row= 3, padx=35, pady=5, columnspan=7)
        self.boton1 = Button(self.root, text="Recuperar",command=self.procesar)
        self.boton1.grid(column=0, row= 4, padx=5, pady=5, sticky="we")
        self.scrolledtext1 = scrolledtext.ScrolledText(self.root, width=50, height=10)
        self.scrolledtext1.grid(column=0, row=6, padx=10, pady=10)
        self.boton2 = Button(self.root, text="Borrar Contenido", command=self.borrar)
        self.boton2.grid(column=0, row = 7, padx=5, pady=5, sticky="we")
        self.root.mainloop()
    def procesar(self):
        try:
            pagina = request.urlopen(self.dato.get())
            consulta = pagina.read().decode("utf-8")
            self.scrolledtext1.delete(1.0, END)
            self.scrolledtext1.insert(INSERT, consulta)
        except error.HTTPError as err:
            messagebox.showinfo("Oops","No se ha podido acceder a la url")
        except ValueError:
            messagebox.showerror("Error","No se ingreso la url de manera adecuada")
    def borrar(self):
        self.scrolledtext1.delete(1.0, END)
        messagebox.showinfo("Exitoso","Se ha limpiado correctamente")
aplicacion1 = Aplicacion()