import os

#print(os.path.dirname(__file__))

pasta_raiz = os.path.dirname(__file__)


arquivo = open(pasta_raiz + "\\arquivo.txt", "rt")

for linha in arquivo.readlines():
    print(linha)

#print(arquivo.readline())

arquivo.close()
