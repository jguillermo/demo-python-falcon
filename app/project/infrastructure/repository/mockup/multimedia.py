# -*- coding: utf-8 -*-

from project.domain.repository.multimedia import MultimediaRepository
from project.domain.entities.multimedia import Multimedia
from project.domain.factories.entities.multimedia import MultimediaFactory


class MockMultimediaRepository(MultimediaRepository):

    def __init__(self):
        self.data = [
            {"state": 1, "url": "img", "name": "368490_plgalaxy.jpg", "id": 1, "type": 5},
            {"state": 1, "url": "img", "name": "368490_imagencasatest.jpg", "id": 2, "type": 1},
            {"state": 1, "url": "img", "name": "368490_plgalaxy.jpg", "id": 3, "type": 5}
        ]

    def create(self, multimedia: Multimedia):
        self.data.append(
            {'id': multimedia.id, 'name': multimedia.name}
        )
        return True

    def update(self, multimedia):
        pass

    def delete(self, id):
        pass

    def find_all(self, params=None):
        resp = []
        for multimedia in self.data:
            resp.append(MultimediaFactory.create(multimedia))
        return resp

    def find_by_id(self, id):
        for multimedia in self.data:
            if multimedia['id'] == id:
                return MultimediaFactory.create(multimedia)
