# -*- coding: utf-8 -*-

from project.domain.entities.department import Department
from project.domain.valueObjects.department import Id, Name, Alias, CountryId, Beach, Status

state_active = 1


class DeparmentFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if id is None else id)
        name = Name(kwargs['name'])
        alias = Alias(kwargs['name'])
        country_id = CountryId(kwargs['countryId'])
        beach = Beach(kwargs['beach'])
        status = Status(kwargs['status'])

        name.is_null()

        department = Department(id, name, alias, country_id, beach, status)
        department.to_dict(kwargs)
        return department
