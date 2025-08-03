from flask import Blueprint, request, jsonify
from controllers.relatorio_controller import criar_relatorio, listar_relatorios

relatorio_bp = Blueprint('relatorio', __name__)

@relatorio_bp.route('/relatorios', methods=['POST'])
def criar():
    data = request.get_json()
    relatorio = criar_relatorio(data)
    return jsonify({'id': relatorio.id, 'titulo': relatorio.titulo}), 201

@relatorio_bp.route('/relatorios', methods=['GET'])
def listar():
    relatorios = listar_relatorios()
    return jsonify([{'id': r.id, 'titulo': r.titulo, 'conteudo': r.conteudo} for r in relatorios])
