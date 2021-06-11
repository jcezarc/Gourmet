from modelo.Pergunta import Pergunta
from regras.jogo import (
    Jogo,
    MENSAGEM_QUAL_PRATO,
    MENSAGEM_ACERTOU
)
from util.testador import Testador


def pergunta_inicial():
    return Pergunta('vegetariano', sim='Berinjela', nao='Hambúrguer')

def acertou():
    return MENSAGEM_ACERTOU in Testador.saidas

def test_falha_ao_adivinhar():
    jogo = Jogo(
        Testador.objeto_cli(['N'] * 20),
        pergunta_inicial() 
    )
    jogo.adivinha_prato(10)
    qtd_novos = Testador.saidas.count(MENSAGEM_QUAL_PRATO)
    assert qtd_novos == 3
    assert not acertou()

def test_adivinha_com_sucesso():
    roteiro = [
        'Início',
        'N', # --- Não é vegetariano
        'S', # --- ..É Hambúrguer !!
        'Parabéns', 'Fim'
    ]
    jogo = Jogo(
        Testador.objeto_cli(roteiro),
        pergunta_inicial() 
    )
    jogo.adivinha_prato(3)
    assert acertou()
