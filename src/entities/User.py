class User:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


def to_json(self):
    return {
        'id': self.id,
        'email': self.email,
        'name': self.name
    }
