x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
matriz = [[k,j,i] for i in range(x+1) for j in range(y+1) for k in range (z+1)]
# la lista [i,j,k] se crea como parte de los iteradores

respuesta = [result for result in matriz if result != n]

print(respuesta)

# "I" iterador ingresa a "X" (1) luego "J" ingresa a "Y" (1) y luego "K" ingresa a "Z", así sin nada más daría 
# una lista con dos elementos nada mpas

# Tradicional

contador = []
for i in range(1+1):
    for j in range(1):
        for k in range(1+1):
            contador.append([i,j,k])

resultado_lista = []
for resultado in contador:
    if sum(resultado) != 2:
        resultado_lista.append(resultado)
print(resultado_lista)