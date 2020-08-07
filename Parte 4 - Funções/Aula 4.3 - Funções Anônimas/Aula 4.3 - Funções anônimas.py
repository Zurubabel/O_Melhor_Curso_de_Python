"""def somar(a, b):
    return a + b

x = lambda a, b: a + b

#print(x(43, 11))

print(somar)
print(x)"""

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

def multiplicar(x, y):
    return x * y

print(calcular(30, 20, lambda a, b: b - a))