from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

class Busca_Minas:
    def __init__(self):
        self.root = Tk()
        self.root.title("Buscaminas")
        self.destapadas = 0
        self.enjuego = True
        self.root.geometry("500x500")
        self.root.configure(background="#BEF781")
        # Llamada de metodos
        self.generar_tablero()
        self.generar_bombas()
        self.root.mainloop()
    def generar_tablero(self):
        self.tablero = []
        listafila = [] # variable local que agregara los botones
        for fila in range(0,10):
            for columna in range(0,10):
                boton = Button(self.root, text="", command=lambda fi = fila, co = columna: self.presion(fi,co))
                # el comando recibe una función lambda (anonima) teniendo dos parametros, que son contadores de los for, y se van a disparar
                # cuando se presione cualquier boton, y se va a enviar los datos
                boton.place(x=columna*50, y=fila*50,width=50, height=50) # se ubican los botones con coordenadas absolutas
                listafila.append(boton) # se agregan 10  botones
            self.tablero.append(listafila)
            listafila = []
    def generar_bombas(self):
        self.bombas = []
        listafila = []
        for fila in range(0,10):
            for columna in range(0, 10):
                listafila.append("0")
            self.bombas.append(listafila)
            listafila = []
        cantidad = 10
        while cantidad != 0:
            fila = random.randint(0,9)
            columna = random.randint(0,9)
            if self.bombas[fila][columna]!= "*":
                self.bombas[fila][columna] = "*"
                self.tablero[fila][columna].config(text="*")
                cantidad -= 1



# Correr programa        
buscaminas1 = Busca_Minas()