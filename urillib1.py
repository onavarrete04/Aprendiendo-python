# La libreria urllib es una libreria que permite conectarse a internet

# request es el primer metodo que permite acceder a internet

from urllib import request

pagina = request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html")
# modulo request e importar metodo urlopen, este retorna un objeto "HTTPResponse" y almaciena en la variable pagina
datos = pagina.read() # recupera el contenido de la variable pagina para leerlos, recupera datos en bloque de bytes
print(datos) # los leemos


print("---"*9)

# Convertir bloque de bytes a "UTF-8" se utiliza metodo decode

pagina = request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html")
datos = pagina.read()
datosutf8 = datos.decode("utf-8")
print(datosutf8)

# Lectura de pagina y posterior grabación en archivo local

from urllib import request

pagina = request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html")
datos = pagina.read()
archivo = open("pagina1.html","wb") #
archivo.write(datos)
archivo.close

imagen = request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/imagen1.jpg")
datos = imagen.read()
archivo2 = open("pagina.png","wb") #
archivo2.write(datos)
archivo2.close()

# --------------------------------------

# Error

"""
Si el recurso no se encuentra o si da cualquier tipo de error, podemos capturar 
la excepción HTTPError
"""

from urllib import request, error

try:
    pagina = request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/paginax.html")
    datos = pagina.read().decode("utf-8")
    print(datos)

except error.HTTPError as err:
    print(f"Código de respuesta HTTP devuelto por el servidor {err.code}") 
    #Muestra el código de error que aparece en la pagina, ejemplo, 404
    print(f"No existe el recursos {err.filename}")
    # devuelve el nombre de la url que da el fallo
finally:
    print("Gracias por usar el servicio") # siempre se ejecuta