# IndexError

# Se produce cuando un subindice (lista, tupla, string) esta fuera de rango

try:
    lista_ejemplo = [1,2,3,4,5,6,7,8,9]
    print(lista_ejemplo[10])
except IndexError:
    print("Ooops, hay un error ene el index, solo existen",len(lista_ejemplo)," elementos dentro del index")