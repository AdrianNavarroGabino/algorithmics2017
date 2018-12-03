# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 8.")
print("Programa que escribe una cantidad de numeros naturales en forma de piramide.")

"""
n es el numero de terminos que queremos poner en la piramide.
m sera el string que iremos imprimiendo con los terminos.
"""

n = int(input("Introduce un numero natural: "))
m = ""

"""
Si la cantidad de terminos es menor que 1, volvemos a pedir la cantidad de
terminos.
"""

while n < 1:
    n = int(input("Introduce un numero natural: "))

"""
Con el primer for imprimimos la parte ascendente de la piramide y con el
segundo for, la parte decreciente.
"""

for i in range(1,n+1):
    m += str(i)
    print(m)

p = n

while p > 0:
    m = ''
    for j in range(1,p):
        m += str(j)
    print(m)
    p -= 1
