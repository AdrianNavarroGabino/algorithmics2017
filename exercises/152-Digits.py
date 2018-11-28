# Digits in a chain?
# Adrián Navarro Gabino

chain = input("Enter a chain: ")

count = 0

for i in chain:
    if "0" <= i <= "9":
        count += 1

if count > 0:
    print("It contains digits")
else:
    print("It doesn't contain digits")
