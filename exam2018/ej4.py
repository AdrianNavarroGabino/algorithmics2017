# Adrian Navarro Gabino

def catalan(n):
    if n == 0:
        C_n = 1
        return C_n
    if n >= 1:
        C_n = 0
        for i in range(n):
            C_n += catalan(i)*catalan(n-(i+1))
        return C_n

print(catalan(15))

"""
Para n=20 el numero de llamadas recursivas es muy grande y Python no es capaz
de resolverlo en un tiempo aceptable.
"""
#print(catalan(20))
