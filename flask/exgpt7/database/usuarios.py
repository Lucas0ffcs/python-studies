from os.path import exists
from flask import render_template
from database.connection import get_connection


def addUser(usuario, email, senha):
    try:
        conexao = get_connection()
        cursor = conexao.cursor()

        usuario = usuario
        email = email
        senha = senha

        verify = f'SELECT email FROM clientes '
        cursor.execute(verify)
        emails = list(map(lambda x: x[0], cursor.fetchall()))
        print(emails)
        if email in emails:
            return "Usuário já cadastrado!!"
        else:
            valores = (usuario, email, senha,)

            comando = f'INSERT INTO clientes (nome, email, senha) VALUES (%s, %s, %s) '
            cursor.execute(comando, valores)
            conexao.commit()
    except Exception as e:
        print(e)



def logUser(usuario, senha):
    try:
        conexao = get_connection()
        cursor = conexao.cursor()

        usuario = usuario
        senha = senha

        if usuario == "" or senha == "":
            return "Preencha ambos os campos!"


        comando = f'SELECT email FROM clientes'
        cursor.execute(comando)
        emails = list(map(lambda x: x[0], cursor.fetchall()))

        comando = f'SELECT nome FROM clientes'
        cursor.execute(comando)
        users = list(map(lambda x: x[0], cursor.fetchall()))
        print(emails, users)
        print(usuario)
        print(usuario in users)
        if usuario in users or usuario in emails:
            comando = f'SELECT senha FROM clientes WHERE BINARY email = %s OR BINARY nome = %s'
            cursor.execute(comando, (usuario, usuario))
            senhabuscada = cursor.fetchone()
            print(senhabuscada[0] == senha)
            if senhabuscada[0] == senha:
                print('asdlalda')
                return render_template('logged.html')
            return None
        return None






    except Exception as e:
        print(e)
        return None
