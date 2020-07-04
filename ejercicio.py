

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

def par(n):

    a , b = 0, 2
    while a < n:
        for x in range(n):
            print(a ) # end se utiliza para que la información se imprima en fila
            a , b = b, a+b
    print()


suma = 0   # suma es una variable global dentro del programa

for x in range(0,102,2): # al ejecutar el ciclo, la variable suma global guarda los datos y esto permite que se de la suma, si fuera variable local, no se podria hacer poque la variable no guardaria el dato, solo lo cambiaria
  suma = suma + x

print(suma) # ahora la variable suma tiene este valor

def es_primo(numero):
    resultado = True
    for divisor in range(2,numero):
        if(numero % divisor) == 0:
            resultado = False
            break
        return resultado

print(es_primo(13))


s = 0

for n in range(1, 10):

    if n % 7 == 0:

        break;

    s += n
    print(n)

s = 0
for n in range(1,10):
    if n % 2 ==0:
        continue;
    s+=n
    print(s)

class suma_dos:
    def __init__(self, datos):
        self.datos = datos
        self.indice = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.indice == len(self.datos):
            raise StopIteration()
        elemento = self.datos[self.indice] + 2
        self.indice += 1
        return elemento
for x in suma_dos([1,2,3,4,5]):
    print(x)