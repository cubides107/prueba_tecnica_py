from flask import Blueprint, request, jsonify
from src.services import UsersServices
from flask_login import login_user, logout_user
from flask_login import login_required

users_route = Blueprint('users', __name__)


# Api para crear un nuevo usuarios
@users_route.route('/new', methods=['POST'])
@login_required
def add():
    dict_user = {
        'email': request.json['email'],
        'password': request.json['password'],
        'name': request.json['name']}

    return jsonify(UsersServices.add(dict_user))


# Api para actualizar un usuario
@users_route.route('/update', methods=['POST'])
@login_required
def update():
    command = {
        'id': request.json['id'],
        'email': request.json['email'],
        'password': request.json['password'],
        'name': request.json['name']}

    return jsonify(UsersServices.update(command))


# Api para obtener todos los usuarios
@users_route.route('/')
@login_required
def get_all():
    dto = UsersServices.get_all()
    return jsonify(dto)


# Api para eliminar un usuario
@users_route.route('/delete/<id>', methods=['GET'])
@login_required
def delete(id):
    return jsonify(UsersServices.delete(id))


# Api para obtener un usuario por id
@users_route.route('/get/<id>', methods=['GET'])
@login_required
def get(id):
    return UsersServices.get(id)


@users_route.route('/login', methods=['POST'])
def login():
    command = {
        'email': request.json['email'],
        'password': request.json['password']}
    user = UsersServices.login(command)
    return str(login_user(user))


# Api para cerrar sesión
@users_route.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify(0)
