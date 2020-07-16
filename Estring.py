my_str = "Hello World"

print(dir(my_str))   # la función dir() significa que se puede hacer o las propiedades que podemos usar con este string

print(my_str.upper()) # upper convierte la variable en mayuscula
print(my_str.lower()) # lower convierte en minuscula
print(my_str.swapcase()) # swapcase pone mayusculas y minusculas
print(my_str.capitalize()) # la primera en mayuscula
print(my_str.replace("Hello",'BYE') ) #reemplaza

#tambien se puede combinar funciones, se conocen como metodos encadenados:

print(my_str.replace("BYE","hello").upper())

print(my_str.count("l"))  #cuenta determinado caracter
print(my_str.startswith("hola"))  #mira si inicia con una palabra con True o False
print(my_str.endswith("World"))   # mira como termina el string

# tambien se puede dividir el string en dos variables

print(my_str.split())  # en este caso separa por defecto donde se encuentra el espacio
print(my_str.split('o')) # tambien se separa con un caracteristica
# con esta función se creo  una lista

print(my_str.find('o')) # busca el caracter y la posición.
print(len(my_str))    # imprime la longitud, inicia en 0 
print(my_str.index("e"))  # mira la posición o indice

print(my_str.isnumeric())  # mira si es numerico
print(my_str.isalpha())    # mira si es alfanumerico

print(my_str[4])   # imprime de una vez el index que deseas, es decir el caracter
print(my_str[0:2]) # imprime los index de 0 antes de 2
print(my_str[2:5]) # imprime desde el 2 antes del 5

#para unir string se pone el + y se llama concatenación

print(f"My favorite word is {my_str}") # concatena y se pone la f al inicio para que sepa que dentro del string va una variable
print("mi palabra favorita es {0}".format(my_str)) # el {} vacio es el index y con .format le dices que quieres que aparezca en ese {}

