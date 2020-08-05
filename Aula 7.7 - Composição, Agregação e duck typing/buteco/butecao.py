class Butecao():
    cachaceiro = ""

    def atribuir_cachaceiro(self, cachaceiro):
        self.cachaceiro = cachaceiro

    def servir_cachaca(self):
        self.cachaceiro.pedir_cachaca()
        print("O butequeiro serviu cachaça para o " + self.cachaceiro.apelido)

        # Duck typing