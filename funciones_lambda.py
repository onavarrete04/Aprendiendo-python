# Lambda

def operar(v1,v2,fncion):
    return fncion(v1,v2)

resultado = operar(10,3, lambda x1,x2: x1+x2)
# lambda se construye indicando dos parametros y la funcionalidad en una sola linea
print(resultado)

resultado2 = operar(10,3, lambda x1,x2: x1-x2)
print(resultado2)

print(operar(10,3, lambda x1,x2: x1*x2))
print("----")
##################

def imprimir_si(lista,fncion):
    for i in lista:
        if fncion(i):
            print(i)
lista1 = [9, 20, 70, 60, 19]

print(imprimir_si(lista1, lambda x: x%2==0))
"""
print("Valores múltiplos de 3 o de 5")
imprimir_si(lista1, lambda x: x%3==0 or x%5==0)
print("Imprimir valores mayores o iguales a 50")
imprimir_si(lista1, lambda x: x>=50)
print("Imprimir los valores comprendidos entre 1 y 50 o 70 y 100")
imprimir_si(lista1, lambda x: x>=1 and x<=50 or x>=70 and x<=100)
print("Imprimir la lista completa")
imprimir_si(lista1, lambda x: True )
"""