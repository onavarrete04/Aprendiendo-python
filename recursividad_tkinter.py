from tkinter import *
from tkinter import ttk
import random


"""
0 = Salida
1 = Pared
9 = Persona
5 = Salida
"""
class Laberinto:

    def __init__(self):
        
        self.root = Tk()
        self.root.title("Juego del Laberinto")
        self.salida = False # Se crea una variable que indica que no se ha salido
        self.generar_laberinto()
        self.boton1 = Button(self.root, text= "Recorrer", command = self.analizar)
        self.boton1.grid(column=0, row= 10, columnspan= 5, padx=10, pady=10)
        self.boton2 = Button(self.root, text= "Generar", command = self.generar_otro_tablero)
        self.boton2.grid(column=5, row= 10, columnspan= 5, padx=10, pady=10)
        self.root.mainloop()

    def generar_laberinto(self):
        self.tablero = []
        listafila = []
        for fila in range(0,10):
            for columna in range(0,10):
                etiqueta = Label(self.root, text=self.retornar_aleatorio(), foreground = "red")
                etiqueta.grid(column=columna, row= fila, padx=10, pady=10)
                listafila.append(etiqueta)
            self.tablero.append(listafila)
            listafila=[]
        self.tablero[0][0].configure(text=0)
        self.tablero[9][9].configure(text=5)
    
    def generar_otro_tablero(self):
        for fila in range(0,10):
            for columna in range(0,10):
                self.tablero[fila][columna].configure(text=self.retornar_aleatorio(), background = "#f0f0f0")
        self.tablero[0][0].configure(text=0)
        self.tablero[9][9].configure(text=5)
    def retornar_aleatorio(self):
        valor = random.randint(1,4)
        if valor == 1:
            return 1
        else:
            return 0
    def analizar(self):
        self.salida = False
        self.recorrer(0,0)
        if self.salida:
            self.root.title("TIENE SALIDA DEL LABERINTO")
        else:
            self.root.title("NO TIENE SALIDA DEL LABERINTO")
    def recorrer(self, fila, columna):
        if fila >=0 and fila < 10 and columna >= 0 and columna<10 and self.salida==False:
            if self.tablero[fila][columna].cget("text")==5:
                self.salida= True
            else:
                if self.tablero[fila][columna].cget("text")==0:
                    self.tablero[fila][columna].configure(text=9)
                    self.tablero[fila][columna].configure(background = "yellow")
                    self.recorrer(fila,columna+1)
                    self.recorrer(fila+1,columna)
                    self.recorrer(fila-1,columna)
                    self.recorrer(fila,columna-1)


laberinto1 = Laberinto()
