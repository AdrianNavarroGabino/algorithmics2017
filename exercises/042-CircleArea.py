# Perimeter and area of a circunference
# Adrián Navarro Gabino

from math import pi

radius = float(input("Radius: "))

area = pi * radius**2
perimeter = 2 * pi * radius

print(round(area,2))
print(round(perimeter,2))
