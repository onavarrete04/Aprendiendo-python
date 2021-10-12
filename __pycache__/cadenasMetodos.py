# METODOS STR (STRING)

# upper() Mayusculas 
# lower() Minuscula
# capitalize () Primera letra mayuscula
# count() contar caracteres o numero de caracteres en una lista
# find() indice de un caracter o grupo de caracteres
# isdigit() devuelve un booleano
# isalum() verifica si son alfanumericos
# isalpha() verifica si son solo letras
# split() separa palabras con un espacio
# strip() elimina espacios entre palabras
# replace() remplaza una palabra o letra por otra
# rfind() indice desde la parte atras (r) -> reverse.

# http://pyspanishdoc.sourceforge.net/

nombre = input("introduce tu nombre de usuario")

print("El nombre es: ",nombre.capitalize())
print("El nombre es: ",nombre.upper())

# aplicabilidad práctica

edad = input("introduce la edad: ")
print(edad.isdigit())

while(edad.isdigit()==False):
    print("introduce un valor numerico")
    edad = input("ingrese la edad")
if (int(edad)<18):
    print("No puede pasar")

else:
    print("puede pasar")
    
# si se pone un valor NO numerico el programa cae, por eso se creo el while y se verifico

## Ejercicio ##

correo = input("ingrese su correo por teclado")

while True:
    
    if (correo.count("@") > 1 or correo.find("@") == 0 or correo.endswith("@")):
        print("su correo es erroneo, intente nuevamente")
    
        correo = input("ingrese su correo por teclado")
    
    else:
        print("correo correcto",correo)
        
        break
         