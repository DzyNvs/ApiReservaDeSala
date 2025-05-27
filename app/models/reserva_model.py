from database import db

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(10), nullable=False)       # Formato: 'YYYY-MM-DD'
    hora_inicio = db.Column(db.String(5), nullable=False) # Formato: 'HH:MM'
    hora_fim = db.Column(db.String(5), nullable=False)    # Formato: 'HH:MM'

    def __repr__(self):
        return f"<Reserva {self.id} - Turma {self.turma_id} - Sala {self.sala}>"
