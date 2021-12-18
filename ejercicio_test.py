class NumerosRomanos:
    diccionario = {1:"I",2:"II",3:"III",4:"IV",5:"V",
                        6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X",
                        50:"L",100:"C",500:"D",1000:"M"}
    def __init__(self):
        
        self.numero = (input("ingrese el número que desa convertir a número romano"))
        
            
    def calcular(self):

        opcion = int(self.numero)  
        if opcion <=10:
            self.resultado = self.diccionario[opcion]
            return self.resultado
        if opcion >10 and opcion <20:
            segundo_numero = self.numero[1]
            self.resultado = "{0}{1}".format(self.diccionario[10],self.diccionario[int(segundo_numero)])
            return self.resultado
        if opcion > 20 and opcion <30:
            segundo_numero = self.numero[1]
            self.resultado = "{0}{1}{2}".format(self.diccionario[10],self.diccionario[10],self.diccionario[int(segundo_numero)])
            return self.resultado
        if opcion > 30 and opcion <40:
            segundo_numero = self.numero[1]
            self.resultado = "{0}{1}{2}{3}".format(self.diccionario[10],self.diccionario[10],self.diccionario[10],self.diccionario[int(segundo_numero)])
            return self.resultado
            
    def mostrar(self):
        print("el resultado es ",self.resultado)
        


prueba1 = NumerosRomanos()
prueba1.calcular()
prueba1.mostrar()


# Se concreta que no puede hacerse el ejercicio del test de esta manera, porque no es optima
# y no se lograria realizar ni el programa de manera optima, ni tampoco los test
# porque no serian sencillos