RESP_SIM = ['S', 's']
RESP_NAO = ['N', 'n']

MENSAGEM_RESP_INVALIDA = 'Resposta inválida. Tente novamente'
MENSAGEM_INICIO = '''------------------------------
Pense em um prato que gosta.
(Pressione qualquer tecla para continuar)
...ou Ctrl-C para interromper)'
'''
MENSAGEM_ACERTOU = 'Acertei de novo!'
MENSAGEM_QUAL_PRATO = 'Qual prato você pensou?'
FORMATO_MSG_TIPO_PRATO = '{} é _________ mas {} não.'


class CLI:
    '''
    Classe que faz a interface com usuário,
    através de linha de comando / terminal
    '''
    def __init__(self, pergunta, metodo_entrada=input, metodo_saida=print):
        self.primeira_pergunta = pergunta
        self.pergunta_atual = None
        self.metodo_entrada = metodo_entrada
        self.metodo_saida = metodo_saida

    def prompt(self, titulo, valores_esperados=''):
        self.metodo_saida(titulo)
        valido = False
        while not valido:
            resposta = self.metodo_entrada()
            if not valores_esperados:
                valido = len(resposta.strip()) > 0
            else:
                valido = resposta in valores_esperados
            if not valido:
                self.metodo_saida(MENSAGEM_RESP_INVALIDA)
        return resposta

    def inicia_adivinhacao(self):
        self.metodo_saida(MENSAGEM_INICIO)
        self.metodo_entrada()
        self.pergunta_atual = self.primeira_pergunta

    def adivinha_prato(self):
        self.inicia_adivinhacao()
        while True:
            concordou = self.prompt(
                self.pergunta_atual.enunciado(), 
                RESP_SIM+RESP_NAO
            ) in RESP_SIM
            proxima = self.pergunta_atual.respostas[concordou]
            if not proxima:
                if concordou:
                    self.metodo_saida(MENSAGEM_ACERTOU)
                    self.metodo_entrada()
                else:
                    novo_prato = self.prompt(MENSAGEM_QUAL_PRATO)
                    tipo_novo = self.prompt(FORMATO_MSG_TIPO_PRATO.format(
                        novo_prato, self.pergunta_atual.descr
                    ))
                    self.pergunta_atual.insere_pergunta(tipo_novo, novo_prato)
                self.inicia_adivinhacao()
                continue
            self.pergunta_atual = proxima
