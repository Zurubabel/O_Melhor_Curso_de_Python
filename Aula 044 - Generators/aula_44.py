# Aula 44 - Funções Generator
#   Conceito de Generators
#   Entendendo o yeld
#   Um pouco mais do __next__

# Importação para calcular a diferença de tempo
from time import time

#def retornar_numeros(n):
#    return [numero for numero in range(0, n)]

#print(retornar_numeros(50))

def retornar_com_generator(n):
    for numero in range(0, n):
        yield numero

x = retornar_com_generator(4)

#print(list(x))

#for numero in x:
#    print(numero)

#for numero in x:
#    print(numero)

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# print(tempo passado: "{:.4f} segundos".format(time() - t)
