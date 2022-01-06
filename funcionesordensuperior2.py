

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mayor_edad(self, fncion):
        
            return fncion(self.edad)
def EEUU(edad):
    if edad >=21:
        return True
    else:
        return False
def argentina(edad):
    if edad >=18:
        return True
    else:
        return False

persona1=Persona("Camila",18)
print(persona1.mayor_edad(argentina))
print(persona1.mayor_edad(EEUU))



