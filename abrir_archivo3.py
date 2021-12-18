from io import open

archivo = open("archivo.txt","r")
# archivo = open("archivo.txt","r+")
#archivo.write("asfdadf") -> si se hace esto, indiscriminadamente se añadira la nueva línea desde el inicio de la cadena



# puntero dentro del elemnto
archivo.seek(1) # el puntero indica desde cuando se va desplaza el puntero a la posición, en este caso a la posición 0
# tambien podemos posicionar el puntero con read, pero el read solo leera hasta donde le indicamos, y el solo leera hasta donde le digamos
print("...")
lectura = archivo.read(10)
print(lectura)

# puntero en la mitad del texto
print("...")
archivo.seek(len(archivo.read())/2)
lectura = archivo.read()
print(lectura)

############


archivo.close()