def imprimir(numero):

    if numero <= 1:
        return 1   
    print(numero)
    return( numero * imprimir(numero-1))
    

print(imprimir(5))

