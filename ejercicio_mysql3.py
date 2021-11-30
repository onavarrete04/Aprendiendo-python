
# INSERTAR FILAS EN UNA TABLA DE LA BASE DE DATOS BD1 - tabla articulos.

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost",user = "root", passwd="on7760284",database="bd1")

cursor1 = conexion1.cursor() # cursor es como un puntero que nos va a permitir hacer 
# las consultas, pero al mismo tiempo, manipular los datos
sql = "insert into articulos(descripcion,precio) values (%s,%s)"
datos=("naranjas",24.50)
cursor1.execute(sql, datos) # por ejemplo aqui estamos creando las consultas, y estamos pidiendole, que mande dos parametros
# el primer paramatro envia la variable sql que envia las instrucciones a la base de datos
# el segundo envia los datos en forma de tupla para almacenar
datos=("peras", 34)
cursor1.execute(sql,datos) # enviar dos parametros y se va actualizando los datos.
datos=("bananas",25.1)
cursor1.execute(sql,datos)
conexion1.commit() # es importante hacer el commit, porque confirma de manera
# los cambios sean permanentes en la base de datos
conexion1.close() #