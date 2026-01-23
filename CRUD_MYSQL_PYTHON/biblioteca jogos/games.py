import mysql.connector




def exbJogos(jogos):
    for i in jogos:
        print(f'Id: {i[0]}')
        print(f'Titulo: {i[1]}')
        print(f'Gênero: {i[2]}')
        print(f'Plataforma: {i[3]}')
        print(f'Horas jogadas: {i[4]}')
        print(f'Status: {i[5]}\n')
        c += 1

def cadJogo(conexao):
    try:
        cursor = conexao.cursor()
        titulo = input("Titulo: ")
        genero = input("Gênero: ")
        plataforma = input("Plataforma: ")
        horas_jogadas = input("Horas jogadas: ")
        status = input("Status :")
        valores = (titulo, genero, plataforma, horas_jogadas, status,)
        comando = """
                  INSERT INTO jogos (titulo, genero, plataforma, horas_jogadas, status)
                  VALUES (%s, %s, %s, %s, %s) \
                  """
        cursor.execute(comando, valores)
        conexao.commit()
    except Exception as e:
        print(e)


def listJogos(conexao):
    try:
        cursor = conexao.cursor()
        comando = """
                SELECT * FROM jogos
                  """
        cursor.execute(comando)
        resultado = cursor.fetchall()
        exbJogos(resultado)
    except Exception as e:
        print(e)

def buscJogos(conexao):
    try:
        cursor = conexao.cursor()
        titulo = input("Titulo: ")
        valores = (f"%{titulo}%",)
        comando = """
                SELECT * FROM jogos WHERE titulo LIKE %s
                """
        cursor.execute(comando,valores)
        resultado = cursor.fetchall()
        exbJogos(resultado)
    except Exception as e:
        print(e)

def attJogos(conexao):
    try:
        cursor = conexao.cursor()
        titulo = input('Titulo: ')
        horas_jogadas = input("Horas jogadas: ")
        status = input("Status: ")
        valores = (horas_jogadas, status, f"%{titulo}%")
        comando = """
                  UPDATE jogos SET horas_jogadas = %s, status = %s WHERE titulo LIKE %s   
        """
        cursor.execute(comando,valores)
        conexao.commit()
    except Exception as e:
        print(e)

def remJogos(conexao):
    cursor = conexao.cursor()
    id = input("id: ")
    valores = (id,)
    comando = """
            DELETE FROM jogos WHERE id = %s
        """
    cursor.execute(comando, valores)
    conexao.commit()
