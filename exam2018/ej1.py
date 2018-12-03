# Adrian Navarro Gabino

def borraPares(lista):
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            del lista[i]
        else:
            i += 1

def eliminaPares(lista):
    lista2 = []
    for i in lista:
        if i%2 != 0:
            lista2.append(i)
    return lista2
