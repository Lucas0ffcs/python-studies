import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ninofelino8!',
    database = 'bdyoutube'
)

cursor = conexao.cursor()

# CRUD e todos comandos do banco de dados ficam aqui

nome_produto = "toddynho"
valor = 6
comando = f'DELETE FROM vendas WHERE Nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #EDITA O BANCO DE DADOS



cursor.close()
conexao.close()



#CREATE
'''Nome_Produto = "Chocolate"
Valor = 15
comando = f'INSERT INTO vendas (Nome_Produto, Valor) VALUES ("{Nome_Produto}",{Valor})'
cursor.execute(comando)
conexao.commit() #SEMPRE COMMITAR AO EDITAR O BANCO DE DADOS, POIS ESTÁ ATUALIZANDO ELE / CREATE UPDATE DELETE
'''
#READ
'''comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
'''
#UPDATE
'''nome_produto = "toddynho"
comando = f'DELETE FROM vendas WHERE Nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #EDITA O BANCO DE DADOS
'''
#DELETE
'''nome_produto = "toddynho"
valor = 6
comando = f'DELETE FROM vendas WHERE Nome_produto = "{nome_produto}"'
cursor.execute(comando)
'''