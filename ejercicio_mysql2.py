import mysql.connector

conexion1 = mysql.connector.connect(host="localhost",user="root",passwd="on7760284",database="bd1")

cursor1 = conexion1.cursor() #

cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close()