# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 9")
print("Programa que escribe la sucesion de Fibonacci hasta un cierto termino")

"""
Pedimos el numero de terminos que queremos calcular y la lista que llenaremos
con la sucesion de Fibonacci.
"""

n = int(input("Introduce un numero natural: "))
f = []

"""
Si el numero de numeros que introducimos en el input es menor que 1, volvemos
a pedir el numero de terminos.
"""

while n < 1:
    n = int(input("Introduce un numero natural: "))

"""
Diferenciamos entre que el numero de terminos sea 1 o 2, o que sea un numero
mayor, ya que la sucesion se define de manera diferente para esos dos casos.
"""

if n <= 2:
    for i in range(1,n+1):
        f.insert(i-1,i-1)
    print(f)
else:
    for i in [1,2]:
        f.insert(i - 1,i - 1)
    for i in range(3,n+1):
        f.insert(i - 1,f[i - 2] + f[i - 3])
    for j in range(0,len(f) - 1):
        print(f[j], end = ", ")
    print(f[len(f) - 1], end = ".")
