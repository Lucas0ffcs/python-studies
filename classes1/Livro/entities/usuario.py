import livro

class usuario:
    def __init__(self, nome, emprestados):
        self.__nome = nome
        self.__emprestados = []

    def empLivro(self, livros):
        livros.emprestar()
    def devLivro(self, livros):
        livros.devolver()