
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

personas [["Jorge",36],["Silvia",24]]