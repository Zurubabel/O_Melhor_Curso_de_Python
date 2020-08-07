try:
    raise(GeneratorExit("Erro de overflow"))
except ZeroDivisionError as er:
    print("Bloco Zero Division")
    print(er)
except ArithmeticError as er:
    print("Bloco Arithmetic")
    print(er)
except Exception as er:
    print("Bloco Exception")
    print(er)
