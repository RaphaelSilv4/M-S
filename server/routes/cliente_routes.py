from flask import Blueprint, request, jsonify
from config.database import db
from models import Cliente

cliente_bp = Blueprint('cliente_bp', __name__, url_prefix='/routes')


@cliente_bp.route("/cliente", methods=("GET", "POST"))
def registrar_cliente(cliente=None):
    # listagem dos clientes
    if request.method == "GET":
        clientes = Cliente.query.all()
        return jsonify([cliente.serialize() for cliente in clientes]), 200
    # adicionar novo cliente
    elif request.method == "POST":
        data = request.get_json()
        print(data)
        cliente_nome = data["nome"]
        print(cliente_nome)
        cliente_email = data['email']
        cliente_senha = data['senha']
        cliente = Cliente(
            nome=cliente_nome,
            email=cliente_email,
            senha=cliente_senha
        )
        if not cliente_nome or not cliente_email or not cliente_senha:
            return jsonify('Faltam dados obrigatórios'), 404

        db.session.add(cliente)
        db.session.commit()
        return jsonify("Cliente cadastrado com sucesso"), 200
