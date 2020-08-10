# CSV significa Valores separados por coma, es un formato de archivo muy utilizado para la 
# importación y exportación de datos en hojas de calculo, es un formato de archivo muy liviano ya que es
# texto plano, cabe decir, que CSV tiene diferentse dialectos, por ejemplo 
# puede ir separdo por comas , por puntos, por tbs, etc.

# Esta libreria es una libreria estandar de python, permite leer y escribir archivos csv, permite decir
# escribe esos datos como un excel o lee los datos por excel, ademas puede escribirse para que tambien
# sea soportado por otras aplicaciones

# Nombre      ->>> descripcion

# Excel            Propiedades usuales de los archivos csv generados por excel
# Excel-tab        Archivo delimitados por TAB generados por excel
# UNIX             propiedades de archivos csv generados por unix
# QUOTE_ALL        entre comillas todos los campos
# QUOTE_MINIMAL    Solo los campos que tienen un caracter especial, como comillas
# QUOTE_NONNUMERIC Entre comilla todo el campo numerico
# QUOTE_NONE       No entrecomilla ningun campo


# atributos que hacen que el archivo se interprete de una u otra manera

# delimiter        Un caracter para separar campos, ejemplo (,)
# doublequote      controla cuando se deben entrecomillar las instanciar de quotachar en un campo
                   # Cuando esta en True el caracter se duplica, cuando esta en False se utiliza el escapechar
                   # como prefijo de quotechar, por defecto esta en True

# Escapechar       Un caracter utlizado para escapar del delimitador quoting esta definido por QUOTE_NONE  y el 
                    # quatechar si double quote esta en false
# lineterminator   string utilizado para terminar una linea, por defecto "\r\n"
# quotechar        Un caracter utilizado para entrecomillar los campos, por defecto ("")
# quotin           indica cuando se debe entrecomillar, los valores son los de las constantes QUOTE_* , el valor por
                    # defecto es QUOTE_MINIMAL
# skipinitialspace Si esta en True ignora el espacio inmediatamente al delimitador, por defecto esta en False
# stric            Cuando esta en True lanza una excepción en caso de ingresar un csv mal formado, por defecto esta en False

# Formas de leer CSV 

# 1. Reader: Lee los datos en secuencias cada linea de archivo es una secuencia

# para crear un reader se pasa la funcion reader y un objeto de tipo archivo o una lista, adicionalmente se puede pasar un dialecto con parametros
# la funcion readr devuelve un objeto reader que s iterable cada una de las lineas,

""""
import csv
with open('some.csv', newline='') as f:
 reader = csv.reader(f)
 for row in reader:
 print(row)
with open('passwd', newline='') as f:
 reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
 for row in reader:
 print(row)
with open('example.csv', newline='') as csvfile:
 reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in reader:
 print(', '.join(row))
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('passwd', newline='') as f:
 reader = csv.reader(f, 'unixpwd')
"""

# 2. DictReader : Lee los datos en diccionarios, cada linea de archivo es un diccionario, donde la clave, es el nombre de la columna y el valor es el leido en la fila actual

# la clase DictReader crea un objeto que opera similar al objeto reader, pero mapea la información de cada linea del archivo en un diccionario ordenado, donde sus claves son dadas
# por el usuario en el parametro fieldnames. si el parametro fieldnames no esta definido, entonces se tomaran los parametros de la primera linea del archivo como las claves

""""
import csv
with open('names.csv', newline='') as csvfile:
 reader = csv.DictReader(csvfile)
 for row in reader:
 print(row['first_name'], row['last_name'])
"""

# Escritora CSV 

# PUEDE UTILIZANDO EL OBJETO WRITER O LA CLASE DictWriter
# el objeto writer escribe datos en un archivo a partir de secuencias
# se puede hacer con la funcion writer, es rseonsable de convertir y guardar los datos que pasa el usuario en cade de texto




# DictWriter lo hace a partir de diccionarios


import csv

with open("/home/oscar/Escritorio/PYTHON APRENDER 1/csv_example.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in DictcReader:
        print(", ".join(row))
with open("/home/oscar/Escritorio/PYTHON APRENDER 1/csv_example.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hola, Mundo!"])