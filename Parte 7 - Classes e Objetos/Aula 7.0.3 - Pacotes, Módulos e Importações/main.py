#from buteco.tipos_cachaceiros.corno_sofrencia import Corno_Sofrencia
#from buteco.tipos_cachaceiros.tiozao import Tiozao

from buteco.tipos_cachaceiros.classes_tipos_cachaceiros import Corno_Sofrencia, Tiozao


cs = Corno_Sofrencia()
cs.apelido = "Tião Chifurdo"
tiozao = Tiozao()
tiozao.apelido = "Josielson"

cs.reclamar()
tiozao.falar_mulher()