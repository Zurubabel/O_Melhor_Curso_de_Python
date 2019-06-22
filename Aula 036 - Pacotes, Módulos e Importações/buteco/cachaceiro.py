# Módulos, Pacotes e importações
# Refatorar as pastas
# Tipos de importação

from buteco.tipos_cachaceiros.corno_sofrencia import Corno_Sofrencia

class Cachaceiro():
    nome = ""
    apelido = ""
    idade = ""

    def pedir_cachaca(self):
        print(self.apelido + " pediu cachaça")
