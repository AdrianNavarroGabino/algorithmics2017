# Adrian Navarro Gabino

def catalan_Rec(n,memo=None):
    if memo == None:
        memo = [0]*(n+1)

    if memo[n] == 0:
        if n == 0:
            memo[n] = 1
        else:
            solucionesParciales = []
            memo[n] = 0
            for i in range(n):
                memo[n] += catalan_Rec(i,memo)*catalan_Rec(n-(i+1),memo)
    return memo[n]


print(catalan_Rec(50))

"""
El coste espacial es de phi(n).
Se puede reducir utilizando como almacen un vector de menor longitud.
"""
