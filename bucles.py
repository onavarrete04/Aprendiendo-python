comidas = ["manzanas","bread","cheese","milk"]
# los bucles permiten hacer una tarea tipica, y no se rompen hasta cumplir el objetivo o si no cumplen el parametro no entra

for comida in comidas:
    print(comida)
    break

x = 0

for x in range(10): # range es un rango 0 a 10 y lo cumple y luego se rompe, en otras aplicaciones se hace diferente
    print(x)
    x+1

for number in range(1,8): # <- cuando se hace for number in range, el number se convierte en una nueva variable
    print("hola",number)

# Bucle while

x = 0

while x <=10:
    print(x)
    x=x+1
# si no se rompe el bucle se ejecutara por siempre
# esto es conocido como bucle infinito
# 
   

