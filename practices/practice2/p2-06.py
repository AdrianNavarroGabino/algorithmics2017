# Adrián Navarro Gabino

#! /usr/bin/python3

def numEntero(cad):
    while True:
        try:
            n = int(input())
            if n > 0:
                return n
            else:
                print("El número de {0} debe ser mayor que 0".format(cad))
        except:
            print("Número de {0} incorrecto.".format(cad))

def leeMatriz(n,m):
    M = []
    while True:
        try:
            for i in range(n):
                a = [int(x) for x in input().split()]
                while len(a) != m:
                    print("Debes introducir {0} elementos en la fila " \
                          "{1}.".format(m,i+1))
                    a = [int(x) for x in input("Introduce la fila {0}" \
                        " separada por espacios: ".format(i+1)).split()]
                M.append(a)
            return M
        except:
            M = []
            print("Fila incorrecta.")
    

def matrizTraspuesta(M,n,m):
    Mt = []
    for i in range(m):
        a = [M[j][i] for j in range(n)]
        Mt.append(a)
    return Mt

def prodMatriz(M,n,m):
    MporMt = []
    for i in range(n):
        a = [0]*n
        MporMt.append(a)
    a = 0
    for i in range(n):
        for j in range(m):
            a = a + M[i][j]*M[i][j]
        MporMt[i][i] = a
        a = 0
    for i in range(n-1):
        for j in range(1,n):
            for k in range(m):
                a = a + M[i][k]*M[j][k]
            MporMt[i][j] = a
            MporMt[j][i] = a
            a = 0
    return MporMt

n = numEntero("filas")
m = numEntero("columnas")

while n == 1 and m == 1:
    print("Una matriz 1x1 es un escalar.")
    n = numEntero("filas")
    m = numEntero("columnas")

M = leeMatriz(n,m)

Mt = matrizTraspuesta(M,n,m)

for i in range(m):
    for j in range(n-1):
        print(Mt[i][j],end=" ")
    print(Mt[i][n-1])

MporMt = prodMatriz(M,n,m)

print()

for i in range(n):
    for j in range(n-1):
        print(MporMt[i][j],end=" ")
    print(MporMt[i][n-1])
