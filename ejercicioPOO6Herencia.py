class Persona:
    def __init__(self):
        self.nombre = input("ingrese su nombre")
        self.edad = int(input("ingrese su edad"))
        
    def imprimir(self):
        print(self.nombre," tiene ",self.edad," años")
    def retornar(self):
        return self.nombre, self.edad
    
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("ingrese el sueldo: "))
    def imprimor(self):
        self.imprimir()
        print("Sueldo: ",self.sueldo)
    def paga_impuestos(self):
        
        if self.sueldo > 3000:
            
            print("Debe pagar impuestos")
        else:
            
            print("su sueldo ",self.sueldo," no llega a los topes para declarar")
    
persona1 = Persona()
persona1.imprimir()
print("_____________________________")
empleado1 = Empleado()
empleado1.imprimor()
empleado1.paga_impuestos()

class Operacion:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0
    
    def cargar(self):
        self.valor1 = int(input("ingrese el primer valor"))
        self.valor2 = int(input("ingrese el segundo valor"))
    def mostrar(self):
        print(self.resultado)
    def operar(self):
        pass
    
class Suma(Operacion):
    def operar(self):
        Operacion.resultado=self.valor1+self.valor2
class Resta(Operacion):
    def operar(self):
        self.resultado = self.valor1 - self.valor2
        
suma1 = Suma()
suma1.cargar()
suma1.operar()
print("la suma de los valores es ")
suma1.mostrar()

resta1 = Resta()
resta1.cargar()
resta1.operar()
print("la resta de los valores es ")
resta1.mostrar()

class Cuenta:
    
    def __init__(self):
        
        self.nombre = input("ingrese su nombre")
        self.monto = float(input("ingrese monto de dinero"))
        self.meses = 0 # no debi llamar este atributo aqui
        self.resultado = 0 # no debi llamar este atributo aqui porque no es compartido por las clases herederas
    
    def imprimir(self):
        print(self.nombre," tiene en su cuenta ",self.monto," ahorrados")
    def imposicion(self): # esta clase no sirve para el ejercicio, aunque podría funcionar si se 
                            # esta incentivando hacer cambios en la clases hijas
        
        pass
    
class CajaAhorra(Cuenta):
    
    def imposicion(self):
        super().imprimir() 
        
        print("Esta cuenta esta libre de imposiciones e intereses, es una cuenta de Ahorros")
        
class PlazoFijo(Cuenta):
    # debi definir la clase __init__(parametros, intereses, meses, resultado) aunque ltambien los llame por teclado
    # debi llamar la clase super().__init__() # todavía me encuentro buscando la respuesta del porqué
    def imposicion(self):
        self.interes = float(input("ingrese el interes del periodo fijado mensual"))
        self.interes = self.interes/100
        self.meses = int(input("ingrese el numero de meses fijos"))
        self.resultado = (self.monto * self.interes) * self.meses
        super().imprimir()
        print("Usted ha acumulado un interes de ",self.resultado)
        

ahorro1 = CajaAhorra()
ahorro1.imposicion()

fijo1 = PlazoFijo()
fijo1.imposicion()

# Conclusiones

# cuando se usa herencia de clases, en la clase secundaria o hija se utilisa class Empleado(Persona):
# Con el fin de indicar de que clase esta heredando
# dentro de la clase herencia, la clase hijo puede llamar al metodo super().
# y este metodo buscara hacia arriba en clases superiores que estan heredandole, buscando 
# el metodo especifico que se llamo, por ejemplo el metodo __init__
# El metodo super() no sirve en ocasiones cuando la herencia es multiple, por lo que debera
# definirse las clases que se llaman, junto con los  parametros que se llaman