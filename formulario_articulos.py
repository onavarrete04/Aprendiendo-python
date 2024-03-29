import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrar()
        self.modificar_articulo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Precio:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta= self.articulo1.consultal(datos)
        
        if len(respuesta) > 0:
            
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")
        
    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")
    def borrar(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de artículos")
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Artículo")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label4 = ttk.Label(self.labelframe4, text = "Código")
        self.label4.grid(column= 0, row= 0, padx= 4, pady= 4)
        self.codigo_borrar = StringVar()
        self.entry_borrar = ttk.Entry(self.labelframe4, textvariable=self.codigo_borrar)
        self.entry_borrar.grid(column=1, row=0, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe4, text="Borrar",command=self.borra_codigo)
        self.boton2.grid(column=0, row=2, columnspan=2, padx=4, pady=4 )

    def borra_codigo(self):
        datos = (self.codigo_borrar.get(),)
        self.articulo1.borrando(datos)
        mb.showerror("Información","Artículo borrado exitosamente")
        self.entry_borrar.set("")
    def modificar_articulo(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")
        self.labelframe5 = ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe5.grid(column=0 , row=0, padx=5, pady=10)
        self.label5 = ttk.Label(self.labelframe5, text="Código")
        self.label5.grid(column=0, row=1, padx=4, pady=4)
        self.codigo_modificar = StringVar()
        self.entry_codigo_modificar = ttk.Entry(self.labelframe5, textvariable=self.codigo_modificar)
        self.entry_codigo_modificar.grid(column=1, row= 1, padx=4, pady=4)
        self.label6 = ttk.Label(self.labelframe5, text="Descripción")
        self.label6.grid(column=0, row=2, padx=4, pady=4)
        self.descripcion_modificar = StringVar()
        self.entry_descripcion_modificar = ttk.Entry(self.labelframe5, textvariable=self.descripcion_modificar)
        self.entry_descripcion_modificar.grid(column=1, row= 2, padx=4, pady=4)
        self.label5 = ttk.Label(self.labelframe5, text="Precio")
        self.label5.grid(column=0, row=3, padx=4, pady=4)
        self.precio_modificar = StringVar()
        self.entry_precio_modificar = ttk.Entry(self.labelframe5, textvariable=self.precio_modificar)
        self.entry_precio_modificar.grid(column=1, row= 3, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe5, text= "Modificar", command=self.modificar)
        self.boton3.grid(column=0, row=4, columnspan=2, padx=4, pady=7)
        self.boton3 = ttk.Button(self.labelframe5, text= "Consultar", command=self.consultar_mod)
        self.boton3.grid(column=0, row=5, columnspan=2, padx=4, pady=7)

    def modificar(self):
        datos = (self.descripcion_modificar.get(),self.precio_modificar.get(),self.codigo_modificar.get())
        self.articulo1.modificando(datos)
        cantidad=self.articulo1.modificando(datos) # se envia consulta a articulos para que retorne
        
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
            self.codigo_modificar.set("")
            self.descripcion_modificar.set("")
            self.precio_modificar.set("")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")
    def consultar_mod(self):
        datos=(self.codigo_modificar.get(), )
        respuesta=self.articulo1.consultal(datos)
        if len(respuesta)>0:
            self.descripcion_modificar.set(respuesta[0][0])
            self.precio_modificar.set(respuesta[0][1])
        else:
            self.descripcion_modificar.set('')
            self.precio_modificar.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")
       



aplicacion1=FormularioArticulos()