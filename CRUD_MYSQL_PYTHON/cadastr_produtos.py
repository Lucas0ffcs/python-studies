import sys
from decimal import Decimal
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ninofelino8!',
    database = 'cadprodutos'
)

var = True






def menu():
    print("\n1 - Cadastrar produto")
    print("2 - Listar todos os produtos")
    print("3 - Buscar produto por nome")
    print("4 - Atualizar produto")
    print("5 - Remover produto")
    print("6 - Registrar venda")
    print("0 - Sair")
    escolha = int(input("\n\nSelecione qual operação deseja realizar: \n\n"))
    match (escolha):
        case 1:
            cadProd()
        case 2:
            listProd()
        case 3:
            buscProd()
        case 4:
            attProd()
        case 5:
            remProd()
        case 6:
            regVenda()
        case 0:
            sys.exit()

def cadProd():
    nome = input("\nDigite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade disponível no estoque: "))
    comando = f'INSERT INTO produtos (nome, categoria, preco, estoque) VALUES (%s, %s, %s, %s)'
    valores = (nome, categoria, preco, estoque)
    cursor.execute(comando, valores)
    conexao.commit()

def listProd():
    comando = 'SELECT * FROM produtos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for r in resultado:
        print(str(r))
    input("\n\n\nPressione Enter...")

def buscProd():
    nome = input("\nDigite o nome do produto a ser buscado: ")
    comando = 'SELECT * FROM produtos WHERE nome = %s'
    valores = (nome)
    resultado = cursor.fetchall()
    print("\n" + resultado)
    input("\n\n\nPressione Enter...")

def attProd():
    print("1 - Nome")
    print("2 - Categoria")
    print("3 - Preço")
    print("4 - Estoque")
    print("5 - Atualizar produto por inteiro")
    print("6 - Retornar ao menu principal")
    escolha = int(input("Selecione o campo que deseja atualizar: "))

    match(escolha):
        case 1:
            id = int(input("Digite o id do produto a ser atualizado: "))
            nome = input("Digite o novo nome do produto: ")
            comando = 'UPDATE produtos SET nome = %s WHERE id = %s'
            valores = (nome, id)
            cursor.execute(comando,valores)
            conexao.commit()
        case 2:
            id = int(input("Digite o id do produto a ser atualizado: "))
            categoria = input("Digite a nova categoria do produto: ")
            comando = 'UPDATE produtos SET categoria = %s WHERE id = %s'
            valores = (categoria)
            cursor.execute(comando, valores)
            conexao.commit()
        case 3:
            id = int(input("Digite o id do produto a ser atualizado: "))
            preco = Decimal(input("Digite a nova categoria do produto: "))
            comando = 'UPDATE produtos SET preco = %s WHERE id = %s'
            valores = (preco)
            cursor.execute(comando, valores)
            conexao.commit()
        case 4:
            id = int(input("Digite o id do produto a ser atualizado: "))
            estoque = int(input("Digite a nova categoria do produto: "))
            comando = 'UPDATE produtos SET estoque = %s WHERE id = %s'
            valores = (estoque)
            cursor.execute(comando, valores)
            conexao.commit()
        case 5:
            id = int(input("Digite o id do produto a ser atualizado: "))
            nome = input("Digite o novo nome do produto: ")
            categoria = input("Digite a nova categoria do produto: ")
            preco = Decimal(input("Digite a nova categoria do produto: "))
            estoque = int(input("Digite a nova categoria do produto: "))
            comando = 'UPDATE produtos SET nome = %s, categoria = %s, preco = %s, estoque = % WHERE id = %s'
            valores  = (nome, categoria, preco, estoque)
            cursor.execute(comando, valores)
            conexao.commit()
        case 6:
            menu()





def remProd():
    id = int(input("Digite o id do produto a ser removido do estoque: "))
    input("Tem certeza que deseja remover esse produto? S/N")
    comando = f'DELETE FROM livros WHERE WHERE id = %s'
    valores = (id)
    cursor.execute(comando, valores)
    conexao.commit()
    input("\n\n\nPressione Enter...")

def regVenda():
    id = int(input("Digite o id do produto a ser vendido: "))

    comando1 = 'SELECT estoque FROM produtos WHERE id = %s'
    estoque = cursor.fetchall()
    print("Quantidade disponível: " + estoque)
    quantidade = int(input("Digite a quantidade desejada: "))
    if quantidade <= 0 or quantidade > estoque:
        print("Quantidade indiponível!\n\n")
        input("Digite Enter para continuar")
        menu()
    valores = (estoque - quantidade)
    comando = 'UPDATE produtos SET estoque = %s WHERE id = %s'
    cursor.execute(comando, valores)
    conexao.commit()
    input("\n\n\nPressione Enter...")


cursor = conexao.cursor()



while 1:
    menu()









cursor.close()
conexao.close()
