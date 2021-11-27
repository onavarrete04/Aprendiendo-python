from tkinter import *
from tkinter import scrolledtext 
import sys
from tkinter import filedialog 
from tkinter import messagebox

class Aplicación:
    def __init__(self):
        self.root = Tk()
        self.agregar_menu()
        self.scrolltext_1 = scrolledtext.ScrolledText(self.root, width = 80, height = 20) # es la parte visual para escribir
        self.scrolltext_1.grid(column = 0, row = 0, padx = 10, pady=10)
        self.root.mainloop()
    def agregar_menu(self):
        menubar1 = Menu(self.root)
        self.root.config(menu = menubar1)
        opciones1 = Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar Archivo", command = self.guardar)
        opciones1.add_command(label="Recuperar archivo", command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
    def salir(self):
        sys.exit(0)
    def guardar(self):
        nombre_archivo = filedialog.asksaveasfilename(initialdir="/", title="Guardar o", filetypes= (("txt files","*.txt"),("todos los archivos","*.*")))
        # con el metodo filedialog se entra a observar en que ubicación se quiere guardar el documento
        # asksavesasfilename permite guardar el archivo
        # initialdir = indica en que ruta se debe guardar 
        if nombre_archivo != "":
            archivo = open(nombre_archivo, "w", encoding="utf-8")
            archivo.write(self.scrolltext_1.get("1.0",END)) # significa que se va a extraer desde la fila 1, hasta la ultima de el archivo de texto para guardarlo
            archivo.close()
            messagebox.showinfo("Información", "Los datos fueron guardados en el archivo")
    def recuperar(self):
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccione archivo", filetypes=(("txt files", "*.txt"),("todos los archivos","*.*")))
        if nombre_archivo!= "":
            archivo1 = open(nombre_archivo, "r", encoding="utf-8")
            contenido1 = archivo1.read()
            archivo1.close()
            self.scrolltext_1.delete("1.0",END)
            self.scrolltext_1.insert("1.0", contenido1)      

ejercicio = Aplicación()