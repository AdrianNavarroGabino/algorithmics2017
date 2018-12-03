# Adrian Navarro Gabino

def recorta(M,i=None,j=None):
    if i == None and j == None:
        M2 = M[:]
    else:
        #Para trabajar con indices normales (empezando en 0):
        i,j = i-1,j-1
        M2 = []
        if i > len(M)-1 or j > len(M[0])-1:
            pass
        elif i <= 0:
            if j <= 0:
                M2 = M[:]
            else:
                for x in range(len(M)):
                    M2.append([M[x][y] for y in range(j,len(M[0]))])
        else:
            for x in range(i,len(M)):
                M2.append([M[x][y] for y in range(j,len(M[0]))])
    return M2
