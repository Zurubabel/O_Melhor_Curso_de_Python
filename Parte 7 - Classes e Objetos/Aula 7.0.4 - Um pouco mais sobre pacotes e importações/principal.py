# Como o Python verifica as importações
# sys.path
# __init__.py
# Importações circulares

from buteco.tipos_cachaceiros.classes_tipos_cachaceiros import Corno_Sofrencia, Tiozao

cs = Corno_Sofrencia()
cs.apelido = "Tião Chifurdo"
tiozao = Tiozao()
tiozao.apelido = "Josielson"

cs.reclamar()
tiozao.falar_mulher()

#import sys
#for i in sys.path:
#    print(i)