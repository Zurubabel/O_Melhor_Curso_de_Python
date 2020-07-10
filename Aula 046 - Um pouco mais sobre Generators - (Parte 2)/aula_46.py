# Aula 45 - Um pouco mais sobre Generators (Parte 2)
#   Um pouco mais sobre o funcionamento de generators
#   yield e return
#   --- generator expressions
#   --- yield from
#x = [x ** 2 for x in range(0,20)]

def retornar_numeros(n):
    for numero in range(0,n):
        yield numero

def retornar_numeros_gen(n):
    yield from (numero for numero in range(0,n))

print(list(retornar_numeros(10)))
print(list(retornar_numeros_gen(10)))

"""#print(x)

#print(type(x))
#exp = ({x: x ** 2} for x in range(0,20))

#print(type(exp))

#print(exp)

#for i in exp:
#    print(i)

#print(type(next(exp)))

#print(next(exp))

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

# Exemplo com generator
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
print(next(x))

# Generator Expression"""