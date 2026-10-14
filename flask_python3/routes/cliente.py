from flask import Blueprint, render_template 
from database.CLIENTES import CLIENTES

cliente_route = Blueprint('cliente', __name__)

#anotação de rota para listar clientes no caderno 20/09

@cliente_route.route('/') 
def lista_cliente():
    return render_template('lista_cliente.html', clientes=CLIENTES)

@cliente_route.route('/create', methods=['POST'])
def inserir_cliente():
    pass

#formulario pra criar cliente
@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

#exibir detalhes do cliente
@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')

#formulario pra editar cliente
@cliente_route.route('/<int:cliente_id>/edit')
def form_editar_cliente(cliente_id):
    return render_template('form_editar_cliente.html')

#atualizar infos do cliente
@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    pass

#deletar cliente
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    pass