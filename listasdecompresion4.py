
# Lista por extension, se enumeran todos los elementos
numero = [1,2,3,4,5]

# listas por comprension

# se define un conjunto bajo una propiedad, en la que todos los elementos
# cumplen esa propiedad

# extension

numeros = []

for n in range(1,6):
    numeros.append(n)
print(numeros)

# comprension

numeros = [n for n in range(1,6)]
"""
la n significa los elementos que queremos incluir, es el priemr valor

a) se componen por una expresion (n) en este caso
b) un ciclo for -> for (n)
c) un iterable, en este caso es un range(1,10)
"""

print(["*"*n for n in range(1,6)])

#----------------

print("-"*9)

numeros = [2,3,5,8,9]

cuadrado = [n**2 for n in numeros]
print(cuadrado)

cadena = "artefacto"
letras = [letra for letra in cadena]
print(letras)

palabras = ["Casa", "Mesa", "Silla", "Puerta", "Ventana"]

iniciales = [caracter[0] for caracter in palabras]
print(iniciales)

#----------

datos = [14, 18, 21, 29, 36, 41, 58, 63, 74]

pares = [n for n in datos if n % 2== 0]
print(pares)

pares = [n for n in datos if n % 2== 0 if n>30]
print(pares)

utensillos = ["mesa", "interruptor","silla","microscopio","cubo"]
letrasmayor= [caracter for caracter in utensillos if len(caracter)>=7]
print(letrasmayor)


#-----------------

lista = [ numeros+1 for numeros in range(1,30) if numeros%7==0 or numeros%11 ==0 ]
print(lista)
lista = [ numeros+1 for numeros in range(1,30) if numeros%7==0 if numeros%11 ==0 ] # el if subsiguiente funciona como un and
print(lista)

datos = [2,3,5,8,10,12,15]

pares = [n if n % 2 == 0 else 0 for n in range(1,10) ] # si n es par se incluye el numero, sino el 0 
print(pares)
# Cuando se incluye un bloque else, este debe ser antes del ciclo for

datos = [7,"h",2.5,8.2,24,"p"]
tipos = ["cadena" if type(elemento) == str else "numérico" for elemento in datos]
print(tipos) # pero aqui hay tres tipos de datos

# forma a
tipos = ["cadena" if type(elemento) == str else
 "float" if type(elemento)== float else
 "entero"  for elemento in datos]
print(tipos)

# forma b
tipos = ["cadena" if isinstance(elemento,str) else
 "float" if isinstance(elemento,float) else
  "entero"  for elemento in datos]
print(tipos)

personas = [["Jorge",36],["Silvia",24], ["Tomas",47],
            ["Irene",19],["Ignacio",21],["Julia",43],
            ["Sara",38],["Miguel",22]]

# forma 1
personas4 = [[nombre,"mayor"] if edad>30 else
            [nombre,"menor"]  for nombre, edad in personas]
print(personas4)
print("---")
# forma 2
personas4 = [[persona[0],"mayor"] if persona[1]>30 else
            [persona[0],"menor"] for persona in personas]
print(personas4)
print("---")
# forma3
personas5=[[p[0],"mayor" if p[1]> 30 else "menor"]for p in personas] 
# la mejor forma es esta
print(personas5)
print("---")



# LISTAS DE COMPRENSION A PARTIR DE DICCIONARIOS

inventario = {"Puntas":30,
              "Tornillos":140,
              "Tuercas":250,
              "Arandelas":70
}
# forma 1
pedido = [articulo for articulo in inventario if inventario[articulo]<100]
print(pedido)
print("--")
#forma 2-")
pedido2 = [clave for clave, valor in inventario.items() if valor<100] 
# la función items imprime los datos referentes a las llaves, un diccionario es {llave:valor}
print(pedido2)
print("---")
alumnos = [
  {"Nombre":"Claudia","Nota":9,"Grupo":"A"},
  {"Nombre":"Esteban","Nota":4,"Grupo":"B"},
  {"Nombre":"Silvia","Nota":7,"Grupo":"C"},
  {"Nombre":"Jorge","Nota":3,"Grupo":"B"},
  {"Nombre":"Roberto","Nota":6,"Grupo":"A"}
]

lista_alumnos = [valor["Nombre"] for valor in alumnos if valor["Nota"]>5]
print(lista_alumnos)

print("---")

alumnos_2 = {
  "Claudia":{"Matematicas":8,"Lengua":7,"Ingles":6},
  "Esteban":{"Matematicas":7,"Lengua":3,"Ingles":8},
  "Silvia":{"Matematicas":5,"Lengua":5,"Ingles":9},
  "Jorge":{"Matematicas":3,"Lengua":4,"Ingles":5},
  "Roberto":{"Matematicas":9,"Lengua":6,"Ingles":7}
}

# Ejercicio dificil para mi
alumnos_2_lengua = [nombre for nombre,  asignaturas in alumnos_2.items()
                    if asignaturas["Lengua"]>=5]


print(alumnos_2_lengua)
print("---")

aprobados = [nombre for nombre in alumnos_2 if alumnos_2[nombre]["Lengua"]>=5] # más facil,
# nombre accede a las llaves, y nombre["lenguas"] accede a la segnda llave
# alumnos_2[nombre]["Lengua"] se accede al valor de la clave lengua, que esta en la clave del nombre, que estan en alumnos

print("---")

valores_decimales = [1.2342432423, 2.34523432, 3.452837657556]

# poner solo un decimal

valores_redondeados = [round(numero,2) for numero in valores_decimales]
print(valores_redondeados)

minusculas = ["mesa","silla","puerta","ventana","armario"]
mayusculas = [palabra.upper() for palabra in minusculas]
print(mayusculas)

import math
radio_circulos = [7,12,21,32,41]

area = [round(math.pi * r**2,1) for r in radio_circulos]
print(area)


# ANIDADOS

# normal

pares = []
for i in range(1,6):
  for j in range(1,6):
    pares.append((i,j))
print(pares)

pares2 = [(i,j) for i in range(1,6) for j in range(1,6)]
print(pares2)


formas = ["Cuadrado","Triangulo","Circulo"]
colores = ["Rojo","Verde","Amarillo","Azul","Negro"]

combinacion = [[forma,color] for forma in formas for color in colores ]
print(combinacion)

dato_1 = [2,3,5]
dato_2 = [2,4,6]
dato_3 = [1,3,5]

matriz = [[a+b+c] for a in dato_1 for b in dato_2 for c in dato_3
          if sum([a,b,c])>10] # asi guarda las listas con los numeros mayores
print(matriz)
print("---")
matriz2 = [[a+b+c] for a in dato_1 for b in dato_2 for c in dato_3
          if a+b+c>10]
print(matriz2)

print("---")
cantidades = [1,4,6,7,8]
aumentos = [2,3,4,5,6]

cantidad_11 = [(c,a) for c in cantidades for a in aumentos if sum((c,a))==11
              if c % 2== 0 and a % 2== 1 or c%2 == 1 and a%2==0]
print(cantidad_11)
print("---")

#------------

lista = [[1,2],[3,4,5,6],[7,8,9]]

#plana = [elemento for elemento in sublista for sublista in lista]
# primero debe sacarse las sublistas o sino dara error como en este caso
plana = [elemento for sublista in lista for elemento in sublista]
print(plana)