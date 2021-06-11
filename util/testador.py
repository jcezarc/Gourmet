from view.cli import CLI


class Testador:
    entradas = None
    saidas = None

    @classmethod
    def objeto_cli(cls, entradas):
        cls.entradas = entradas
        cls.saidas = []
        return CLI(
            metodo_entrada=cls.simula_entrada,
            metodo_saida=cls.registra_saida
        )

    @classmethod
    def simula_entrada(cls):
        return cls.entradas.pop(0)

    @classmethod
    def registra_saida(cls, texto):
        if texto: cls.saidas.append(texto)
