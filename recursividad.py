"""def repetir():
    repetir()

repetir() """

"""
1) Permite ejecutar un bloque de instrucciones n veces

2) Es un tema dificil de entender

3) Un metodo que se llame a si mismo puede decirse que es recursivo

4) La recursividad consume más recursos de la maquina

En la funcion repetir sucede;

- Se llama a la funcion repetir

- Cada vez que se llama se reserva un conjunto de bytes de la memoria que se liberaran
cuando finalice la ejecución

-  La primera linea permitira reservar más bytes nuevamente y se ejecutara 
hasta que la pila estática se colme y se culgue el programa

"""

"""def factorial(numero):
    resultado = 1

    for i in range(numero):
        if i >= 1: 
           
            resultado = resultado * numero 
            numero -= 1
    return resultado

print(factorial(5))"""


# Se simplifica usando la recursividad, pero se usan más recursos

def factorial_recursiva(numero):
    
    if numero <= 1:
        return True # Cuando se retorna True, pasa el return 
        
    return numero * factorial_recursiva(numero -1)

print(factorial_recursiva(5))