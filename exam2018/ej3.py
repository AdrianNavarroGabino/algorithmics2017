# Adrian Navarro Gabino

from sys import argv

def leer(filename):
    archivo = open(filename,'r')
    dato_inutil = archivo.readline()
    n = archivo.readline()
    n = int(n)
    matriz_de_valores = []
    for i in range(n):
        linea = archivo.readline()
        matriz_de_valores.append([float(x) for x in linea.split()])
    archivo.close()
    return matriz_de_valores

def copiar(filename,matriz_de_valores):
    archivo = open(filename,'w')
    for i in range(len(matriz_de_valores)):
        archivo.write(str(matriz_de_valores[i][0]))
        archivo.write(" ")
    archivo.write("\n")
    for i in range(len(matriz_de_valores)):
        archivo.write(str(matriz_de_valores[i][1]))
        archivo.write(" ")
    archivo.write("\n")
    archivo.close()

try:
    matriz_de_valores = leer(argv[1])
    copiar(argv[2],matriz_de_valores)
except:
    print("error")
