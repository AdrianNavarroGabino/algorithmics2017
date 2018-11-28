# How many characters in a file?
# Adrián Navarro Gabino

filename = input("filename: ")

myFile = open(filename,'r')
a = myFile.readline(1)
steps = 0
while a != "":
    steps += 1
    a = myFile.readline(1)
myFile.close()

print(steps)
