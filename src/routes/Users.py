from flask import Blueprint, request, render_template
from src.services import Users

users_route = Blueprint('users', __name__)


@users_route.route('/')
def home():
    return render_template('index.html')


@users_route.route('/new', methods=['POST'])
def add_user():
    dict_user = {'email': request.form['email'],
                 'password': request.form['password'],
                 'name': request.form['name']}

    Users.add_user(dict_user)
    return 'save'
