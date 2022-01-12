
lista = [1,2,3,4,5]

listas_cuadrado = [entero**2 for entero in lista]
print(listas_cuadrado)

print("---"*9)

personas=[('pedro',33),('ana',3),('juan',13),('carla',45)]

mayores = [per_mayor for per_mayor in personas if per_mayor[1]>=18]
print(mayores)

print("---"*9)

multiplos = [multiplo for multiplo in range(1,500) if multiplo%8==0]
print(multiplos)

print("---"*9)

nombres=['juan','pablo','luis','mauro','hector']

nombres_duplicados = [[nombre1, nombre2] for nombre1 in nombres for nombre2 in  nombres if nombre1 != nombre2]
print(nombres_duplicados)
 

print("---"*9)

numeros = ["fizz"*(not numero%3) + "Buzz"* (not numero%5) or numero for numero in range(1,101)]
print(numeros)

# cuando "fizz"*(not numero%3) da True(1) el "not convierte a bolleano el dato" lo convierte a 1 y este se multiplica  con el string
# si este llega a dar False, el valor se combierte a True se multiplica por 0 por lo cuál el string queda en blanco

print("---"*9)
impares = ["impar"*(not numero%2==1) or numero for numero in range(1,101)]
print(impares)
print("---"*9)
impares = ["impar"*( numero%2==1) or numero for numero in range(1,101)]
print(impares)

"""
La clausula NOT es una negación que cambia el valor


True (1, verdadero) y False (0, falso).


"""