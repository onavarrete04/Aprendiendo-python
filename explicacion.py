tupla = ()
lista = []
diccionario = {}

def suma(a,b):
    suma = a + b
    print(suma)
class Operaciones:

    def __init__(self,a,b):

        self.a = a
        self.b = b
    def sumar(self):

        suma = self.a + self.b
        print(suma)
########################
suma1 = Operaciones(5,6)

suma1.sumar()