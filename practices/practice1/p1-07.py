# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 7.")
print("Programa que calcula la media aritmetica de las notas aprobadas.")

"""
suma sera la suma de las notas entre 0 y 10.
notas es la lista con las notas que vamos a sumar.
i es la posicion de la lista donde iremos guardando las notas.
"""

suma = 0
notas = []
i = 0

"""
Con el while llenamos la lista de notas hasta que una de las notas introducidas
sea -1, que se para el proceso.
"""

while True:
    n = float(input("Introduce una nota: "))
    if n == -1: break
    if n >= 0 and n <= 10:
        notas.insert(i,n)
        i += 1

"""
Sumamos todas las notas y dividimos por el numero de notas.
Imprimimos el resultado.
"""
    
cantnotas = len(notas)

for j in notas:
    suma += j

print(suma/cantnotas)
