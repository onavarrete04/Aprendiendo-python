# son funciones que toman una función y devuelven otras funcion, reducien el codigo repetitivo
# mantienen la legitimidad del programa y lo hacen mas legible

#1 se crea la función que analizara las otras funciones, por eso se indica que recibira un parametro
# que es una función, y luego se crea otra función con dos parametros y se evalua
def smart_division(div_func):
    def div(a,b):
        if b == 0:
            print("No se puede dividir por cero!")
            return
        return div_func(a,b)
    return div
#2
@smart_division  #así se llama el decorador para que actue sobre una función
def division(a,b):
    return a/b
#3 cuando ejecutemos, el decorador ya estara actuando sobre la función división y dara un resultado
print(division(1,2)) 
print(division(2,0))


def log(f):
    def wrap(*args, **kwargs): # * indica que se ejecutara antes de **
        print("Ejecutando la función ",f.__name__,
        "con los argumentos", ",".join([str(arg) for arg in args]))
        return f(*args, **kwargs)
    return wrap

@log
def suma (a,b):
    return a + b

print(suma(1,2))

@log
@smart_division
# se pueden usar varios decoradores en una función
def division_2(a,b):
    return a / b


print(division_2(2,1))
print(division_2(1,0))

