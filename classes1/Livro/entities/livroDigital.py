from .livro import Livro

class LivroDigital(Livro):
    def __init__(self, titulo, autor, tamArq, ano):
        super().__init__(titulo, autor, ano, )
        self.__tamArq = tamArq