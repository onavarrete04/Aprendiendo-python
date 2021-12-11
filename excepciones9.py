
try:
    a = int(input("ingrese el primer valor"))
    b = int(input("ingrese el segundo valor"))
    division = a/b
    print(division)
except ZeroDivisionError:
    print("Ooops, No se puede dividir por 0")