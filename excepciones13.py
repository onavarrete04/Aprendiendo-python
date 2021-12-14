import mysql.connector

try:
    conexion1 = mysql.connector.connect(host = "localhost", user="root", passwd = "on7760284", database = "bd1")
    cursor = conexion1.cursor()
    sql = "select + from articulos"
    cursor.execute(sql)
    for linea in cursor:
        print(linea)
except mysql.connector.errors.ProgrammingError: #ProgrammingError se encuentra en el modulo de mysql.connector.errors
    print("ERROR EN COMANDO SQL")
finally:
    conexion1.close()
    print("Conexión cerrada - Saludos!")