# BORRAR UNA TABLE y CREAR UNA CON EL MISMO NOMBRE

import mysql.connector

conexion1 = mysql.connector.connect(host = "localhost", user = "root", passwd = "on7760284", database= "bd2")
cursor1 = conexion1.cursor()
sql = "drop table if exists usuarios"
cursor1.execute(sql)

# crear tabla

sql = """create table usuarios(
    nombre varchar(30) primary key,
    clave varchar(30)
)
"""
cursor1.execute(sql)
conexion1.commit()
conexion1.close()