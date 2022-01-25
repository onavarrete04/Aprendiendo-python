# Recupera datos de un archivo json generado en un servidor de internet accediendo
# a una base mysql por php

from urllib import request
import json

pagina = request.urlopen("http://localhost/pythonya/retornararticulos.php")
datos = pagina.read().decode("uft-8")
print(datos)
print("-"*10)

lista = json.loads(datos) # convertimos los datos en lista
print(lista) # mostramos la lista
print("-"*10)

for elemento in lista:
    print(elemento)


    
