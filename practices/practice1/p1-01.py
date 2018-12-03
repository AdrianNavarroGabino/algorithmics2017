# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 1.")
print("Programa que cambia las letras mayusculas a minusculas y viceversa.")

# Pedimos la letra con la que vamos a trabajar.
letra = input("Introduce una letra: ")

"""
Para cumplir con el enunciado, si la variable letra tiene mas de un caracter,
vuelvo a definir la variable con otro input.
"""

while len(letra) > 1:
    letra = input("Introduce SOLO una letra: ")

"""
Separamos la variable letra en tres casos:
1) Que sea minuscula, y la hacemos mayuscula.
2) Que sea mayuscula, y la hacemos minuscula.
3) Que se introduzca un caracter que no se encuentre entre a y z, ni entre
A y Z. Entonces damos un mensaje de error.
"""

if "a" <= letra <= "z":
    print(letra.upper())
elif "A" <= letra <= "Z":
    print(letra.lower())
else:
    print("error")
