# los generadores devuelven una secuencia, pero en vez de ejecutarla completamente
# esta lo hace pausadamente cada vez que la llamamos, por ejemplo si la llamamos la 
# primera vez solo se ejecuta una vez asi este en rango, además, no utiliza el return sino 
# el yield 

def primeros_1000():
    "Genera los primeros 1000 números"
    for x in range(1000):
        yield x

generador_primeros_100 = primeros_1000()
print(generador_primeros_100)
for x in generador_primeros_100:
    print(x)


def numeros_pares(n):
    return (x for x in range(n) if x % 2 == 0)

gen = numeros_pares(15)

gen.__next__()
gen.__next__()

print("_________________________________")
print(list(gen))