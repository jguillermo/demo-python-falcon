# -*- coding: utf-8 -*-
from context.domain.repository.example import ExampleRepository
from context.domain.entities.example import Example


class ExampleSqlAlchemyRepository(ExampleRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = Example

    def create(self, example: Example):
        try:
            example_id = self.__adapter.create(example)
            return {'idExample': example_id}
        except Exception as e:
            raise e

    def update(self, id, **kwargs):
        try:
            return self.__adapter.update(id, **kwargs)
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
