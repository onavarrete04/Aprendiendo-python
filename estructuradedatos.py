import string   # se imoprta para trabajar linea 73

# ESTRUCTURA DE DATOS

# CADENAS DE CARACTERES, FECHAS, TUPLAS, LISTAS CON VARIANTES

# UNA ESTRUCTURA DE DATOS ES UNA FORMA ESPECIFICA DE MOSTRAR LOS DATOS EN EL COMPUTARDOR

# strings

# los string o str son secuencias ordenadas de caracteres, los string son inmutables, es decir que no se pueden modificar
# lo que se puede hacer es construir otro string nuevo
# en caso de modificar un string se levantara una excepción del tipo TypeError

palabra = "Hola Mundo!"

# palabra[6] = "o" # dara error TypeError

nueva_palabra = palabra + "?"
print(nueva_palabra)

nueva_palabra = palabra[:6]+"o"+palabra[7:]
print(nueva_palabra)

# el operador + concatena strings de manera que crea un nuevo string a partir de dos


# ESCAPE

#para escapar caracteres dentro de un string se debe utilizar la (\)

print("linea1 \n linea2 \n linea3") # \n da un salto de linea se supone que ("linea1\linea2\linea3") da: linea1 linea2 linea3

print("\\")  # imprime solo una \

print("linea1 \
    linea2 \
    linea3")
#print('\") # imprime una comilla '



print("hola \n mundo") # hace un salto de linea (LF)
print("hola \r mundo") # hace un salto de linea (CR)
print("hola \t mundooooooooo") # tabulador horizontal

# STRING CONTENIDO DINAMICO

name= "Agustin"
print("Hola %s"%name) # %s significa que el valor que le pases lo interpretara como un str
print("el numero es %d"%5) # %d interpreta un int
print("el numero es %02d"%5) # %02d le agrega dos 0 a la izquiera sinedo aun entero
print("el numero es %f"%6.45) # %f interpreta un numero decimal
print("Hola %(name)s" % {'name': name}) # Resultado: Hola Agustín este es un digsionario)


print("Hola {}".format(name))   #directamente lee que valor debe ir en las {}
print("la suma de 1 + 2 es {0}".format(1+2)) # lee que valor debe ir en las {} segun la posicion
''.join(["hola",name])  # funcion join permite concatenar en una lista lso valores

# CODIFICACIÓN STRING

# los string en esta versión son unicode, pero necesitaremos codificarlso cuando ingresen al sistema ocuando salgan
a_string = 'Otoño'
# Codifico el string a utf-8
coding_string = a_string.encode('utf-8') # Respuesta: b'Oto\xc3\xb1o'
# Decodifico el byte array en utf-8
coding_string.decode('utf-8') # Respuesta: 'Otoño


# FORMATER

# Al ejecutarlo como hoja falla
name = "agustín"
formatter = string.Formatter()
print(formatter.format("hola {}",name))

"{}+{} = {}".format(7,5,2)

"hola {name}.format(name = name)"

'{0}+{2}={1}'.format(2,5,6)

"{0}+{1} = {resultado}".format(2,5,resultado=7)
"{0:.3f}+{1:3f}={resultado:.3f}.format(2,5,resultado = 7)"
"hola{name:16}.format(name=name)"
"hola{name:<16}.format(name=name)"
"hola"

print("{:f}".format(2.5))