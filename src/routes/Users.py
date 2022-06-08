from flask import Blueprint

from src.services import Users

users_route = Blueprint('users', __name__)


@users_route.route('/')
def get_user():
    return Users.get_user()
