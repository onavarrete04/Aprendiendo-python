import sys

try:
    archivo = open("datos.txt")
    ejemplo = archivo.readline()
    archivo1 = int(ejemplo.strip)
  
except OSError as err:    
    print("Error OS: {}".format(err))
except ValueError:
    print("El dato no corresponde")