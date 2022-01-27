
# Consumiendo una API de datos abiertos Turismo

from urllib import request
import json
from tkinter import  ttk, Tk, Label, Button



class Aplicacion:
    def __init__(self):
        self.root = Tk()
        #Etiquetas / Label
        self.etiqueta_tipo = Label(self.root, text="Tipo: ")
        self.etiqueta_tipo.grid(column=0,row=0,padx=5,pady=5,sticky="we")
        self.etiqueta_tipo_r = Label(self.root, text="")
        self.etiqueta_tipo_r.grid(column=2,row=0,padx=75,pady=5)
        self.etiqueta_actividad = Label(self.root, text="Empresa: ")
        self.etiqueta_actividad.grid(column=0,row=1,padx=5,pady=5)
        self.etiqueta_actividad_r = Label(self.root, text="")
        self.etiqueta_actividad_r.grid(column=2,row=1,padx=75,pady=5)
        self.etiqueta_u_name = Label(self.root, text="Nombre: ")
        self.etiqueta_u_name.grid(column=0,row=2,padx=5,pady=5)
        self.etiqueta_u_name_r = Label(self.root, text="")
        self.etiqueta_u_name_r.grid(column=2,row=2,padx=75,pady=5)
        self.etiqueta_mail = Label(self.root, text="Correo: ")
        self.etiqueta_mail.grid(column=0,row=3,padx=5,pady=5)
        self.etiqueta_mail_r = Label(self.root, text="")
        self.etiqueta_mail_r.grid(column=2,row=3,padx=75,pady=5)
        self.etiqueta_phone_ = Label(self.root, text="Teléfono: ")
        self.etiqueta_phone_.grid(column=0,row=4,padx=5,pady=5)
        self.etiqueta_phone_r = Label(self.root, text="")
        self.etiqueta_phone_r.grid(column=2,row=4,padx=75,pady=5)
       
        # Botones
        self.boton1 = Button(self.root, text="Anterior",command=self.anterior)
        self.boton1.grid(column=0,row=16,padx=5,pady=5)
        self.boton2 = Button(self.root, text="Siguiente",command=self.siguiente)
        self.boton2.grid(column=2,row=16,padx=5,pady=5,sticky="we")
        # contadores
        self.lista_usuario = []
        self.contador = 0
        self.recuperar_usuarios() # No se puede declarar antes de la lista, porque esta quedaria vacia
        self.mostrar_usuarios()
        self.root.mainloop()
    def anterior(self):
        if self.contador > 0:
            self.contador -=1
            self.mostrar_usuarios()
    def siguiente(self):
        if self.contador < len(self.lista_usuario)-1:
            self.contador +=1
            self.mostrar_usuarios()
    def mostrar_usuarios(self):
        if len(self.lista_usuario)>0:
            # {'tipo': 'Otro', 'entidad': 'Zona camping el Diamante', 'nombre': 'Ignacio Ruiz', 
            # 'correo_electronico': 'fincaeldiamantecombiaalta@gmail.com',
            #  'telefono': '3153616587'}

            self.etiqueta_tipo_r.config(text=self.lista_usuario[self.contador]["tipo"])            
            self.etiqueta_actividad_r.config(text=self.lista_usuario[self.contador]["entidad"])
            self.etiqueta_u_name_r.config(text=self.lista_usuario[self.contador]["nombre"])
            self.etiqueta_mail_r.config(text=self.lista_usuario[self.contador]["correo_electronico"])
            self.etiqueta_phone_r.config(text=self.lista_usuario[self.contador]["telefono"])
                
    def recuperar_usuarios(self):
        pagina = request.urlopen("https://www.datos.gov.co/resource/f6ve-8jtx.json")
        datos = pagina.read().decode("utf-8")
        self.lista_usuario = json.loads(datos)
               
        



aplicacion1 = Aplicacion()