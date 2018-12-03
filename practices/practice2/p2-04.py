# Adrián Navarro Gabino

#! /usr/bin/python3

def leePosicion():
    while True:
        try:
            p = int(input())
            if p >= 0:
                return p
            print("La posición debe ser mayor o igual que 0.")
        except:
            print("Posición incorrecta.")

def leeVector():
    while True:
        try:
            v = [int(x) for x in input().split()]
            if len(v) > 1:
                return v
            print("Un vector de longitud 1 es un escalar.")
        except:
            print("Vector incorrecto.")

def leeLongitud():
    while True:
        try:
            l = int(input())
            if l > 0:
                return l
            print("La longitud debe ser mayor que 0.")
        except:
            print("Longitud incorrecta.")

def Comparar(p,l,n):
    if 0 <= p <= (n-1) and p + l <= n:
        return True
    else:
        return False

def nuevoVector(v,p,l):
    return v[p:p+l]


v = leeVector()
n = len(v)
p = leePosicion()
l = leeLongitud()

if Comparar(p,l,n):
    resultado = nuevoVector(v,p,l)
    for i in resultado:
        print(i,end=" ")
    print()
else:
    print("error")
