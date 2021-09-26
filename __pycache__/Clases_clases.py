# Este es un ejemplo que muestra como hacer referencia a distintos ámbitos y espacios de nombres, y cómo las declaraciones
# global y nonlocal afectan la asignación de variables:

def prueba_ambitos():
    def hacer_local():
        algo = "algo local"
    def hacer_nonlocal():
        nonlocal algo
        algo = "algo NOOOO local" 
    def hacer_global():
        global algo
        algo = "algo global"
    algo = " algo de prueba"
    hacer_local()
    print("luego de la asignacion local",algo)
    hacer_nonlocal()
    print("Luego de la asignacion no local: ",algo)
    hacer_global()
    print("Luego de la asignacion global: ",algo)

prueba_ambitos()
print("En alcance global: ", algo)

# sintaxis de clases

class MiClase:
    """tienen funciones def que deben ejecutarse antes de que tengan un efecto
    
    Simple clase de ejemplo
    """
    i = 123456
    def f(self):
        return "Hola Mundo"
print(MiClase.f)
print(MiClase.i)

class Complejo:
    def __init__(self,partereal,parteimaginaria):
        self.lr = partereal
        self.i = parteimaginaria

x = Complejo(3.0, -4.5)

print(x.lr, x.i)


x.contador = 1

while x.contador < 10:
    x.contador = x.contador * 2
print(x.contador)

class Perro:
    tipo = 'canino' # variable de clase compartida por todas las instancias
    def __init__(self, nombre):
        self.nombre = nombre # variable de instancia única para la instancia
d = Perro('Fido')
e = Perro('Buddy')
print(d.tipo) # compartido por todos los perros 'canino'
print(e.tipo) # compartido por todos los perros'canino'
print(d.nombre) # único para d
 
print(e.nombre) # único para e 'Buddy'

class Perro:
    trucos = [] # uso incorrecto de una variable de clase
    def __init__(self, nombre):
        self.nombre = nombre
    def agregar_truco(self, truco):
        self.trucos.append(truco)
d = Perro("Fido")
e = Perro("pleto")
d.agregar_truco('girar')
e.agregar_truco('hacerse el muerto')

# como la variable de clase  compartida es una lista, esta guarda todos los trucos y los comparte

class PerroS:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trucos = [] # crea una nueva lista vacía para cada perro
    def agregar_truco(self, truco):
        self.trucos.append(truco)


class Dinero:
         
    
    def __init__(self,dolar,euro,centavo):

        penny = 0.01
        self.dolar = dolar * (penny * 100)
        self.euro = euro* (penny * 100)
        self.centavo = centavo * penny 
        
        print("Dolar USD$: ",self.dolar,"\n")
        print("Euro EU$: ",self.euro,"\n")
        print("Centavos = ",self.centavo)

    def Sumar(self,dolar1, euro1, centavo1,):
        
        print("dolar + dolar es: ",dolar1+self.dolar)
        print("dolar + euro es: ",dolar1 + euro1)
        print("dolar + centavo es: ",dolar1 + (centavo1*0.01))
        print("euro + euro es: ",euro1 + self.euro)
        print("dolar + euro es: ",euro1 + euro1)
        print("dolar + centavo es: ",euro1 + (centavo1*0.01))
        print("centavo + centavo es ",(centavo1*0.01 )+self.centavo)

    def Restar(self,d, e, c,):
        
        print("dolar - dolar es: ",d-self.dolar)
        print("dolar - euro es: ",d - self.euro)
        print("dolar - centavo es: ",d - self.centavo)
        print("euro - euro es: ",e - self.euro)
        print("euro - euro es: ",e - self.euro)
        print("euro - centavo es: ",e - self.centavo)
        print("centavo - centavo es ",(c*0.01 )-self.centavo)




moneda_1 = Dinero(1,1,1)
moneda_1.Sumar(2,2,2)
moneda_2 = Dinero(3,3,3)
moneda_2.Restar(3,3,3)



    
"""class Perro:
    
    def __init__(self):

        self.ladra = False
    def prueba(self):

        self.ladra = True

Drako = Perro()

print(Drako.ladra)
print("-"*6)
Drako.prueba()
print(Drako.ladra)"""

# PRINCIPIOS

# 1. POLIMORFISMOS

# Un polimorfismo es utilizar metodos de otras clases mayores para un mismo fin, diferenciando el fin. Ejemplo, agregar un nuevo usuario
# pero ese usuario sera administrador, es decir, tendra unos permisos especiales, pero para crear el usuario utilizara la clase Usuario ya 
# diseñada previamente.

# 2. HERENCIA

# Organizar el conocimiento junto con sus relaciones entre si. Como bien dice, la herencia, crea clases a partir de una clase mayor o superior
# vinculando atributos y metodos de la clase superior, y creando atributos y metodos nuevos necesarios para la nueva clase