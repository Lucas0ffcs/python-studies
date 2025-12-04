class Plataforma:

    def __init__(self, nome):
        self.__nome = nome
        self.__cursos = []

    def addCurso(self, curso):
        self.__cursos.append(curso)
        return
    def listCursos(self):
        return self.__cursos
    def buscaCursoInstrutor(self, instrutor):
        lista = list(filter(lambda x: x.__nome == instrutor, self.__cursos))
        return lista

