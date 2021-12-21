def ordenar(lista, cant): # cantidad es el numero de elementos dentro de la lista
    if cant>1: 
        for f in range(0, cant-1): 
            if lista[f]>lista[f + 1]:
                aux=lista[f] # el auxiliar guarda el mayor
                lista[f]=lista[f + 1] # se guarda el menor en la posicion del index f
                lista[f + 1] = aux # se guarda el mayor de la posición del index en f + 1 
            ordenar(lista, cant - 1) # pide que se ejecute otra vez rstandole el len

datos=[60,44,22,33,2]
print(datos)
ordenar(datos, len(datos))
print(datos)

if 2 > 1:
    print("si")
