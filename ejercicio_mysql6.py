# RECUPERAR EL VALOR AUTO_INCREMENT en un INSERT

import mysql.connector

conexion = mysql.connector.connect(host = "localhost", user = "root", passwd="on7760284", database = "bd1")

mi_cursor = conexion.cursor()
sql = "INSERT INTO articulos(descripcion, precio) values (%s, %s)"
datos = ("naranjas", 23.66)
mi_cursor.execute(sql,datos)
conexion.commit()
print("Valor del último código del artículo generado: ", mi_cursor.lastrowid) # se obtiene el auto_increment
conexion.close()

# Es importante observar el auto_increment porque aveces este es la primary key de las tablas.
