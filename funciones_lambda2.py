
def recibir_str(cadena, fncion):
    caracter = ""
    for i in cadena:
       if fncion(i):
           caracter = caracter + i
    return caracter



print(recibir_str("a",lambda x:  x == "a" or x == "e" or x == "i" or x == "o" or x == "u"))

print(recibir_str("O", lambda palabra: palabra>="a" and palabra<="z" ))

print(recibir_str("i", lambda palabra: palabra.isalpha() ))