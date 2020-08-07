# Declaração de funções
# 1 - Parâmetros posicionais
# 2 - Parâmetros facultativos (x = "shj")
# 3 - Parâmetro de posição variável
# 4 - Parâmetros de somente palavras-chave

def iugh(x, y, z, a = "Jujuba", *args, d, **kwargs):
    print(x)
    print(y)
    print(z)
    print(a)
    print(args)
    print(d)
    print(kwargs)
    pass

iugh(1, 2, 3, "a", "b", "c", "d", d = "asd")