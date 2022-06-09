from src.entities.User import User
from src.database.db import db


def add_user(dict_user):
    new_user = User(dict_user['email'], dict_user['password'], dict_user['name'])
    db.session.add(new_user)
    db.session.commit()
