# -*- coding: utf-8 -*-

from project.domain.repository.operation_type import OperationTypeRepository
from project.domain.factories.entities.operation_type import OperationTypeFactory


class MockOperationTypeRepository(OperationTypeRepository):

    def __init__(self):
        self.data = [
            {'id': 1, 'name': 'Venta', 'state': 1},
            {'id': 2, 'name': 'Alquiler', 'state': 1}
        ]

    def find_all(self, params=None):
        resp = []
        for operation_type in self.data:
            resp.append(OperationTypeFactory.create(operation_type))
        return resp
