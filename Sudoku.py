
 
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
 
pasos = 0
retrocediendo = False
 
def validar(num, col, fil):
    # Fila
    if num in tablero[fil]:
        return False
 
    # Columna
    for numcol in range(9):
        if tablero[numcol][col] == num:
            return False
 
    # Cuadrante 3x3
    inicio_f = (fil // 3) * 3
    inicio_c = (col // 3) * 3
    for numfil in range(inicio_f, inicio_f + 3):
        for numcol in range(inicio_c, inicio_c + 3):
            if tablero[numfil][numcol] == num:
                return False
 
    return True
 
 
def fcdisponible():
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return fila, columna
    return -1, -1
 
 
def sudoku():
    global pasos, retrocediendo
 
    fil, col = fcdisponible()
    if fil == -1 and col == -1:
        return True
    else:
        for num in range(1, 10):
            if validar(num, col, fil):
                tablero[fil][col] = num
                pasos += 1
 
                if retrocediendo:
                    print("Retroceso hasta fila", fil + 1, "columna", col + 1)
                    retrocediendo = False
 
                print("Paso", pasos, ": fila", fil + 1, "columna", col + 1, "->", num)
                imprimir()
                print()
 
                if sudoku():
                    return True
 
                tablero[fil][col] = 0
 
        retrocediendo = True
        return False
 
 
def imprimir():
    for fila in range(9):
        if fila % 3 == 0 and fila != 0:
            print("------+-------+------")
        linea = ""
        for columna in range(9):
            if columna % 3 == 0 and columna != 0:
                linea += "| "
            if tablero[fila][columna] == 0:
                linea += ". "
            else:
                linea += str(tablero[fila][columna]) + " "
        print(linea)
 

print("Sudoku inicial:")
imprimir()
 
if sudoku():
    print("\nSudoku resuelto:")
    imprimir()
else:
    print("\nEste sudoku no tiene solución.")