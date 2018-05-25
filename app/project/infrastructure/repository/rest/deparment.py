# -*- coding: utf-8 -*-
from project.domain.factories.entities.department import DeparmentFactory


class DepartmentMicroServiceRepository():

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = DeparmentFactory
        self.__adapter.name_microservice = 'ms_location'
        self.__adapter.name_resource = 'department'

    def find_by_id(self, id):
        try:
            return self.__adapter.find_by_id(id)
        except Exception as e:
            raise e
