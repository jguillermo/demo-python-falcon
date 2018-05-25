# -*- coding: utf-8 -*-
from project.domain.repository.property_type import PropertyTypeRepository
from project.domain.entities.property_type import PropertyType


class PropertyTypeSqlAlchemyRepository(PropertyTypeRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = PropertyType

    def create(self, property_type: PropertyType):
        try:
            self.__adapter.create(property_type)
        except Exception as e:
            raise e

    def update(self, property_type: PropertyType):
        try:
            kwargs = {'name': property_type.name}
            return self.__adapter.update(property_type.id, **kwargs)
        except Exception as e:
            raise e

    def delete(self, id):
        try:
            return self.__adapter.delete(id)
        except Exception as e:
            raise e

    def find_all(self, params):
        try:
            return self.__adapter.find_all(params)
        except Exception as e:
            raise e

    def find_by_id(self, id):
        try:
            return self.__adapter.find_by_id(id)
        except Exception as e:
            raise e
