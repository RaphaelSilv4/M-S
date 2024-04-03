from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.database import db
from routes import app_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Rr159789852@127.0.0.1:5432/M & S'
db.init_app(app)

app.register_blueprint(app_routes)
if __name__ == '__main__':
    app.run()
