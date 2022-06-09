from src.entities.User import User
from src.database.db import db
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph


# Servicio para agregar un usuario
def add(request):
    encrypt_password = genph(request['password'])
    new_user = User(request['email'], encrypt_password, request['name'])

    db.session.add(new_user)
    db.session.commit()


# Servicio para obtener un usuario por el id
def get(id):
    user = User.query.get(id)
    return user.to_json()


# Servicio para obtener todos los usuarios
def get_all():
    users = User.query.all()
    users_aux = []

    for user in users:
        users_aux.append(user.to_json())

    return users_aux


# Servicio para actualizar un usuario
def update(request):
    user = User.query.get(request['id'])
    user.change_attributes(request['email'], request['password'], request['name'])
    db.session.commit()
    return 'ok'


# Servicio para eliminar un usuario
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return 'ok'


def login(command):
    user = User.query.filter_by(email=command['email']).first()
    print(f"hola {user.password}")
    return checkph(user.password, command['password'])
