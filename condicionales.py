#vamos a ver el condicional if y el else
# los condicionales se comparan en tre si para que de como resultado un boleano
#esto nos permite recrear rutas para realizar determinados procedimientos
x = 2
if x >= 0:
    print("el numero es mayor o igual",x)
else:
    print("el numero es menor",x)
a = 1
if a>0:
    print(a,"es mayor o igual a 0")
elif a<0:
    print(a,"es un numero negativo")
else:
    print("el numero es igual a 0")
# anidación de condicionales
z=2
if z > 0:
    print(z, "z es mayor")
else:
    if z < 0:
         print("el numero",z,"es negativo")
    else:
         print("el numero es igual a 0")

s = 40

if s < 30:
    print(s," es menor que 30 ")
elif s > 30:
    print(s,"es mayor que 30")

color = "red"
if color == "Red" or "red":
    print("su color favorito es ",color)
elif color != "Red" or "red":
    print("su color favorito no es red, es ",color)

x = int(input("ingresa un entero por favor: "))

if x < 0: 
    print("Numero negativo cambiado a cero ")
elif x==0:
    print("cero")
elif x ==1:
    print("El numero es mayor que 0")
else:
    print("Más")

# Sentencias For

#La sentencia for difiere de los lenguajes como C, en leguar de iterar sobre una preogresión
#aritmetica (como pascal) o darle al usuario definir tanto el paso de la iteracion como la condición
# (como en C) la sentencia for en python itera sobre los items de cualquier secuencia (una lista o cadena de texto)

palabras = ["Gato","Perro","Burro","Pericotesco"]

for p in palabras:  
    print(p, len(p)) # En este caso la variable p, es cada string y len cuenta cuantos cracteres tiene cada string

for p in palabras[:]: # hace una copia de la palabra y la vuelve a meter a la lista en la primera posición
        if len(p)>6:
            palabras.insert(0,p) # se supone que esto crearia una lista infinita
print(palabras)

for i in range(5):
    print(i)
a = ["Mary","tenia","un","corderito"]
for i in range(len(a)):
    print(i,a[i])


# sin embargo conviene mas utilizar la función enumerate sin embargo no he abordado esta info
# For itera sobre cualquier objeto, y son utiles para repetir uns sentencia sobre algo determinada

for i in range(10):
    print(i)

# sentencias break

# la sentencia break termina el lazo de for o while, es decir, rompen el ciclo y hace el salto para encontrar otro tipo de sentencia.
# se dice que termina el ciclo mas anidado


# Sentencia else

# la sentencia else da otra condicion u otra opcion, casi siempre es para for y while, pero no sirve cuando termina en la sentencia break
# se entiende como un sino

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, "es un numero par",x,"*", n/x)
            break
    else:
        # sigue el bucle sin encontrar un factor
        print(n, " es un numero primo")

for num in range(2,10):
    if num % 2 == 0:
        print("Encontre un numero par", num) # en este caso busca numeros pares
        continue # continua con la siguiente iteración del ciclo si no se cumple la primera sentencia
    print("encontre un numero", num)

# Iteradores

# los iteradores son tipos dedatos que pueden ser recorridos secuencialmente por el ciclo for
# para esto, los objetos deben responder los mensajes __iter__  y  __next__
# __iter__ devuelve un iterador que debe ser un objeto que sepa responder el mensaje __next__
# __next__ devuelve el proximo elemento de la secuencia
lista = ["a",2,3,4,5,"b"]

for x in lista:
    print(x)
# las listas son objetos iterables, las tuplas noooooo
# lo que primero hace el ciclo for es llamar la funcion iter() del contenedor o iterable
# esta función devuelve un objeto iterado que define el metodo __next__ que accede a los elementos del contenedor
# uno a la vez, cuando no hay mas elementos, la función __next__ se levanta una excepción
# StopIteration que le avisa al ciclo for que debe terminar

# entonces se habra que definir una CLASE que defina los metodos
# __iter__ y __next__, en el caso de iter si la misma clase tiene definido el metodo next
# alcansa que devuelva self (se devuelva a si misma).
# el metodo next debera contener logica para acceder al siguiente elemento
# iter y next son metodos magicos y comienzan con guien abajo, y estos son llamados por python
# los elementos magicos son llamados eventualmente por python y no son manuales


# creando una clase que devuelva de atras para delante

# class Reversa:
#     """ Iterador para recorrer una secuencia de atras para delante ."""
#     def __init___(self,datos):
#         self.datos = datos
#         self.indice = len(datos)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.indice == 0:
#             raise StopIteration()
#         self.indice=self.indice -1
#         return self.datos[self.indice]
class Reversa:
    """Iterador para recorrer una secuencia de atrás para adelante."""
    def __init__(self, datos):
        self.datos = datos
        self.indice = len(datos)
    def __iter__(self):
        return self
    def __next__(self):
        if self.indice == 0:
            raise StopIteration()
        self.indice = self.indice - 1
        return self.datos[self.indice]

for elemento in Reversa([1,2,3,4,5]):
    print(elemento)




# Continue

#La sentencia continue continua con la siguiente iteración sin ejecutar las sentencias que quedan debajo


# Pass

# la sentencia pass no hace nada, se puede usar cuando una sentencia es requerida por la sintaxis pero no por el programa

""" while True:
    pass # Espera ocupada hasta una interrupción de teclado ctrl+c """

def initlog(*arg):
    pass #Acuerdate de implementar esto -> (mo de ejemplo del pass)
