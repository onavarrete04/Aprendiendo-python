
lista_tablero = []
for i in range(9):
    
    lista_tablero.append("")



def tablero(lista):
    """
        Se pinta el tablero utilizando las listas anidadas
    """
    pos = 0
    for i in range(3):
        for x in range(3):
            print("|",lista_tablero[pos], end = "" )
            pos +=  1
        print("|")
            
    print("---"*5)

def gano(lista):
    for i in range(9):
            # vertical
            if (lista[0] == "X" and lista[1] == "X" and lista[2] == "X"
            or lista[0] == "O" and lista[1] == "O" and lista[2] == "O"):
                return True 
            if (lista[3] == "X" and lista[4] == "X" and lista[5] == "X"
            or lista[3] == "O" and lista[4] == "O" and lista[5] == "O"):
                return True       
            if (lista[6] == "X" and lista[7] == "X" and lista[8] == "X"
            or lista[6] == "O" and lista[7] == "O" and lista[8] == "O"):
                return True
            
            # horizontal
            if (lista[0] == "X" and lista[3] == "X" and lista[6] == "X"
            or lista[0] == "O" and lista[3] == "O" and lista[6] == "O"):
                return True
            if (lista[1] == "X" and lista[4] == "X" and lista[7] == "X"
            or lista[1] == "O" and lista[4] == "O" and lista[7] == "O"):
                return True       
            if (lista[2] == "X" and lista[5] == "X" and lista[8] == "X"
            or lista[2] == "O" and lista[5] == "O" and lista[8] == "O"):
                return True
            # diagonal
            if (lista[0] == "X" and lista[4] == "X" and lista[8] == "X"
            or lista[0] == "O" and lista[4] == "O" and lista[8] == "O"):
                return True
            if (lista[2] == "X" and lista[4] == "X" and lista[6] == "X"
            or lista[2] == "O" and lista[4] == "O" and lista[6] == "O"):
                return True   
                

   

usu = input("primer jugador ingrese su nombre")
usu_2 = input("primer jugador ingrese su nombre")
usuario = int(input("ingrese 1 para usar el [O] o 2 para [X]"))
print("INICIA PRIMER JUGADOR")
usuario_1 = ""
usuario_2 = ""
if usuario == 1:
    usuario_1 = "O"
    usuario_2 = "X"
    print("inicia el usuario 1")
else:
    usuario_1 = "X"
    usuario_2 = "O"
    print("inicia el usuario 2")

contador = 0 
        
while True:

    tablero(lista_tablero)
    if contador %2 == 0:
        
        casilla = int(input("casilla del 1 al 9"))
        casilla = casilla - 1
        if lista_tablero[casilla] != "":
            print("casilla ocupada, intente nuevamente")
        
        else:
            lista_tablero[casilla] = usuario_1
            print(lista_tablero)
            contador += 1
            if gano(lista_tablero) == True:
                print("el usuario ",usu," ha ganado - ficha victoriosa, ",usuario_1)
                tablero(lista_tablero)
                break

    else:
        casilla = int(input("casilla del 1 al 9"))
        casilla = casilla - 1 
        
        
        if lista_tablero[casilla] != "":
            print("casilla ocupada, intente nuevamente")
        
        else:
            lista_tablero[casilla] = usuario_2
            print(lista_tablero)
            contador += 1
            if gano(lista_tablero) == True:
                print("el usuario ",usu_2," ha ganado - ficha victoriosa, ",usuario_2)
                break 

        
    if contador == 9:
                    
        print("LA PARTIDA ESTUVO REÑIDA, HUBO UN EMPATE")
        break
        
    
        


        
    

