from datetime import datetime
from flask import Blueprint, request, jsonify
from models import db, AssistenciaTecnica, Cliente, Oficina, Estoque

routes = Blueprint('routes', __name__)

# Rotas GET
@routes.route('/assistencias', methods=['GET'])
def get_assistencias():
    assistencias = AssistenciaTecnica.query.all()
    return jsonify([assistencia.to_dict() for assistencia in assistencias])

@routes.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes])

@routes.route('/oficinas', methods=['GET'])
def get_oficinas():
    oficinas = Oficina.query.all()
    return jsonify([oficina.to_dict() for oficina in oficinas])

@routes.route('/estoques', methods=['GET'])
def get_estoques():
    estoques = Estoque.query.all()
    return jsonify([estoque.to_dict() for estoque in estoques])

# Rotas POST
@routes.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.get_json()
    novo_cliente = Cliente(
        nome=data.get('nome'),
        documento=data.get('documento'),
        email=data.get('email'),
        telefone=data.get('telefone'),
        celular=data.get('celular'),
        endereco=data.get('endereco'),
        observacao=data.get('observacao'),
        assistencia_id=data.get('assistencia_id')
    )
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify(novo_cliente.to_dict()), 201

@routes.route('/assistencias', methods=['POST'])
def add_assistencia():
    data = request.get_json()
    nova_assistencia = AssistenciaTecnica(
        razao_social=data.get('razao_social'),
        nome_fantasia=data.get('nome_fantasia'),
        cnpj=data.get('cnpj'),
        inscricao_estadual=data.get('inscricao_estadual'),
        email=data.get('email'),
        telefone=data.get('telefone'),
        celular=data.get('celular'),
        endereco=data.get('endereco'),
        observacao=data.get('observacao')
    )
    db.session.add(nova_assistencia)
    db.session.commit()
    return jsonify(nova_assistencia.to_dict()), 201



@routes.route('/oficinas', methods=['POST'])
def create_oficina():
    data = request.json
    nova_oficina = Oficina(
        aparelho=data['aparelho'],
        marca=data.get('marca'),
        modelo=data.get('modelo'),
        numero_serie=data.get('numero_serie'),
        data_entrada=datetime.strptime(data.get('data_entrada'), '%Y/%m/%d').date(),  # Converter string para objeto de data Python
        data_saida=datetime.strptime(data.get('data_saida'), '%Y/%m/%d').date(),  # Converter string para objeto de data Python
        garantia=data.get('garantia'),
        observacao=data.get('observacao'),
        cliente_id=data.get('cliente_id')
    )
    db.session.add(nova_oficina)
    db.session.commit()
    return jsonify({"message": "Oficina criada com sucesso!"}), 201




@routes.route('/estoques', methods=['POST'])
def add_estoque():
    data = request.get_json()
    novo_estoque = Estoque(
        componente=data.get('componente'),
        quantidade=data.get('quantidade'),
        descricao=data.get('descricao'),
        preco=data.get('preco'),
        observacao=data.get('observacao'),
        oficina_id=data.get('oficina_id')
    )
    db.session.add(novo_estoque)
    db.session.commit()
    return jsonify(novo_estoque.to_dict()), 201
