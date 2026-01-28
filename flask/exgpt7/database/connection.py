import sys
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Ninofelino8!',
        database = 'exgpt7'
        )
    except Error as e:
        print(e)

usuarios = {"lucas":"deus"}