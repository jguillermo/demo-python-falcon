# -*- coding: utf-8 -*-
from project.domain.factories.entities.district import DistrictFactory


class DistrictMicroServiceRepository():

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = DistrictFactory
        self.__adapter.name_microservice = 'ms_location'
        self.__adapter.name_resource = 'district'

    def find_by_id(self, id):
        try:
            return self.__adapter.find_by_id(id)
        except Exception as e:
            raise e
