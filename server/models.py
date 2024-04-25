from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from config.database import db

class Cliente(db.Model):
    __tablename__ = "usuario_cliente"

    id = mapped_column(Integer, primary_key=True,autoincrement=True)
    nome = mapped_column(String(30), nullable=False)
    def __init__(self, nome):
        self.nome = nome

