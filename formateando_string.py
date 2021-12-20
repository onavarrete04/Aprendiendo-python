valor1 = int(input("Ingrese primer valor"))
valor2 = int(input("Ingrese segundo valor"))

suma = valor1 + valor2

print(f"La suma {valor1} y {valor2} es {suma} ") # Se coloca la f - format

lista = [2000,500,17000,24,7]


for i in lista:
    print(f"{i:5}") #->>>> :10 son los espacios que ocupara la variable
print("----")
print(f"{sum(lista):40}")

valor1=10
print(F"{{valor1}} tiene el valor {valor1}") # doble llaves para que 