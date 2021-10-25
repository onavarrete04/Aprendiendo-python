
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
    for i in range(3):
        for x in range(3):
            # vertical
            if (lista[0] == "x" and lista[1] == "x" and lista[2] == "x"
            or lista[0] == "o" and lista[1] == "o" and lista[2] == "o"):
                print("Ha ganado")
            if (lista[3] == "x" and lista[4] == "x" and lista[5] == "x"
            or lista[3] == "o" and lista[4] == "o" and lista[5] == "o"):
                print("Ha ganado")        
            if (lista[6] == "x" and lista[7] == "x" and lista[8] == "x"
            or lista[6] == "o" and lista[7] == "o" and lista[8] == "o"):
                print("Ha ganado")
            # horizontal
            if (lista[0] == "x" and lista[3] == "x" and lista[6] == "x"
            or lista[0] == "o" and lista[3] == "o" and lista[6] == "o"):
                print("Ha ganado")
            if (lista[1] == "x" and lista[4] == "x" and lista[7] == "x"
            or lista[1] == "o" and lista[4] == "o" and lista[7] == "o"):
                print("Ha ganado")        
            if (lista[2] == "x" and lista[5] == "x" and lista[8] == "x"
            or lista[2] == "o" and lista[5] == "o" and lista[8] == "o"):
                print("Ha ganado")
            # diagonal
            if (lista[0] == "x" and lista[4] == "x" and lista[8] == "x"
            or lista[0] == "o" and lista[4] == "o" and lista[8] == "o"):
                print("Ha ganado")
            if (lista[2] == "x" and lista[4] == "x" and lista[6] == "x"
            or lista[2] == "o" and lista[4] == "o" and lista[6] == "o"):
                print("Ha ganado")        

   
print("inicia la ficha [0]")
usuario = int(input("ingrese 1 para usar el [O] o 2 para [X]"))
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
    else:
        casilla = int(input("casilla del 1 al 9"))
        casilla = casilla - 1
        
        
        if lista_tablero[casilla] != "":
            print("casilla ocupada, intente nuevamente")
        
        else:
            lista_tablero[casilla] = usuario_2
            print(lista_tablero)
            contador += 1
        
    if contador == 9:
        tablero(lista_tablero)
        break
    

