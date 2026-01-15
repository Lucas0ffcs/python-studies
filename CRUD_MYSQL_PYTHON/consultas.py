import sys
import mysql.connector
from mysql.connector import Error

status = ["AGENDADA", "CANCELADA", "REALIZADA"]

#-----------CONEXAO------------"
try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Ninofelino8!',
        database = 'clinica'
    )
    cursor = conexao.cursor()
except Error as e:
    print(f"Erro ao conectar ao banco: {e}")
    sys.exit()

#=============MENU=============


def menu():
    try:
        print("\n1 - Agendar consulta")
        print("2 - Listar consultas")
        print("3 - Buscar consultas por paciente")
        print("4 - Atualizar status da consulta")
        print("5 - Cancelar consulta")
        print("0 - Sair")

        escolha = int(input("\nSelecione uma opção\n\n"))

        match escolha:

            case 1:
                agdConsulta()
            case 2:
                print(2)
            # case "3":
            #
            # case "4":
            #
            # case "5":
            #
            # case "0":
            #
            case _:
                print("Digite um valor válido!")






    except ValueError:
        print("Digite um valor válido!")

#===========AGENDAR CONSULTA=========#

def agdConsulta():
    try:
        paciente = input("\nDigite o nome do paciente: ")
        medico = input("Digite o nome do médico: ")
        data = input("Digite a data da consulta YYYY-MM-DD: ")
        horario = input("Digite o horario HH:MM:SS: ")
        status = "AGENDADA"
        valores = (paciente, medico, data, horario, status)
        comando = f'INSERT INTO consultas (paciente, medico, data, horario, status) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(comando,valores)
        conexao.commit()

    except Exception as e:
        print(f"ERRO: {e}")

# def listConsulta():
#     comando = ""























def encerrar():
    sys.exit()


while True:
    menu()