# humano = O    IA = X

from doctest import ELLIPSIS_MARKER
import os
import time
tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
victoriaHumano = False
victoriaIA = False
empate = False
posicion = 0
caracter = " "
turno = 1


def imprimirTablero(tablero):
    print(str(" ┌")+str("───")+str("┬")+str("───")+str("┬")+str("───")+str("┐"))
    print(str(" | ")+str(tablero[0])+str(" | ")+str(tablero[1])+str(" | ")+str(tablero[2])+str(" |"))
    print(str(" ├")+str("───")+str("┼")+str("───")+str("┼")+str("───")+str("┤"))
    print(str(" | ")+str(tablero[3])+str(" | ")+str(tablero[4])+str(" | ")+str(tablero[5])+str(" |"))
    print(str(" ├")+str("───")+str("┼")+str("───")+str("┼")+str("───")+str("┤"))
    print(str(" | ")+str(tablero[6])+str(" | ")+str(tablero[7])+str(" | ")+str(tablero[8])+str(" |"))
    print(str(" └")+str("───")+str("┴")+str("───")+str("┴")+str("───")+str("┘"))
def validarVictoriaHumano():
    if tablero[0] == "O" and tablero[1] == "O" and tablero[2] == "O":
        return True
    elif tablero[3] == "O" and tablero[4] == "O" and tablero[5] == "O":
        return True
    elif tablero[6] == "O" and tablero[7] == "O" and tablero[8] == "O":
        return True
    elif tablero[0] == "O" and tablero[3] == "O" and tablero[6] == "O":
        return True
    elif tablero[1] == "O" and tablero[4] == "O" and tablero[7] == "O":
        return True
    elif tablero[2] == "O" and tablero[5] == "O" and tablero[8] == "O":
        return True
    elif tablero[0] == "O" and tablero[4] == "O" and tablero[8] == "O":
        return True
    elif tablero[6] == "O" and tablero[4] == "O" and tablero[2] == "O":
        return True
    else:
        return False
def validarVictoriaIA():
    if tablero[0] == "X" and tablero[1] == "X" and tablero[2] == "X":
        return True
    elif tablero[3] == "X" and tablero[4] == "X" and tablero[5] == "X":
        return True
    elif tablero[6] == "X" and tablero[7] == "X" and tablero[8] == "X":
        return True
    elif tablero[0] == "X" and tablero[3] == "X" and tablero[6] == "X":
        return True
    elif tablero[1] == "X" and tablero[4] == "X" and tablero[7] == "X":
        return True
    elif tablero[2] == "X" and tablero[5] == "X" and tablero[8] == "X":
        return True
    elif tablero[0] == "X" and tablero[4] == "X" and tablero[8] == "X":
        return True
    elif tablero[6] == "X" and tablero[4] == "X" and tablero[2] == "X":
        return True
    else:
        return False
def checarEmpate():
    for elemnto in tablero:
        if elemnto == " ":
            return False
    return True
def posicionLibre(posicion):
    if tablero[posicion-1] == " ":
        return True
    else:
        return False
def insertar(posicion,caracter):
    if posicionLibre(posicion):
        # Inserto en el tablero el caracter en la posicion del jugador actual
        tablero[posicion-1] = caracter
        # Validar si ya se acabo el juego
        if validarVictoriaIA():
            os.system("cls")
            print("  ¡GANA EL IA!")
            imprimirTablero(tablero)
            xd = input()
        elif validarVictoriaHumano():
            os.system("cls")
            print("  !GANA HUMANO¡")
            imprimirTablero(tablero)
            xd = input()
        elif checarEmpate():
            os.system("cls")
            print("  !GANA GATO¡")
            imprimirTablero(tablero)
            xd = input()
    else:
        print("POSICION OCUPADA, ELIGE NUEVAMENTE: ",end=" ")
        posicion = int(input( ))
        insertar(posicion, caracter)
def algoritmoMinimax(tablero,profundidad,Maximizar):
    if validarVictoriaHumano():
        return -1
    elif validarVictoriaIA():
        return 1
    elif checarEmpate():
        return 0

    # juega la IA
    if Maximizar == True:
        mejor = -1000
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = "X"
                puntaje = algoritmoMinimax(tablero,profundidad+1,False)
                tablero[i] = " "
                if puntaje > mejor:
                    mejor = puntaje
        return mejor
    else:
        mejor = 1000
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = "O"
                puntaje = algoritmoMinimax(tablero, profundidad+1, True)
                tablero[i] = " "
                if puntaje < mejor:
                    mejor = puntaje
        return mejor
def moverIA():
    mejor = -1000
    mejorMovimiento = 0
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = "X"
            puntaje = algoritmoMinimax(tablero,0,False)
            tablero[i]=" "
            if puntaje > mejor:
                mejor = puntaje
                mejorMovimiento = i+1
    insertar(mejorMovimiento,"X")
    return
def imprimirTitulo():
    print("  ┌───┬───┬───┐    _____   _____   _____   _____   ┌───┬───┬───┐  ")
    print("  | O | X | X |   |  ___| |  _  | |     | |  _  |  | X |   | X |  ")
    print("  ├───┼───┼───┤   | | __  | |_| | |_   _| | | | |  ├───┼───┼───┤  ")
    print("  | X | O |   |   | ||_ | |  _  |   | |   | | | |  | X | O | O |  ")
    print("  ├───┼───┼───┤   | |__|| | | | |   | |   | |_| |  ├───┼───┼───┤  ")
    print("  | O |   | O |   |_____| |_| |_|   |_|   |_____|  | X |   | O |  ")
    print("  └───┴───┴───┘                                    └───┴───┴───┘  ")
    print("                                                                  ")
    print(" ██      ██  ██████  ██    ██  ██████  ██      ██  ██████  ██  ██ ")
    print(" ████  ████  ▒▒██▒▒  ████  ██  ▒▒██▒▒  ████  ████  ██▒▒██  ██  ██ ")
    print(" ██▒▒██▒▒██  ░░██░░  ██▒▒████  ░░██░░  ██▒▒██▒▒██  ██████  ▒▒██▒▒ ")
    print(" ██░░▒▒░░██    ██    ██░░▒▒██    ██    ██░░▒▒░░██  ██▒▒██  ██▒▒██ ")
    print(" ██  ░░  ██  ██████  ██  ░░██  ██████  ██  ░░  ██  ██░░██  ██░░██ ")
    print(" ▒▒      ▒▒  ▒▒▒▒▒▒  ▒▒    ▒▒  ▒▒▒▒▒▒  ▒▒      ▒▒  ▒▒  ▒▒  ▒▒  ▒▒ ")
    print(" ░░      ░░  ░░░░░░  ░░    ░░  ░░░░░░  ░░      ░░  ░░  ░░  ░░  ░░ ")
    print("                                                                  ")
    print("                          ¿QUIÉN EMPIEZA?                         ")
    print("                              HM = [0]                            ")
    print("                              IA = [1]                            ")
    opcion = int(input())
    if opcion == 0:
        return 1
    else:
        return -1


turno = imprimirTitulo()
while checarEmpate() == False and validarVictoriaHumano() == False and validarVictoriaIA() == False:
    if turno == 1:
        os.system("cls")
        imprimirTablero(tablero)
        print(" TU TURNO : ",end=" ")
        posicion = int(input())
        caracter = "O"
        insertar(posicion, caracter)
    else:
        os.system("cls")
        moverIA()
    turno *= -1
        
        

