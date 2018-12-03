# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 4.")
print("Programa que calcula los divisores primos de un numero.")

n = int(input("Introduce un numero: "))
divisores = []
i = 0
m = 2


# Si n es un numero no natural, volvemos a pedir el numero.
while n <= 0:
    n = int(input("Introduce un numero mayor que 0: "))

"""
Dividimos en dos casos: que el numero natural sea el numero 1,
que solo se tiene a si mismo de divisor. O que sea cualquier otro
numero natural.
"""

if n == 1:
    print("El numero 1 solo tiene como divisor al numero 1")
else:
    # Para saber si m es elemento de la lista, calculamos el resto
    # de n entre m para ver si m es un divisor de n.
    while m < n:
        if n%m == 0:
            divisores.insert(i,m)
            i += 1
            m += 1
        else:
            m += 1

j = 1

"""
Si el numero que introducimos es el numero 1, lo ponemos como un caso especial.
Si uno de los divisores es multiplo de uno anterior de la lista, lo eliminamos de la lista.
Sino, pasamos al siguiente numero.
"""

if len(divisores) == 0 and n != 1:
    print("El numero {0} es primo.".format(n))
elif len(divisores) != 0 and n != 1:
    while j < len(divisores):
        k = 0
        while k < j:
            if divisores[j] % divisores[k] == 0:
                divisores.remove(divisores[j])
                k = j
                j -= 1
            else:
                k += 1
        j += 1
    for l in range(0,len(divisores) - 1):
        print(divisores[l], end = ", ")
    print(divisores[len(divisores) - 1], end = ".")
