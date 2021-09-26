import math # se importa la biblioteca math para llamar math.floor

TABLERO_FILAS = 3 
TABLERO_COLUMNAS = 3

tablero = []  # el tablero es una lista

for i in range(9):
    tablero.append(' ') 
    
# tablero.append agrega cada valor a la lista

def numero(literal, inferior, superior): # se establecen 3 variables, literal, inferior y superior
    while True:
        Valor = input (literal)
        while(not Valor.isnumeric()): # isnumeric es para que no agreguen letras
            print("solo se admiten numeros entre {0} y {1}".format(inferior,superior))
            valor = input(literal)
        coor = int(Valor)
        if (coor >= inferior and coor <= superior): # se establece un limite inferior y superior, entendiendo que el tablero es 3 * 3
            return coor
        else:
            print("El valor indicado es incorrecto, introduzca un número entre {0} y {1}". format(inferior,superior))

def colocarFicha(ficha): 
    print("Elije la posición de la ficha en el tablero")
    while True:
        fila = numero("Fila entre [1 y 3]: ",1,3)-1  # se llama la fila, y se establece un rango entre 1 y 3 y se le resta 1 porque el rango seria el 2
        columna = numero("Columna entre[1 y 3]: ",1,3)-1
        casilla = fila*TABLERO_COLUMNAS  + columna
        if tablero[casilla]  != " ": # ya esta cubierta:
            print("La casilla esta ocupada")
        else:
            tablero[casilla] = ficha
            return casilla

def pintar_Tablero():
    pos = 0 # se define la variable pos fuera del cilo para que guarde las variables cada que cambien
    print("-"*18)
    for fila in range(3):
        for columna in range(3):
            print("| ",tablero[pos], end="")
            pos += 1
        print("|\n","-"*12)
    

def numeroHermanos(casilla,ficha, v, h): # se establecen los hermanos para verificar si se gano o no, se establecen 4 variables
    f = math.floor(casilla/TABLERO_COLUMNAS) # se obtiene la fila
    c = casilla % TABLERO_COLUMNAS # es la columna
    fila_nueva = f + v
    if (fila_nueva <0 or fila_nueva >= TABLERO_FILAS):
        return 0
    columna_nueva = c + h
    if(columna_nueva < 0 or columna_nueva >= TABLERO_COLUMNAS):
        return 0
    # se calcula la posición para determinar el limite
    pos = (fila_nueva*TABLERO_COLUMNAS+columna_nueva)
    if(tablero[pos]!= ficha):
        return 0
    else:
        return 1+numeroHermanos(pos,ficha,v,h)

def hemos_Ganado(casilla,ficha): # se verifica si hay elementos iguales en diagonal, vertical y horizontal
    hermanos = numeroHermanos(casilla,ficha,-1,-1)+numeroHermanos(casilla,ficha,1,1)
    if(hermanos == 2):
        return True
    hermanos = numeroHermanos(casilla,ficha,1,-1)+numeroHermanos(casilla,ficha,-1,1)
    if(hermanos == 2):
        return True
    hermanos = numeroHermanos(casilla,ficha,-1,0)+numeroHermanos(casilla,ficha,1,0)
    if(hermanos == 2):
        return True
    hermanos = numeroHermanos(casilla,ficha,0,-1)+numeroHermanos(casilla,ficha,0,1)
    if(hermanos == 2):
        return True

print("La ficha X inicia la partida")   
print("-"*12)  
while True:
    pieza = int(input("Elija la pieza con la que desea jugar, 1 para X y 2 para O"))
    if pieza == 1:
        Usuario_1 = str(input("ingrese su nick jugador 1"))
        Usuario_2 = str(input("ingrese su nick jugador 2"))
        print("Inicie la partida ",Usuario_1) 
        break
    elif pieza == 2:
        Usuario_2 = str(input("ingrese su nick jugador 2"))
        Usuario_1 = str(input("ingrese su nick jugador 1"))
        print("Usuario ",Usuario_2," debido a que eligio la O iniciara la partida el usuario ",Usuario_1)
        break
    elif pieza != 1 or pieza != 2:
        print("Ha ingresado un numero incorrecto, intente nuevamente")
    
    


 
# juego en marcha
continuar = True
ficha_Tablero = 0

 # se establece la variable fuera del ciclo, para que pueda ir guardando los valores


while continuar:
     # mientras la condición sea verdadera continua el ciclo
    
    pintar_Tablero()
    ficha = "O" if (ficha_Tablero & 1 ) else "X"
    casilla = colocarFicha(ficha)
    if ( hemos_Ganado(casilla,ficha)):
       print("Ganaste!!! :", Usuario_2  if (ficha_Tablero & 1 ) else Usuario_1)
       print("La pieza que vencio fue: ","O" if (ficha_Tablero & 1 ) else "X")
       continuar = False
         
    ficha_Tablero += 1

    if (ficha_Tablero == 9):
        continuar = False 
        print("La partida ha sido reñida, ha habido un empate entre ",Usuario_1," y ",Usuario_2)
pintar_Tablero()


