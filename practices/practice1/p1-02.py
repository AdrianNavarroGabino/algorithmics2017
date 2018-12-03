# Adrián Navarro Gabino

#! /usr/bin/python3

print("Practica 1. Ejercicio 2.")
print("Programa que lee una fecha en el formato dd/mm/aaaa.")

"""
Pedimos el dia, mes y año para despues comprobar si son correctos.
"""

dia = int(input("Introduce un dia: "))
mes = int(input("Introduce un mes: "))
año = int(input("Introduce un año: "))

"""
Si el año no entra dentro del formato aaaa, pedimos otro año que
este entre el 0 y el 9999.

Si el mes no esta entre el 1 y el 12, pedimos un mes correcto.
"""

while año < 0 or año > 9999:
    año = int(input("Introduce un año entre el 0 y el 9999: "))
while mes < 1 or mes > 12:
    mes = int(input("Introduce un mes correcto: "))
    
"""
Creamos dos listas para diferenciar los meses que tienen
31 dias de los que tienen 30.

Febrero como es un unico elemento no necesita lista.
"""

dias31 = [1,3,5,7,8,10,12]
dias30 = [4,6,9,11]

"""
Con el if, diferenciamos entre los meses que tienen 31 dias,
los de 30 y febrero.

Si en los de 31 y 30 no se introduce un numero correcto, se
vuelve a pedir uno que lo sea.

En el caso de febrero, diferenciamos entre que el año sea
bisiesto o no y, por tanto, que pueda haber 28 o 29 dias.
"""

if mes in dias31:
    while dia < 1 or dia > 31:
        dia = int(input("Introduce un dia correcto: "))
elif mes in dias30:
    while dia < 1 or dia > 31:
        dia = int(input("Introduce un dia correcto: "))
else:
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        while dia < 1 or dia > 29:
            dia = int(input("Introduce un dia correcto: "))
    else:
        while dia < 1 or dia > 28:
            dia = int(input("Introduce un dia correcto: "))
    
print(str(dia).zfill(2) + "/" + str(mes).zfill(2) + "/" + str(año).zfill(4))

