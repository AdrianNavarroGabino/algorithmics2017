# Adrián Navarro Gabino

#! /usr/bin/python3

def leeOrden():
    while True:
        try:
            n = int(input())
            if n > 1:
                return n
            else:
                print("El orden de una matriz cuadrada debe ser mayor que 1.")
        except:
            print("Orden incorrecto.")

def leeMatriz(n):
    M = []
    while True:
        try:
            for i in range(n):
                a = [int(x) for x in input().split()]
                while len(a) != n:
                    print("Debes introducir {0} elementos en la fila.".format(n))
                    a = [int(x) for x in input("Introduce la fila {0} de la " \
                        "matriz separada por espacios: ".format(i+1)).split()]
                M.append(a)
            return M
        except:
            M = []
            print("Fila incorrecta.")

def hacerMedia(M):
    lista = []
    for i in range(n):
        lista.append(M[i][i])
    media = sum(lista)/n
    return media

def maxOpuesta(M):
    lista = []
    for i in range(n):
        lista.append(M[i][n-1-i])
    return max(lista)

def distEuclidea(M):
    a = M[n//2-1]
    b = M[n//2]
    dist = 0
    for i in range(n):
        dist = dist + (a[i] - b[i])**2
    dist = dist**0.5
    return dist
        

n = leeOrden()
M = leeMatriz(n)

print(hacerMedia(M))
print(maxOpuesta(M))
print(distEuclidea(M))
