class Curso:
    def __init__(self, nome, carga, instrutor):
        self.nomes = nome
        self.__carga = carga
        self.__instrutor = instrutor
    def detalhes(self):
        detalhes = "Curso: " + self.nomes + "—" + self.__carga +"h — Instrutor: " + self.__instrutor.nome
        return detalhes