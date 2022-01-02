import sqlite3 # en mysql se conecta es mysql.connector

conexion1 = sqlite3.connect("PrimeraBase")
cursor = conexion1.cursor()
#sql = "CREATE TABLE book( ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT, PRICE INTEGER, PAGES INTEGER)"
#cursor.execute(sql)

cursor.execute("SELECT * FROM book ")

for i in cursor:
    print(i)
variable = cursor.fetchall()# se almacenara un lote de registros para leerlos

conexion1.commit()

conexion1.close()