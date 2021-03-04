# Herança
# Múltipla Herança
# Diferença entre Composição e Agregação
# - Composição: Outros objetos na classe
# - Agregação: Instância independente
# Dica: Prefira Agregação ao invés de Herança

from buteco.tipos_cachaceiros.classes_tipos_cachaceiros import Corno_Sofrencia, Tiozao, TiozaoSofrencia
from buteco.tipos_cigarros.tipos_cigarros import Eight, Fox, SanMarino
from buteco.butecao import Butecao

cs = Corno_Sofrencia()
cs.apelido = "Tião Chifurdo"
tiozao = Tiozao()
tiozao.apelido = "Josielson"
tiao = TiozaoSofrencia()
tiao.apelido = "Tião Marreco"

butecao = Butecao()
butecao.atribuir_cachaceiro(tiao)
butecao.servir_cachaca()


"""cs.reclamar()
cs.cantar()
tiozao.falar_mulher()
tiozao.cantar()"""

"""
tiao.cigarro = Fox()

tiao.cigarro.fumar()


tiao.reclamar()
tiao.falar_mulher()
tiao.cantar()"""

