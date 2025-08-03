from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Relatorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
