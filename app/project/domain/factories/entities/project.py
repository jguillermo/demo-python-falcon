# -*- coding: utf-8 -*-

from project.domain.entities.project import Project
from project.domain.valueObjects.project import Id, Name, Description
import datetime


class ProjectFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(id)
        name = Name(kwargs['name'] if 'name' in kwargs else None)
        description = Description(kwargs['description'] if 'description' in kwargs else None)
        id_property_type = kwargs['idPropertyType']
        id_stage = kwargs['idStage']
        id_profile = kwargs['idProfile']
        id_department = kwargs['idDepartment']
        id_province = kwargs['idProvince']
        id_district = kwargs['idDistrict']
        id_urbanization = (kwargs['idUrbanization'] if 'idUrbanization' in kwargs else None)
        id_beach = (kwargs['idBeach'] if 'idBeach' in kwargs else None)
        address = kwargs['address']
        reference = (kwargs['reference'] if 'reference' in kwargs else None)
        finished = (kwargs['finished'] if 'finished' in kwargs else None)
        towers = (kwargs['towers'] if 'towers' in kwargs else None)
        floors = (kwargs['floors'] if 'floors' in kwargs else None)
        units = (kwargs['units'] if 'units' in kwargs else None)
        elevators = (kwargs['elevators'] if 'elevators' in kwargs else None)
        garages = (kwargs['garages'] if 'garages' in kwargs else None)
        date_delivery = (kwargs['dateDelivery'] if 'dateDelivery' in kwargs else None)
        date_publication = datetime.datetime.today()
        date_expire = ProjectFactory.create_date_expire(date_publication, 30)
        state = (kwargs['state'] if 'state' in kwargs else 1)

        return Project(id.value, name.value, description.value, id_property_type, id_stage, id_profile, id_department,
                       id_province, id_district, id_urbanization, id_beach, address, reference,
                       finished, towers, floors, units, elevators, garages, date_delivery, date_publication,
                       date_expire, state)

    @staticmethod
    def create_date_expire(date, days):
        date_expire = date + datetime.timedelta(days=days)
        return date_expire
