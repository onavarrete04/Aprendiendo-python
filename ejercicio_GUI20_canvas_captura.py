# ---------------- Canvas - captura de datos con mouse-.

# dibujar patrones donde se presione el mouse dentro del canvas

from tkinter import *

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.canvas1 = Canvas(self.root, width=600, height=400, background="black")
        # el metodo bin indica el evento que se va a capturar y el metodo que lo capturara
        self.canvas1.bind("<Motion>",self.mover_mouse) 
        # para el desplazamiento del mouse se utiliza el motion
        self.canvas1.bind("<Button-1>",self.presion_mouse)
        # para capturar cada vez que se presione el boton iz del mouse se captura con button-1
        self.canvas1.grid(column=0, row=1)
        self.root.mainloop()
    def presion_mouse(self, evento): # reciben un evento del bind mover mouse que son cordenadas x - y

        self.canvas1.create_oval(evento.x-5,evento.y-5,evento.x+5,evento.y+5,fill="red")
       
        # se crea un circulo, y se le pasan los parametros del evento y se suman más 5
    def mover_mouse(self,evento): # recibe un evento del bin presionar mouse
        self.root.title(str(evento.x)+"-"+str(evento.y))
        # este evento se mueve cada que movemos el mouse asi no se de click
aplicacion1 = Aplicacion()

###
# Si necesitamos capturar el evento clic del botón derecho del mouse y a su vez que se encuentre presionada la tecla Shift tenemos que codificar:
# self.canvas1.bind("<Shift Button-1>", self.presion_mouse)

# En lugar de Shift podemos verificar si se está presionando la tecla control:
# self.canvas1.bind("<Control Button-1>", self.presion_mouse)

# Inclusive detectar el evento si se presiona Shift, Control y el botón izquierdo del mouse:
# self.canvas1.bind("<Control Shift Button-1>", self.presion_mouse)

#La tecla Alt, Shift, Control y el botón izquierdo del mouse:
#self.canvas1.bind("<Control Shift Alt Button-1>", self.presion_mouse)

#Si necesitamos hacer algo cuando la flecha del mouse entra al control podemos plantear la captura del evento:
# self.canvas1.bind("<Enter>", self.entrada)

#Y si queremos detectar cuando la flecha del mouse sale de la componente:
# self.canvas1.bind("<Leave>", self.salida)

#Para detectar el doble clic de un botón del mouse:
#self.canvas1.bind("<Double-Button-1>", self.presion_mouse)
