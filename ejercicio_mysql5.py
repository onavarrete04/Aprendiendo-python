# BORRAR y modificar datos en un mysql

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost",user ="root", passwd ="on7760284", database="bd1")

miCursor = conexion1.cursor()

# SENTENCIAS DE MYSQL
miCursor.execute("DELETE FROM articulos WHERE codigo = 6")
miCursor.execute("UPDATE articulos SET precio = 50 WHERE codigo = 3")
conexion1.commit() # se hace  directamente con la variable conexion
miCursor.execute("SELECT codigo, descripcion, precio FROM articulos")

for fila in miCursor:
    print(fila)
miCursor.close()