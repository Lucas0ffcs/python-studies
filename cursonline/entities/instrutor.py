class Instrutor:
    def __init__(self, nome, exp):
        self.__nome = nome
        self.__exp = exp
    def info(self):
        info = "Instrutor: " + self.__nome + " — "+ self.__exp + "anos de experiência"
        return info
