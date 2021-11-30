# RECUPERAR TODAS LAS FILAS DE UNA TABLA

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost",user="root",passwd="on7760284",database="bd1")

miCursor = conexion1.cursor()
miCursor.execute("SELECT codigo, descripcion, precio FROM articulos")

# se realiza un ciclo for para mostrar la lista por lineas
for i in miCursor: # i es el iterador de cada fila
    print(i)
print("------")
print(miCursor) # si se imprimiera miCursor, se mostraria la sentencia execute del código.
miCursor.close()