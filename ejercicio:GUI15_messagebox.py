# ---------------------MESSAGEBOX ------------------------->

# Son ventanas de dialogo que se pueden abrir para dar determinada información
# se debe importar el paquete

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
class Suma:

    def __init__(self):
        self.root = Tk()

        
        self.label_frame1 = LabelFrame(self.root, text="Suma de números")
        self.label_frame1.grid(column=0, row= 0, padx=5, pady=10)
        self.label_frame2 = LabelFrame(self.root, text="Resultado")
        self.label_frame2.grid(column=0, row= 1, padx=5, pady=10)
        self.agregar_componentes()
        self.agregar_menu()

        
        self.root.mainloop()
    def agregar_componentes(self):
        self.c_dato1 = StringVar()
        self.c_dato2 = StringVar()
        self.etiqueta1 = Label(self.label_frame1, text="Ingresar primer valor:")
        self.etiqueta1.grid(column=0, row= 0,padx=4 ,pady=4)
        self.entry1 = Entry(self.label_frame1, textvariable=self.c_dato1)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.etiqueta2 = Label(self.label_frame1, text="Ingresar segundo valor:")
        self.etiqueta2.grid(column=0, row= 1,padx=4 ,pady=4)
        self.entry2 = Entry(self.label_frame1, textvariable=self.c_dato2)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.boton = Button(self.label_frame1, text="Sumar", command=self.sumar)
        self.boton.grid(column=1, row=2, padx=4, pady=4)
    
    def agregar_menu(self):
        self.menubar1 = Menu(self.root)
        self.root.config(menu = self.menubar1)
        self.opciones = Menu(self.menubar1, tearoff= False)
        self.opciones.add_command(label="Acerca de ...", command=self.acerca)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones)
    def sumar(self):
        if self.c_dato1.get() == "" or self.c_dato2 =="":
            messagebox.showerror("Cuidado ","No puede dejar los cuadros de entrada de números vacíos")
        else:
            self.etiqueta3 = Label(self.label_frame2, text="Dato: ")
            self.etiqueta3.pack(side=LEFT,fill=BOTH,padx=4,pady=4)
            self.etiqueta4 = Label(self.label_frame2)
            self.etiqueta4.pack(side=RIGHT,fill=BOTH,padx=4,pady=4)
            resultado = int(self.c_dato1.get() )+ int( self.c_dato2.get())
            self.etiqueta4.config(text=resultado)

    def acerca(self):
        messagebox.showerror("Información","Esta aplicación es para aprender python")
        


sumando = Suma()

# digamos en showerror se muestra una x negativa, pero en showinfo se muestra un aviso informativo amarillo, 
# hay diferentes mensajes de messagebox que se pueden utilizar.