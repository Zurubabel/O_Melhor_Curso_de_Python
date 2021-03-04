# Herança
# Múltipla Herança
# Diferença entre Composição e Agregação
# - Composição: Outros objetos na classe
# - Agregação: Instância independente
# Dica: Prefira Composição/Agregação ao invés de Herança

from buteco.tipos_cachaceiros.classes_tipos_cachaceiros import Corno_Sofrencia, Tiozao, TiozaoSofrencia

"""cs = Corno_Sofrencia()
cs.apelido = "Tião Chifurdo"
tiozao = Tiozao()
tiozao.apelido = "Josielson"

cs.reclamar()
cs.cantar()
tiozao.falar_mulher()
tiozao.cantar()"""

tiao = TiozaoSofrencia()

tiao.apelido = "Tião Marreco"
tiao.reclamar()
tiao.falar_mulher()
tiao.cantar()