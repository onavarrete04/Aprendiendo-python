# paquetes son directorios que almacenan directores relacionados entre si
# sirven para reutilizar y organizar modulos
# se crea una carpeta con un archivo __init__.py que esta diciendo que se crea un paquete
# se pueden crear modulos donde se quieran

# Paquetes distribuibles

"""Para ello hay que instalarlo y distribuirlo para llamarlo independientemente
de donde uno se encuentre, para ello se instala en el sistema operativo.

se crea un archivo setup.py en la raiz de la carpeta python

setup.py"""

from setuptools import setup

setup(
    name="calculos_paquete",
    version = "1.0", # la versión es por si se va ir actualizando
    description = "Paquete de redondeo y potencia",
    author = "Oscar Navarrete",
    author_email = "onavarrete@unicolmayor.edu.co",
    packages=["calculos_paquete","calculos_paquete.basicos"], # rutas y subpaquetes y donde se encuentran teniendo en cuenta que esta desde raiz
)


# Luego en se dirige uno a la consola desde la carpeta

#cd Documentos/Aprendiendo_python/

#python setup.py sdist #-> sdist es lo que convertira el paquete en un distribuible



# Despues de ejecutarse la sentencia creara dos carpetas

# 1) paquete_calculos.egg-info
# 2) dist

# El paquete dist es el que puede distribuirse por todo el mundo o instalarse
# en nuestro sistema operativo

# para ello ingresamos a la dirección donde esta la carpeta disc dsede la terminal
# y colocamos -> pip3 install nombre_paquete

# luego de esto podemos importar las funcionalidades de este paquete dentro
# de python para ser utilizadas dentro de un script, o para practicar desde la consola

#IMPORTANTE FORMA DE IMPORTAR

# from paquete.subpaquete.modulos import nombre_funcino  o *

# caso particular 

# from calculos_paquete.basicos.operaciones_basicas import *

# DESISTALAR PAQUETE

# pip3 uninstall calculos_paquete 