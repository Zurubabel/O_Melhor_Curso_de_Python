class Cachaceiro():
    nome = ""
    apelido = ""
    idade = ""

    def pedir_cachaca(self):
        print(self.apelido + " pediu cachaça")


class Corno_Sofrencia(Cachaceiro):
    def reclamar(self):
        print(self.apelido + " chora pra cacete pq é corno")
    

class Tiozao(Cachaceiro):
    def falar_mulher(self):
        print(self.apelido + " fala que pegou 213 mulheres no forró, sendo 3 com todos os dentes na boca")

cs = Corno_Sofrencia()
cs.apelido = "Tião Chifurdo"
tiozao = Tiozao()
tiozao.apelido = "Josielson"

cs.reclamar()
tiozao.falar_mulher()

"""cv = Cachaceiro()
cv.apelido = "Chico Virilha"
cv.pedir_cachaca()"""


"""cv = Cachaceiro()
cv.apelido = "Chico Virilha"
print(cv.apelido)
ct = Cachaceiro()
ct.apelido = "Chico Tuíta"
print(ct.apelido)
print(cv.apelido) """