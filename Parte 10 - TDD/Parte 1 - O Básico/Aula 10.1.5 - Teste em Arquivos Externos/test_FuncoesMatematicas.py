"""
    OK Criar a classe FuncoesMatematicas
    - Criar o método de somar dois números, sendo esses dois números passados 
    como parâmetro
"""
from FuncoesMatematicas import FuncoesMatematicas

def test_ExecutarMetodoSomarDoisNumeros():
    funcoes = FuncoesMatematicas()
    funcoes.somarDoisNumeros(1, 2)

def test_SomarUmMaisDoisNoMetodoSomarDoisNumerosERetornarTres():
    funcoes = FuncoesMatematicas()
    assert funcoes.somarDoisNumeros(1, 2) == 3