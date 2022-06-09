from flask import Blueprint, request, jsonify
from src.services import UsersServices

users_route = Blueprint('users', __name__)


# Api para crear un nuevo usuarios
@users_route.route('/new', methods=['POST'])
def add():
    dict_user = {
        'email': request.form['email'],
        'password': request.form['password'],
        'name': request.form['name']}

    UsersServices.add(dict_user)
    return 'save'


# Api para actualizar un usuario
@users_route.route('/update', methods=['POST'])
def update():
    command = {
        'id': request.json['id'],
        'email': request.json['email'],
        'password': request.form['password'],
        'name': request.form['name']}

    UsersServices.add(command)
    return 'ok'


# Api para obtener todas las publicaciones
@users_route.route('/')
def get_all():
    dto = UsersServices.get_all()
    return jsonify(dto)


# Api para eliminar un usuario
@users_route.route('/delete<id>', methods=['GET'])
def delete(id):
    UsersServices.delete(id)
    return 'ok'
