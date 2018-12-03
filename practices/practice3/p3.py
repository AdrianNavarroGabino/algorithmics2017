# Adrián Navarro Gabino

from sys import argv

#-------------------------
#  Leer e imprimir el laberitno: p3-1.py
#--------------------------
def leeMaze(fichero):
    maze = []
    for linea in fichero:
        l = linea.split()
        if len(l) != 0:
            maze.append([int(x) for x in linea.split()])
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                maze[i][j] = False
            else:
                maze[i][j] = True
    return maze


def imprime(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()

#-------------------------
#  Divide y venceras recursivo: p3-2.py
#--------------------------
def pequeno(maze, x, y):
    return x == len(maze)-1 and y == len(maze[0])-1 


def trivial(maze, x, y):
    if maze[x][y]:
        return 1
    return 0


def descomponer(maze, x, y):
    subP = []
    if maze[x][y]:
        if x < len(maze)-1: subP.append((x+1, y))
        if y < len(maze[0])-1: subP.append((x, y+1))
        if x < len(maze)-1 and y < len(maze[0])-1: subP.append((x+1, y+1))
    return subP


def combinar(solP):
    return sum(solP)


def maze_DyV(maze, x=None, y=None):
    if x == None: x = 0
    if y == None: y = 0
    
    if pequeno(maze, x, y):
        return trivial(maze, x, y)
    
    solucionesParciales = []
    for q in descomponer(maze, x, y):
        solucionesParciales.append(maze_DyV(maze, q[0], q[1]))
    return combinar(solucionesParciales)
#-------------------------
#  Programación dinámica recursiva (memoización) p3-3.py
#--------------------------
def maze_PD_Rec(maze, memo, x=None, y=None):
    if x == None: x = 0
    if y == None: y = 0

    if memo[x][y] == -1:
        if pequeno(maze, x, y):
            memo[x][y] = trivial(maze, x, y)
        else:   
            solucionesParciales = []
            for q in descomponer(maze, x, y):
                    solucionesParciales.append(maze_PD_Rec(maze, memo, q[0], q[1]))
            memo[x][y] = combinar(solucionesParciales)
    return memo[x][y]


def printMemo(memo):
    print('Memoization (recursive DP) table:')
    for row in memo:
        for i in row:
            if i != -1:
                print(i, end=' ')
            else:
                print('-', end=' ')
        print()
    print()

#-------------------------
#  Programación dinámica iterativa p3-4.py
#--------------------------
def maze_DP_iter(maze):
    A = []
    for i in range(len(maze)):
        A.append([0]*len(maze[0]))
    if maze[0][0]:
        A[0][0] = 1
        j = 1
        while j < len(maze[0]) and maze[0][j]:
            A[0][j] = 1
            j += 1
        i = 1
        while i < len(maze) and maze[i][0]:
            A[i][0] = 1
            i += 1
    for i in range(1, len(maze)):
        for j in range(1, len(maze[0])):
            if maze[i][j]:
                A[i][j] = A[i-1][j] + A[i][j-1] + A[i-1][j-1]
    return A

def printDPTable(A):
    print('Iterative dynamic programming table:')
    for row in A:
        for x in row:
            print(x, end=' ')
        print()

#-------------------------
#  Programación dinámica iterativa almacen unidimensional p3-5.py
#--------------------------
def maze_DP_unidimensional(maze):
    A = [0]*len(maze[0])
    B = [0]*len(maze[0])
    if maze[0][0]: A[0] = 1
    i = 1
    while i < len(A) and maze[0][i]:
        A[i] = 1
        i += 1
    for i in range(1, len(maze)):
        if maze[i][0]: B[0] = A[0]
        else: B[0] = 0
        for j in range(1, len(A)):
            if maze[i][j]:
                B[j] = B[j-1] + A[j-1] + A[j]
            else: B[j] = 0 
        A, B = B, A
    return A[len(A)-1]

#-------------------------
#  Camino de salida: p3-6.py
#--------------------------
def printExitPath(maze):
    M = maze_DP_iter(maze)
    print('A possible dynamic programming exit path:')
    length = 0
    if M[0][0] == 0: print('No accessway')
    elif M[-1][-1] == 0: print('No exit')
    else:
        i = len(M) - 1
        j = len(M[0]) - 1
        length += 1
        while i != 0 or j != 0:
            maze[i][j] = '*'
            if i > 0 and j > 0 and M[i-1][j-1] != 0: i, j = i-1, j-1
            elif i > 0 and M[i-1][j] != 0: i -= 1
            elif j > 0:  j -= 1
            else: print('Somtehing wrong in printExitPath()')
            length += 1
        maze[i][j] = '*'
        for row in maze:
            for x in row:
                if x == True: print(1, end=' ')
                elif x == False: print(0, end=' ')
                else: print('*', end=' ')
            print()
    print('Path length =', length)
            
#-------------------------
#  Greedy:     p3-7.py
#--------------------------
def maze_Greedy(maze):
    print('A greedy path:')
    length = 0
    if not maze[0][0]: print('No accessway')
    else:
        maze[0][0] = '*'
        length += 1
        i = 0
        j = 0
        while True:
            if i + 1 < len(maze) and j + 1 < len(maze[0]) and \
                maze[i+1][j+1]: i, j = i+1, j+1
            elif j + 1 < len(maze[0]) and maze[i][j+1]: j += 1
            elif i + 1 < len(maze) and maze[i+1][j]: i += 1
            else: break
            length += 1
            maze[i][j] = '*'
        if i != len(maze)-1 or j != len(maze[0])-1: length = 0
        for row in maze:
            for x in row:
                if x == True: print(1, end=' ')
                elif x == False: print(0, end=' ')
                else: print('*', end=' ')
            print()
        if length == 0:
            print('Blocked')
    print('Path length =', length)



#--------------------------
def main():
    if len(argv) != 2:
        print('Usage: python3', argv[0], 'filename')
    else:
        try:
            fichero = open(argv[1], 'r')
            maze = leeMaze(fichero)
            fichero.close()
            #print('Recursive:', maze_DyV(maze))
            #memo = []
            #for i in range(len(maze)):
            #    memo.append([-1]*len(maze[0]))
            #print('Memoization:', maze_PD_Rec(maze, memo))
            #print()
            #printMemo(memo)
            #A = maze_DP_iter(maze)
            #print('Iterative table: ...', A[len(A)-1][len(A[0])-1])
            #print()
            #printDPTable(A)
            #print('Iterative 2-vectors:', maze_DP_unidimensional(maze))
            #printExitPath(maze)
            maze_Greedy(maze)
        except IOError:
            print('Can\'t open file', argv[1])


if __name__ == '__main__':
    main()
