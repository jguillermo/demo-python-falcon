# -*- coding: utf-8 -*-
from project.domain.repository.multimedia import MultimediaRepository
from project.domain.entities.multimedia import Multimedia


class MultimediaSqlAlchemyRepository(MultimediaRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = Multimedia

    def create(self, multimedia: Multimedia):
        try:
            multimedia_id = self.__adapter.create(multimedia)
            return multimedia_id
        except Exception as e:
            raise e

    def update(self, multimedia: Multimedia):
        try:
            kwargs = {'name': multimedia.name}
            return self.__adapter.update(multimedia.id, **kwargs)
        except Exception as e:
            raise e

    def delete(self, id):
        try:
            return self.__adapter.delete(id)
        except Exception as e:
            raise e

    def find_all(self, params):
        try:
            return self.__adapter.find_all(params)
        except Exception as e:
            raise e

    def find_by_id(self, id):
        try:
            return self.__adapter.find_by_id(id)
        except Exception as e:
            raise e
