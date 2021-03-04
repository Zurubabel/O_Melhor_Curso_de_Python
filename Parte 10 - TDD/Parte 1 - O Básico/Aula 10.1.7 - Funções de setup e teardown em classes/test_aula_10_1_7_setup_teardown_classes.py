class TestTestes:
    @classmethod
    def setup_class(classe):
        print("\nSetup da classe ", classe.__name__)

    @classmethod
    def teardown_class(classe):
        print("\nTeardown da classe ", classe.__name__)

    def setup_method(self, metodo):
        print("\nSetup do método ", metodo.__name__)

    def teardown_method(self, metodo):
        print("\nTeardown do método ", metodo.__name__)

    def test_Teste1(self):
        print("\nEscopo da função Teste1")
        assert True

    def test_Teste2(self):
        print("\nEscopo da função Teste2")
        assert True