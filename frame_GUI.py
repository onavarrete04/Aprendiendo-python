# Normalmente a todo se le llama widgets incluido la raiz y el frame

# Vamos a crear nuestro Frame

from tkinter import *

root = Tk()

# root.iconbitmap() hacer logo

root.config(bg = "blue") # le da color a la raiz

miFrame = Frame() # se crea el frame, el frame es un contendor

# hay que empaquetar el frame

miFrame.pack() # se empaqueta

# miFrame.pack(side = "right o bottom o left")
# si se desea a la izquierda y arriba como es?
# miFrame.pack(side = "right", anchor = "n") es con letras, n nort, s south, e este o oste  


# rellenado del frame
# miFrame.pack(fill = "x") x = redimensionar la raiz horizontalmente
# miFrame.pack(fill = "y", expand = "True" ) para redimensionar vertical, debe meterle el partametro expand = "True"
# miFrame.pack(fill ="boot" , expand = "True")

miFrame.config(bg = "red") # cambia el color del frame pero no se ve si no se le da tamaño

# LA RAIZ SIEMPRE SE VA AA ACOPLAR AL TAMAÑO DE SU FRAME INTERNO

miFrame.config(width = "650", height = "300")

# cambiar comportamientos del FRAME - borde

miFrame.config(bd = 35) #bd = borde
miFrame.config(relief = "groove") # bd (groove, sunken)

# cambiar forma de raton

miFrame.config(cursor = "hand2") # pirate es otro cursor

root.mainloop()


