def imprimir(x):
    if x>0:
        imprimir(x-1)
        print(x)

imprimir(5)

"""
Se llama la función imprimir con el parametro 5
cuando entra al programa se verifica el el numero sea mayor que cero para ingresar a la operación

en ese momento se usa la recursividad llamando a la variable
cuando se llama a la variable se le indica que va a ser x -1, es decir 5 - 1, 4 y asi sucesivamente

Los números quedarán de la siguiente forma
5
4
3
2
1
Dentro del ciclo, todos esos números estan utilizando un espacio en bytes dentro dle programa
cada vez que el programa se llama asi mismo, se crea un espacio para guardar el numero anterior
así, cuando finaliza la condicional, la función pasa a liberar el espacio que habia asignado para la misma
por eso imprime primero el ultimo valor que debia dar, y asi sucesivamente.


"""

def imprimir(x):
    lista = ["a","e","i","o","u","AA"]
    if x>0:
        imprimir(x-1)
        print(x, lista[x])
        

imprimir(5)
