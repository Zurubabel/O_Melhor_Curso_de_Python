import os

pasta_raiz = os.path.dirname(__file__)

"""try:
    arquivo = ""
    arquivo = open(pasta_raiz + "\\arquisvo.txt", "rt")
    for linha in arquivo.readlines():
        print(linha)
except FileNotFoundError as exp:
    print("Não encontrou o arquivo")
finally:
    if arquivo != "":
        arquivo.close()"""
try:
    with open(pasta_raiz + "\\arquivvo.txt", "rt") as arquivo:
        for linha in arquivo:
            print(linha)
except FileNotFoundError as exp:
    print("Não encontrou o arquivo")
