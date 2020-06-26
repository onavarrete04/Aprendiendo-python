#vamos a ver el condicional if y el else
# los condicionales se comparan en tre si para que de como resultado un boleano
#esto nos permite recrear rutas para realizar determinados procedimientos
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

s = 40

if s < 30:
    print(s," es menor que 30 ")
elif s > 30:
    print(s,"es mayor que 30")

color = "red"
if color == "Red" or "red":
    print("su color favorito es ",color)
elif color != "Red" or "red":
    print("su color favorito no es red, es ",color)



    
