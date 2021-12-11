# Las excepciones son errores que se disparan durante la ejecución del programa.
# La idea es que dentro de los programas se generen algoritmos que puedan capturar
# dichos errores

while True:
    # capturara la excepción si ocurre
    try: 
        valor1 = int(input("Ingrese primer valor: "))
        valor2 = int(input("Ingrese segundo valor"))
        suma = valor1 + valor2
    except ValueError:
        print("¡Debe ingresar numeros enteros")
    respuesta = input("¿Desea intentarlo nuevamente [s/n]?")
    if respuesta =="n":
        break

# ValueError indica que el valor introducido es erroneo, es decir, se espera otro tipo de dato
# en nuestro caso los unicos datos validos son los enteros