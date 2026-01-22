from menu import menu
from db import conectar

conexao = conectar()

while True:
        menu(conexao)

conexao.close()