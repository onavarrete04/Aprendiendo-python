import unittest
from unittest.case import TestCase

class EnterosRomanos:
    def numeros_romanos(self, numero_ingresado):
        romanos = ["M","CM","D","C","L","X","V","IV","I"]
        enteros = [1000,900,500,100,50,10,5,4,1]
        # Para el algoritmo se escriben los números primero de mayor a menor, para que pueda hacer la iteración
        
        respuesta = "" # la respuesta comienza vacia
        i = 0          # el iterador comienza en 0

        while numero_ingresado>0: # si el numero ingresado es mayor que cero el ciclo continua
            
            
            for elemento in range(numero_ingresado//enteros[i]): 
    # En este elemento se le esta haciendo una división que de un número entero, si el número que da es 0, pues no entra al ciclo
    # si el número que da es 1 pues entra al ciclo, toda división entera, donde el dividendo sea menor que el divisor, dara cero si se divide como entero


                respuesta +=  romanos[i]    # cada vez que se permita entrar al ciclo, se va sumar hasta una vez la letra que se encuentre en ese index
                numero_ingresado = numero_ingresado - enteros[i]  # posteriormente, se va a restar el numero ingresado - la lista(index) en el que se encuentre el numero, con el fin de ir disminuyendo el valor



            i= i + 1 # fuera del ciclo el iterador se ira aumentando, para que vaya mirando en la lista enteros un index mayor
        
            
        return respuesta 

class NumerosRomanosTest(unittest.TestCase):
    def setUp(self):
        self.objeto_enteros_romanos = EnterosRomanos() 

    def test_uno_to_romano(self):
        local_enteros_romanos = self.objeto_enteros_romanos.numeros_romanos(1)        
        self.assertEqual("I",local_enteros_romanos)
    def test_dos_to_romano(self):
        local_enteros_romanos = self.objeto_enteros_romanos.numeros_romanos(5)        
        self.assertEqual("V",local_enteros_romanos)
    def test_tres_to_romano(self):
        local_enteros_romanos = self.objeto_enteros_romanos.numeros_romanos(10)        
        self.assertEqual("X",local_enteros_romanos)
    def test_cuatro_to_romano(self):
        local_enteros_romanos = self.objeto_enteros_romanos.numeros_romanos(50)        
        self.assertEqual("L",local_enteros_romanos)
    def test_cinco_to_romano(self):
        local_enteros_romanos = self.objeto_enteros_romanos.numeros_romanos(100)        
        self.assertEqual("C",local_enteros_romanos)
    def test_siete_to_romano(self):
        local_enteros_romanos = self.objeto_enteros_romanos.numeros_romanos(500)        
        self.assertEqual("D",local_enteros_romanos)
    def test_ocho_to_romano(self):
        local_enteros_romanos = self.objeto_enteros_romanos.numeros_romanos(1000)        
        self.assertEqual("M",local_enteros_romanos)
    def test_nueve_to_romano(self):
        local_enteros_romanos = self.objeto_enteros_romanos.numeros_romanos(900)        
        self.assertEqual("CM",local_enteros_romanos)
    
prueba = EnterosRomanos()
prueba.numeros_romanos(900)  


    
if __name__ == '__main__':
    unittest.main()

# __name__ cuando la variable name se ejecuta dentro del mismo script da un resultado "__main__"
# asi, cuando le estamos indicando __name__ == "__main__" estamos diciendo
# si te ejecutas dentro del mismo script, haz esto, sino pues no

# si llegase a importarce ejercicio_test1 a otro script, cuando se ejecute esa importación desde ese otro
# script, arrojara el nombre del scrit ejercicio_test1
        
        


