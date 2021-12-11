try:
    a = int(input("primer numero"))
    b = int(input("segundo numero"))
    division = a/b
    print(division)

except ValueError:
    print("Error, ingrese un número entero")
except ZeroDivisionError:
    print("El divisor no puede ser Cero")
