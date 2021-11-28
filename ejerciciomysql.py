import mysql.connector # modulo que permite conectarse a mySQL

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="on7760284") 
#Se llama la función connet más la clave
cursor1=conexion1.cursor() # el objeto conexion1 es de la clase connection de MySql
cursor1.execute("show databases") # le indicamos que se ejecuta y le pasamos en el parametro un comando de MySql
for base in cursor1:
    print(base)
conexion1.close()  