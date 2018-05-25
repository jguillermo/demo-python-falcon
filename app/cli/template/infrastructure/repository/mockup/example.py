# -*- coding: utf-8 -*-

from context.domain.repository.example import ExampleRepository
from context.domain.entities.example import Example
from context.domain.factories.entities.example import ExampleFactory


class MockExampleRepository(ExampleRepository):

    def __init__(self):
        self.data = [
            {'id': 1, 'name': 'Escalera al cielo'},
            {'id': 2, 'name': 'Dulce hogar'}
        ]

    def create(self, example: Example):
        self.data.append(
            {'id': example.id, 'name': example.name}
        )
        return True

    def update(self, id, example):
        pass

    def delete(self, id):
        pass

    def find_all(self, params=None):
        resp = []
        for example in self.data:
            resp.append(ExampleFactory.create(example))
        return resp

    def find_by_id(self, id):
        for example in self.data:
            if example['id'] == id:
                return ExampleFactory.create(example)
