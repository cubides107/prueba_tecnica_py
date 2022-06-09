from src.database.db import db
import uuid


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.VARCHAR(36), primary_key=True)
    email = db.Column(db.VARCHAR(80))
    password = db.Column(db.VARCHAR(120))
    name = db.Column(db.VARCHAR(120))

    def __init__(self, email, password, name):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.name = name


def to_json(self):
    return {
        'id': self.id,
        'email': self.email,
        'name': self.name
    }
