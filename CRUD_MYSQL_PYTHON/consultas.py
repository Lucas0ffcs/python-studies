import sys
import mysql.connector
from mysql.connector import Error
from datetime import timedelta

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
        print("0 - Sair")

        escolha = int(input("\nSelecione uma opção\n\n"))

        match escolha:

            case 1:
                agdConsulta()
            case 2:
                listConsulta()
            case 3:
                busConsulta()
            case 4:
                attStauts()

            case 0:
                sys.exit()
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

def listConsulta():
    try:
        comando = f'SELECT * FROM consultas'
        cursor.execute(comando)
        resultado = cursor.fetchall()

        for r in resultado:
            print(f'Consulta #{r[0]}')
            print("Paciente: " + str(r[1]))
            print("Médico: " + str(r[2]))
            print("Data:", r[3].strftime('%d/%m/%Y'))
            print(f"Hora: {r[4]}")
            print("Status: " + r[5])

            print("\n\n")
        input("\n\n\nPressione Enter...")
    except Exception as e:
        print(e)

def busConsulta():
    paciente = input("Digite o nome do paciente: ")
    comando = f'SELECT * FROM consultas WHERE paciente LIKE "%{paciente}%"'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    for r in resultado:
        print(f'Consulta #{r[0]}')
        print("Paciente: " + str(r[1]))
        print("Médico: " + str(r[2]))
        print("Data:", r[3].strftime('%d/%m/%Y'))
        print(f"Hora: {r[4]}")
        print("Status: " + r[5])

        print("\n\n")
    input("\n\n\nPressione Enter...")

def attStauts():

    try:
        id = input("Digite o id da consulta: ")
        comando = f'SELECT status FROM consultas WHERE id = %s'
        valores = (id,)
        cursor.execute(comando,valores)
        resultado = cursor.fetchall()
        print("Status: " + resultado[0][0])
        if resultado[0][0] == "AGENDADA":
            print("1 - Marcar como realizada")
            print("2 - Cancelar consulta")
            escolha = int(input("Selecione uma opção: "))
            match(escolha):
                case 1:
                    comando = f'UPDATE consultas SET status = "REALIZADA" WHERE id = %s'
                    cursor.execute(comando,valores)
                    conexao.commit()
                case 2:
                    comando = f'UPDATE consultas SET status = "CANCELADA" WHERE id = %s'
                    cursor.execute(comando, valores)
                    conexao.commit()

        if resultado[0][0] == "REALIZADA":
            print("Esta consulta já foi realizada!\n\n")

        if resultado[0][0] == "CANCELADA":
            print("Consulta cancelada, reagendar.")

    except Exception as e:
        print(e)


def encerrar():
    sys.exit()


while True:
    menu()