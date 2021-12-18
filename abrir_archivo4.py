from io import open

archivo = open("archivo.txt","r+")
#print(archivo.readlines())

lista = archivo.readlines()

lista[1] = " Esta línea esta siendo incluida desde el exterior \n"
archivo.seek(0)
archivo.writelines(lista)