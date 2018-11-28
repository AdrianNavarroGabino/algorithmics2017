# Binary numbers
# Adrián Navarro Gabino

a = True
chain = input("Enter a binary number: ")

while chain.count("0") + chain.count("1") != len(chain):
    chain = input("Enter a binary number: ")

print("Correct")
