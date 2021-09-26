# una clase es un molde que agrupa varias (funciones / metodos) y atributos (variable)
#  un atributo es como una variable o un dato, puede ser un entero, un str, un float, etc.
# metodo es una función especifica que cumple su rol, por ejemplo sumar, dividir, etc.

class Alumno: # molde para hacer alumnos
    def iniciar(self, nombre, nota): # el atributo self se refiere a los objetos, por eso es importante.
        self.nombre = nombre 
        self.nota = nota
    def imprimir(self):
        print(self.nombre, self.nota)
    def mostrar(self): # aqui pasa el objeto completo
        
        if self.nota > 8: # aqui el objeto completo llama a su atributo nota y es evaluado en la condicional
            print("Esta bien la nota")
        elif self.nota >= 4 and self.nota < 8:
            print("Esta regular la nota")
        else:
            print("Va perdiendo")

# Objeto 1
    
alumno1 = Alumno()
alumno1.iniciar("Angela",8.5)
alumno1.imprimir()
alumno1.mostrar()

# Objeto 2

alumno2 = Alumno()
alumno2.iniciar("Oscar",6.2)
alumno2.imprimir()
alumno2.mostrar()


class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def imprimir(self):
        print("El nombre de la persona es ",self.nombre)
        print("La edad de la persona es ",self.edad)
    def mayor_edad(self):
        if self.edad >= 18:
            print(self.nombre," es mayor de edad")
        else:
            print(self.nombre," es menor de edad")

 # objetos   
persona1 = Persona("Camila",25)
persona1.imprimir()
persona1.mayor_edad()

persona2 = Persona("Oscar",26)
persona2.imprimir()
persona2.mayor_edad()

persona3 = Persona("Juan Camilo", 12)
persona3.imprimir()
persona3.mayor_edad()

# Conclusión: el atributo self siempre va a hacer referencia al objeto, los cuales ya llevan 
# sus atributos, y por eso es importante, y en estos ejemplos, no se hace necesario
# llamar más varialbes, debido a que ya sabemos que un objeto tiene dos atributos, y ese
# es el que se va a mostrar, comparar, imprimir, etc, según sea la funcionalidad que tenga el metodo.

# Variable __init__

# es importante porque "inicializa" el codigo indistintamente, ya python la reconoce y hace
# la inicialización sin que sea necesario llamarla en los objetos, esto ayuda para que
# no se nos olvide hacerlo, pero puede que otros programadores cambien este metodo __init__
# por una palabra como inicializar, inicio, etc, aunque no es recomendable porque ya es un
# estandar dentro del lenguaje de python, puede ser que en otros lenguajes esto pueda suceder o ser distinto
# sin embargo en python se estandarizo para que no haya confusion, y que python haga esta
# tarea automaticamente. 

# En sintesis, las clases sirven para reducir codigo, pero es importante entender el self y el __init__
# para poder practicar, si ya sabemos que el self va a ser referencia al objeto (sea este el 1, 2, 3, etc)
# ya entendemos que cada atributo es de ese objeto y no hay confusión. Y el __init__ es para
# facilitar el trabajo.