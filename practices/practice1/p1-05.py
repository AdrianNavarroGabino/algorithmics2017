# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 5.")
print("Programa que calcula una cantidad de primos que no tengan el 3 en la ultima cifra")

"""
Definimos con un input la cantidad de primos que queremos.
Definimos la posicion en la lista de primos, que ira variando.
La lista de primos, que empezamos con el primer numero primo, e iremos
llenandola.
Almaceno en una variable la longitud de la lista de primos, que tambien se
ira actualizando dentro del bucle.
"""

numero_de_primos=int(input("Introduce el numero de primos: "))
posicion_en_lista = 1
primos = [2]
numero_a_probar = 3
cantidad_de_primos_actual = len(primos)

"""
Si se piden menos de un numero primo, se vuelve a pedir el numero de primos.
"""

while numero_de_primos < 1:
    numero_de_primos=int(input("Introduce el numero de primos: "))

"""
Dentro del while vamos buscando todos los numeros primos, y eliminando de la
lista aquellos cuya ultima cifra es un 3.
"""

while cantidad_de_primos_actual < numero_de_primos:
    cantidad_de_primos_actual = len(primos)
    listaprimo = []
    for i in range(0,cantidad_de_primos_actual):
        if numero_a_probar % primos[i] != 0:
            listaprimo.append(i)
        if len(listaprimo) == cantidad_de_primos_actual:
            primos.append(numero_a_probar)  
    for j in range(3,primos[len(primos)-1]+1,10):
        if j in primos:
            primos.remove(j)
        for k in primos:
            if k % j == 0:
                primos.remove(k)
    numero_a_probar += 1

for m in primos[:len(primos)-1]:
    print(m, end = ', ')
print(primos[len(primos)-1], end = '.')
