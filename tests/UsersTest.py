from src.services.UsersServices import add


def test_add_user():
    request = {
        'email': 'cristian@gmail.com',
        'password': '12345',
        'name': 'Julian Cubides'}
    assert add(request) == 0
