

MENSAGEM_INICIO = '''------------------------------
Pense em um prato que gosta.
(Pressione qualquer tecla para continuar)
...ou Ctrl-C para interromper)'
'''
MENSAGEM_ACERTOU = 'Acertei de novo!'
MENSAGEM_QUAL_PRATO = 'Qual prato você pensou?'
FORMATO_MSG_TIPO_PRATO = '{} é _________ mas {} não.'


class Jogo:
    '''
    Classe que implementa as regras do jogo
    '''
    def __init__(self, view, pergunta):
        self.view = view
        self.primeira_pergunta = pergunta
        self.pergunta_atual = None

    def inicia_adivinhacao(self):
        self.view.aviso(MENSAGEM_INICIO)
        self.pergunta_atual = self.primeira_pergunta

    def adivinha_prato(self, limite=-1):
        '''
        Faz uma sequência de perguntas para o usuário
        para tentar adivinhar qual prato ele pensou.

        :limite -- se for definido, interrompe o jogo 
                depois de um certo número de tentativas
        '''
        self.inicia_adivinhacao()
        tentativas = 0
        while tentativas != limite:
            concordou = self.view.concordou(
                self.pergunta_atual.enunciado()
            )
            tentativas += 1
            proxima = self.pergunta_atual.respostas[concordou]
            if not proxima:
                if concordou:
                    self.view.aviso(MENSAGEM_ACERTOU)
                else:
                    novo_prato = self.view.prompt(MENSAGEM_QUAL_PRATO)
                    tipo_novo = self.view.prompt(FORMATO_MSG_TIPO_PRATO.format(
                        novo_prato, self.pergunta_atual.descr
                    ))
                    self.pergunta_atual.insere_pergunta(tipo_novo, novo_prato)
                self.inicia_adivinhacao()
                continue
            self.pergunta_atual = proxima
