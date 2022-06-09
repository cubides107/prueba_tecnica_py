from flask import Flask
from src.routes import Users, Publications
from config import config
from flask_sqlalchemy import SQLAlchemy
from src.database.db import db
from flask import Flask, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)
# Configuracion de Swagger
app.json_encoder = LazyJSONEncoder


def page_not_found(error):
    return "<h1> Not found page 11</h1>", 404


swagger_template = dict(
    info={
        'title': LazyString(lambda: 'My first Swagger UI document'),
        'version': LazyString(lambda: '0.1'),
        'description': LazyString(
            lambda: 'This document depicts a      sample Swagger UI document and implements Hello World functionality after executing GET.'),
    },
    host=LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'hello_world',
            "route": '/hello_world.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app)

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

    #crear el contexto
    with app.app_context():
        db.create_all()

    # Error handler
    app.register_error_handler(404, page_not_found)
    app.run()
