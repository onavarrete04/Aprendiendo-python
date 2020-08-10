# para usar rebanado de cadenas y operaciones de concatenado podras crear cualquier forma que puedas imaginar
# los estring pueden manejar cadenas para determinar su ancho y la otra forma es

# formatted string literals o str.format()

# El modulo string contine la clase string.Template que ofrece una formula para sustituir valores en cadenas.

# ¿como convertir valores en cadenas? python tiene la forma de hacerlo con la funcion repr() o str(
# 
# La función STR devuelve representaciones de valores que son mas legibles para los humanos

# La funcion Repre() genera representaciones que pueden ser leidas por el interprete

# entonces cuando la representación no haya sido para ser leida por humano, lanzara el repre()

s = "Hola mundo"

print(str(s))

print(repr(s))

print(str(1/7))

print(repr(1/7))

x = 10 * 3.25
y = 200 * 200

s = "El valor de x es "+repr(x)+", y es " + repr(y)+"..."
print(s)


# dos maneras de escribir una tabla de cuadrados y cubos, ejemplo

# a)
# str.rjust() ordena una cadena a la derecha en un campo del ancho
# str.ljust() y str.ljust son metodos similares

# puedes agregar una opcion de rebanado si la lista es larga:
# x.ljust(n)[:n]

#str.zfill() rellena una cadena numerica con ceros a la izquierda

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), end=" ") 

    print(repr(x*x*x).rjust(4))

# b)
for x in range(1,11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x*x,x*x*x))
# str.format indica a que lugar deseas pasar cada dato, en este ejemplo aparecen los datos
# {0}{1}{2} y luego le indica la cantidad de digitos o ceros a la izquierda {0:2d}

contenido = "aguilas"

print("mis aerodeslizador esta leno de {}".format(contenido))

print("mi aerodeslizador esta lleno de{!r}".format(contenido))

# !a = aplica para alply()
# !s = aplica para str()
# !r = aplica para repr()

import math

print("El valor de PI es aproximadamente {0:.3f}".format(math.pi))

tabla = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for nombre, telefono in tabla.items():
    print('{0:10} ==> {1:10d}'.format(nombre, telefono))

#Si tenés una cadena de formateo realmente larga que no querés separar, podría ser bueno que puedas hacer referencia a
#las variables a ser formateadas por el nombre en vez de la posición. Esto puede hacerse simplemente pasando el diccionario
#y usando corchetes '[]' para acceder a las claves

tabla = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    'Dcab: {0[Dcab]:d}'.format(tabla))

tabla = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; '
    'Dcab: {Dcab:d}'.format(**tabla))

# Viejo formateo de cadenas

import math
print("El valor de PI es aproximadamente %5.3f" % math.pi)

h = open("archivodetrabajo","w") # el primer caracter es el nombre del archivo, y el segundo, la forma como sera usado
"print(f)"

r = " El archivo solo sera leido"
w = "para solo escribirlo (un archivo con el mismo nombre sera borrado)"
a = "abre el archivo para gregarle información, cualquier dato sra añadido automaticamente"
r+= "abre el archivo tanto para leerlo como para escribirlo"
b = "se abrira en modo binario"

# al finalizar una linea se agrega \n, esto puede corromper los archivos binarios, asi que acuerdate de abrirlos bien

"""with open("archivodetrabajo") as f:
    datos_leidos = f.read()
print(f.closed)"""

# cuando el metodo es cerrado sea por with o por f.close() si lo intentas abrir nuevamente fallara automaticamente



# METODOS DE LOS OBJETOS ARCHIVO

# el 

"f.read()"

# formato JSON

# PERMITE ENVIAR INFORMACIÓN MAS COMPLEJA Y OBTENER INFORMACIÓN NUMERICA DE FORMA JERARJICA

import json

json.dumps([1,"simple","lista"]) # crea una lista con la función dumps

json.dump(x,f) # dump serializa un objeto a un archivo de texto, asi que si f es un objeto archivo de texto haremos esto

x = json.load(x,f)

with open("/home/oscar/Escritorio/PYTHON APRENDER 1/ejemplo.txt" , "r") as a_file:
 	print(a_file.read())  # la función read lee todo el contenido del archivo

with open("/home/oscar/Escritorio/PYTHON APRENDER 1/ejemplo.txt" , "r") as a_file:
	print(a_file.readlines()) # readlines lee todo linea a linea, y lo muestra como una lista.

with open("/home/oscar/Escritorio/PYTHON APRENDER 1/ejemplo.txt" , "r") as a_file:
 	print(list(a_file))   # genera una lista con la función list

with open("/home/oscar/Escritorio/PYTHON APRENDER 1/ejemplo.txt" , "r") as a_file:
	for line in a_file: # el for recorre linea a linea 
 		print(line)
with open("/home/oscar/Escritorio/PYTHON APRENDER 1/ejemplo.txt" , "w") as a_file: 
    a_file.write("hola munda") # es una forma de escribir con la función write, pero cabe decir que borral o que ya esta escrito en el documento
with open("/home/oscar/Escritorio/PYTHON APRENDER 1/ejemplo.txt" , "w") as a_file:
    a_file.writelines(["linea1.\n","linea2.\n","linea3.\n"]) # escribir muchas lineas en un archivo

with open("/home/oscar/Escritorio/PYTHON APRENDER 1/ejemplo.txt" , "a") as a_file:
    a_file.write("Hola mundo") # escribir un string en el archivo agregandolo a la linea final

json.dumps([1,2,3])