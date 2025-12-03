class Livro:
    def __init__(self, titulo, autor, ano, disp):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self._disp = disp
     def emprestar(self):
