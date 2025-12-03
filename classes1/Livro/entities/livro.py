class Livro:
    def __init__(self, titulo, autor, ano, disp):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__disp = disp
    def emprestar(self):
        if not self.__disp:
            print('"'+ self.__titulo + '" não está disponível')
        else:
            self.__disp = False
    def devolver(self):
        if not self.__disp:
            print('"'+ self.__titulo + '" não está disponível')
        else:
            self.__disp = False
