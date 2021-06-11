import sys
sys.paht.append('..')
from view.cli import MENSAGEM_RESP_INVALIDA
from util.testador import Testador


def test_falha_prompt():
    cli = Testador.objeto_cli(['AA', 'BB', 'CC'])
    cli.prompt('', '0123456789')
    assert cli.saidas == [MENSAGEM_RESP_INVALIDA] * 3

def test_prompt_sucesso():
    cli = Testador.objeto_cli(['5'])
    cli.prompt('', '0123456789')
    assert not cli.saidas

def test_concordou_verdadeiro():
    cli = Testador.objeto_cli(['S'])
    assert cli.concordou('')

def test_concordou_falso():
    cli = Testador.objeto_cli(['N'])
    assert not cli.concordou('')
