from flask import Blueprint, request, render_template, jsonify
from src.services import PublicationsService
from flask_login import login_required
from flask_login import current_user
from flasgger import swag_from
from src.docs.docs import specs_dict

publications_route = Blueprint('publications', __name__)


# Api para crear una publicacion
@publications_route.route('/new', methods=['POST'])
@login_required
@swag_from(specs_dict)
def add_publication():
    dict_publication = {
        'id': current_user.id,
        'title': request.json['title'],
        'description': request.json['description'],
        'priority': request.json['priority']}

    PublicationsService.add(dict_publication)
    return jsonify(id)


# Api para obtener una publicacion por id
@publications_route.route('/update/<id>')
@login_required
@swag_from(specs_dict)
def get_publication(id):
    dto = PublicationsService.get(id)
    return dto


# Api para obtener todas las publicaciones
@publications_route.route('/<id>')
@login_required
def get_all(id):
    dto = PublicationsService.get_all(id)
    return jsonify(dto)


# Api para actualizar una publicacion
@publications_route.route('/update', methods=['POST'])
@login_required
def udpate():
    command = {
        'id': request.json['id'],
        'title': request.json['title'],
        'description': request.json['description'],
        'priority': request.json['priority'],
        'time': request.json['time'],
    }

    dto = PublicationsService.update(command)
    return dto


# Api para eliminar un publicacion
@publications_route.route('/delete/<id>', methods=['GET'])
@login_required
def delete(id):
    dto = PublicationsService.delete(id)
    return dto


# Api para obtener una publicacion
@publications_route.route('/get/<id>', methods=['GET'])
@login_required
def get(id):
    return PublicationsService.get(id)
