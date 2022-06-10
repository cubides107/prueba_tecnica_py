from flask import Flask
from src.routes import Users, Publications
from config import config
from flask_sqlalchemy import SQLAlchemy
from src.database.db import db
from auth import login_manager

app = Flask(__name__)


# Rutas no encontradas
def page_not_found(error):
    return "<h1> Not found page 11</h1>", 404


if __name__ == '__main__':
    # Config
    app.config.from_object(config['development'])

    # Blueprint
    app.register_blueprint(Users.users_route, url_prefix='/api/users')
    app.register_blueprint(Publications.publications_route, url_prefix='/api/publications')

    # config database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/PruebaTecnica'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLAlchemy(app)

    # crear el contexto
    with app.app_context():
        db.create_all()

    # Configuracion para Autenticacion
    login_manager.init_app(app)

    # Error handler
    app.register_error_handler(404, page_not_found)
    app.run()
