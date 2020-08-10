# antes de las listas toca decir que len() cuenta el string
# la lista se escribe en [] y separa sus datos por ,
cuadrados = [1,4,9,16,25]
print (cuadrados)
# como vimos, las se puede usar len en la lista para contar los elementos
print(len(cuadrados))
# asi mismo, se pueden llamar datos especificamente
print(cuadrados[0])
print(cuadrados[:2])
print(cuadrados[2:])
print(cuadrados[1:2])
# tambien se pueden concadenar
print(cuadrados + [36,49,64,81,100])
# las listas si son mutables, las cadenas de texto no, ejemplo
cubos = [1,8,27,65,125] # el dato 65 esta mal, es 64, 4**3
print(cubos)
cubos[3]=64 # se corrige el error
print(cubos)
# agregar elementos al final de la lista con append()
cubos.append(216)
cubos.append(7**3)
print(cubos)
# tambien podemos reemplazar valores y eliminarlos de las listas
letras = ['a','b','c','d','e','f','g']
print(letras)
#asi se reemplazan
letras[2:5]=['C','D','E']
print(letras)
# asi se eliminan
letras[2:5]= []
print(letras)
#anidar listas o listas que contengan otras listas
a= ['a','b','c']
b=[1,2,3]
x = [a,b]
print(x)
# tambien podemos llamarlos por su posicion
print(x[0])
print(x[0][1]) 
# las listas tambien pueden tener cualquier tipo de dato por ejemplo
xl=[True, 'Grande', 40, 40.1]
print(xl)
# en este ejemplo vemos que una lista puede tener un boleano, un string, y un int
# y si le damo type() nos dara que es una lista
print(type(xl))

# se pueden crear una lista dentro de una lista

sublistas=[1,2,3,4,['a','b','c']]

#con la función list() se puede crear una listas

numer_list= list((2,3,4,5,6,7,8))
print(numer_list)
print(type(numer_list))
#numero= list(1,2), la función list() solo soporta un dato, por eso se presento la tupla para que pudiera conformar la lista, la tupla es 1 dato

# listas con range() introduce numeros enteros y asi se puede crear una lista
r = list(range(1,11))
print(r)

print(dir(r))  #dir() muestra las funciones que puedes usar

print(1 in r) # se pregunta si 1 esta en la lista r, in significa "esta en" en este caso
colores = ["rojo","amarillo","azul"]

#METODOS

colores.append('violeta') #append() agrega elementos pero solo acepta 1 elemento
colores.extend(('marron','cafe')) # agrega colores de una tupla o lista, pero los agrega como individuales, append no puede hacerlo, tambien solo espera 1 argumento
print(colores)
colores.insert(-1, 'verde') # puedes insertar elementos segun su posición

colores.pop()  # elimina el ultimo elementos del index, osea puedes poner un indice colores.pop(1)
colores.remove('violeta')
print(colores)
colores.sort() #sort organiza alfabeticamente lso colores
colores.sort(reverse=True)  # asi lo hace de manera inversa
print(colores.index("amarillo"))

colores.clear() # limpia toda la lista, los elimina todos


# Lo importante de las listas, es que permiten guardar todo tipo de dato, por eso vamos a hacer ejemplos

a_lista = [3, 7.5, "Hola", 7j + 5, [1,2]]

# se accede por index

a_lista[0]
a_lista[-2]
a_lista[-1]

# porciones de la lista

a_lista[1:]
a_lista[2:3]
a_lista[:]
a_lista[2:2]

# LEN

len(a_lista)

# APPEND

a_lista.append(2)

# EXTEND

a_lista.extend([3,4])

# INSERT

a_lista.insert(4, "intercalado") # el numero es el indice

# COUNT

a_lista.count(3)

# REMOVE

a_lista.remove(3)

# COPY
"""
a_lista.copy = a_lista.copy()"""

# POP

a_lista.pop()

a_lista.pop(3) # indica indice a quitar a la lista

# CLEAR

a_lista.clear()

# las listas y los string son secuencias ordenadas de elementos, las listas son mutables, los string no

nombre = "oscar"

lista = list(nombre)

# indexado

nombre[0]
lista[0]

nombre[:4]
lista[:4]

len(nombre)
len(lista)

"A" in nombre
"A" in lista

"x" not in nombre
"x" not in lista


for letra in nombre:
    print(letra)

lista[2] = "o"
# no se puede cambiar un estrin

"hola " + nombre

# listas como pilas

stack = [1,2,3]

# ingresar elemento

stack.append(4)
stack.append(5)

# saco elementos

stack.pop()
stack.pop()
stack.pop()

# Listas como Colas
from collections import deque

cola = [1,2,3]

cola.append(4)
cola.append(5)

cola.pop()
cola.pop()


# a diferencia de las listas como pilas, las listas como colas presentan menos eficiencia, por eso
# se utiliza libreria

# colas implementadas correctamente desde libreria

cola = deque([1,2,3])

# para eso utilizaremos la funcion popleft para zacar los elementos de la cola
cola.append(4)
cola.append(5)
cola.popleft()
cola.popleft()

# LISTAS POR COMPRENSION

cuadrados = []

for x in range(10):
    cuadrados.append(x**2)

# listas por comprension ejemplos
cuadros_2 = (x ** 2 for x in range(10))

# utilizando funcion map
cuadrados_3 = list(map(lambda x: x**2, range(10)))

# map devuelve un generador

a_list = [-4,-2,0,1,2,4]

# lista con positivos

positivos = [x for x in a_list if x>=0]

positivo_2 = list(filter(lambda x: x>0, a_list))

# pares numero y su cuadrado

([x,x**2] for x in range(10))

# lista pares combinando

pares = [(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]

# pares seria igual a 

pares_2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y :
            pares_2.append((x,y))
