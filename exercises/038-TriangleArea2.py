# Perimeter and area of a triangle
# Adrián Navarro Gabino

side1 = float(input("Side 1: "))
side2 = float(input("Side 2: "))
side3 = float(input("Side 3: "))

s = (side1+side2+side3)/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
perimeter = side1 + side2 + side3

print(perimeter)
print(area)
