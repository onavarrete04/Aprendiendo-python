class Personas:
    def __init__(self,nombre):
        self.nombre = nombre
        
persona1 = Personas("Juan")
persona2 = Personas("Maria")
persona3 = Personas("Karla")

# cada objeto persona tiene un atributo self.nombre, y cada uno es independiente.

class Persona:

    variable=20 # Es una variable Global, por eso esta fuera de los metodos definidos,
    # en este caso esta fuera del metodo __ini__
    
    def __init__(self,nombre):
        self.nombre=nombre
        
persona1 = Persona("Karla")        
print(persona1.variable) # 20
persona1.variable=5
persona2 = Persona("Maria")
Persona.variable = 5 # se modifica la variable global de persona
print(persona2.variable,"--") # 5
print(persona1.variable) # queda definida la variable global como #5
                        # Esta variable solo tiene un espacio y es compartida por los objetos
                        # por lo anterior, habrá que saber que valores deben ser compartidos y bajo 
                        # que estructuras de datos.

class Jugador:
    pasar = 30
    def __init__(self,nombre,puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        
    def imprimir(self):
        print(self.nombre," tiene un puntaje de ",self.puntaje)
    def pasar_tiempo(self):
        Jugador.pasar = Jugador.pasar - 1
        print("Tiempo restante para acabar el juego ",Jugador.pasar)

jugador1 = Jugador("Angela", 25)
jugador2 = Jugador("Camila", 30)

while Jugador.pasar > 0:
    jugador1.imprimir()
    jugador1.pasar_tiempo()
    
    jugador2.imprimir()
    jugador2.pasar_tiempo()
    
    print("--")
print("--")

# Conclusiones del día.

# Las variables globales se llaman indicando el nombre de la clase como prefijo, se agrega punto
# y luego se coloca el nombre de la variable.

# Persona.edad - Jugador.pasar --- así tambien se llaman fuera de la clase. 