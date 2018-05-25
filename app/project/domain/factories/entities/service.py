# -*- coding: utf-8 -*-

from project.domain.entities.service import Service
from project.domain.valueObjects.service import Id, IdParent, Name, Alias, Level, State


class ServiceFactory:


    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if id is None else id)
        id_parent = IdParent(kwargs['name'])
        name = Name(kwargs['name'])
        alias = Alias(kwargs['alias'])
        level = Level(kwargs['level'])
        state = State(kwargs['state'])

        return Service(id, id_parent, name, alias, level, state)
