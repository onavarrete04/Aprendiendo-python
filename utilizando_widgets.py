
from tkinter import *

# ----------- pack & grid ---------------

root = Tk()

etiqueta = Label(text = "Hola amigos")
#etiqueta.pack() # se posiciona inmediatamente el Label de froma centrada
etiqueta.grid(column = 0, row = 0) # se posiciona en la columna que le digamos

root.mainloop()

# https://guia-tkinter.readthedocs.io/es/develop/chapters/6-widgets/6.1-Intro.html

# Conclusiones día de revisión tkinter

# para una etiqueta o cualquier widgets es mejor utilizar el GRID si se quiere dejar una posicion
# fija del elemento, en una columna en especifico o un lugar en forma de cuadrilla. ideal para diseños estructurados

# para el widgets PACK sirve para diseños complejos y faciles, especialmente cuando se trabaja en una sola fila o columna

# ------------ Radiobutton --------------

#  muestra un conjunto de botones y permite seleccionar solo uno de ellos. Se los debe agrupar para que actuen
# en conjunto