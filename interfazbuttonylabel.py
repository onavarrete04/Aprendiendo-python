# cabe decir que las ventanas son contenedores [] que contienen otros contenedores [[frame[widgets]]]
# el frame (aglutinador o contenedor mas grande) tambien puede ser considerado como un widgets

from tkinter import *

class Ventana:

    def __init__(self):
        self.valor = 1 # se define el atributo valor que se mostrara en el label
        self.raiz = Tk() # se crea la raiz (ventana)
        self.raiz.title("MI INTERFAZ GRÁFICA 1") # se le da titulo a la ventana
        self.label_1 = Label(self.raiz, text= self.valor) # se realiza una etiqueta (label)
        self.label_1.grid(column=0,row=0) # se define la composicion que va tomar la etiqueta (label)
        self.label_1.config(foreground = "red")# se da al color a la raiz (ventana) en todo el plano

# Botones

# los botones se crean con el metodo Button.
# el primer parametro es la raiz(ventana) donde queremos hacer el boton
# el segundo parametro es el texto que se va a mostrar dentro del boton
# el tercer parametro es command pasamos el metodo que se va a ejecutar.

        self.boton_1 = Button(self.raiz, text = "incrementar", command = self.incrementar)
        self.boton_1.grid(column=0, row=1)
        self.boton_2 = Button(self.raiz, text = "Disminuir", command = self.decrementar)
        self.boton_2.grid(column=0, row=2) # con el metodo grid se define la composición layaout donde se va a mostrar cada boton
        self.raiz.mainloop()

    def incrementar(self):
        self.valor = self.valor + 1
        self.label_1.config(text= self.valor) # con el metodo config, vamos cambiando el valor mostrado
    def decrementar(self):
        self.valor = self.valor - 1
        self.label_1.config(text= self.valor)


aplicacion = Ventana()