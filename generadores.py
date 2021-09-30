# los generadores devuelven una secuencia, pero en vez de ejecutarla completamente
# esta lo hace pausadamente cada vez que la llamamos, por ejemplo si la llamamos la 
# primera vez solo se ejecuta una vez asi este en rango, además, no utiliza el return sino 
# el yield 

def primeros_1000():
    "Genera los primeros 1000 números"
    for x in range(1000):
        yield x

generador_primeros_100 = primeros_1000()
print(generador_primeros_100)
for x in generador_primeros_100:
    print(x)


def numeros_pares(n):
    return (x for x in range(n) if x % 2 == 0)

gen = numeros_pares(15)

gen.__next__()
gen.__next__()

print("_________________________________")
print(list(gen))

#ENTENDIENDO EL CONCEPTO GENERADORES

# Generadores son extructuras que almacenan objetos iterables y cada vez cada que 
# se solicita, entrega un valor y queda guardado en pausa.

# En una función normal, se retornan los valores y se guarda toda la
# lista de numeros pares

  


# la ventaja de los GENERADORES es que se puede trabajar con numeros infinitos, y es más eficiente.

# la eficiencia esta vista desde el tema de memoria que no se ocupa cuando no
# se llaman elementos que no se necesitan.

# Ejercicio pildoras informaticas:

# Ejemplo función normal con return
def generaPares(limite):
    
    num = 1
    mi_lista = []
    
    while num < limite:
        mi_lista.append(num*2) # El primer numero se multiplica con el 1 de num y luego sucesivamente va creciendo
        
        num = num + 1
    return mi_lista

print(generaPares(10))

# Ejemplo función con yield (generador)

def generaPares(limite):
    
    num = 1
    #mi_lista = [] --> se elimina la lista porque el generador hace ese trabajo
    
    while num < limite:
        # mi_lista.append(num*2) # se elimina tambien esto
        
        yield  num * 2 
        
        num = num + 1 # se establece como va hacer el proceso
    
# se debe crear un objeto que guarde el generador

devuelvePares = generaPares(10)

# se crea un ciclo for o while para recorrer el generador si es que quiero que vaya recorriendo todo el generador

#for i in devuelvePares:
     
 #   print(i)
    
# La gran diferencia radica en que solo se va a mostrar el numero iterador (generador)
# cada vez que sea llamado, no muestra toda la información de sopeton como la función normal


# METODO NEXT

print(next(devuelvePares)) # devolvera el primer valor
print("Aqui hay más codigo")
print(next(devuelvePares))
print("Aqui hay más codigo")
print(next(devuelvePares))

# Conclusiones - Cuando llamamos devuelvePares con la función next, se llama al generador, este se muestra, y el 
# resto de código sigue su curso, si encuentra otra llamada a devuelvePares, vuelve a mostrar el numero generado
# que sigue y vuelve el curso normal del resto del codigo, por lo que si nuestro código es muy grande, se puede usar
# esto cuando lo necesitemos, ahorrando recursos.


#                       yiel from (para listas ciclos anidados)

# yield from

# sirve para simplificar el codigo cuando se usen bucles anidados

# --> el generador puede ser un objeto de diversa indole, (int, tuplas, float, str, etc).

# --> aveces necesitaresmo acceder a esos sub elementos. ->>

# for elemento in ELEMENTOS:
#       for subElemento in elemento:

def devuelve_ciudades(*ciudades): # cuando se pone un asterisco se indica que es un numero indeterminado de elementos en forma de tupla
        for elemento in ciudades:
            yield elemento
            
ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
    
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

def devuelve_ciudades(*ciudades): # cuando se pone un asterisco se indica que es un numero indeterminado de elementos en forma de tupla
        for elemento in ciudades:
            for subElemento in elemento:
                yield subElemento
            
ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
    
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

print("------------------")
# yield FROM -UTILIZANDOLO

def devuelve_ciudades(*ciudades): # cuando se pone un asterisco se indica que es un numero indeterminado de elementos en forma de tupla
        for elemento in ciudades:
            yield from elemento # hace lo mismo que los anidados, e ingresa a la segunda instancia que desamos ver, el sub, sub indice.E
            
ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
    
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))




