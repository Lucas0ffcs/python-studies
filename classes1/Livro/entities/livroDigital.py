import livro

class livroDigital(livro):
    def __init__(self, titulo, autor, peso):
        super().__init__(titulo, autor)
        self.__peso = peso