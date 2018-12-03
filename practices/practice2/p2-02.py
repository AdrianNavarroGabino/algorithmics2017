# Adrián Navarro Gabino

#! /usr/bin/python3

def longitud():
    while True:
        try:
            n = int(input())
            if n > 0:
                return n
        except:
            print("Introduce una longitud correcta.")

def leeVector(n,cad):
    while True:
        v = [float(x) for x in input().split()]
        if len(v) == n:
            return v
        else:
            print("El vector debe ser de longitud {0}".format(n))

def Comparar(v,w,n):
    for i in range(n):
        if v[i] > w[i]:
            return 1
        elif v[i] < w[i]:
            return -1
    return 0


n = longitud()
v = leeVector(n,"primer")
w = leeVector(n,"segundo")

print(Comparar(v,w,n))
