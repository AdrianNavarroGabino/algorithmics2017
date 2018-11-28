# Is a word in a file?
# Adrián Navarro Gabino

def main(filename,word):
    myFile = open(filename,'r')
    count = 0
    for line in myFile:
        a = [x for x in line.split()]
        b = a.count(word)
        count += b
    myFile.close()
    return count

filename = input("Filename: ")
word = input("Word: ")
print(main(filename,word))
