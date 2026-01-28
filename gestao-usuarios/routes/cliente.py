from flask import Blueprint, render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('clientes', __name__)

"""
ROTA DE CLIENTES

 - /clientes/ (GET) - Listar os clientes
 - /clientes/ (POST) - Inserir o cliente no servidor 
 - /clientes/new (GET)- Renderizar o formulário para criar um cliente
 - /clientes/<id> (GET)- Obter um cliente
 - /clientes/<id>/edit (GET) - Renderizar um formulário para editar um cliente
 - /clientes/<id>/update (PUT) - Atualizar os dados do cliente
 - /clientes/<id>/delete (DELETE) - Deleta o registro do usuário
"""



@cliente_route.route('/')
def lista_clientes():
    """Listar os clientes"""


    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir os dados do cliente"""
    pass

@cliente_route.route('/new')
def form_cliente():
    """Formulario para cadastrar um cliente"""
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """Exibir detalhes do cliente  """
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente():
    """Formulario para editar um cliente """
    return render_template('form_edit_client.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente():
    """Formulario para atualizar os dados de um cliente """
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente():
    """ Deletar cliente """
    pass

