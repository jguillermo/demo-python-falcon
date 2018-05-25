# -*- coding: utf-8 -*-

from project.domain.entities.example import Example
from project.domain.valueObjects.example import Id, Name


class ExampleFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if id is None else id)
        name = Name(kwargs['name'])

        return Example(id.value, name.value)
