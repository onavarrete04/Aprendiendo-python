import unittest

class Registradora:
    
    def __init__(self):
        """
            Se inicializa la lista vacia en esta instancia, con el fin de que los productos puedan guardarse correctamente por usuario
            Igualmente se deja el diccionario productos con 5 elementos, podrían agregarse más si se desea, este diccionario podría ir
            también como variable global, pues es un elemento compartido por todos los usuarios
        """


        self.productos = {1:("piña",15.33),2:("mango",11.23),3:("limón",13.33),4:("banano",18),5:("sandia",20.13)}
        self.lista_producto = []

        

        print("MENU")
        print("CODIGO - PRODUCTOS - PRECIO")
        print(" ")
        for i in self.productos:
            print(i,self.productos[i])

        print(" ")
        
        
        
    
    def cargar_productos(self, codigo):
        
        self.codigo = int(codigo)
        if self.codigo in self.productos:
            self.lista_producto.append(self.productos[self.codigo])
            return self.lista_producto
        else:
            print("Verifique el listado de productos")       
    
    def calcular_precio(self):
        
        nombre_productos = ""
        precio_productos = 0

        for i in range(len(self.lista_producto)):
            nombre_productos += "| " + self.lista_producto[i][0] + " | "
            precio_productos += self.lista_producto[i][1] 
            
        if nombre_productos != "":
            print("Gracias por su compra, sus productos son :")
            print("----"*8)
            print(nombre_productos)
            print("----"*8)
            print("Total: ")
            print(precio_productos)
            print("--")
            resultado = (nombre_productos, precio_productos)
            return resultado
            
        
       

"""
# PRUEBA POR CONSOLA 

registradora1 = Registradora()
registradora1.cargar_productos(1)
registradora1.cargar_productos(5)
registradora1.calcular_precio()"""


class Test(unittest.TestCase):
    def setUp(self):
        self.objeto_registrador = Registradora()

    # 1. Test de carga de productos individuales    
    def test_carga1(self):
        local_prueba_registradora = self.objeto_registrador.cargar_productos(1)
        self.assertEqual([('piña', 15.33)],local_prueba_registradora)
    def test_carga2(self):
        local_prueba_registradora = self.objeto_registrador.cargar_productos(2)
        self.assertEqual([('mango', 11.23)],local_prueba_registradora)
    def test_carga3(self):
        local_prueba_registradora = self.objeto_registrador.cargar_productos(3)
        self.assertEqual([('limón', 13.33)],local_prueba_registradora)
    def test_carga4(self):
        local_prueba_registradora = self.objeto_registrador.cargar_productos(4)
        self.assertEqual([('banano', 18)],local_prueba_registradora)
    def test_carga5(self):
        local_prueba_registradora = self.objeto_registrador.cargar_productos(5)
        self.assertEqual([('sandia', 20.13)],local_prueba_registradora)
    def test_caja1(self):
        local_prueba_registradora = self.objeto_registrador.cargar_productos(1)
        local_prueba_registradora = self.objeto_registrador.cargar_productos(2)
        local_prueba_registradora = self.objeto_registrador.calcular_precio()
        self.assertEqual(('| piña | | mango | ',26.560000000000002), local_prueba_registradora)

        # 2. Test de suma de la Caja
    def test_caja2(self):
        local_prueba_registradora = self.objeto_registrador.cargar_productos(3)
        local_prueba_registradora = self.objeto_registrador.cargar_productos(4)
        local_prueba_registradora = self.objeto_registrador.calcular_precio()
        self.assertEqual(('| limón | | banano | ',31.33), local_prueba_registradora)
    def test_caja3(self):
        local_prueba_registradora = self.objeto_registrador.cargar_productos(1)
        local_prueba_registradora = self.objeto_registrador.cargar_productos(5)
        local_prueba_registradora = self.objeto_registrador.calcular_precio()
        self.assertEqual(('| piña | | sandia | ',35.46), local_prueba_registradora)




if __name__ == "__main__":
    unittest.main()
