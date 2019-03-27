def comprobarPartida(tabla, ficha):
    if tabla[0][0] == ficha:
        if tabla[1][0] == ficha and tabla[2][0] == ficha:
            return True
        if tabla[0][1] == ficha and tabla[0][2] == ficha:
            return True
        if tabla[1][1] == ficha and tabla[2][2] == ficha:
            return True
    if tabla[0][1] == ficha:
        if tabla[1][1] == ficha and tabla[2][1] == ficha:
            return True
    if tabla[0][2] == ficha:
        if tabla[1][2] == ficha and tabla[2][2] == ficha:
            return True
        if tabla[1][1] == ficha and tabla[2][0] == ficha:
            return True
    return False

def imprimirTabla(tabla):
    print("-------------")
    for i in range(len(tabla)):
        print("|", end="")
        for j in range(len(tabla[0])):
            print(" " + tabla[i][j] + " |", end="")
        print()
        print("-------------")

partidaAcabada = False
fichas = ["o","x"]
turno = 0
tabla = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

while not partidaAcabada:
    imprimirTabla(tabla)
    
    print()
    print("Turno de \"%s\"." % (fichas[turno % 2]))
    movimiento = [int(x) for x in input("Introduce movimiento: ").split()]

    if len(movimiento) == 2 and 1 <= movimiento[0] <= 3 and 1 <= movimiento[1] <= 3 and tabla[movimiento[0] - 1][movimiento[1] - 1] == " ":
        print("Movimiento correcto.")
    else:
        while not (len(movimiento) == 2 and 1 <= movimiento[0] <= 3 and 1 <= movimiento[1] <= 3 and tabla[movimiento[0] - 1][movimiento[1] - 1] == " "):
            print("Movimiento incorrecto.")
            movimiento = [int(x) for x in input("Introduce movimiento: ").split()]
            if len(movimiento) == 2 and 1 <= movimiento[0] <= 3 and 1 <= movimiento[1] <= 3 and tabla[movimiento[0] - 1][movimiento[1] - 1] == " ":
                print("Movimiento correcto.")
    
    tabla[movimiento[0] - 1][movimiento[1] - 1] = fichas[turno % 2]
    
    if comprobarPartida(tabla, fichas[turno % 2]) or turno == 8:
        if comprobarPartida(tabla, fichas[turno % 2]):
            print("Ha ganado \"%s\"." % (fichas[turno % 2]))
        elif turno == 8:
            print("No quedan movimientos.")

        imprimirTabla(tabla)

        nuevaPartida = input("¿Empezamos de nuevo? s/n: ").lower()
        if nuevaPartida == "s":
            turno = 0
            tabla = [[" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]]
        else:
            partidaAcabada = True
    else:
        turno += 1