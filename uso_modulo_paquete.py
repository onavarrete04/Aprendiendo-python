from calculos_paquete.calculos_generales import dividir, potencia

# en este caso para llamar el modulo se hace

# nombre_carpeta.nombre_modulo  import nombre_funcion

dividir(5,5)
potencia(2,2)
print(5*5*5*5*5)

#### Usar paquetes, con carpetas modulos

from calculos_paquete.basicos.operaciones_basicas import sumar, multiplicar

# carpeta_paquete_grande.carpeta_subpaquete.modulo import funcion

sumar(5,6)
multiplicar(5,7)