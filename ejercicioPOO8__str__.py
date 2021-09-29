# Metodo especial __str__

class Persona:
    def __init__(self,nomb,apell):
        self.nombre = nomb
        self.apellido = apell
        
persona1 = Persona("José","Rodriguez")
print(persona1)

# se imprime <__main__. Objeto Persona en 0 x 7f353083bcf8>

# Para tal efecto se usa la función __str__

class Persona:
    def __init__(self,nom,ape):
        self.nombre = nom
        self.apellido = ape
    def __str__(self):
        cadena = self.nombre+","+self.apellido
        return cadena
    
persona1 = Persona("Karla","Meneces")
print(persona1)

class Punto:
    
    def __init__(self, x, y):
    
        self.xx = x
        self.yy = y
    
    def __str__(self):
                
        return "["+str(self.xx)+","+str(self.yy)+"]"
    
ejemplo = Punto(10,3)
print(ejemplo)

class Familia:
    
    def __init__(self,papa,mama,hijos=[]):
        self.papa = papa
        self.mama = mama
        self.hijos = hijos
    
    def cantidad_hijos(self):
       
        contador = int(input("ingrese el numero de hijos que tiene"))
        
        for i in range(contador):
            nombre_hijx = input("ingrese el nombre de su hijo")
            self.hijos.append(nombre_hijx)
    
    
    def __str__(self):
        
        cadena = "!!"+self.papa +" y "+self.mama
        for i in self.hijos:
            cadena = cadena + " - "+i
        return cadena

penac = Familia("Fernando","Ruth")
penac.cantidad_hijos()
print(penac)

# Dentro de este ejercicio pretendi llamar la variable local "contador" al metodo __str__, pero la unica forma
# de llamarlo es que contador fuera un objeto, o que fuera una variable global, esto con el fin de hacerlo un
# ciclo for i in range(contador), pero también es posible hacer un ciclo for in self.lista, sin indicar previamente
# la cantidad que se iba a iterar. Aprendi a que se llaman son los objetos creados para un metodo, no la variable
# ni el parametro.

class Jugador:
    
    def __init__(self,nom,punt):
        self.nombre = nom
        self.puntaje = punt
    
    def __str__(self):
        
        cadena = "Jugador "+ self.nombre+ " ,puntaje "+ str(self.puntaje)
        
        if self.puntaje <= 1000:
            return cadena + " - " + "usted se encuentra en la categoria de un jugador principiante"
        else:
            return cadena +" - " + "usted se encuentra en la categoria de jugador experto"
    
persona1 = Jugador("alberto",100)
persona2 = Jugador("Karla",1050)
print(persona1)
print(persona2)

# Conclusiones y aprendizajes. # si se define la cadena así:
# cadena = "Jugador ", self.nombre, " ,puntaje ", str(self.puntaje)
# se genera el error: solo puede concatenar tupla (no "str") a tupla
# solo se puede concatenar con + los objetos y string, tuplas, etc.
# La función __str__ se ejecuta sola sin tener que llamarla.