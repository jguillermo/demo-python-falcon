# -*- coding: utf-8 -*-

from project.domain.entities.property_type import PropertyType
from project.domain.valueObjects.property_type import Id, Id_Parent,  Name, Level, State

state_active = 1


class PropertyTypeFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(id)
        id_parent = Id_Parent(kwargs['id_parent'])
        name = Name(kwargs['name'])
        level = Level(kwargs['level'])
        state = State(state_active)

        name.is_null()

        return PropertyType(id, id_parent, name, level, state)

