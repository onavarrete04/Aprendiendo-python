# EXCEPT

# se puede utilizar solo el except dentro de un valor, pero no es un elemento recomendado
# porque no sabriamos que tipo de error se esta ejecutando

while True:
    try:
        a = int(input("ingrese un valor"))
        b = int(input("ingrese otro valor"))

        division = a/b
        print(division)
    except:
        print("Ocurrio un error, pero no se sabe cual es")

    continuar = input("¿Desea continuar? [s/n]")
    if continuar == "n":
        break

# En este ejercicio pueden ocurrir dos errores, el primero es ValueError cuando se ingrese otro dato
# y tambien puede ocurrir ZeroDivisionError