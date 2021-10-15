from tkinter import *

raiz = Tk()

raiz.title("VENTANA DE PRUEBA")

raiz.resizable(0,0) # recibe parametros boleean (0) false (1) true (width, heigt) 
                    # impide que se sobredimensione la ventana

# raiz.icobitmap("archivo.ico") agrega un icono a la ventana
# raiz.geometrey("650*350") # redimensiona la ventana

raiz.config(bg="green") # configura el color de la ventana (raiz)

raiz.mainloop()