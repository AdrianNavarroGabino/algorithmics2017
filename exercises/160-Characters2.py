# Words of n characters (version 2)
# Adrián Navarro Gabino

sentence = input("Enter a sentence: ")
k = int(input("Enter the number of characters: "))

sentence = sentence.split()
count = 0

for i in sentence:
    if len(i) == k:
        count += 1

if count == len(sentence):
    print("Sí")
else:
    print("No")
