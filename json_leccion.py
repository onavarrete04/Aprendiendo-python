# El formato json puede transformar en python a un diccionario

import json 


cadena = """{
    "codigo":"1",
    "descripcion":"papas",
    "precio":"13.45"
}
"""

print(cadena) # imprimimos un string
diccionario = json.loads(cadena) #-> convierte este string en un diccionario
print(diccionario)

# vector: vector o arreglo es igual a listas que contienen elementos

cadena1 = """
[
    {
        "codigo":"1",
        "descripcion":"papas",
        "precio":"14.45"
    },
    {
        "codigo":"2",
        "descripcion":"manzanas",
        "precio":"45"
    }
]

"""
# no se debe poner , al ultimo elemento, o sino se entenderá que esta esperando un elemento adicional


print(cadena1) # Muestra el string
lista=json.loads(cadena1) # convierte el estring en una lista que contiene diccionarios
print(lista)
