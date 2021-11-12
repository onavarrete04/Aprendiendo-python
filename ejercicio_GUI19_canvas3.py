from tkinter import *
from tkinter import font

class Ejercicio:
    def __init__(self):
        self.root = Tk()
        self.ingresar_datos()
        self.canvas1 = Canvas(self.root, width=600, height=400,background="black")
        self.canvas1.grid(column=0,row=1)
        self.root.mainloop()
    def ingresar_datos(self):
        self.label_frame = LabelFrame(self.root,text="Partidos políticos")
        self.label_frame.grid(column=0,row=0,sticky="w")
        self.etiqueta1 = Label(self.label_frame, text="Partido A:")
        self.etiqueta1.grid(column=0,row=0,padx=5,pady=5)
        self.captura1 = StringVar()
        self.entry1 = Entry(self.label_frame, textvariable=self.captura1)
        self.entry1.grid(column=1,row=0,padx=5,pady=5,sticky="e")

        self.etiqueta2 = Label(self.label_frame, text="Partido B:")
        self.etiqueta2.grid(column=0,row=1,padx=5,pady=5)
        self.captura2 = StringVar()
        self.entry2 = Entry(self.label_frame, textvariable=self.captura2)
        self.entry2.grid(column=1,row=1,padx=5,pady=5,sticky="e")

        self.etiqueta3 = Label(self.label_frame, text="Partido C:")
        self.etiqueta3.grid(column=0,row=2,padx=5,pady=5)
        self.captura3 = StringVar()
        self.entry3 = Entry(self.label_frame, textvariable=self.captura3)
        self.entry3.grid(column=1,row=2,padx=5,pady=5,sticky="e")

        self.boton = Button(self.label_frame, text="Añadir gráfico", command=self.graficar)
        self.boton.grid(column=0, row=3, padx=5, pady=5, columnspan=2, sticky="we")
        self.entry1.focus
    def graficar(self):
        self.canvas1.delete(ALL)
        valor1 = float(self.captura1.get())
        valor2 = float(self.captura2.get())
        valor3 = float(self.captura3.get())

        if valor1 > valor2 and valor2 > valor3:
            mayor = valor1
        elif valor2> valor1 and valor1>valor3:
            mayor = valor2
        else:
            mayor = valor3
        suma = valor1+valor2+valor3
        largo1 = (valor1/suma)*400
        largo2 = (valor2/suma)*400
        largo3 = (valor3/suma)*400
        a = (valor1/suma)*100
        b = (valor2/suma)*100
        c = (valor3/suma)*100
        print(largo1,largo2,largo3)
        self.canvas1.create_rectangle(10,270,10+largo1,190,fill="red")
        self.canvas1.create_rectangle((largo1+15),270,(largo1+10+largo2),190,fill="blue")
        self.canvas1.create_rectangle((largo2+largo1+15),270,10+(largo1+largo2+largo3),190,fill="green")
        self.canvas1.create_text(50,220, text=str("{:.2f}".format(a)) + "%",fill="white", font="arial")
        self.canvas1.create_text(50+largo1,220, text=str("{:.2f}".format(b)) + "%",fill="white", font="arial")
        self.canvas1.create_text(50+largo1+largo2,220, text=str("{:.2f}".format(c)),fill="white", font="arial")

ejercicio1 = Ejercicio()