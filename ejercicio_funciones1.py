def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(input())

"""
En el ejercicio para verificar años bisiestos se deben tener en cuenta solo dos condicionse

a) si el modulo del año (año%4) en 4 es igual a 0 pero el (año%100) no es igual a cero, significa que es bisiesto
b) si el modulo del año (año%4) y (año%100) y (año%400) es igual a cero, significa que es bisiesto. 

"""