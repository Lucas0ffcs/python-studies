import livro



class biblioteca:
    catalogo = []

    def addLivro(self,livru: livro):
        biblioteca.catalogo.append(livro)

    def remLivro(self,livru: livro):
        biblioteca.catalogo.remove(livro)

    def buscaLivro(self, livru: livro):
        if livru not in biblioteca.catalogo:
            print("Título não encontrado")
            return
        else:
            texto_busca = livru.titulo

    def listDisp(self):
        return biblioteca.catalogo