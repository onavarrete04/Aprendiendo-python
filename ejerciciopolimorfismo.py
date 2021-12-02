import math

class Figuras_Geometricas: #PADRE
 
    def __init__(self):
        self.valor_1 = float(input("ingrese primer dato"))
        self.valor_2 = float(input("ingrese segundo dato"))
    def mensaje(self): # metodo
        print("------------------------------------")
        print("Su resultado es: ")

class Cono(Figuras_Geometricas):
    def __init__(self):
        super().__init__() # esta heredando de padre
    def hallar_area(self):
        g = math.sqrt((self.valor_1*self.valor_1)+(self.valor_2*self.valor_2))
        # variable local
        resultado = ((math.pi*(self.valor_1*self.valor_1)+(math.pi*self.valor_1*g)))

        print(resultado)

class Triangulo(Figuras_Geometricas):
    def __init__(self):
        super().__init__()
    def hallar_area(self):
        
        resultado = (self.valor_1*self.valor_2)/2

        print(resultado)

class Triangulo_Equilatero(Figuras_Geometricas):
    def __init__(self):
        super().__init__()
    def hallar_area(self):

        resultado = math.sqrt(3)/4 * (self.valor_1*self.valor_1)
        print(resultado)

class Rectangulo(Figuras_Geometricas):
    def __init__(self):
        super().__init__()
    def hallar_area(self):

        resultado = (self.valor_1*self.valor_2)
        print(resultado)
class Cilindro(Figuras_Geometricas):
    def __init__(self):
        super().__init__()
    def hallar_area(self):

        resultado = (2*math.pi *self.valor_1)*(self.valor_1+self.valor_2)
        print(resultado)

# program
class Mostrar():
    def menu(self):
    
        while True:
            print("Por favor ingrese la figura que desea calucular el area")
            print("1 - cono")
            print("2 - triangulo")
            print("3 - equilatero")
            print("4 - rectangulo")
            print("5 - cilindro")
            print("6 - salir")
            opcion = int(input("ingrese la opción"))
            if opcion == 1:
                cono1 = Cono()
                cono1.mensaje()
                cono1.hallar_area()
            if opcion == 2:
                triangulo1 = Triangulo()
                triangulo1.mensaje()
                triangulo1.hallar_area()
            if opcion == 3:
                equilatero1 = Triangulo_Equilatero()
                equilatero1.mensaje()
                equilatero1.hallar_area()
            if opcion == 4:
                rectangulo1 = Rectangulo()
                rectangulo1.mensaje()
                rectangulo1.hallar_area()
            if opcion == 5:
                cilindro1 = Cilindro()
                cilindro1.mensaje()
                cilindro1.hallar_area()
            if opcion < 1 or opcion > 5:
                break
ejemplo = Mostrar()
ejemplo.menu()
    


#prueba = menu()