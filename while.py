# vamos a utilizar el while

a, b = 0, 1
while b<10:
    print(b)
    a,b = b, a+b

# < menor que
# > mayor que
# == igual que
#<= menor o igual que
# => mayor o igual que y != distinto que
while b < 1000:
    print(b, end= ',')
    a,b = b, a+b
# end se utiliza para que nos e den saltos, sino que se presente la informacion en una fila

