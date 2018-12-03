# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 6.")
print("Programa que calcula la media aritmetica de n numeros.")

"""
Pedimos la cantidad de numeros con los que hacer la media y creamos
una lista vacia para ir llenandola con los valores.
"""

n = int(input("Introduce la cantidad de numeros a leer: "))
numeros = []

while n < 1:
        n = int(input("Introduce la cantidad de numeros a leer: "))

"""
Pedimos cada uno de los numeros que queremos calcular y lo añadimos a
la lista numeros.
"""

for i in range(1,n+1):
	m = int(input("Introduce el numero {0}: ".format(i)))
	numeros.insert(i-1,m)

# La suma comienza con el 0 para despues sumar todos los valores
suma = 0

"""
Sumamos todos los valores y sacamos con el print la division de la suma
entre el numero de valores, que seria la variable n.
"""

for i in numeros:
        suma += i

print(suma/n)
