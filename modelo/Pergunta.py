

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

