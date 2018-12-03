# Adrián Navarro Gabino

# /usr/bin/python3

print("Practica 1. Ejercicio 10.")
print("Programa que calcula la raiz cuadrada de un numero")

"""
Definimos la variable que queremos operar, a, y el que sera el resultado, sqrt.

Multiplicamos a por 1000 para minimizar el error de los decimales (despues se
deshace).

Partimos de que sqrt = a y, mientras que al multiplicar sqrt por si mismo,
sea mayor que a, le restamos 1.

Volvemos a colocar la coma de los decimales en su sitio e imprimimos el
resultado.
"""
try:
    a = float(input("Introduce un numero: "))
    a = a*1000
    sqrt = a
    if a >= 0:
        while sqrt*sqrt/1000 > a:
            sqrt -= 1
        sqrt /= 1000
        print(sqrt)
    elif a < 0:
        print("a debe ser un numero entero no negativo.")
except:
    print("Debes introducir un numero.")
