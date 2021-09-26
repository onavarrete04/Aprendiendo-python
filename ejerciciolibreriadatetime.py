# Ejercicio de restar a un tiempo inicial de 30 minutos, los segundos y mostrar cuanto falta para
# terminar el juego.

from datetime import datetime
from datetime import time
from datetime import timedelta


tiempo_i = timedelta(minutes=30)
tiempo_s = timedelta(seconds = 1)
segundo =  timedelta(seconds=1)
continuar = "s"
tiempo_restante = 0
while continuar == "s":
    tiempo_restante = tiempo_i - tiempo_s
    print(tiempo_restante)
    tiempo_s = tiempo_s + segundo
    if tiempo_restante == timedelta(0):
        break

# Conclusiones

# En este ejercicio logre que el tiempo restante llegara a 0, pero
# creo queria que la resta se hiciera de manera natural, sin embargo, solo se estan restando
# los segundos que yo le estoy diciendo que reste, no es como si fuera el cronometro natural o
# se restara con la hora actual.

# Dentro de las dificultades que más encontre en este ejercicio sencillo y principiante
# fue que al intentar hacer operaciones matematicas con entre timedelta y datetime se genera
# un error, hasta el momento considero que esto es por el formato.

