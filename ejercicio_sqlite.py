# Se guarda en host, es muy eficiente y rapido, multiplataforma
# sin administración, es de dominio público.

# no admite clausulas anidades where, no existen usuarios
# falta de clave foranea cuando se crea en consola


"""
Pasos de conexión:

Crear conexion
crear puntero
ejecutar query
manejar resultados de la query
cerrar puntuero
cerrar conexion
"""

import sqlite3 # en mysql se conecta es mysql.connector

conexion1 = sqlite3.connect("PrimeraBase")
cursor = conexion1.cursor()
#sql = "CREATE TABLE book( ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT, PRICE INTEGER, PAGES INTEGER)"
#cursor.execute(sql)

"""
se puede hacer los siguientes

varios_datos = [
    (1,'title1',20,100),
    (2,'title2',220,300)
    (3,'title3',10,1100)

]
micursor.executemany("INSER INTO book VALUES(?,?,?,?)",varios_datos)
"""

cursor.execute("DELETE FROM book WHERE ID = 2")

conexion1.commit()

conexion1.close()


"""
Metodos más importantes conexion a ases de datos

conexion -> conecta
commit -> certifica que los cambios implementados se guarden definitavmente
rollback -> revierte lo ultimo hecho en comit
close -> cierra automaticamente la base de datos
execute -> atajo que crea cursor y envia parametros
execute many -> crea cursor
create function -> se crea una función creada por uno mismo
finalize -> devuelve datos str, int, y otros


"""