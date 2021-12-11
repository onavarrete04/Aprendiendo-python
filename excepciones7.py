
#OverflowError:

# Se produce cuando numeros float son demasiado grandes para ser procesados

try:
    resultado = 5.25 **25665
    print(resultado)

except OverflowError:
    print("Número demasiado grande para mostrar")
