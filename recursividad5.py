import os

# Recorrer directorios

def leer(directorio):
    lista = os.listdir(directorio) # retorna una lista con todos los nombres dearchivos y directorios
    for elemento in lista:
        if os.path.isfile( elemento): # isfile verifica si es archivo
            print(elemento + "[archivo]")
        if os.path.isdir(elemento): # verifica si es directorio o carpeta
            print(elemento + " [directorio]")
leer("/home/oscar/Documentos/Aprendiendo-python")

print(leer("/home/oscar/Documentos/Aprendiendo-python"))

