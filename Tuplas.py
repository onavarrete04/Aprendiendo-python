#TUPLAS
#se utilizan especialmente con datos que no cambian, digamos las listas si pueden cambiar, las tuplas no.
# se representa en () es decir, es inmutable
a=(22,20,30,25)
print(type(a))

#son mas rapidas las tuplas que las listas, osea se procesa mas rapido y se utiliza para no cambiar datos

x = (1,2,3,4)
print(x)
semana("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

#función tuple() crea tuplas

y = tuple((1,2,3))
print(y)

# con la función dir() ves todo lo que puedes hacer con ella
# una tupla con 1 solo valor se guarda como un dato entero, porque 
# una tupla es con varios elementos, si quieres una tupla con un dato, debes poner ,
x = (1,)

z = (1,2,3,4,5)

print(z[2]) # vemos la posición del index, solo que no se modifica

#la tupla se puede eliminar con del

del x 










