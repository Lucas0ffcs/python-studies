from .livro import Livro

class Biblioteca:
    catalogo = []

    def addLivro(self,livro):
        Biblioteca.catalogo.append(livro)

    def remLivro(self,livro):
        Biblioteca.catalogo.remove(livro)

    def buscaLivro(self, livro):
        if livro not in Biblioteca.catalogo:
            print("Título não encontrado")
            return
        else:
            texto_busca = livro.titulo

    def listDisp(self):
        for i in Biblioteca.catalogo:
            print(i.__str__())



