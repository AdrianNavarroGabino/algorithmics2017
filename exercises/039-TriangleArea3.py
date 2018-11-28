# Area of a triangle with two sides and an angle
# Adrián Navarro Gabino

from math import sin, pi

a = float(input("Side a: "))
b = float(input("Side b: "))
rho = float(input("Angle (in degrees) between a and b: "))
rho = rho*pi/180

area = a*b*sin(rho)/2

print(round(area,2))
