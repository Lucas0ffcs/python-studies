class Plataforma:

    def __init__(self, nome):
        self.__nome = nome
        self.__cursos = []

    def addCurso(self, curso):
        self.__cursos.append(curso)
        return
    def listCursos(self):

        lista = []
        for curso in self.__cursos:
            lista.append(curso.nomes)

        return lista


    def bCInstrut(self, instrutor):
        lista = list(filter(lambda x: x.nomes == instrutor, self.__cursos))
        return lista
