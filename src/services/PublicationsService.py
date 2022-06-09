from src.entities.Publication import Publication
from src.entities.StatusEnum import StatusEnum

from src.database.db import db


# Servicion para agregar una publicacion
def add(dict_publication):
    new_publication = Publication(
        dict_publication['title'],
        dict_publication['description'],
        dict_publication['priority'])

    new_publication.status = StatusEnum.CREATED.value

    db.session.add(new_publication)
    db.session.commit()


# Servicio para obtener una publicacion por id
def get(id):
    publication = Publication.query.get(id)
    return publication.to_json()


# Servicio para obtener todas las publicaciones
def get_all():
    publications = Publication.query.all()
    publications_aux = []

    for publication in publications:
        publications_aux.append(publication.to_json())

    return publications_aux


# Servicio para actualizar una publicacion
def update(request):
    publication = Publication.query.get(request['id'])
    publication.change_attributes(request['title'], request['description'], request['priority'], request['time'])
    db.session.commit()
    return 'ok'


# Servicio para eliminar una publicacion
def delete(id):
    publication = Publication.query.get(id)
    db.session.delete(publication)
    db.session.commit()
    return 'ok'