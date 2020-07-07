#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!

print("¡Hola mundo!")

# Ejercicio 2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
a = "¡Hola mundo!"
print(a)

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre = input("Ingrese su nombre")
print("¡Hola ",nombre,"!")

# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = str(input("ingrese nuevamente su nombre"))
numero = int(input("ingrese un numero"))

for x in range(numero):
    print(nombre)

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre

nombre = input("ingrese su nombree")
print(nombre.upper()," tiene", len(nombre), " caracteres")

# Escribir un programa que realice la siguiente operación aritmética (3+22⋅5)2.

operacion_aritmetica = ((3+2)/(2*5)*2)

print(operacion_aritmetica)

# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde

horas_trabajadas = float(input("Cuantas horas trabajo hoy"))
valor_horas = float(input("Ingrese el valor de cada hora"))
salario = horas_trabajadas * valor_horas

print(salario)

numero = int(input("ingrese un numero entero positivo"))

for x in range(numero):
    suma = x*(x+1)/2
    print(suma) 

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("ingrese su peso"))
estatura = float(input("ingrese su estatura"))
IMC = peso/(estatura*estatura)

print(IMC)

# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n , m = int(input("ingrese dos numeros enteros")),int(input("ingrese el otro numero"))
cociente = n//m
residuo = n%m

print(cociente,"/",residuo)

# scribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.


inversion = float(input("cuanto dinero desea invertir"))
interes = float(input("ingrese el numero del interes anual"))
años = int(input("ingrese el numero de años"))
capital = (inversion * (interes/100))*años

print("los intereses de su inversión son: ",capital," lo que implica que su ganancia total es : ",capital + inversion )

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

PAYASOS = 112
MUÑECAS = 75

solicitud_payasos = int(input("cuantos payasos desea solicitar, ingrese el valor: "))
solicitud_muñecas = int(input("cuantas muñecas desea solicitar, ingrese el valor: "))

peso = ((PAYASOS * solicitud_payasos)+(MUÑECAS *solicitud_muñecas))

print("el peso total de la carga es: ",peso)
print("el peso de payasos es : ",PAYASOS*solicitud_payasos)
print("el peso de muñecas es: ",MUÑECAS*solicitud_muñecas)