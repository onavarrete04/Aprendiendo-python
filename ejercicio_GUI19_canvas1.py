from tkinter import *


class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.entrada_datos()
        self.canvas1 = Canvas(self.root, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=1)
        self.root.mainloop()
    def entrada_datos(self):

        self.label_frame1 = LabelFrame(self.root, text="Partidos Políticos")
        self.label_frame1.grid(column=0, row= 0, sticky="w")
        self.etiqueta1 = Label(self.label_frame1, text="Partido A:")
        self.etiqueta1.grid(column=0,row=0,padx=5, pady=5)
        self.captura1 = StringVar()
        self.entry1 = Entry(self.label_frame1, textvariable=self.captura1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        
        self.etiqueta2 = Label(self.label_frame1, text="Partido B:")
        self.etiqueta2.grid(column=0,row=1,padx=5, pady=5)
        self.captura2 = StringVar()
        self.entry2 = Entry(self.label_frame1, textvariable=self.captura2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        self.etiqueta3 = Label(self.label_frame1, text="Partido C:")
        self.etiqueta3.grid(column=0,row=2,padx=5, pady=5)
        self.captura3 = StringVar()
        self.entry3 = Entry(self.label_frame1, textvariable=self.captura3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        self.boton1 = Button(self.label_frame1, text= "Generar gráfico", command=self.generar_grafico)
        self.boton1.grid(column=0, row=3, padx=5, columnspan=2 ,pady= 5, sticky="we")
        self.entry1.focus()
    def generar_grafico(self):
        self.canvas1.delete(ALL) #
        valor1 = int(self.captura1.get()) # se convierte en int
        valor2 = int(self.captura2.get()) 
        valor3 = int(self.captura3.get()) 
        # condicional

        if valor1 > valor2 and valor1 > valor3:
            mayor = valor1
            
        elif valor2 > valor1 and valor2 > valor3:
            mayor = valor2
            
        else:
            mayor = valor3
        
        largo1 = valor1/mayor*400
        largo2 = valor2/mayor*400
        largo3 = valor3/mayor*400

        self.canvas1.create_rectangle(10,10,10+largo1,90,fill="red") # el dato 5 "90" es el ancho
        # (10,10) "columna y fila superior izq" (10+largo1) columna y fila inferior derc. -> 
        # (90 se compara con el 10 inicial de la fila para dar el ancho en pixeles)
        self.canvas1.create_rectangle(10,120,10+largo2,200,fill="yellow") # el dato 5 "90" es el ancho
        # 200 se compara con el 120 de la fila inicial para dar e lancho
        self.canvas1.create_rectangle(10,230,10+largo3,310,fill="green") # el dato 5 "90" es el ancho
        self.canvas1.create_text(largo1+70, 50, text="partido A", fill="white", font="Arial")
        # se presume que todas iniciaran en la columna 70 + el largo que den 
        # y esta en la fila 50, es decir, en el mas abajito de centro
        self.canvas1.create_text(largo2+70, 160, text="partido B", fill="white", font="Arial")
        self.canvas1.create_text(largo3+70, 270, text="partido C", fill="white", font="Arial")
        print(largo1,largo2,largo3) 
            


aplicacion1 = Aplicacion()