

class MockPergunta:
    def __init__(self, descr, sim, nao, pai=None, escolha_pai=None):
        self.respostas = {True:1, False:0}
        self.descr = descr
        pass

    def enunciado(self):
        pass

    def insere_pergunta(self, tipo, objetivo):
        pass
