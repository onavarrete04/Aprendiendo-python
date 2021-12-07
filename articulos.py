import mysql.connector

class Articulos:
    
    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="on7760284", 
                                              database="bd1")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consultal(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        consulta = cursor.fetchall()# si no se coloca la consulta antes de cerrar la base de datos, dara una lista vacia
        cone.close()
        
        return consulta
        

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        consulta = cursor.fetchall()
        cone.close()
        return consulta
    def borrando(self,datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM articulos WHERE codigo = %s"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    
    def modificando(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        print(cursor.rowcount)
        return cursor.rowcount # retornamos la cantidad de filas modificadas