# MODULOS O BIBLIOTECAS

# Es crear algo pero no desde cero, podemos descargar un modulo que podemos utilizar para hacer algo +
# La razón de utilizar modulos es evitar la tarea repetitiva una y otra vez

# Tres tipos de Modulo

#1. El hecho por nosotros mismos. -> own modules
#2. El descargado por internet. -> thirdy party modules
#3. Modulos de python -> python modules

# Modulos de python 

import datetime    # Siempre leer la documentación oficial, porque es la información real
# tambien se puede importar asi 
# -> from datatime import timedelta, estas diciendo (from = desde) la bilioteca datatime, import = importa su propiedad time delta
# -> asi puedes ejecutar directamente sin usar el datetime.
# antes print(datatime.timedelta(minutes=70))
# ahora print(timedelta(minutes=70)) debido a que traes directamente el metodo del modulo

print(datetime.date.today())  # se pone primero datatime. que es el modulo, la función

print(datetime.timedelta(minutes=70))

# vamos a importar el modulo que hice

import mismatematicas

mismatematicas.agregar(1,2)
mismatematicas.suprimir(1,2)

from mismatematicas import agregar, suprimir
agregar(1,2)
suprimir(1,2)

# Modulos descargados por internet

# pagina pypi.org   -> permite utilizar modulos de terceros

# se instala pip o pip3 colorama etc ...
# importas -> import colorama
# o from colorama import Fore, Style, init
# init(convert=True)
# print(Fore.RED + "Hello World")

# si uno sale del a hoja o modulo de python que creo y entra a otra, las variables  y funciones se peirden
# por lo tanto es bueno ejecutar ese archivo como entrada, conocido como un script
#para esto en python permite que tus archivos se conviertan en script o instancias y llamarlos como modulo
# por lo cual puedes importarlas a otros modulos.
# un modulo es un archivo conteniendo definiciones y declaraciones de python, el nombre del archivo
# siempre tiene un sufijo .py, con esto reutilizaras el codigo ya elaborado anteriormente
# si es necesario puedes llamar esa función y luego denominar una localmente

# normalmente se ubican todos los import al inicio de la hoja o modulo.
#sys.path es un dictorio de modulos