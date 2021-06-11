from modelo.Pergunta import Pergunta


def localiza_comida(dados, roteiro):
    '''
    Usa um objeto Pergunta como dados
    para localizar um item, seguindo
    um roteiro -- para testes
    '''
    ultimo = None
    while roteiro and dados:
        ultimo = dados
        condicao = roteiro.pop(0)
        dados = dados.respostas[condicao]
    return ultimo

def test_falha_inserir_pergunta():
    pergunta_lanche = Pergunta(
        'sanduíche', sim='Misto quente', nao='Pizza'
    )
    try:
        pergunta_lanche.respostas.insere_pergunta(
            'com salsicha', 'Cachorro quente'
        ) # ... deveria inserir no "Misto quente"
        com_erro = False
    except:
        com_erro = True
    # --- Não tem como substituir a pergunta inicial
    assert com_erro

def test_insere_pergunta_com_sucesso():
    GOIABA = 'Goiaba'
    pergunta_fruta = Pergunta('Fruta', sim=GOIABA, nao='Batata frita')
    pergunta_goiaba = pergunta_fruta.respostas[True]
    pergunta_goiaba.insere_pergunta('espinhuda', 'Abacaxi')
    roteiro = [
        True, # --- É fruta
        False, # -- ...mas não é espinhuda
        True, # --- É Goiaba !!
    ]
    resultado = localiza_comida(pergunta_fruta, roteiro)
    assert resultado.descr == GOIABA
