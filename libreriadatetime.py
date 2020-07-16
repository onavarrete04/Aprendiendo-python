# La libreria datatime provee distintas clases que definen tipos de fecha y hora

# (date) -> fecha
# (datatime) -> fecha y hora
# (time) -> hora
# (timedelta) -> delta de tiempos

# TIMEDELTA

# un objeto timedelta representa una duración entre dos fechas u horas

# para crearlo se puede indicar opcionalmente la cantidad de dias, de segundos, microsegundos, milisegundos, minutos, horas, semanas.

# por defecto todos tienen valor 0 pero puede ser positivo o negativo solo los dias, los segundos y microsegundos son guardados internamente
# el eresto se calculan

import datetime


date = datetime.date(2019, 4, 30)
print(date)

print(date.day)
print(date.year)
print(date.weekday())
print(date.isocalendar())
today = datetime.date.min
print("la fecha es",today)
hoy = datetime.date.today()
print(hoy)

ayer = hoy- datetime.timedelta(days=1)
print(ayer)

# resta de dos fechas

delta = hoy - ayer
print(delta)

#DAYTIME

dia_y_tiempo = datetime.datetime(2019, 10, 10, 9, 15, 30)

print(dia_y_tiempo.year) # imprime solo el año
print(dia_y_tiempo.month) # imprime el mes
print(dia_y_tiempo.day) # hora y dia
print(dia_y_tiempo.hour)
print(dia_y_tiempo.minute)
print(dia_y_tiempo.second)
print(dia_y_tiempo.microsecond)

print(dia_y_tiempo.date()) # la fecha 

ahora = datetime.datetime.now()
print(ahora) # hora actual

tiempo = datetime.time(10,20,35)
print(tiempo)

print(tiempo.hour)

print(tiempo.minute)

print(tiempo.second)

print(tiempo.microsecond)

# CONVERTIR FECHAS EN STRING O VICEVERSA 

# Esto es importante cuando queremos exportar o importar archivos
# FUNCION STRFTIME -> FECHAS A STR
# FUNCION STRPTIME -> STR A FECHAS

# PRIMER SE IMPORTA DATETIME

dato_y_tiempo = datetime.datetime(2019, 4, 30, 11, 25, 30)


# creando un string con la funcion strftime

print(dato_y_tiempo.strftime("%Y-%m-%d"))
print(type(dato_y_tiempo))
print(dato_y_tiempo.strftime("%Y-%m-%d-%H:%M:%S"))
print(dato_y_tiempo.strftime("%Y/%m/%d"))

# creando una fecha con la funcion strptime

print(datetime.datetime.strptime("2019-01-10","%Y-%m-%d"))
print(datetime.datetime.strptime("2019-01-10-11:30:25","%Y-%m-%d-%H:%M:%S"))

date_time = '2019-01-30 15:30:45'


datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')



date_time = datetime.datetime(2010, 8, 25, 10, 35, 15)


print(date_time.strftime('%Y/%m/%d %H:%M:%S'))



print(date_time.strftime('%y/%m/%d %H:%M:%S'))


print(date_time.strftime('%Y/%m/%d %H:%M:%s'))

print('\'Hola \n Mundo!\'')