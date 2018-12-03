# Adrián Navarro Gabino

#! /usr/bin/python3

def leeVector():
    while True:
        try:
            v = [int(x) for x in input().split()]
            if len(v) > 1:
                return v
        except:
            print("Escribe un vector correcto.")

def ordenarVector(v):
    for i in range(len(v)):
        minimo = min(v[i:])
        #Tengo que calcular el índice del mínimo de v[i:] porque, si hay
        #valores repetidos, cuando ese valor pasa a la primera posición,
        #su índice es 0 y ya no lee el otro índice del mismo número.
        #A la variable "indice" le tengo que sumar i porque el indice lo calcula
        #desde i hasta el final de la lista por lo que se queda i posiciones
        #por detrás.
        indice = v[i:].index(minimo) + i
        v[indice] = v[i]
        v[i] = minimo
    return v


v = leeVector()
w = ordenarVector(v)

for i in range(len(w)):
    print(w[i],end=" ")
print()
