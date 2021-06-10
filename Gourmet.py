"""
    Adaptação do _Jogo Gourmet_ para python
    Faz parte do `Desafio Técnico` da Objective,
    feito por *Júlio Cascalles*
"""


RESP_SIM = ['S', 's']
RESP_NAO = ['N', 'n']


class Pergunta:
    '''
    Lista encadeada onde cada resposta pode levar a uma nova pergunta
    '''
    def __init__(self, descr, sim, nao, pai=None, escolha_pai=None):
        self.descr = descr
        if isinstance(sim, str):
            sim = Pergunta(sim, None, None, self, True)
        if isinstance(nao, str):
            nao = Pergunta(nao, None, None, self, False)
        self.respostas = {
            True: sim,
            False: nao,
        }
        self.parentesco = (pai, escolha_pai)

    def insere_pergunta(self, tipo, objetivo):
        '''
        Coloca uma nova pergunta no lugar da atual.
        E a atual vai para o `Não` da nova pergunta.
        '''
        pai, escolha_pai = self.parentesco
        pergunta = Pergunta(
            tipo,
            sim=objetivo,
            nao=self,
            pai=pai, escolha_pai=escolha_pai
        )
        self.parentesco = (pergunta, False)
        pai.respostas[escolha_pai] = pergunta
        return pergunta

    def enunciado(self):
        return 'É {}? (S/N)'.format(self.descr)

# --- Funções auxiliares: ----------
def prompt(titulo, valores_esperados=''):
    print(titulo)
    valido = False
    while not valido:
        resposta = input()
        if not valores_esperados:
            valido = len(resposta.strip()) > 0
        else:
            valido = resposta in valores_esperados
        if not valido:
            print('Resposta inválida. Tente novamente')
    return resposta

def adivinha_prato():
    def inicia_adivinhacao():
        print('-'*30)
        print('Pense em um prato que gosta.')
        print('(Pressione qualquer tecla para continuar)')
        input()
    primeira = pergunta = Pergunta('massa', sim='Lasanha', nao='Bolo de chocolate')
    acertou = False
    inicia_adivinhacao()
    while not acertou:
        concordou = prompt(
            pergunta.enunciado(), 
            RESP_SIM+RESP_NAO
        ) in RESP_SIM
        proxima = pergunta.respostas[concordou]
        if not proxima:
            if concordou:
                print('Acertei de novo!')
                acertou = True
            else:
                novo_prato = prompt('Qual prato você pensou?')
                tipo_novo = prompt('{} é _________ mas {} não.'.format(
                    novo_prato, pergunta.descr
                ))
                pergunta.insere_pergunta(tipo_novo, novo_prato)
                inicia_adivinhacao()
                pergunta = primeira
                continue
        pergunta = proxima
# -----------------------------------


if __name__ == '__main__':
    adivinha_prato()
