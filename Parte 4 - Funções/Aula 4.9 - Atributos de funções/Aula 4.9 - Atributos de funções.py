def somar(num_1, num_2, num3 = 5, num_8 = "Churros", x= {"a":1}):
    """ Soma dois números """
    return num_1 + num_2

atributos = ["__name__", "__doc__", "__module__", "__defaults__", "__kwdefaults__"]

#for atributo in atributos:
#    print(atributo, " -> ", getattr(somar, atributo))

print(somar.__name__)

#print(somar(1, 2))