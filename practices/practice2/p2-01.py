# Adrián Navarro Gabino

#! /usr/bin/python3

def leeNumero():
    while True:
        try:
            lista = [int(x) for x in input().split()]
            #Si la lista es vacía, vuelvo a pedir la lista.
            if len(lista) > 0:
                return lista
        except:
            print("Introduce una lista válida.")

def hacerMedia(x):
    media = sum(x)/len(x)
    return(media)

def desvTipica(x):
    if len(x) == 1:
        return x[0]
    desv = 0
    med = hacerMedia(x)
    for i in x:
        desv = desv + (i - med)**2
    desv = (desv/(len(x)-1))**0.5
    return desv

def hacerModa(x):
    repeticiones = x.count(x[0])
    moda = x[0]
    for i in x:
        if x.count(i) > repeticiones:
            repeticiones = x.count(i)
            moda = i
    return moda


lista = leeNumero()

print(hacerMedia(lista))
print(desvTipica(lista))
print(hacerModa(lista))
