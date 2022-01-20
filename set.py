# Esto es un conjunto

# es una colección desordenada que no tiene indice o index

colores ={'red','green','blue','violet'}

print(type(colores))

print('red' in colores)

colores.add('yelow')   # add() agrega, pero lo hace al inicio

colores.remove('red')   # elimina el dato especificado

colores.clear()         # imprime el valor set() limpio sin elementos dentro

del colores    # el del borra el dato set completo

conjunto1 = {1,5,10,20}

# 

conjunto = {} # si se define el conjunto de esta manera será de forma erronea
# esto definirá un diccionario lo cuál generara un error futuramente
print(type(conjunto))

# La manera correcta de hacerlo es de esta forma
conjunto = set()
print(type(conjunto))

# Una cáracteristica importantisima de los conjuntos es que no repiten un dato
# repetido

# Los elementos de un conjunto pueden ser contener tipo de estructura
#  distinto

conjunto = {(1,2,3),True}

print(conjunto)


# Pertinencia en los conjuntos

# in


lenguajes = {"C","Pascal","PHP","Python"}

if "PHP" in lenguajes:
    print("si contiene este lenguaje")
else:
    print("El lenguaje no se encuentra")

lenguaje1 = {"C","Pascal","PHP","Python"}
lenguaje2 = {"C++","Java","Python"}

# Unión se utiliza la ->       |

conjunto1 = lenguaje1 | lenguaje2 # 
print(conjunto1)

# Intersección  utiliza la ->    &

conjunto2 = lenguaje1 & lenguaje2
print(conjunto2)

# Diferencia utiliza signo ->  (-)

conjunto3 = lenguaje1 - lenguaje2
print(conjunto3)
# La diferencia indica, cual es la diferencia del lenguaje1 respecto al comando 2

# Diferencia simetrica se utiliza el signo - ^

conjunto4 = lenguaje1 ^ lenguaje2

print(conjunto4)

# Elementos en común

dias_feriados = {"sabado","domingo"}
dias_laborales = {"lunes","martes","miercoles","jueves","viernes","sabado","domingo"}

if dias_laborales.isdisjoint(dias_feriados):
# isdisjoint -> metodo
    print("Días laborales no tienen elementos en común con dias feriados")


"""
En Python podemos utilizar los operadores:

conjunto1==conjunto2
conjunto1!=conjunto2
conjunto1<conjunto2 (si el conjunto1 es un subconjunto de conjunto2)
conjunto1<=conjunto2 (si el conjunto1 es un subconjunto o es igual que conjunto2)
conjunto1>conjunto2 (si el conjunto1 es un superconjunto de conjunto2)
conjunto1>=conjunto2 (si el conjunto1 es un superconjunto o es igual que conjunto2)

"""

dias_semana={"lunes", "martes", "miércoles","jueves","viernes","sábado","domingo"}
dias_feriados={"sábado","domingo"}
dias_laborables={"lunes", "martes", "miércoles","jueves","viernes"}
if dias_feriados<dias_semana:
    print("dias_feriados es un subconjunto de dias_semana")
if dias_feriados!=dias_laborables:
    print("dias_feriados es distinto a dias_laborables")    
if dias_semana>dias_laborables:
    print("dias_semana es un superconjunto de dias_laborables")