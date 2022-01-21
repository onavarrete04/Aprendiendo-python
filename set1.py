def nombres_alumnos(alumnos):
    nombre = ""
    while True:
        nombre = input("Nombre de alumno: ")
        if nombre != "x":
            alumnos.add(nombre)
        else:
            return alumnos
       
primaria = set()
print(nombres_alumnos(primaria))
print("----")
secundaria = set()
print(nombres_alumnos(secundaria))

print("---")
print("Esto muestra el nombre de todos los alumnos - UNIÓN")
for elemento in primaria | secundaria:
    print(elemento)

print("---")
print("Esto muestra los elementos que no son repetidos, es decir, elimina los nombres que aparecen en los dos conjuntos")
if primaria ^ secundaria:
    for elemento in (primaria^secundaria):
        print(elemento)


print("---")
print("Estos son los elementos que se repiten en los dos conjuntos")
if primaria & secundaria:
    for elemento in (primaria & secundaria):
        print(elemento)

print("---")
print("Vemos si unos elementos pertenecen a otros")
for elemento in (primaria - secundaria):
    print(elemento)
print("--")
for elemento in (secundaria - primaria):
    print(elemento)



