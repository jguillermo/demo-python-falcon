# -*- coding: utf-8 -*-

from project.domain.entities.stage import Stage
from project.domain.valueObjects.stage import Id, Name, Alias, Type, State


class StageFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if id is None else id)
        name = Name(kwargs['name'])
        alias = Alias(kwargs['alias'])
        type= Type(kwargs['type'])
        state = State(kwargs['state'])

        return Stage(id, name, alias, type, state)
