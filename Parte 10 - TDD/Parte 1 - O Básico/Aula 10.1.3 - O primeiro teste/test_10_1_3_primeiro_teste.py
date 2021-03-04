# x Se a função somarDoisNumeros existe
# x Passar dois números como parâmetro
# x Testar o resultado da função

def test_TestarSomaDaFuncaoSomarDoisNumeros():
    assert somarDoisNumeros(1,2) == 3

def somarDoisNumeros(num_1, num_2):
    return num_1 + num_2