# -*- coding: utf-8 -*-

from project.domain.entities.district import District
from project.domain.valueObjects.district import Id, Name, Alias, IdDepartment, IdProvince, Beach, Status

state_active = 1


class DistrictFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if id is None else id)
        name = Name(kwargs['name'])
        alias = Alias(kwargs['alias'])
        id_department = IdDepartment(kwargs['departmentId'])
        id_province = IdDepartment(kwargs['provinceId'])
        beach = Beach(kwargs['beach'])
        status = Status(kwargs['status'])

        name.is_null()

        district = District(id, name, alias, id_department, id_province, beach, status)
        district.to_dict(kwargs)
        return district
