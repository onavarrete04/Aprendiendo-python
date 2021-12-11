# NameError

# Se produce cuando llamamos un metodo, clase, variable, etc de manera erronea o no existe

try:
    numero_1 = 3.24
    numero_2 = 3.88
    suma = numero_1 + numero_2
    #print(sumar) # el nombre real de la variable es suma, por eso da error
except NameError:
    print("Ooops, hay un error con los nombres ejecutados")