# -*- coding: utf-8 -*-

from project.domain.repository.multimedia_project import MultimediaProjectRepository
from project.domain.entities.multimedia_project import MultimediaProject
from project.domain.factories.entities.multimedia_project import MultimediaProjectFactory


class MockMultimediaProjectRepository(MultimediaProjectRepository):

    def __init__(self):
        self.data = [
            {'id': 1, 'name': 'Escalera al cielo'},
            {'id': 2, 'name': 'Dulce hogar'}
        ]

    def create(self, multimedia_project: MultimediaProject):
        self.data.append(
            {'id': multimedia_project.id, 'name': multimedia_project.name}
        )
        return True

    def update(self, multimedia_project):
        pass

    def delete(self, id):
        pass

    def find_all(self, params=None):
        resp = []
        for multimedia_project in self.data:
            resp.append(MultimediaProjectFactory.create(multimedia_project))
        return resp

    def find_by_id(self, id):
        for multimedia_project in self.data:
            if multimedia_project['id'] == id:
                return MultimediaProjectFactory.create(multimedia_project)
