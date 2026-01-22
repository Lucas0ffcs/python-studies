import sys

from games import cadJogo, listJogos, buscJogos, attJogos, remJogos


def menu(conexao):
    print("\n1 - Cadastrar jogo")
    print("2 - Listar jogos")
    print("3 - Buscar por título")
    print("4 - Atualizar jogo")
    print("5 - Remover jogo")
    print("0 - Sair\n\n")

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        cadJogo(conexao)
    elif opcao == 2:
        listJogos(conexao)
    elif opcao == 3:
        buscJogos(conexao)
    elif opcao == 4:
        attJogos(conexao)
    elif opcao == 5:
        remJogos(conexao)
    elif opcao == 0:
        sys.exit()
    else:
        print("Digite um valor válido")
