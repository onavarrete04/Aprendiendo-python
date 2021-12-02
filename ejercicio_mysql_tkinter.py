from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

class Formulario_articulo:
    def __init__(self):
        self.root = Tk()
        self.root.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.root)
        self.carga_articulos()
        self.consulta_codigo()
        self.consulta_completa()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.root.mainloop()

    def carga_articulos(self):
        self.pagina1 = Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        self.labelframe1 = LabelFrame(self.pagina1, text="Artículo")
        self.labelframe1.grid(column=0,row=0, padx=5, pady=10)
        self.etiqueta1 = Label(self.labelframe1, text="Nombre:")
        self.etiqueta1.grid(column=0, row=1, padx=4, pady=4)
        self.captura_nombre = StringVar()
        self.entrynombre = Entry(self.labelframe1, textvariable=self.captura_nombre)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.etiqueta2 = Label(self.labelframe1, text="Precio:")
        self.etiqueta2.grid(column=0,row = 2, padx=4, pady=4)
        self.captura_pago = StringVar()
        self.entrypago = Entry(self.labelframe1, textvariable=self.captura_pago)
        self.entrypago.grid(column=1, row=2, padx= 4, pady= 4)
        self.boton1 = Button(self.labelframe1, text="CONFIRMAR", command=self.agregar)
        self.boton1.grid(column=0, row= 3, columnspan=2, padx= 5, pady= 5)
    def agregar(self):
        datos = (self.captura_nombre.get(), self.captura_pago.get())
        self.articulo1.alta(datos)
        messagebox.showinfo("Información","Los datos fueron cargados")
        self.captura_nombre.set("")
        self.captura_pago.set("")
# Instancia



    def consulta_codigo(self):
        self.pagina2 = Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2 = LabelFrame(self.pagina2, text = "Artículo")
        self.labelframe2.grid(column=0, row= 0, padx=5, pady=10)
        
        self.etiqueta3 = Label(self.labelframe2, text="Código:")
        self.etiqueta3.grid(column=0, row=1, padx=4, pady=4)
        self.captura_dato3 = StringVar()
        self.entrycodigo = Entry(self.labelframe2, textvariable= self.captura_dato3)
        self.entrycodigo.grid(column=1, row=1, padx=4, pady= 4)

        self.etiqueta4 = Label(self.labelframe2, text="Descripción:")
        self.etiqueta4.grid(column=0, row=2, padx=4, pady=4)
        self.captura_dato4 = StringVar()
        self.entrydescripcion = Entry(self.labelframe2, textvariable= self.captura_dato4, state="readonly") # readonly = solo lectura, para no pasar datos
        self.entrydescripcion.grid(column=1, row=2, padx=4, pady= 4)

        self.etiqueta5 = Label(self.labelframe2, text="Precio:")
        self.etiqueta5.grid(column=0, row=3, padx=4, pady=4)
        self.captura_dato5 = StringVar()
        self.entryprecio = Entry(self.labelframe2, textvariable= self.captura_dato5, state="readonly")
        self.entryprecio.grid(column=1, row=3, padx=4, pady= 4)

        self.boton2 = Button(self.labelframe2, text="CONSULTAR", command= self.consultar)
        self.boton2.grid(column=0, row= 4, columnspan=2, padx=5, pady=5)
    
    def consultar(self):
        pass
    def consulta_completa(self):
        self.pagina3 = Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3 = LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        self.boton3 = Button(self.labelframe3, text="CONSULTA COMPLETA", command=self.listar)
        self.boton3.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        self.scrolltext1 = scrolledtext.ScrolledText(self.labelframe3, width = 30, heigh = 10)
        self.scrolltext1.grid(column=0, row=2)
    def listar(self):
        pass

administrar1 = Formulario_articulo()

        

