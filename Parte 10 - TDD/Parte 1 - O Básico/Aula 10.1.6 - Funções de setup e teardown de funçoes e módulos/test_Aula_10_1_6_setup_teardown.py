import pytest

def setup_module(modulo):
    print("\nIniciando o módulo ", modulo.__name__)

def teardown_module(modulo):
    print("\nFinalizando o módulo ", modulo.__name__)

def setup_function(funcao):
    print("\nIniciando a função ", funcao.__name__)

def teardown_function(funcao):
    print("\nFinalizando a função ", funcao.__name__)

def test_TestarOsTestes():
    print("\nEscopo da função 'TestarOsTestes'")
    assert True

def test_TestarOsTestes2():
    print("\nEscopo da função 'TestarOsTestes2'")
    assert True
