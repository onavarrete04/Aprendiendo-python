# FINALLY

# ES UN ELEMENTO QUE SIEMPRE SE EJECUTA DENTRO DEL ALGORITMO

try:
    archivo_1 = open("datos.txt","w")
    archivo_1.write("Primera Línea. \n ")
    archivo_1.write("Segunda Línea. \n ")
    archivo_1.write("Tercera Línea. \n ")
    archivo_1.write(12345)
except TypeError:
    print("No se puede grabar un entero con write")
finally:
    archivo_1.close()
    print("Se cerro el archivo - saludos")
