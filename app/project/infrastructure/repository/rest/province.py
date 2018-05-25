# -*- coding: utf-8 -*-
from project.domain.factories.entities.province import ProvinceFactory


class ProvinceMicroServiceRepository():

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = ProvinceFactory
        self.__adapter.name_microservice = 'ms_location'
        self.__adapter.name_resource = 'province'

    def find_by_id(self, id):
        try:
            return self.__adapter.find_by_id(id)
        except Exception as e:
            raise e
