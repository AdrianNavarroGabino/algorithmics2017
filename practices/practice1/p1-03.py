# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 3.")
print("Programa que muestra los divisores de un numero.")

"""
Definimos n que es el numero del que queremos saber los
divisores.
divisores, que es la lista que vamos a ir llenando.
i, que son las posiciones dentro de la lista divisores.
Y m, que son los posibles elementos de la lista.
"""

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
    print("El numero 1 solo tiene como divisor al numero 1.")
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

# Si la lista esta vacia, quiere decir que n es un numero primo.            
if len(divisores) == 0 and n != 1:
    print("El numero {0} es primo".format(n))
# En caso contrario, imprimimos la lista de divisores.
elif len(divisores) != 0 and n != 1:
    for j in divisores[:i-1]:
        print(j, end = ", ")
    for j in divisores[i-1:i]:
        print(j, end = ".")
