#Te permiten agrupar datos que pertenecen a una misma entidad
#se agrupan en corchetas {}
diccionario={"name":"ryan",
"lastname":"ray",
"nickname":"faz"}
print(diccionario)

print(type({"name":"ryan",
"lastname":"ray",
"nickname":"faz"}))

producto_biblioteca = {
    "nombre":"book",
    "cantidad": 3,
    "precio": 5.59
}
persona ={
    "primer_nombre":"oscar",
    "apellido_persona":"baena" 
}

print(type(producto_biblioteca))

print(persona.keys())   # la función keys imprime la llave de los diccionarios
print(persona.items())  # la función items imprime los datos referentes a las llaves

# la función del tambien elimina los diccionarios, o si quieres limpiarlos puedes usar clear()

productos = [
    {"name":"book", "precio":10.99}  # una lista puede contener diccionarios
    
]

# CONJUNTOS

# Los conjuntos verificcan si hay un contenido dentro del conjunto, se puede hacer
# union, intersección, diferencia, diferencia simetrica

frutas = {"manzana","naranja","manzana","pera","banana","kiwi"} # si bien hay repetidos, al crearlo solo se deja uno

"pera" in frutas
"yerba" in frutas

# para crear un conjunto vacio se utiliza set
set()

a = set("abracadabra")
b= set("alcazam")

# operaciones de conjuntos

"""a . b # devuelve las letras de a pero no en b
a | b # devuelve las letras que estan en a o en b o ambas
a & b # letras de a y b
a ^ b # letras en a o en b pero no en ambas"""

# conjuntos por compresion

a = {x for x in "abracadabra" if x not in "abc"}
a.add("z")
a.remove("z")

# son un conjunto de datos y se indexan por claves, se pueden definir de varias formas

# formas de definir

precios = {"manzana":3.5,"banana":4.5,"kiwi":6.0,"pera":9.75}
print(precios)
precios = dict(manzana=3.5,banana=4.5,kiwi=6.0,pera=3.75)
print(precios)
precios = dict([("manzana",3.45),("banana",4.5),("kiwi",6.0),("pera",3.65)])
print(precios)

# para acceder a los elementos es a traves de la clave

# agregar un numero elemento

precios["melon"]=5.75
print(precios)

# se agrego melon

# actualizar valor de un elemento

precios["manzana"] = 2.88
print(precios)

# borrar un elemento (clave-valor)

del precios["kiwi"]
print(precios)

# preguntar pertenencia

"sandia" in precios
"manzana" not in precios

# metodos

len(precios)

precios.get("melon") # obtiene el elemnto, si no existe da un none

precios.setdefault("banana") # si esxiste el valor lo devuelve, si no lo crea o devuelve un none
precios.setdefault("sandia",0.2)
print(precios)

# update actualiza el valor, si no existe lo crea

precios.update({"banana":4.0,"durazno":5.0})
print(precios)

precios.keys() # devuelve una vista con las claves del diccionario
print(precios)

precios.values() # devuelve una vista con los valores del diccionario

precios.items() # devuelve una vista del diccionario

# POP saca el elemento de la clave indicada, y se puede poner un default si no existe

print(precios.pop("manzana"))
print(precios.pop("merlon",000.0))

# cuando el elemento no este dara error

precios.popitem()

# el elemento clear borra todos los elementos del diccionario

# vistas

claves = precios.keys()
valores = precios.values()
items = precios.items()

# iteraciones de diccionarios

for fruta, precio in precios.items():
    print(fruta, "----",precio)

# las claves de los diccionarios deben ser hasheables, que significa que el valor nunca cambia en el programa y puede compararse compararse con otros objetos
# los inmutables son hasheables string, tuplas, numeros, fechas
# los mutables tuplas, conjuntos, diccionarios no son hasheables


precios = {"manzana":3.5,"banana":4.5,"kiwi":6.0,"pera":3.75,"ciruela":2.45,"durazno":4.55,"melon":7.35,"sandia":9.70,"anana":11.25}
valores = precios.values()
print(valores)



total = 0
#[2,2.5,1,3,1,2,5,10,3]"""
for i in valores:
    cantidad=  float(input("ingrese los kilos a comprar"))
    precio = cantidad * i
    total = total + precio

    print(precio,"-----------",total)    
   