# ejemplo 1

#función que escribe la serie de Fibonacci hasta un limite determinado

def fib(n):

    a , b = 0,1
    while a < n:
        print(a, end="") # end se utiliza para que la información se imprima en fila
        a, b = b, a+b
    print()

print(fib(2000))

# def se utiliza para definir funciones, se le da una lista de parametros formales entre parentesis, las sentencias forma el cuerpo de la función

#docstring son una cadena de texto literal de documentación de la función
# la ejecución de la función introduce unas tablas de datos para las variables locales
#las funciones tambien pueden ser redefinidas

f = fib
print(f(1000))

# en otros lenguajes se puede objetar que la función fib es un procedimiento y no una función porque no devuelve un valor
#de hecho, tecnicamente hablando, los procedimientos si retornan un valor: None,

print(f(0))  # es igual a None

def fib2(n):
    result = []  # aca se dice que la variable result va a ser una lista
    a, b = 0, 1
    while a < n:
        result.append(a)   # append() añade contenido al final como le especifiquemos
        a,b = b, a+b           # append esta definido para objetos listas
    return result     # la función return () Retorne inmediatemente de esta función y use la siguiente expresión como un valor de retorno

f100 = fib2(100)
print(f100)

# definir funciones con un numero variable de argumento

def pedir_confirmacion(prompt, reintentos = 4, recordatorio='por favor, intente nuevamente!'):
    while True:
        ok = input(prompt)   #input permite insertar información y prompt la muestra
        if ok in ('s','S', 'si','Si','SI'):
            return True
        if ok in ('n','no','No','NO'):
            return False
        if reintentos <0:
            raise ValueError('respeusta de usuario invalida')
        print(recordatorio)

pedir_confirmacion('¿Sobreescribir archivo?', 2)

pedir_confirmacion('te llamas oscar', 1)

i = 5

def f(arg=i):
    print(arg)

print(i)

i = 6

print(f(1))
print(f(2))
print(f(3))

def f(a, L =None):
    if L is None:
        L = []  # L es una lista
    L. append(a) # L agregara las letras a ingresadas y las ira sumando
    return L
print(f(1))
print(f(1))

#las funciones pueden ser llamadas por palabras claves
def loro(tension, estado="muerto", accion = " explotar",tipo="Azul Nordico"):
    print("-- Este loro no va a ", accion, end="")
    print("si le aplicas",tension,"voltios.")
    print("-- Gran plumaje tiene el ",tipo)
    print("-- Esta, ",estado,"!")

print(100)
print(loro(tension=1000))
print(loro(tension=100000, accion="VOOOOOM"))
print(loro(accion="VOOOOOOOOOM", tension="100000"))
print(loro("un millon","despojado de vida","saltar"))

#cuando un parametro tiene la forma *nombre esta presente al final, recibe un diccionario de contenidos, exepto 
# aquellos correspondientes al parametro formal, esto puede ser combiado
# parametro formal * nombre recibe tupla y debe ocurrir antes que **palabrasclaves

def venta_de_queso(tipo,*argumentos,**palabrasclaves):
    print("--¿Tiene ",tipo,"?")
    print("--Lo siento, nos quedamos sin ",tipo)
    for arg in argumentos:
        print(arg)
    print("-" * 40)
    for c in palabrasclaves:
        print(c," : ",palabrasclaves[c])

venta_de_queso("Limburger", "Es muy liquido, sr.",
 "Realmente es muy muy liquido, sr.",
 cliente="Juan Garau",
 vendedor="Miguel Paez",
 puesto="Venta de Queso Argentino")

 #Lista de Argumentos Arbitrarios
def muchos_items(archivo,separador,*args):
    archivo.write(separador.join(args))   #este tipo de función da error debido a que no se ha cerrado

def concatenar(*args, sep="/"):
    return sep.join(args)
    
print(concatenar("tierra","marte","venus"))

# .write escribe un archivo, join convierte en un string en una lista de caracteres separados por,

# DESEMPAQUTANDO LISTA DE ARGUMENTOS
 # La situación inversa ocurre cuando los argumentos estan en una lista y necesitan ser desempaquetados
 #para eso se usa la función range() predefinida

list(range(3,6)) # se utiliza la función list para crear una lista y la función rango para que sea de 3 a 6

print(list(range(3,6)))

def loro(tension, estado="rostizado",accion="explotar"):
    print("-- Este loro no va a",accion,end=" ")
    print("si le aplicas",tension," voltios.",end="")
    print("Esta",estado,"!")

d={"tension":"cincomil",
"estado":"demacrado",
"accion":"VOLAR"
}
print(loro(**d))  # **d significa darle predominancia a esta info y se lee como la lectura de un diccionario
                  
                  #  *d un parametro, este puede ser individual o en lista

#Expresiones Lambda

# Lambda es una función que retorna la suma de sus dos argumentos, puede ser usada cuando es requerido un objeto de tipo funcion.
# Son funciones anonimas o sin nombre o lambda, estan sintacticamente restringidas a una expresion

agregar = lambda numero1, numero2: numero1 + numero2 # los : refieren un return en esta expresión

print(500,500)

def hacer_incrementador(n):
    return lambda x: x + n  # dice que x va a hacer 42 + el n que le sumes

def funcion_tiempo(ñ,*arg):
    inicio_tiempo=tiempo.tiempo()
    resultado =ñ(*arg)
    final_tiempo = tiempo.tiempo()
    print("Tiempo de ejecución",final_tiempo - inicio_tiempo, "milisegundos" )
    return resultado

ñ = hacer_incrementador(42)

print(ñ(0)) # se le sumo 0
print(ñ(1)) # se le sumo 1

print("funcion tiempo ",funcion_tiempo,(ñ,5))
# Cadenas de Texto Documentativas

# la primera linea debe ser un resumen conciso del objeto. solo se describe el nombre o tipo del objeto cuando se utiliza un verbo, de resto no porque esa info ya esta
# Se inicia con una mayuscula y se termina con un punto, la segunda linea debe ir en blanco

def mi_funcion():
    """No hace mas que documentar la función.
    
    No, de verdad. No hace nada
    """
    pass

print(mi_funcion.__doc__)  # __doc__ imprime la cadena documentativa

#Anotación de Funciones

# son información opcional sobre los tipos usados en funciones definidas por el usuario
# se almacenan en el atributo __annotations__ y se hace asi

def f(jamon: str, huevos : str = 'huevos') -> str:
    print("anotaciones:",f.__annotations__)
    print("argumentos: ",jamon,huevos)
    return jamon + ' y ' + huevos

print(f('carne'))

# variables locales, las variables locales existen dentro del contexto de la función, es decir,
# si se llama la variable por si sola, python la recibira como un error.
# .

def suma(h,j):   #h,j son los parametros, en este caso pueden ser int, o float, o cualquier tipo de dato, toca usar type() para saberlo
    resultado = h + j   # resultado es una variable local, si se llama por fuera no sirve
    return resultado

#lectura flujo de ejecución

# lee el programa desde la primer linea uft-8, en este caso, leera primero las funciones, las comprobara,
# pero solo las ejecutara cuando estas sean llamadas.



#Funciones Utiles

#Son funciones que siempr estan disponibles, son conocidos como built-ins de python :

""" print - imprime texto en pantalla
range - da un rango inmutable
enumerate - devuelve un objeto enumerador, con el indice correspondiente
input - permite pedirle al usuario un valor
int - devuelve un entero, o convierte otro dato en entero
float - devuelve un decimal
str - devuelve un string
bool - devuelve un falso o verdadero
type - devuelve el tipo de un objeto 


"""
for x in range(10):
    print(x)

for x in range(1,10): # le dices iniciamos en 1 , y terminamos en 10
    print(x)    
for x in range(1,10,2): # le dices, iniciamos en 1 , terminas en 10, y va a ser de 2 en 2
    print(x)
for x in range(10,0,-1): # comienzas en 10, terminas en 0, y vas a ir en -1
    print(x)

# Permiten reutilizar codigo durante el programa, todas tienen entradas y devuelven algo

def hello(): 
    print('hello world')

    # solo se utilizan cuando se llama

hello()

# las funciones reciben parametros

def hello(name):
    print("hola "+name)

hello('oscar')
# cuando le dices que recibiras un parametro y no le das nada, te da error

def hello(name="persona"): # eso es un parametro por defecto
    print("hola "+name)

hello('oscar')