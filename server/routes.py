from flask import Blueprint, request, jsonify
from config.database import db
from models import Cliente

app_routes = Blueprint('routes',__name__,url_prefix='/routes')

@app_routes.route("/cliente",methods=("GET", "POST"))
def register_cliente():
    if request.method == "POST":
        data = request.get_json()
        cliente_nome = data["nome"]
        cliente = Cliente(
            nome = cliente_nome
        )
        db.session.add(cliente)
        db.session.commit()
        return jsonify("Cliente cadastrado com sucesso"),200
