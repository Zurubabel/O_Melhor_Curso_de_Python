# Bazuca de matar mosca

class CalcularDoisNumeros():
    num1 = 0
    num2 = 0

    def somar_dois_numeros(self):
        return self.num1 + self.num2

calculadora = CalcularDoisNumeros()
calculadora.num1 = 1
calculadora.num2 = 2

x = (1,2)
print(x[0] + x[1])


print(calculadora.somar_dois_numeros())