class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.monto = 0
        
    def depositar(self,monto):
        self.monto = self.monto + monto
    
    def extraer(self,monto):
        self.monto = self.monto - monto
    def retornar_monto(self):
        return self.monto
    def imprimir(self):
        print(self.nombre," tiene depositado la suma de",self.monto)
        
class Banco:
    
    def __init__(self):
        self.cliente1 = Cliente("juan")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Diego")
        
    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(100)
    
    def depositos_totales(self):
        total = self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total del dinero del banco es: ",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        

banco1 = Banco()
banco1.operar()
banco1.depositos_totales()

import random

class Dado:
    def tirar(self):
        self.valor  = random.randint(1,6)
    def imprimir(self):
        print("Valor del dado: ",self.valor)
    def retornar_valor(self):
        return self.valor
   

class JuegoDeDados:
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()
    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        
        if self.dado1.retornar_valor() == self.dado2.retornar_valor() and self.dado1.retornar_valor() == self.dado3.retornar_valor():
            print("gano")
        else:
            print("Perdio, Siga intentando")
    
jugador1 = JuegoDeDados()
jugador1.jugar()

class Socio:
    def __init__(self):
        self.nombre = str(input("ingrese su nombre"))
        self.antiguedad = int(input("ingrese la antigudad que lleva en el club"))
    def imprimir(self):
        print("Nombre: ",self.nombre," Antiguedad ",self.antiguedad)
    def retornar(self):
        return self.antiguedad
    
class Club:
    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()
    def masantiguo(self):
        if (self.socio1.retornar() > self.socio2.retornar() and
            self.socio2.retornar() > self.socio3.retornar() or
            self.socio1.retornar() > self.socio3.retornar() and
            self.socio3.retornar() > self.socio2.retornar()):
            print("El socio mayor es el socio 1 ")
            self.socio1.imprimir()
        elif (self.socio2.retornar() > self.socio1.retornar() and
            self.socio1.retornar() > self.socio3.retornar() or
            self.socio2.retornar() > self.socio3.retornar() and
            self.socio3.retornar() > self.socio1.retornar()):
            print("El socio mayor es el socio 2 ")
            self.socio2.imprimir()
        elif (self.socio3.retornar() > self.socio1.retornar() and
            self.socio1.retornar() > self.socio2.retornar() or
            self.socio3.retornar() > self.socio2.retornar() and
            self.socio2.retornar() > self.socio1.retornar()):
            print("El socio mayor es el socio 3 ")
            self.socio3.imprimir()
                
club1 = Club()
club1.masantiguo()



# Conclusiones
# Atributo - es definido por el objeto, por lo tanto tiene el self.socio1
# parametro - se define dentro del metodo, por lo tanto se solicita cuando se crea el metodo 
# para hacer las operaciones necesarias

#variable global - es una variable que es compartida por todos los metodos.
# variable local - es una variable de un metodo es pecifico, puede ser tambien el "parametro"
# si es que este no se define como un atributo del objeto.

# argumento - es el valor o dato que pide el metodo cuando es llamado o invocado para ejecutarse
# si no se pasa el argumento dara error.


