import funciones_matematicas

funciones_matematicas.sumar(1,2)
# se llama utilizando el POO.

# para evitar escribir el modulo antes de cada funcion, se utiliza

from funciones_matematicas import * # se puede llamar con * todas las funciones

restar(2,1)

# cuando se utilizan modulos muy grandes, no se recomienda utilizar el *
# por temas de optimización.