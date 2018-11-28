# Searching words in a file
# Adrián Navarro Gabino

def wordInText(filename,word):
    myFile = open(filename,'r')
    M = []
    for line in myFile:
        a = [x for x in linea.split()]
        M.append(a)
    myFile.close()
    for i in M:
        if word in i:
            return True
    return False
        
filename = input("Filename: ")
word = input("Word: ")
if wordInText(filename,word):
    print("The word {0} is in {1}".format(word,filename))
else:
    print("The word {0} is NOT in {1}".format(word,filename))
