TABLERO_FILAS = 3
TABLERO_COLUMNAS = 3

tablero = []  # se hace solo con un talbero que se multiplica por 9

for i in range(9):
    tablero.append(' ') 
    
# tablero.append agrega cada valor a la lista

def numero(literal, inferior, superior):
    while True:
        Valor = input (literal)
        while(not Valor.isnumeric()):
            print("solo se admiten numeros entre {0} y {1}".format(inferior,superior))
            valor = input(literal)
        coor = int(Valor)
        if (coor >= inferior and coor <= superior):
            return coor
        else:
            print("El valor indicado es incorrecto, introduzca un número entre {0} y {1}". format(inferior,superior))

def colocarFicha(ficha):
    print("Elije la posición de la ficha en el tablero")
    while True:
        fila = numero("Fila entre [1 y 3]: ",1,3)-1
        columna = numero("Columna entre[1 y 3]: ",1,3)-1
        casilla = fila*TABLERO_COLUMNAS  + columna
        if (tablero[casilla]  != " "): # ya esta cubierta:
            print("La casilla esta ocupada")
        if(tablero[casilla] == ficha):
            return casilla

def pintar_Tablero():
    pos = 0
    print("-"*18)
    for fila in range(3):
        print("| ",tablero[pos], end="")
        pos += 1
    print("|\n",("_"*12))

def numeroHermanos(casilla, v, h):
    f = math.floor(casilla/TABLERO_COLUMNAS)
    c = casilla % TABLERO_COLUMNAS
    fila_nueva = f + v
    if (fila_nueva <0 or fila_nueva >= TABLERO_FILAS):
        return 0
    columna_nueva = c + h
    if(columna_nueva < 0 or columna_nueva >= TABLERO_COLUMNAS):
        return 0

    pos = (fila_nueva*TABLERO_COLUMNAS+columna_nueva)
    if(tablero[pos]!= ficha):
        return 0
    else:
        return 1+numeroHermanos(pos,ficha,v,h)

def hemos_Ganado(casilla,ficha):
    hermanos = numeroHermanos(casilla,-1,-1)+1+numeroHermanos(casilla,1,1)
    if(hermanos == 2):
        return True
    hermanos = numeroHermanos(casilla,1,-1)+1+numeroHermanos(casilla,-1,1)
    if(hermanos == 2):
        return True
    hermanos = numeroHermanos(casilla,-1,0)+1+numeroHermanos(casilla,1,0)
    if(hermanos == 2):
        return True
    hermanos = numeroHermanos(casilla,0,-1)+1+numeroHermanos(casilla,0,1)
    if(hermanos == 2):
        return True
    

Usuario_1 = str(input("ingrese su nick jugador 1"))
Usuario_2 = str(input("ingrese su nick jugador 2"))

# juego en marcha
continuar = True
ficha_Tablero = 0

 # se establece la variable fuera del ciclo, para que pueda ir guardando los valores


while continuar:
     # mientras la condición sea verdadera continua el ciclo
    
    pintar_Tablero()
    ficha = "X" if (ficha_Tablero & 1 ) else "O"
    casilla = colocarFicha(ficha)
    if ( hemos_Ganado(casilla,ficha)):
       continuar = False
       print("Has ganado")  
    ficha_Tablero += 1
    if (ficha_Tablero == 9):
        continuar = False 
print(pintar_Tablero())


