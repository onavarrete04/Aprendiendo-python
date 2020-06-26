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





