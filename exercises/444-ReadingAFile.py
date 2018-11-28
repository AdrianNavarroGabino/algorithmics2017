# Display text from a file
# Adrián Navarro Gabino

filename = input("Filename: ")

myFile = open(filename,'r')
i = 1
for line in myFile:
    print(i,line,end="")
    i += 1
