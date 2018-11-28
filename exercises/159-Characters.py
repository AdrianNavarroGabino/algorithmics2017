# Words of n characters
# Adrián Navarro Gabino

sentence = input("Enter a sentence: ")
k = int(input("Enter the number of characters: "))

sentence = sentence.split()
count = 0

for i in sentence:
    if len(i) == k:
        count += 1

print("Words of {0} characters: {1}".format(k,count))
