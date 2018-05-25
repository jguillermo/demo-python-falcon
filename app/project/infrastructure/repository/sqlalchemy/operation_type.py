# -*- coding: utf-8 -*-
from project.domain.repository.operation_type import OperationTypeRepository
from project.domain.entities.operation_type import OperationType


class OperationTypeSqlAlchemyRepository(OperationTypeRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = OperationType

    def find_all(self, params):
        try:
            return self.__adapter.find_all(params)
        except Exception as e:
            raise e
