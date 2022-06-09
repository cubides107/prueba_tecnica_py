from flask import Blueprint, request, render_template
from src.services import Publications

publications_route = Blueprint('publications', __name__)


@publications_route.route('/')
def home():
    return render_template('index.html')


# Api para crear una publicacion
@publications_route.route('/new', methods=['POST'])
def add_user():
    dict_publication = {'title': request.form['title'],
                        'description': request.form['description'],
                        'priority': request.form['priority']}

    Publications.add_publication(dict_publication)
    return 'save'
