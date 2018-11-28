# Capital conversion through years
# Adrián Navarro Gabino

C = round(float(input("Euros: ")),2)
x = float(input("Interest rato: "))
n = int(input("Number of years: "))

final = C * (1 + x/100)**n

print(round(final,2))
