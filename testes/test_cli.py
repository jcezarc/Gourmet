import sys
sys.paht.append('..')
from view.cli import CLI, MENSAGEM_RESP_INVALIDA
from modelo.Pergunta import Pergunta

class Testador:
    entradas = None
    saidas = []

    @classmethod
    def objeto_cli(cls, entradas):
        cls.entradas = entradas
        return CLI(
            Pergunta('vegetariano', 'fruta', 'hambúrguer'), 
            metodo_entrada=cls.simula_entrada,
            metodo_saida=cls.registra_saida
        )

    @classmethod
    def simula_entrada(cls):
        return cls.entradas.pop(0)

    @classmethod
    def registra_saida(cls, texto):
        if texto: cls.saidas.append(texto)

# ------ Testes: ----------------------------------
def test_falha_prompt():
    cli = Testador.objeto_cli(['AA', 'BB', 'CC'])
    cli.prompt('', '0123456789')
    assert cli.saidas == [MENSAGEM_RESP_INVALIDA] * 3

def test_prompt_sucesso():
    cli = Testador.objeto_cli(['5'])
    cli.prompt('', '0123456789')
    assert not cli.saidas

