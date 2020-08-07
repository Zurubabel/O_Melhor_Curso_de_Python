# Parâmetros posicionais
# Parâmetros facultativos
    # Um dos últimos parâmetros
# Parâmetros de palavras-chave
# Parâmetros de posição variável
# Parâmetros de palavras-chave de posição variável
# Argumento somente de palavras-chave

def somar(num_1, num_2, num_3, num_4):
    return num_1 + num_2 + num_3 + num_4

#print(somar(num_4 = 10, num_2 = 22, num_1 = 9, num_3 = 10))
# somar(10, 20, 30, 40)

vals = {"num_1":10, "num_2":20, "num_3": 30, "num_4":40}

print(somar(**vals))

def somar_2(*args):
    resultado = 0
    for num in args:
        resultado += num

    print(resultado)


def printar(*args):
    for valor in args:
        print(valor)
        print(type(valor))

def variaveis_palavra_chave(**kwargs):
    print(kwargs)
    print(type(kwargs))

d = {"a": 1, "b": 2, "c": 3}

def param_somentePalavraChave(*args, c = ""):
    print(args, c)

param_somentePalavraChave(1, 2, 3, 4, 1, c = "sd")

#variaveis_palavra_chave(**d)

#printar(1, 2.3, "x", (1,2), [1,2], {"a":1})

#somar_2(1, 3, 4, 6, 1, 5, 6, 2, 32, 344, 304, 90, "is")
#numeros = [10, 20, 30, 40]

#print(somar(*numeros))

#print(somar_2(1, 2, 3, 4, 5))