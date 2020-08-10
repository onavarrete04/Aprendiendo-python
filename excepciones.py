# Excepciones

# Excepciones son tipos de errores que no son fatales dentro del programa, sin embargo, si setas no son tratadas
# dentro de las funciones, al final se extenderan a todo el programa

# las excepciones cambian el flujo de ejecución del programa, debido a que se propaga hacia la función que la llama, no todas las
# excepciones pueden interruptir el programa.

while True:
    try:  # try funciona asi, primero se ejecuta el bloque try es decir
        x = int(input("ingrese un numero ")) # <---- Este bloque
        break                                # <---- Este bloque  --> si no ocurre una excepción se saltea y termina la ejecución de la declaración try
    # se saltea la función try pero si hay una palabra reservada "except" se ejecuta ese bloque
    except ValueError:   # es decir, se ejecuta este bloque 
        print("Oops! No era valido, intente nuevamente") # < --- Esteee y la ejecución continua

# si ocurre que el "except" no coincide con la excepció nombrada, se pasa a una decración try si hay mas afuera, si no se encuentra el try
# y otra except que maneje la excepcion, la ejecucion se terminara

# Una declaración try puede tener mas de un except, para especificar distintos manejadores,

"""except (RuntimeError, TypeError, NameError): # para mantener diferentes manejadores se usa el parentesis
    pass"""

# Una clase except es compatible con una excepcion si la misma clase es compatible en la misma clase, o una clase base de la misma

class B(Exception ):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D") # SI ESTA CLAUSULA FUERA LA DE LA B, HUBIERA IMPRESO 3 B
    except C:
        print("C")
    except B:
        print("B")

import sys # este siempre se importa al inicio, sin embargo, por facilidad del ejercico se hara aca.

try:
    f = open("miarchivo.txt")
    s = f.readline()
    i = int(s.strip)
except OSError as err:
    print("Error OS: {}".format(err))
except ValueError:
    print("No se pudo convertir el dato a un entero")
except:
    print("Error inesperado: ", sys.exc_info() [0])
    raise

# la declaración try  ... except tiene un bloque   else   opcional el cual debe seguir a los except
# es util cuando se debe ejecutar el bloque try si no genera una excepcion

for arg in sys.argv[1:]:
    try:
        f = open(arg, "r")
    except OSError:
        print("No pude abrir, ", arg)
    else:
        print(arg, "tiene ", len(f.readline()), "lineas")
        f.close()
    
# El uso de else es mejor que agregar otro try adicional, porque evita la captura accidental de una excepcion que no fue agregada por el codigo

# cuando ocurre una excepcion puede tener un valor asociado tambien conocido como argumento de la excepcion, la presencia y el tipo de argumento depende de la excepcion

# el except puede especificar una variable luego del nombre de excepcion, la variable vincula los argumentos
# en instance.args, por conveniencia la instancia define __str__() para que se pue mostrar los argumentos sin hacer referencia a .args

try:
    raise Exception("carne" , "huevos")
except Exception as inst:
    print(type(inst))  # la instancia de la excepcion
    print(inst.args)   # argumentos guardados en .args
    print(inst)        # __str__ permite imprimir args directamente, pero puede ser cambiado por sub clases

    """ x , y = inst
    print("x = ", x) #no se entiende porque no funciono
    print("x = ", y) """

def esto_falla():
    x = 1/0
try:
    esto_falla()
except ZeroDivisionError as err:
    print("Manejando el erroe en tiempo de ejecucion: ",err)


# LEVANTANDO EXCEPCIONES

# la declaración raise permite al programador forzar a que ocurra una excepcion especifica

#raise NameError("Hola")

# El unico argumento a raise indica la excepcion a generarse, tiene qque ser una instancia de excepcion, o una clase
# de excepcion (clase heredada de exception). 

# raise_ValueError__  atajo para raise ValueError() no lo leyo!!

# cuando quieres saber cuando una excepcion fue lanzada pero no quieres manejarla
"""
try:
    raise NameError("Hola")
except NameError:
    print("Volo una excepcion")
    raise
"""


# EXEPCIONES DEFINIDAS POR EL USUARIO

# los programas pueden nombrar su propias excepciones creando una nueva clase de excepcion, las excepciones deberan derivar de la clase Exception 
# directa o indirectamente, normalmente estas clases se mantienen simples ofreciendo información sobre el error que los leera

class Error(Exception):
    """Clase base para excepciones en el módulo"""
    pass

class EntradaError(Error):
    """
    Excepcion lanzada por errores de entrada.

    Atributos

    expresion --expresión de entrada en la que ocurre el error
    mensaje   --explicación del error
    """
    def __init__(self, expresion, mensaje):
        self.expresion = expresion
        self.mensaje = mensaje

class Transicion_Error(Error):
    """Lanzada cuando una operacion internta una transicion de estado no permitida

    atributos

    previo -- estado al principio de la transicion
    siguiente -- nuevo estado intentando
    mensaje -- explicacion de por que la transición no esta permitida
    """

    def __init__(self, previo, siguiente, mensaje):
        self.previo = previo
        self.siguiente = siguiente
        self.mensaje = mensaje

# Definiendo acciones de limpieza

# La declaración try tiene otra cláusula opcional que intenta definir acciones de limpieza que deben ser ejecutadas bajo
"""
try:
    raise KeyboardInterrupt
finally:
    print("chau mundo")

"""

# Una cláusula finally siempre es ejecutada antes de salir de la declaración try, ya sea que una excepción haya ocurrido o no.
#Cuando ocurre una excepción en la cláusula try y no fue manejada por una cláusula except (o ocurrió en una cláusula
#except o else), es relanzada luego de que se ejecuta la cláusula finally . El finally es también ejecutado "a la salida"
#cuando cualquier otra cláusula de la declaración try es dejada via break, continue or return. Un ejemplo más

# Acciones predefinidas de limpieza
"""
for linea in open("miarchivo.txt"):
    print(linea, end="")
    """
# el problema seria que esto deja al archivo abierto por un tiempo indeterminado

"""
with open("miarchivo.txt") as f: -> el with permite que los arvhicos usados sean liberados de forma correcta
    for linea in f:
        print(linea, end="")
    
    luego de la declaracion ejecutada el archivo es cerrado, incluso si hay un problema al procesar lineas

    """

import math

def raiz_cuadrada(number):
    if number < 0:
        raise ValueError("Numero negativo")
    return math.sqrt(number)

# para crear una clase excepción esta debe heredar de exception

class NegativeNumber(Exception):
    "Excepción de tipo numero negativo"
    pass