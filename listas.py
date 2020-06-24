# antes de las listas toca decir que len() cuenta el string
# la lista se escribe en [] y separa sus datos por ,
cuadrados = [1,4,9,16,25]
print (cuadrados)
# como vimos, las se puede usar len en la lista
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


#TUPLAS
#se utilizan especialmente con datos que no cambian, digamos las listas si pueden cambiar, las tuplas no.
# se representa en () es decir, es inmutable
a=(22,20,30,25)
print(type(a))



