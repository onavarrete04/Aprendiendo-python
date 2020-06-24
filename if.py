#vamos a ver el condicional if y el else
x = 2
if x >= 0:
    print("el numero es mayor o igual",x)
else:
    print("el numero es menor",x)
a = 1
if a>0:
    print(a,"es mayor o igual a 0")
elif a<0:
    print(a,"es un numero negativo")
else:
    print("el numero es igual a 0")
# anidación de condicionales
z=2
if z > 0:
    print(z, "z es mayor")
else:
    if z < 0:
         print("el numero",z,"es negativo")
    else:
         print("el numero es igual a 0")
    