from datetime import datetime
from src.entities.PriorityEnum import PriorityEnum
from src.database.db import db
import uuid


class Publication(db.Model):
    __tablename__ = 'Publications'

    id = db.Column(db.VARCHAR(36), primary_key=True)
    title = db.Column(db.VARCHAR(40))
    priority = db.Column(db.Integer())
    description = db.Column(db.String(80))
    status = db.Column(db.Integer())
    time = db.Column(db.DateTime)
    user_id = db.Column(db.VARCHAR(36),
                        db.ForeignKey('Users.id'),
                        nullable=True)

    def __init__(self, title, description, priority: PriorityEnum):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.time = datetime.now()

    def change_attributes(self, title, description, priority: PriorityEnum, time):
        self.title = title
        self.description = description
        self.priority = priority
        self.time = time

    def calculate_time(self):
        return datetime.now() - self.time

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'time': str(self.calculate_time())
        }
