# --------------------- ScrolledText -----------------------

# es un widget igual a entry, pero permite ingresar diferentse lineas

# cuenta con metodos especiales para extraer partes de texto

# hay que importar el modulo scrolledtext

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class Ejercicio:
    def __init__(self):
        self.root = Tk()
        self.scrolledtext1 = scrolledtext.ScrolledText(self.root, width=50, height=10)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
        self.framecopia() # se llama una función para que imprima
        self.scrolledtext2 = scrolledtext.ScrolledText(self.root, width=50, height=10)
        self.scrolledtext2.grid(column=0, row=2, padx=10, pady=10)
        self.root.mainloop()
    def framecopia(self):
        self.label_frame = LabelFrame(self.root, text="Región")
        self.label_frame.grid(column=0, row= 1, padx=5, pady=5)
        # labels y entrys
        self.etiqueta1 = Label(self.label_frame, text="Desde fila:")
        self.etiqueta1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.captura1 = StringVar()
        self.entry1 = Entry(self.label_frame, textvariable=self.captura1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5, sticky="e")

        self.etiqueta2 = Label(self.label_frame, text="Desde columna:")
        self.etiqueta2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.captura2 = StringVar()
        self.entry2 = Entry(self.label_frame, textvariable=self.captura2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5, sticky="e")

        self.etiqueta3 = Label(self.label_frame, text="Hasta fila:")
        self.etiqueta3.grid(column=0, row=2, padx=5, pady=5, sticky="e")
        self.captura3 = StringVar()
        self.entry3 = Entry(self.label_frame, textvariable=self.captura3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5, sticky="e")

        self.etiqueta4 = Label(self.label_frame, text="Hasta columna:")
        self.etiqueta4.grid(column=0, row=3, padx=5, pady=5, sticky="e")
        self.captura4 = StringVar()
        self.entry4 = Entry(self.label_frame, textvariable=self.captura4)
        self.entry4.grid(column=1, row=3, padx=5, pady=5, sticky="e")

        self.boton = Button(self.label_frame,text="Copia",command=self.copia)
        self.boton.grid(column=1, row=4, pady=15,padx=15)  

    def copia(self):
        inicio_fila = self.captura1.get()
        inicio_columna = self.captura2.get()
        fin_fila = self.captura3.get()
        fin_columna = self.captura4.get() 
        datos = self.scrolledtext1.get(inicio_fila+"."+inicio_columna, fin_fila+"."+fin_columna)
        self.scrolledtext2.delete("1.0", END) # fila 1 columna 1
        self.scrolledtext2.insert("3.0", datos)  # fila 1 columna 1

        """scrolledtext1.get("1.0","3.10") Para extraer
         cadenas de caracteres de un control ScrolledText 
         debemos llamar la método get y pasar dos String.
          Por ejemplo si queremos extraer todos los caracteres 
          de la primer fila hasta los 10 primeros caracteres de 
          la tercer fila deberemos codificar:"""

ejercicio1 = Ejercicio()