"""
Un paradigma de la prograamción funcional es el de las funciones de orden superior

Son funciones que pueden recibir funciones como parametros o devolverlas como resultado


"""
def operar(v1,v2,fncion):
    return fncion(v1,v2)
def sumar(x1,x2):
    return x1+x2
def restar(x1,x2):
    return x1-x2
def multiplicar(x1,x2):
    return x1*x2
def dividir(x1,x2):
    return x1/x2

resultado = operar(10,20,sumar) # envia la función sumar

print(resultado) # devuelve el resultado 30 de la suma

resultado2 = operar(20,10,restar)
print(resultado2)

print(operar(2,2,multiplicar))
print(operar(99,5,dividir))