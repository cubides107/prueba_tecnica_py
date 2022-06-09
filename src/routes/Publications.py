from flask import Blueprint, request, render_template, jsonify
from src.services import PublicationsService
from src.entities.Publication import Publication


publications_route = Blueprint('publications', __name__)


# Api para crear una publicacion
@publications_route.route('/new', methods=['POST'])
def add_publication():
    dict_publication = {'title': request.json['title'],
                        'description': request.json['description'],
                        'priority': request.json['priority']}

    PublicationsService.add(dict_publication)
    return jsonify('ok')


# Api para obtener una publicacion por id
@publications_route.route('/update/<id>')
def get_publication(id):
    dto = PublicationsService.get(id)
    return dto


# Api para obtener todas las publicaciones
@publications_route.route('/')
def get_all():
    dto = PublicationsService.get_all()
    return jsonify(dto)


# Api para actualizar una publicacion
@publications_route.route('/update', methods=['POST'])
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
def delete(id):
    dto = PublicationsService.delete(id)
    return dto


# Api para obtener una publicacion
@publications_route.route('/get/<id>', methods=['GET'])
def get(id):
    return PublicationsService.get(id)
