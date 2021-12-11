
meses = ("enero","febrero","marzo","abril","junio","julio",
"agosto","septiembre","octubre","noviembre","diciembre")

try:
    numero_mes = int(input("ingrese el numero del mes a consultar"))
    print(meses[numero_mes-1])
except IndexError:
    print("El numero de mes consultado no existe")