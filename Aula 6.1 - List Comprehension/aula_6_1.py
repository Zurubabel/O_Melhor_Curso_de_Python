# List Comprehension
#   O que caramba é isso?
#   Onde posso usar isso?
#   LC simples
#   LC com condicionais
#   LC Aninhados
#   Vantagens e desvantagens


texto = "Morango do Nordeste"

#lista_letras = []

"""for letra in texto:
    lista_letras.append(letra)

print(lista_letras)"""

numeros = range(0, 35)

#print([letra for letra in texto])

# Só números pares
#print([numero + (numero * 2) for numero in numeros if numero % 2 == 0])
"""pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)"""

numeros = [1, 2, 3, 4, 5]
texto = "ABCDE"

print([{numero, letra}  for numero in numeros for letra in texto])
#retorno = []
#for numero in numeros:
#    for letra in texto:
#        retorno.append((numero, letra))

#print(retorno)