

x= 1+4*3+8/2*4+5**2
if x%2 == 0: # con modulo %2==0 podemos saber si es par o inpar
    print("el numero x es par y se le suma 1",x+1 )
else:
    print("el numero es x impar y se le resta 1",x-1) 

# sucesión de Fibonacci 

# es una sucesión de numeros naturales de manera infinita, comienza con 0 y 1
# cada termino es la suma de los dos anteriores

def fib(n):

    a , b = 0, 1
    while a < n:
        for x in range(n):
            print(a ) # end se utiliza para que la información se imprima en fila
            a , b = b, a+b
    print()


print(fib(36))
print(fib(2))
