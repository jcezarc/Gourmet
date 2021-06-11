"""
    Adaptação do _Jogo Gourmet_ para python
    Faz parte do `Desafio Técnico` da Objective,
    feito por *Júlio Cascalles*
"""

from modelo.Pergunta import Pergunta
from view.cli import CLI
from regras.jogo import Jogo


if __name__ == '__main__':
    jogo = Jogo(
        CLI(), # --- A interface com o usuário será através do terminal
        Pergunta('massa', sim='Lasanha', nao='Bolo de chocolate')
    )
    jogo.adivinha_prato()
