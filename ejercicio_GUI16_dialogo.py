# ----------------> Mensajes de Dialogo

# Se utilizara TopLevel pasando parametro de la ventana principal, se asemeja
# a label, button, entry, es utilizado con entrada de datos para pasar a la ventana principal

from tkinter import *
from tkinter import ttk


class Ejercicio():

    def __init__(self):
        self.root = Tk()
        self.menu_1()
        self.root.mainloop()
    
    def menu_1(self):
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.opciones = Menu(self.menu_bar,tearoff=0)
        self.opciones.add_command(label="Configurar", command=self.configurar)
        self.menu_bar.add_cascade(label="Opciones", menu=self.opciones)
    def configurar(self):
        # variable local dialogo
        dialogo1 = DialogoTamano(self.root)
        s = dialogo1.mostrar()
        self.root.geometry(s[0] + "x" + s[1]) # se crea una tupla hasta que se cierra la ventana

    
class DialogoTamano:

    def __init__(self, ventanaprincipal):
        self.dialogo = Toplevel(ventanaprincipal)
        self.etiqueta1 = Label(self.dialogo, text= "Ingrese ancho: ")
        self.etiqueta1.grid(column=0,row=0,padx=5,pady=5)
        self.captura_dato = StringVar()
        self.entry1 = Entry(self.dialogo, textvariable = self.captura_dato)
        self.entry1.grid(column=1,row=0,padx=5,pady=5)
        self.entry1.focus() # ejerce foco en el teclado, no he entendido bien apra que sirve
        self.etiqueta2=Label(self.dialogo, text="Ingrese alto:")
        self.etiqueta2.grid(column=0, row=1, padx=5, pady=5)
        self.captura_dato2=StringVar()
        self.entry2=Entry(self.dialogo, textvariable=self.captura_dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.boton1=Button(self.dialogo, text="Confirmar", command=self.confirmar)
        self.boton1.grid(column=1, row=2, padx=5, pady=5)
        self.dialogo.protocol("WM_DELETE_WINDOW", self.confirmar) # se indica que metodo debe ejecutarse si se cierra la ventana con la "x"
        self.dialogo.resizable(0,0) # no se expande la pantalla
        self.dialogo.grab_set() # desactiva la pantalla principal

    def mostrar(self):
        # hace visibleel dialogo y cuando termina retorna la tupla
        self.dialogo.wait_window()
        return (self.captura_dato.get(), self.captura_dato2.get()) #tupla

    def confirmar(self):
        self.dialogo.destroy() # destruye la ventana principal de dialogo


aplicacion1=Ejercicio() 
        

