

class Curso:
    def __init__(self, nome, carga, instrutor):
        self.__nome = nome
        self.__carga = carga
        self.__instrutor = instrutor
    def detalhes(self):
        detalhes = "Curso: " + self.__nome + "—" + self.__carga +"h — Instrutor: " + self.__instrutor.__nome
        return detalhes