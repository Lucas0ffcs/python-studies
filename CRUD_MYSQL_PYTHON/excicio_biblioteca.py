import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ninofelino8!',
    database = 'bibliobd'
)
cursor = conexao.cursor()
def addLivro():
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano de lançamento YYYY-MM-DD: ")
    lido = input("Digite se ja foi lido ou não 0/1: ")
    comando = f'INSERT INTO livros (Titulo, Autor, Ano, Lido) VALUES ("{titulo}","{autor}","{ano}", "{lido}")'
    cursor.execute(comando)
    conexao.commit()


def listLivro():
    comando = f'SELECT * FROM livros'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for c in resultado:
        data = str(c[3])
        print("Id : "+ str(c[0]) + " Titulo : "+ c[1] + " Autor : "+ c[2] + " Data : " + data + " Lido : " + str(c[4]))



def remLivro():
    titulo  = input("Digite o titulo do livro: ")
    comando = f'DELETE FROM livros WHERE titulo = "{titulo}"'
    cursor.execute(comando)
    conexao.commit()



def attLivro():
    substituido = input("Digite o titulo do livro que deseja atualizar: ")
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano de lançamento YYYY-MM-DD: ")
    lido = int(input("Digite se ja foi lido ou não 0/1: "))
    comando = f'UPDATE livros SET titulo = "{titulo}", autor = "{autor}", ano = "{ano}", lido = {lido} WHERE titulo = "{substituido}"'
    cursor.execute(comando)
    conexao.commit()


print('Bem vindo ao catálogo eletrônico!\n\n\n')
input("Pressione Enter para continuar\n")

print("1 - Adicionar livro ao catálogo")
print("2 - Exibir catálogo completo")
print("3 - Remover livro do catálogo")
print("4 - Atualizar item do catálogo\n")

switch = int(input("Selecione uma opção\n"))

match(switch):
    case 1:
        addLivro()
    case 2:
        listLivro()
    case 3:
        remLivro()
    case 4:
        attLivro()





cursor.close()
conexao.close()

