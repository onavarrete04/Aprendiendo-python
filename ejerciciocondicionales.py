# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no

edad = int(input("Por favor ingrese su edad"))

if edad >= 18:
    print("Usted es mayor de edad, tiene: ",edad," años!")
else: 
    print("usted es menor de edad, prohibido el ingreso")

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
key  = "ConTraSeÑa"
contraseña = str(input("Escriba su contraseña"))

if contraseña == key.lower():
    print("La contraseña coincide",key.lower())
else:
    print("contraseña invalida")

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error

a , b = int(input("Ingrese un numero")),int(input("Ingrese otro numero"))

if True: 
    if (a/b) == 0:
        print("Ha habido un error en el programa, su resultado fue 0")
    else:
        print(a/b)
    
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("ingrese un numero entero"))

if numero % 2 == 0:
    print("Su numero es par : ",numero)
else:
    print("su numero es impar : ",numero)

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no

edad = int(input("ingrese su edad por favor"))
ingresos = int(input("Ingrese sus ingresos por mes en Euros, evite puntos y comas"))

if edad >= 18 and ingresos>=1000:
    print("Usted esta obligado a tributar, cumple con las dos condiciones para eso")
else:
    print("Usted no debe tributar")

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

name = input("Cual es su nombre?")
genero = input("Cual es su genero? (H o M)")

if genero == "M" and name.lower() < "m" or  genero == "H" and name.lower() > "n":
    print("Tu grupo es el A")
else: 
    print("Tu grupo es el B")

# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
renta = int(input("Cual es su renta anual"))

if renta > 60000:
    print("usted debe pagar el valor de 45%. Su renta es ",renta," por lo tanto su tipo es, ",renta * 0.45)
else:
    if renta > 35000  and renta <=60000:
        print("30%",renta," tipo ",renta * 0.30)
    else: 
        if renta > 20000 and renta <= 35000:
            print("20%  ",renta*0.20)
        else:
            if renta > 10000 and renta <= 20000:
                print("15%  ",renta*0.15)
            else: 
                if renta <= 10000:
                    print("5%  ",renta*0.05)

#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

opinión = int(input("califique su rendimiento (inaceptable - 0), (aceptable - 1) o (meritorio - 2)"))


if opinión == 0:
    calificacion = 0.0
    print("su calificación es inaceptable : ",calificacion)
    print("su bonificacion es de : ",calificacion*2400)
elif opinión ==1:
    
    calificacion = 0.4
    print("Su calificación es aceptable")
    print("bonificación de : ",calificacion*2400)
else:
    if opinión == 2:
        calificacion = 0.6
        print("Felicidades, su trabajo ha sido reconocido") 
        print("bonificación de : ",calificacion*2400)
    
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("ingrese su edad"))

if edad < 4:
    print("puede entrar gratis")
elif edad >= 4 and edad <=18:
    print("la entrada cuesta 5 Euros")
else:
    if edad > 18:
        print("la entrada cuesta 10 Euros")

vegetariana = ["pimiento","tofu"]
carne = ["peperoni","jamon","salmon"]
CONSTANTE = ["mozzarella","tomate"]
eleccion = input("marque 1 para vegetariana y 2 para carne")

if eleccion == 1:
    ingredientes = int(input("marque 1 para pimiento y 2 para tofu"))
    orden = []
    orden.append(vegetariana)
    if ingredientes == 1:
        orden.append("pimiento")
        print("su pizza contiene los siguientes ingredientes ",orden)
    else:
        orden.append(ingredientes[1])
        print("sus ingredientes son : ",orden)

