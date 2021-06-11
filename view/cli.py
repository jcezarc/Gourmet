RESP_SIM = ['S', 's']
RESP_NAO = ['N', 'n']
MENSAGEM_RESP_INVALIDA = 'Resposta inválida. Tente novamente'

class CLI:
    '''
    Classe que faz a interface com usuário,
    através de linha de comando / terminal
    '''
    def __init__(self, metodo_entrada=input, metodo_saida=print):
        self.metodo_entrada = metodo_entrada
        self.metodo_saida = metodo_saida

    def prompt(self, titulo, valores_esperados=''):
        '''
        Obtém um valor do usuário 
        e verifica se é um valor válido.
        '''
        self.metodo_saida(titulo)
        retorno, valido = '', False
        while not valido:
            try:
                retorno = self.metodo_entrada()
            except KeyboardInterrupt:
                raise
            except:
                break
            if not valores_esperados:
                valido = len(retorno.strip()) > 0
            else:
                valido = retorno in valores_esperados
            if not valido:
                self.metodo_saida(MENSAGEM_RESP_INVALIDA)
        return retorno

    def concordou(self, texto):
        '''
        Exibe um texto e espera S/N como retorno do usuário.
        Retorna True se a resposta for equivalente a `Sim`
        '''
        return self.prompt(
            texto, 
            RESP_SIM+RESP_NAO
        ) in RESP_SIM

    def aviso(self, texto):
        '''
        Exibe uma mensagem e pausa
        '''
        self.metodo_saida(texto)
        self.metodo_entrada()
