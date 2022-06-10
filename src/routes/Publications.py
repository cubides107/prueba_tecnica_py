from flask import Blueprint, request, render_template, jsonify
from src.services import PublicationsService
from flask_login import login_required
from flask_login import current_user
from flasgger import swag_from

publications_route = Blueprint('publications', __name__)


# Api para crear una publicacion
@publications_route.route('/new', methods=['POST'])
@login_required
# @swag_from(specs_dict)
def add_publication():
    """Example endpoint returning a list of colors by palette
        This is using docstrings for specifications.
        ---
        parameters:
          - name: palette
            in: path
            type: string
            enum: ['all', 'rgb', 'cmyk']
            required: true
            default: all
        definitions:
          Palette:
            type: object
            properties:
              palette_name:
                type: array
                items:
                  $ref: '#/definitions/Color'
          Color:
            type: string
        responses:
          200:
            description: A list of colors (may be filtered by palette)
            schema:
              $ref: '#/definitions/Palette'
            examples:
              rgb: ['red', 'green', 'blue']
        """
    dict_publication = {
        'id': current_user.id,
        'title': request.json['title'],
        'description': request.json['description'],
        'priority': request.json['priority']}

    return jsonify(PublicationsService.add(dict_publication))

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

    return jsonify(PublicationsService.update(command))


# Api para eliminar un publicacion
@publications_route.route('/delete/<id>', methods=['GET'])
@login_required
def delete(id):
    return jsonify(PublicationsService.delete(id))


# Api para obtener una publicacion
@publications_route.route('/get/<id>', methods=['GET'])
@login_required
def get(id):
    return PublicationsService.get(id)
