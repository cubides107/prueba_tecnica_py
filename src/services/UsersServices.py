from src.entities.User import User
from src.database.db import db


# Servicio para agregar un usuario
def add(request):
    new_user = User(request['email'], request['password'], request['name'])
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
