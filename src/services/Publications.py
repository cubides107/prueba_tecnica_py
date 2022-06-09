from src.entities.Publication import Publication
from src.entities.StatusEnum import StatusEnum

from src.database.db import db


def add_publication(dict_publication):
    new_publication = Publication(dict_publication['title'],
                                  dict_publication['description'],
                                  dict_publication['priority'])

    new_publication.status = StatusEnum.CREATED.value

    db.session.add(new_publication)
    db.session.commit()
