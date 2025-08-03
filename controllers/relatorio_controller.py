from models.relatorio import Relatorio, db

def criar_relatorio(data):
    novo_relatorio = Relatorio(**data)
    db.session.add(novo_relatorio)
    db.session.commit()
    return novo_relatorio

def listar_relatorios():
    return Relatorio.query.all()
