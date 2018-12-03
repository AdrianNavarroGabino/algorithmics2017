# Adrián Navarro Gabino

#! /usr/bin/python3

def leeEntero(a):
    n = int(input())
    return n

def leeVector(n):
    while True:
        try:
            v = [float(x) for x in input().split()]
            if len(v) == n:
                return v
            print("La longitud del vector debe ser {0}".format(n))
        except:
            print("Vector incorrecto.")

def leemVectores(m,n):
    M = []
    while True:
        try:
            for i in range(m):
                a = [float(x) for x in input().split()]
                while len(a) != n:
                    print("El vector debe tener {0} elementos.".format(n))
                    a = [int(x) for x in input("Introduce el vector {0} " \
                        "separado por espacios: ".format(i+1)).split()]
                M.append(a)
            return M
        except:
            M = []
            print("Vector incorrecto.")

def distEuclidea(a,b):
    dist = 0
    for i in range(n):
        dist = dist + (a[i] - b[i])**2
    dist = dist**0.5
    return dist

def Comparar(v,M):
    N = []
    for i in range(m):
        a = distEuclidea(v,M[i])
        N.append(a)
    b = N.index(min(N))
    return M[b]


n = leeEntero("n (longitud del vector)")
m = leeEntero("m (número de vectores)")
v = leeVector(n)
M = leemVectores(m,n)

w = Comparar(v,M)

for i in range(n):
    print(w[i],end=" ")
print()
