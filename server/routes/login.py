from flask import Blueprint, jsonify, request
from models import Cliente
from werkzeug.security import check_password_hash

login_bp = Blueprint('login_bp', __name__, url_prefix='/login')


@login_bp.route("/", methods=["POST"])
def login():
    email = request.json.get('email')
    senha = request.json.get('senha')

    if not email or not senha:
        return jsonify({'error': 'Credenciais inválidas'}), 400

    usuario = Cliente.query.filter_by(email=email).first()

    if not usuario or not check_password_hash(usuario.senha, senha):
        return jsonify({'error': 'Credenciais inválidas'}), 401

    return jsonify({'message': 'Login bem-sucedido'}), 200
