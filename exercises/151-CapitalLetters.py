# How many capital letters in a sentence?
# Adrián Navarro Gabino

sentence = input("Enter a sentence: ")

count = 0

for i in sentence:
    if "A" <= i <= "Z":
        count += 1

print(count)
