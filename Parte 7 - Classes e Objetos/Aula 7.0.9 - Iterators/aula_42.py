# Iterators
#   O que são iterators?
#   Funções Mágicas __iter__ (Iterable) e __next__ (Iterator)

# random.choice


#for letra in "Video dificil do cacete que já fazem mais de 1 hora que eu tô tentando gravar essa merda":
#    print(letra)

import random

class ButecoCachaca:

    cachaceiros = ["Biricutico", "Zé do Alho", "Pé preto de Pindamonhangaba", "Jumento Celetino", "fim"]

    def __iter__(self):
        return self

    def __next__(self):
        retorno = random.choice(self.cachaceiros)

        if retorno == "fim":
            raise StopIteration

        return retorno

for cachaceiro in ButecoCachaca():
    print(cachaceiro)

        