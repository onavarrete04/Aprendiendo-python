""" El programa habra de hacer lo siguiente

1. elegir dos dos numeros aleatorios entre 1 y 6 y preguntarle al usuario si 
lanzarlos otra vez

2.imprimir en pantalla, imprimir su suma """


import random   # selecciono la libreria random que tiene la función aleatoria

def lanzar_dados(prompt, intentos=4, recordatorio='Intente Nuevamente!'):
    
    while True:
        afirmativo = input("¿Desea lanzar los dados otra vez?")
        if afirmativo in ("s","S","y","Y","si","Si","sI","SI"):
            a = int(random.random()*7) # elije un numero del 1 al 7 pero no el 7, como son enteros, nunca saldra el 7
            b = int(random.random()*7)
            print(a)
            print(b)
            print("La suma de los dados es: ",a+b)
        if afirmativo in ("n","N","No","NO","nO","no","Not","NoT","NoT","noT","not","NOT"):
            print("Gracias por usar nuestro programa")
            break;
        if intentos < 0 :
            print(recordatorio)
        
lanzar_dados("Lanzando dados") # se pone la variable prompt para iniciar la función

