from flask import Flask

from src.routes import Users
from config import config

app = Flask(__name__)


def page_not_found(error):
    return "<h1> Not found page 11</h1>", 404


if __name__ == '__main__':
    # Config
    app.config.from_object(config['development'])
    # Blueprint
    app.register_blueprint(Users.users_route, url_prefix='/api/users')

    # Error handler
    app.register_error_handler(404, page_not_found)
    app.run()
