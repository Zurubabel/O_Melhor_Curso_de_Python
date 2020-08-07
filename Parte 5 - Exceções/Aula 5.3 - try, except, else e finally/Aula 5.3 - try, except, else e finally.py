valor = 0
try:
    print("Início do bloco try")
    print("Calculando valor")
    valor = 3/0
    print("Fim do bloco try")
except Exception as exp:
    print(exp)
else:
    print("Início do bloco else")
    print("O resultado é ", valor)
    print("Fim do bloco else")
finally:
    print("Bloco finally")
