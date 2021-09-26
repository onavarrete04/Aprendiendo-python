tablero = []
for x in range(9):
    tablero.append(" ")

def pantalla():
    espacio = 0  # este es el indice con el que se iniciara
    print("-"*12)
    for fila in range(3):
        for columna in range(3):
            
            print("| ",fila,columna,tablero[espacio],end=" ") # se llamara el indice 0 y se pintara |
        
            espacio += 1 #se sumara otro indice 
        print("\n") # se imprimira | en la siguiente linea 
pantalla()