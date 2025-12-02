class Pet:
    def __init__(self):
        self.__name = ""
        self.__idade = 0
        self.__tipo = ""

    def falar(self):
        match self.__tipo:
            case "cachorro":
                print("auau")
            case "gato":
                print("miau")
            case _:
                print("som desconhecido")

    def descricao(self):
        print("Meu nome é " + self.__name + " e tenho " + str(self.__idade) + " anos e sou um " + self.__tipo)


class Cachorro(Pet):
    def falar(self):
        print("auau do cahcorro doidão")








dog = Cachorro()

dog._Pet__name = "Rex"
dog._Pet__idade = 5
dog._Pet__tipo = "cachorro"

dog.descricao()
dog.falar()