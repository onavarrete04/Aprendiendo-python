# una actividad de un programa es el almacenañamiento y recuperación de datos almacenados

# modos de almacenar (archivos de texto, binarios, bases de datos, etc)

archivo_1 = open("datos.txt","w") # 
# para crear el archivo se utiliza la función open
# se pasan dos parametros, el primero es el nombre del archivo
# el segundo es "w" indica que se crea un archivo de texto
# si haya un archivo con el mismo nombre, se crea uno nuevo y se borra el otro

archivo_1.write("Primera línea. \n")
archivo_1.write("Segunda línea. \n")
archivo_1.write("Tercera línea. \n")
archivo_1.close() # se cierra obligatoriamente para que otro programa interactue con el archivo
# es una tarea que no se debe olvidar

# leer el archivo

archivo_1 = open("datos.txt","r") # read
contenido = archivo_1.read() # en la función read
# podemos pasar un entero con la cantidad de texto (str) que queremos leer, 
# si le pasamos un 1, va imprimir una P de primera linea, si pasamos un 6, casi la cadena de primera
# si lo dejamos vacio muestra todas los caracteres  y string dentro del documento


print(contenido)
archivo_1.close()

# leer el archivo linea a linea



archivo_1 = open("datos.txt","r")
linea = archivo_1.readline() # se lee la primera linea del archivo
while linea != "":
    print(linea, end="")
    linea = archivo_1.readline() # se lee la linea segunda, y se va actualizando

archivo_1.close()

# guardar lineas de texto en una lista


archivo_1 = open("datos.txt","r") # se abre el archivo
linea_1 = archivo_1.readlines() # la función readlineas crea una lista

print("El archivo tiene", len(linea_1), "lineas") # como ya esta creada la lista, con la función len
# se cuentan los elementos de la lista - especificamente cada linea
print("contenido del archivo")

for i in linea_1: # se itera dentro de la lista, accediendo a cada elemento de la lista
    # la i se convierte en el index que lama a cada elemento de la lista
    print(i, end="")
print(linea_1) # se hace la prueba de impresión de la lista completa
archivo_1.close()


# ABRIR ARCHIVO Y AGREGAR LINEAS

# para abrir el archivo sin que se borren las lineas ya existentes
# se abre con la "a" de append

archivo_1 = open("datos.txt","a")
archivo_1.write("nueva linea 1 ejemplo \n")
archivo_1.write("nueva linea 2 ejemplo \n")
archivo_1.write("nueva linea 3 ejemplo \n")
archivo_1.close()

archivo_1 = open("datos.txt","r")
leer = archivo_1.read() # hay que crear un objeto que lea el contenido
print(leer)
archivo_1.close()

# ABRIR ARCHIVO LEER Y AGREGAR DATOS

archivo_1 = open("datos.txt", "r+")
contenido = archivo_1.read()
print(contenido)
archivo_1.write("Otra otra linea 1 \n")
archivo_1.write("Otra otra linea 2 \n")
contenido = archivo_1.read() # no lee otra vez el archivo
print(".....")
print(contenido) # no lee lo nuevo del archivo
archivo_1.close()

# hay que abrir nuevamente el archivo para leer lo nuevo agregado

archivo_1 = open("datos.txt", "r+") # permite agregar y leer el archivo
contenido = archivo_1.read()
print(contenido)


# CODIFICACIÓN DE CARACTERES UTF-8
print("-------"*5)
archivo_1 = open("datos.txt","w", encoding="utf-8") # como se abrio nuevamente el archivo con la w
# el contenido anterior del archivo se borro en su totalidad
archivo_1.write("Primera línea. \n")
archivo_1.write("Segunda línea. \n")
archivo_1.write("Tercera línea. \n")
archivo_1.close()
archivo_1 = open("datos.txt", "r")
contenido = archivo_1.read()
print(contenido)
archivo_1.close()