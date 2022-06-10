from src.database.db import db
from flask_login import UserMixin
import uuid


# Clase usuario
class User(UserMixin, db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.VARCHAR(36), primary_key=True)
    email = db.Column(db.VARCHAR(80))
    password = db.Column(db.VARCHAR(120))
    name = db.Column(db.VARCHAR(120))
    publications = db.relationship('Publication')

    def __init__(self, email, password, name):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.name = name

    # Cambiar atributos del usuario
    def change_attributes(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    # Convertir a objeto para retornar
    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name
        }
