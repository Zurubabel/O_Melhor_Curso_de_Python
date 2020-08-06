# Aula 45 - Um pouco mais sobre Generators
#   Um pouco mais sobre o funcionamento de generators
#   yield e return
#   generator expressions
#   yield from

#def retornar_numeros(n):
#    for numero in range(0,n):
#        yield numero

#n = retornar_numeros(3)

#def funcao_exemplo_for(n):
#    i = 0
#    while True:
#        if i == n:
#            break
#        print(i)
#        i += 1

#funcao_exemplo_for(12)

"""# Exemplo com generator
def funcao_exemplo_generator(n):
    i = 0
    while True:
        if i == n:
            return
        
        print ("Antes do yield")
        yield i
        print ("Depois do yield")
        i += 1

x = funcao_exemplo_generator(4)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))"""

# Generator Expression