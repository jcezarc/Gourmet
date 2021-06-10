from mock_pergunta import MockPergunta


class MockCLI:
    def __init__(self, entradas):
        self.entradas = entradas
        self.saidas = []

    def objeto_cli(self, classeCLI, params):
        return classeCLI(
            MockPergunta(**params),
            metodo_entrada=self.simula_entrada, 
            metodo_saida=self.registra_saida
        )

    def simula_entrada(self):
        return self.entradas.pop(0)

    def registra_saida(self, texto):
        self.saidas.append(texto)
