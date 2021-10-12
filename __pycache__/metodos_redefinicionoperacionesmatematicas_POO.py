# Redefinir operadores matematicos

# operador (+) -> __add__(self,objeto2)
# operador (-) -> __sub__(self,objeto2)
# operador (*) -> __mul__(self,objeto2)
# operador (//) -> __floordiv__(self,objeto2)
# operador (/) -> __truediv__(self,objeto2)

# -------------------- operadores de comparación 

# operadores comparación

# operador (==) -> __eq__(self,objeto)
# operador (>=) -> __ge__(self,objeto)
# operador (<)  -> __lt__(self,objeto)
# operador (<=) -> __le__(self,objeto)
# operador (!=) -> __ne__(self,objeto)
# operador (>)  -> __gt__(self,objeto)

class Cliente:
    
    def __init__(self,nombre,monto):
        self.nombre = nombre
        self.monto = monto
    def __add__(self,objeto):
        
        s = self.monto + objeto.monto
        return s
    

cliente1 = Cliente("Ana",1200)
cliente2 = Cliente("Luis",1500)

print("el total de los depositos es ",cliente1+cliente2)

class Lista:
    
    def __init__(self,lista):
        
        self.lista = lista
        
    def imprimir(self):
        print(self.lista)
    def __add__(self,entero):
        nueva = []
        
        for i in range(len(self.lista)):
            nueva.append(self.lista[i]+entero)
        return nueva
    def __sub__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]-entero)
        return nueva

    def __mul__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]*entero)
        return nueva

    def __floordiv__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]//entero)
        return nueva
    

# bloque principal

lista1=Lista([3,4,5])
lista1.imprimir()
print(lista1+10)
print(lista1-10)
print(lista1*10)
print(lista1//10)

class Palabra:
    
    def __init__(self, lista1):
        
        self.lista1 = lista1
        
    def imprimir(self):
        
        print(self.lista1)
    
    def __add__(self, vocal):
        
        nueva_lista = []
        
        for i in range(len(self.lista1)):
            nueva_lista.append(self.lista1[i] + vocal)
        return nueva_lista
    
ejemplo = Palabra(["a","b","c"])
print(ejemplo.__add__("a") )



# Como bien se ha mencionado, los metodos __iniciados__ con dos rayas al piso y terminados igualmente, son metodos que
# se ejecutan automaticamente, por lo anterior, no es necesario en este caso, invocar el metodo __add__ para que 
# este haga la suma, no obstante si no se hace, NO darà error y si se llama el objeto.__add__(parametro) igualmente se ejecutara


# Hay que tener en cuenta que operaciones se pueden hacer con los str, con listas, tuplas, enteros y floats


class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __eq__(self, objeto2): # entra el atributo de un dato de otro objeto
        
        if self.edad == objeto2.edad:
            return True
        else:
            return False
    def __ne__(self, objeto2):
        
        if self.edad != objeto2.edad:
            return True
        else:
            return False
        
    def __gt__(self,objeto2):
        
        if self.edad > objeto2.edad:
            return True
        else:
            return False
    def __lt__(self,objeto2):
        
        if self.edad < objeto2.edad:
            return True
        else:
            return False

camila = Persona("Camila",25)
oscar = Persona("Oscar",26)

print(camila.__lt__(oscar)) # se puede llamar de esta manera, y automaticamente compara los objetos

persona1=Persona('juan',22) 
persona2=Persona('ana',22)
if persona1==persona2: # o se puede llamar de esta forma, en la que se evidencia una simple comparación, pareciera
                       # que no hiciera nada, pero automaticamente, se esta comparando el atributo edad. 
    print("Las dos personas tienen la misma edad.")
else:
    print("No tienen la misma edad.")
    
class Persona1:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

ejemplo1 = Persona1("Oscar",26)
ejemplo2 = Persona1("Camila",26)

if ejemplo1 == ejemplo2: # en este caso si hacemos la comparación, estamos buscando que compare las edades, sin embargo
                         # el programa compara inmediatamente son los objetos completos, incluido el atributo nombre
    print(" iguales las edades")
else:
    print(" edades no iguales")

if ejemplo1.edad == ejemplo2.edad: # aqui se llama diretamente a los atributos, sin embargo, para algunos casos es mejor utilizar el metodo
                                    # especial que compara los objetos. Hay que aprender cuando se utiliza
    print("IGUALES")
else:
    print("LAS EDADES SON DIFERENETS")


# COMPARANDO TUPLAS - (se compara la tupla en total, no el index 1, el ejemplo no aplica )
juan = ("juan",5)
oscar = ("o",5)

if juan == oscar:
    print("si es")
else:
    print("no es")

