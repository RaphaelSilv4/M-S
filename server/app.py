from flask import Flask
from flask_cors import CORS
from config.database import db
from routes.cliente_routes import cliente_bp
from routes.cargos_routes import cargo_bp
from routes.login import login_bp

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:passward@127.0.0.1:5432/bd'
db.init_app(app)
app.register_blueprint(cliente_bp)
app.register_blueprint(cargo_bp)
app.register_blueprint(login_bp)
CORS(app)


if __name__ == '__main__':
    app.run()

