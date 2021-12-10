# CREACIÓN DE UNA BASE DE DATOS

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="on7760284") # no se muestra la base de datos porque la idea es solo ingresar a mysql
cursor1=conexion1.cursor() # se crea cursor
sql="create database bd2" # se cre la sentencia
cursor1.execute(sql) # se ejecuta

sql="use bd2" # se ingresa a la base de datos creada
cursor1.execute(sql)

# se crea nuevamente la sentencia para crear la tabla usuario

sql="""create table usuarios (
         nombre varchar(30) primary key,
         clave  varchar(30)
   )"""
cursor1.execute(sql)    

conexion1.commit()
conexion1.close()