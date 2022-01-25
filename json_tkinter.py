from tkinter import Label, Button, ttk, Tk
import json
from urllib import request

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        #Etiquetas
        self.etiqueta_userid = Label(self.root, text="Usuario Id: ")
        self.etiqueta_userid.grid(column=0, row = 1, padx=5, pady=5)
        self.etiqueta_userid_respuesta = Label(self.root, text="")
        self.etiqueta_userid_respuesta.grid(column=1, row = 1, padx=5, pady=5)

        self.etiqueta_id = Label(self.root, text="ID: ")
        self.etiqueta_id.grid(column=0, row = 2, padx=5, pady=5)
        self.etiqueta_id_respuesta = Label(self.root, text="")
        self.etiqueta_id_respuesta.grid(column=1, row = 2, padx=5, pady=5)

        self.etiqueta_title = Label(self.root, text="Titulo: ")
        self.etiqueta_title.grid(column=0, row = 3, padx=5, pady=5)
        self.etiqueta_title_respuesta = Label(self.root, text="")
        self.etiqueta_title_respuesta.grid(column=1, row = 3, padx=5, pady=5)

        self.etiqueta_body = Label(self.root, text="Descripcion")
        self.etiqueta_body.grid(column=0, row = 3, padx=5, pady=5)
        self.etiqueta_body_respuesta = Label(self.root, text="")
        self.etiqueta_body_respuesta.grid(column=1, row = 3, padx=5, pady=5)
        #Botones
        self.boton_anterior = Button(self.root, text="Anterior", command=self.anterior)
        self.boton_anterior.grid(column=0, row=4, padx=5, pady=5)
        self.boton_siguiente = Button(self.root, text="Siguiente", command=self.siguiente)
        self.boton_siguiente.grid(column=1, row=4, padx=5, pady=5)
        #contadores
        self.usuarios = [] # lista vacia que guarde los datos consultados
        self.contador = 0 # se define un contador que guarde los datos cuando se oprima el boton
        self.recuperar_usuario() # se inicializa la función llamandose
        self.mostrar_usuario() # se coloca para que se inicialice el usuario con el index 0
        
        self.root.mainloop()
    
    def anterior(self):
        if self.contador>0:
            self.contador -= 1
            self.mostrar_usuario()
    def siguiente(self):
        if self.contador< len(self.usuarios)-1:
            self.contador  += 1
            self.mostrar_usuario()
    def recuperar_usuario(self):
        pagina = request.urlopen("https://jsonplaceholder.typicode.com/posts")
        datos = pagina.read().decode("utf-8")
        self.usuarios = json.loads(datos) # utilización de la lista vacia para guardar los datos
    def mostrar_usuario(self):

        if len(self.usuarios)>0:

            self.etiqueta_userid_respuesta.config(text=self.usuarios[self.contador]["userId"])
            self.etiqueta_id_respuesta.config(text=self.usuarios[self.contador]["id"])
            self.etiqueta_title_respuesta.config(text=self.usuarios[self.contador]["title"])
            self.etiqueta_body_respuesta.config(text=self.usuarios[self.contador]["body"])

         


aplicacion1 = Aplicacion()