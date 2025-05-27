from flask import Blueprint, request, jsonify
from app.models.reserva_model import Reserva
from database import db
from app.controllers.reserva_controller import validar_turma

reservas_blueprint = Blueprint("reservas", __name__, url_prefix="/reservas")

@reservas_blueprint.route("/", methods=["POST"])
def criar_reserva():
    dados = request.json
    turma_id = dados.get("turma_id")
    sala = dados.get("sala")
    data = dados.get("data")
    hora_inicio = dados.get("hora_inicio")
    hora_fim = dados.get("hora_fim")

    if not all([turma_id, sala, data, hora_inicio, hora_fim]):
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva = Reserva(
        turma_id=turma_id,
        sala=sala,
        data=data,
        hora_inicio=hora_inicio,
        hora_fim=hora_fim
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201

@reservas_blueprint.route("/", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        } for r in reservas
    ])
