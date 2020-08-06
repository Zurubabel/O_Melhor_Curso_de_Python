# Tudo é público
# Padrão do underline
# Underline duplo e visualização (_A__x)
# Cuidado com __x__

class A:
    x = 0
    _x = 1
    __x = 2

    def exibir_dois_underlines(self):
        print(self.__x)

a = A()

#a.exibir_dois_underlines()
print(a._A__x)