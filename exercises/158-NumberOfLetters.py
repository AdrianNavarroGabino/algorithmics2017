# Number of letters
# Adrián Navarro Gabino

chain = input("Enter a chain: ").split()
k = int(input("Number of letters: "))
count = 0

for i in chain:
    if len(i) == k:
        count += 1

print(count)
