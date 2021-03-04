from buteco.cachaceiro import Cachaceiro

class Corno_Sofrencia(Cachaceiro):
    def reclamar(self):
        print(self.apelido + " chora pra cacete pq é corno")

    def cantar(self):
        print(self.apelido + " canta Bruno e Marrone sem parar")

class Tiozao(Cachaceiro):
    def falar_mulher(self):
        print(self.apelido + " fala que pegou 213 mulheres no forró, sendo 3 com todos os dentes na boca")
    
    def cantar(self):
        print(self.apelido + " bota pra tocar Sula Miranda")

class TiozaoSofrencia(Tiozao, Corno_Sofrencia):
    pass

class Cervejeiro(Cachaceiro):
    pass