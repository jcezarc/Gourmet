from view.cli import CLI
from modelo.Pergunta import Pergunta
from regras.jogo import Jogo
from util.testador import Testador


def pergunta_inicial():
    return Pergunta('vegetariano', 'fruta', 'hambúrguer')

def test_falha_ao_adivinhar():
    jogo = Jogo(
        Testador.objeto_cli([
            '...'
        ]),
        pergunta_inicial() 
    )

def test_adivinha_com_sucesso():
    pass