from flask import Flask
from flask_cors import CORS
from database import db
from app.routes.reserva_route import reservas_blueprint  # nome correto do blueprint importado

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registra o blueprint com o prefixo correto
    app.register_blueprint(reservas_blueprint, url_prefix="/api/reservas")

    print(app.url_map)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
