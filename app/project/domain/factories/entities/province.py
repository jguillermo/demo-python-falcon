# -*- coding: utf-8 -*-

from project.domain.entities.province import Province
from project.domain.valueObjects.province import Id, Name, Alias, IdDepartment, Beach, Status

state_active = 1


class ProvinceFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if id is None else id)
        name = Name(kwargs['name'])
        alias = Alias(kwargs['alias'])
        id_department = IdDepartment(kwargs['departmentId'])
        beach = Beach(kwargs['beach'])
        status = Status(kwargs['status'])

        name.is_null()

        province = Province(id, name, alias, id_department, beach, status)
        province.to_dict(kwargs)
        return province
