# Listas de compresion

"""Son listas que se pueden crear en una misma línea de código"""
lista = []

# Metodo normal
for letra in "casa":
    lista.append(letra)
print(lista)

#Usando metodo de compresion

lista = [letra for letra in "casa"]
print(lista)

# Metodo tradicional
lista = []
for numero in range(0,11):
    lista.append(numero**2)
print(lista)
# Usando metodo de compresion
lista = [numero**2 for numero in range(0,11) ]
print(lista)


