# INSERCCIÓN DE MULTIPLES FILAS EN UNA TABLA

# executemany 

# executamany sirve para insertar multiples filas

import mysql.connector

conexion1 = mysql.connector.connect(host = "localhost", user = "root", passwd = "on7760284", database = "bd1")

cursor1 = conexion1.cursor()
sql = "INSERT INTO articulos (descripcion, precio) values (%s, %s)"

filas = [("pepinos", 33.21),
 ("bananas",34), 
 ("Aji", 12.11),
 ("peras",21),
 ("sandía", 19.60)  ]
cursor1.executemany(sql,filas)
conexion1.commit()
conexion1.close()

# Si se llegara a usar cursor1.lastrowid devolveria solo el auto_increment del ultimo
# articulo ingresado