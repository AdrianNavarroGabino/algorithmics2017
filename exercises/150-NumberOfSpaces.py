# How many spaces in a sentence?
# Adrián Navarro Gabino

sentence = input("Enter a sentence: ")

count = 0

for i in sentence:
    if i == " ":
        count +=1

print(count)
