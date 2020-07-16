#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("ingrese una palabra")
for x in range(10):
    print(palabra)

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("cuantos años tiene?"))

for x in range(1,edad+1):
    print("años ",x)

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

entero = int(input("ingrese un numero positivo"))

for x in range(entero+1):
    if x % 2 != 0:
        print(x, end=",")

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("ingrese un numero"))

for x in range(numero,-1,-1):
    print(x)

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

inversion = float(input("ingrese un monto a invertir"))
i = float(input("interes deseado anualmente"))
anual = int(input("años que mantendra su inversion"))
intereses = (inversion*(i/100))

for x in range(1,anual+1):
    
    print("su capital es de : ",inversion," y los intereses ganados, ",intereses*x," año ",x)

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

numero = int(input("Ingrese un numero"))

for x in range(numero):
    for i in range(x+1):
        print("*",end="")   
    print("")
     
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

for x in range(11):
    for i in range(11):
        print(x*i, end="\t")
    print("")

   
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.    
numero = int(input("Ingrese un numero"))
for x in range(numero):
    for i in range(x+1):
        print(i,end="")   
    print("")

a = 
contraseña = str(input("ingrese su contraseña"))


