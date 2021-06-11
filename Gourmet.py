"""
    Adaptação do _Jogo Gourmet_ para python
    Faz parte do `Desafio Técnico` da Objective,
    feito por *Júlio Cascalles*
"""

from modelo.Pergunta import Pergunta
from view.cli import CLI


if __name__ == '__main__':
    cli = CLI(
        Pergunta('massa', sim='Lasanha', nao='Bolo de chocolate')
    )
    cli.adivinha_prato()
