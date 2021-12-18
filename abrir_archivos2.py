# FASES

# crear archivo
# abrir archivo
# manipular archivo
# cerrar archivo

# modo lectura
# modo escritura
# modo adicion

from io import open

# open - Abrir archivo externo

mi_archivo = open("archivo.txt","w")

frase = "Estupendo día para aprender \n Saludos"

mi_archivo.write(frase)

mi_archivo.close()



