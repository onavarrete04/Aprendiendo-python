from tkinter import *

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.entrada_datos()
        self.canvas1 = Canvas(self.root, width= 600, height= 400, background="black")
        self.canvas1.grid(column=0, row=1)
        self.root.mainloop()
    def entrada_datos(self):
        self.label_frame1 = LabelFrame(self.root, text="Partidos políticos")
        self.label_frame1.grid(column=0, row=0,sticky="w")

        self.etiqueta1 = Label(self.label_frame1, text="Partido A:")
        self.etiqueta1.grid(column=0, row=0, padx=5, pady=5)
        self.captura1 = StringVar()
        self.entry1 = Entry(self.label_frame1, textvariable=self.captura1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5, sticky="e")

        self.etiqueta2 = Label(self.label_frame1, text="Partido B:")
        self.etiqueta2.grid(column=0, row=1, padx=5, pady=5)
        self.captura2 = StringVar()
        self.entry2 = Entry(self.label_frame1, textvariable=self.captura2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5, sticky="e")

        self.etiqueta3 = Label(self.label_frame1, text="Partido C:")
        self.etiqueta3.grid(column=0, row=2, padx=5, pady=5)
        self.captura3 = StringVar()
        self.entry3 = Entry(self.label_frame1, textvariable=self.captura3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5, sticky="e")

        self.boton1 = Button(self.label_frame1, text = "Genera gráfico", command=self.graficar)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
    def graficar(self):
        self.canvas1.delete(ALL)
        valor1 = int(self.captura1.get())
        valor2 = int(self.captura2.get())
        valor3 = int(self.captura3.get())

        if valor1 > valor2 and valor2 > valor3:
            mayor = valor1
        elif valor2 > valor1 and valor1 > valor3:
            mayor = valor2
        else:
            mayor = valor3
        suma = valor1 + valor2 + valor3
        grado1 = valor1/suma * 360
        grado2 = valor2/suma * 360
        grado3 = valor3/suma * 360
        self.canvas1.create_arc(10,10,400,400, fill = "red",start=0,extent=grado1)
        self.canvas1.create_arc(10,10,400,400, fill="blue",start= grado1, extent=grado2)
        self.canvas1.create_arc(10,10,400,400, fill="yellow",start=grado1+grado2,extent=grado3)
        self.canvas1.create_text(500,100, text="Partido A", fill = "red",font="TimeNewRoman")
        self.canvas1.create_text(500,150, text="Partido B", fill = "blue",font="TimeNewRoman")
        self.canvas1.create_text(500,200, text="Partido C", fill = "yellow",font="TimeNewRoman")
aplicacion1 = Aplicacion()