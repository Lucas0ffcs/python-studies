import mysql.connector
from mysql.connector import Error
import sys

def conectar():

    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Ninofelino8!',
            database = 'game_db'
        )
        return conexao
    except Error as e:
        print(f'Erro ao conectar: {e}')
        sys.exit()