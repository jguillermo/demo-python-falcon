# -*- coding: utf-8 -*-

from project.domain.entities.operation_type import OperationType
from project.domain.valueObjects.operation_type import Id, Name, State


class OperationTypeFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if id is None else id)
        name = Name(kwargs['name'])
        state = State(kwargs['state'])

        return OperationType(id.value, name.value, state.value)
