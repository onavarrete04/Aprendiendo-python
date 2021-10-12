# Polimorfismo = Muchas formas.

# El objeto puede cambiar de forma segun como lo empleemos dependiendo del
# contexto en el que se utilice -(python tipado dinamico).

class Coche:
    
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")
    
class Moto:
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")
    
    
# Creando objetos / instancias# se hace una función que puede llamar un "vehiculo" que puede ser 
# el contexto al que se le pase

def desplazamientoVehiculo(vehiculo): # como es tipado dinamico, solo vamos a ver que no necesita saber de que tipo de objeto es, por ese puede cambiar
    vehiculo.desplazamiento()

miCamion2 = Camion() # pero si lo cambiamos a Coche() el objeto va a cambiar o si lo cambiamos a Moto()

desplazamientoVehiculo(miCamion2) # ya estamos viendo el polimorfismo

miMoto = Moto()
miMoto.desplazamiento()

miCarro = Coche()
miCarro.desplazamiento()

miCamion = Camion()
miCamion.desplazamiento()

