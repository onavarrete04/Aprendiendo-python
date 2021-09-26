class Empleado:
    def __init__(self):
        self.nombre = str(input("ingrese su nombre"))
        self.sueldo = float(input("ingrese salario"))
        
    def imprimir(self):
        print("Usuario -> ",self.nombre)
        print("Salario -> ",self.sueldo)
    def impuestos(self):
        if self.sueldo >= 3000:
            print("Cumple los requisitos para pagar impuestos, acerquese a la DIAN")
        else:
            print("No cumple los montos para pagar impuestos")
            
empleado1 = Empleado()
empleado1.imprimir()
empleado1.impuestos()


class PlanoCartesiano:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def cuadrantes(self):
        
        if self.x == 0 and self.y > 0:
            print("El punto se encuentra en la parte positiva, en medio del cuadrante I y II ")
        elif self.y == 0 and self.x > 0:
            print("El punto se encuentra en el cuadrante I y cuadrante IV ")
        elif self.y == 0 and self.x < 0:
            print("El punto se encuentra entre  el cuadrante II y III")
        elif self.y > 0 and self.x < 0:
            print("El punto se encuentra en el cuadrante II")
        elif self.y > 0 and self.x > 0: 
            print("El punto se encuentra en el cuadrante I")
        elif self.y < 0 and self.x < 0:
            print("El punto se encuentra en el cuadrante III")
        elif self.y < 0 and self.x > 0:
                  
            print("El punto se encuentra en el cuadrante IV")

plano1 = PlanoCartesiano(0,-1)
plano1.cuadrantes()



class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    def perimetro(self):
        
        perime = self.lado + self.lado + self.lado + self.lado
        
        print(self.perime)
        
    def area(self):
        
        a = self.lado * self.lado
        
        print(a)
        
cuadrado1 = Cuadrado(3)
cuadrado1.perimetro()
cuadrado1.area()