from cgitb import text
from tkinter import Button, Label, Tk, ttk
import json
from urllib import request

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        #Etiquetas / Label
        self.etiqueta_id = Label(self.root, text="Código: ")
        self.etiqueta_id.grid(column=0,row=0,padx=5,pady=5)
        self.etiqueta_id_r = Label(self.root, text="")
        self.etiqueta_id_r.grid(column=1,row=0,padx=5,pady=5)
        self.etiqueta_name = Label(self.root, text="Nombre: ")
        self.etiqueta_name.grid(column=0,row=1,padx=5,pady=5)
        self.etiqueta_name_r = Label(self.root, text="")
        self.etiqueta_name_r.grid(column=1,row=1,padx=5,pady=5)
        self.etiqueta_u_name = Label(self.root, text="Apellido: ")
        self.etiqueta_u_name.grid(column=0,row=2,padx=5,pady=5)
        self.etiqueta_u_name_r = Label(self.root, text="")
        self.etiqueta_u_name_r.grid(column=1,row=2,padx=5,pady=5)
        self.etiqueta_Dir = Label(self.root, text="Calle: ")
        self.etiqueta_Dir.grid(column=0,row=3,padx=5,pady=5)
        self.etiqueta_Dir_r = Label(self.root, text="")
        self.etiqueta_Dir_r.grid(column=1,row=3,padx=5,pady=5)
        self.etiqueta_Dirs_ = Label(self.root, text="Suit: ")
        self.etiqueta_Dirs_.grid(column=0,row=4,padx=5,pady=5)
        self.etiqueta_Dirs_r = Label(self.root, text="")
        self.etiqueta_Dirs_r.grid(column=1,row=4,padx=5,pady=5)
        self.etiqueta_Dirc = Label(self.root, text="Ciudad: ")
        self.etiqueta_Dirc.grid(column=0,row=5,padx=5,pady=5)
        self.etiqueta_Dirc_r = Label(self.root, text="")
        self.etiqueta_Dirc_r.grid(column=1,row=5,padx=5,pady=5)
        self.etiqueta_Dirz = Label(self.root, text="Z/Code: ")
        self.etiqueta_Dirz.grid(column=0,row=6,padx=5,pady=5)
        self.etiqueta_Dirz_r = Label(self.root, text="")
        self.etiqueta_Dirz_r.grid(column=1,row=6,padx=5,pady=5)
        self.etiqueta_Dirgl = Label(self.root, text="Latitud")
        self.etiqueta_Dirgl.grid(column=0,row=7,padx=5,pady=5)
        self.etiqueta_Dirgl_r = Label(self.root, text="")
        self.etiqueta_Dirgl_r.grid(column=1,row=7,padx=5,pady=5)
        self.etiqueta_Dirglg = Label(self.root, text="Longitud")
        self.etiqueta_Dirglg.grid(column=0,row=8,padx=5,pady=5)
        self.etiqueta_Dirglg_r = Label(self.root, text="")
        self.etiqueta_Dirglg_r.grid(column=1,row=8,padx=5,pady=5)
        self.etiqueta_phone = Label(self.root, text="Telefono: ")
        self.etiqueta_phone.grid(column=0,row=9,padx=5,pady=5)
        self.etiqueta_phone_r = Label(self.root, text="")
        self.etiqueta_phone_r.grid(column=1,row=9,padx=5,pady=5)
        self.etiqueta_wb = Label(self.root, text="Web: ")
        self.etiqueta_wb.grid(column=0,row=9,padx=5,pady=5)
        self.etiqueta_wb_r = Label(self.root, text="")
        self.etiqueta_wb_r.grid(column=1,row=9,padx=5,pady=5)
        self.etiqueta_cny = Label(self.root, text="Compañia: ")
        self.etiqueta_cny.grid(column=0,row=10,padx=5,pady=5)
        self.etiqueta_cny_r = Label(self.root, text="")
        self.etiqueta_cny_r.grid(column=1,row=10,padx=5,pady=5)
        self.etiqueta_ph = Label(self.root, text="Frase: ")
        self.etiqueta_ph.grid(column=0,row=11,padx=5,pady=5)
        self.etiqueta_ph_r = Label(self.root, text="")
        self.etiqueta_ph_r.grid(column=1,row=11,padx=5,pady=5)
        self.etiqueta_bs = Label(self.root, text="Bs: ")
        self.etiqueta_bs.grid(column=0,row=12,padx=5,pady=5)
        self.etiqueta_bs_r = Label(self.root, text="")
        self.etiqueta_bs_r.grid(column=1,row=12,padx=5,pady=5)
        # Botones
        self.boton1 = Button(self.root, text="Anterior",command=self.anterior)
        self.boton1.grid(column=0,row=16,padx=5,pady=5)
        self.boton2 = Button(self.root, text="Siguiente",command=self.siguiente)
        self.boton2.grid(column=1,row=16,padx=5,pady=5)
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

            self.etiqueta_id_r.config(text=self.lista_usuario[self.contador]["id"])            
            self.etiqueta_name_r.config(text=self.lista_usuario[self.contador]["name"])
            self.etiqueta_u_name_r.config(text=self.lista_usuario[self.contador]["username"])
            self.etiqueta_Dir_r.config(text=self.lista_usuario[self.contador]["address"]["street"])
            self.etiqueta_Dirs_r.config(text=self.lista_usuario[self.contador]["address"]["suite"])
            self.etiqueta_Dirc_r.config(text=self.lista_usuario[self.contador]["address"]["city"])
            self.etiqueta_Dirz_r.config(text=self.lista_usuario[self.contador]["address"]["zipcode"])
            self.etiqueta_Dirgl_r.config(text=self.lista_usuario[self.contador]["address"]["geo"]["lat"])
            self.etiqueta_Dirglg_r.config(text=self.lista_usuario[self.contador]["address"]["geo"]["lng"])
            self.etiqueta_phone_r.config(text=self.lista_usuario[self.contador]["phone"])
            self.etiqueta_wb_r.config(text=self.lista_usuario[self.contador]["website"])
            self.etiqueta_cny_r.config(text=self.lista_usuario[self.contador]["company"]["name"])
            self.etiqueta_ph_r.config(text=self.lista_usuario[self.contador]["company"]["catchPhrase"])
            self.etiqueta_bs_r.config(text=self.lista_usuario[self.contador]["company"]["bs"])
                        
                
    def recuperar_usuarios(self):
        pagina = request.urlopen("https://jsonplaceholder.typicode.com/users")
        datos = pagina.read().decode("utf-8")
        self.lista_usuario = json.loads(datos)
               
        



aplicacion1 = Aplicacion()