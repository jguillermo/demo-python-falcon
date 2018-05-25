# -*- coding: utf-8 -*-
from project.domain.repository.project import ProjectRepository
from project.domain.entities.project import Project
from project.domain.valueObjects.project import Id, Name, Description
from datetime import date


class MockProjectRepository(ProjectRepository):

    def __init__(self):
        self.data = [
            {
                'id': '1', 'description': 'test_1', 'idPropertyType': '1', 'idStage': '1', 'idProfile': '1',
                'name': 'test_1', 'idDepartment': '1', 'idProvince': '1', 'idDistrict': '1', 'state': '1',
                'idUrbanization': '1', 'idBeach': '1', 'address': 'test_1', 'reference': 'test_1', 'finished': 'test_1',
                'dateDelivery': date(2018, 5, 5), 'datePublication': date(2018, 5, 5), 'dateExpire': date(2018, 5, 5),
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            },
            {
                'id': '2', 'description': 'test_2', 'idPropertyType': '1', 'idStage': '1', 'idProfile': '1',
                'name': 'test_2', 'idDepartment': '1', 'idProvince': '1', 'idDistrict': '1', 'state': '1',
                'idUrbanization': '1', 'idBeach': '1', 'address': 'test_2', 'reference': 'test_2', 'finished': 'test_2',
                'dateDelivery': date(2018, 5, 5), 'datePublication': date(2018, 5, 5), 'dateExpire': date(2018, 5, 5),
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            },
            {
                'id': '3', 'description': 'test_3', 'idPropertyType': '1', 'idStage': '1', 'idProfile': '1',
                'name': 'test_3', 'idDepartment': '1', 'idProvince': '1', 'idDistrict': '1', 'state': '1',
                'idUrbanization': '1', 'idBeach': '1', 'address': 'test_3', 'reference': 'test_3', 'finished': 'test_3',
                'dateDelivery': date(2018, 5, 5), 'datePublication': date(2018, 5, 5), 'dateExpire': date(2018, 5, 5),
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            },
            {
                'id': '4', 'description': 'test_4', 'idPropertyType': '1', 'idStage': '1', 'idProfile': '1',
                'name': 'test_4', 'idDepartment': '1', 'idProvince': '1', 'idDistrict': '1', 'state': '1',
                'idUrbanization': '1', 'idBeach': '1', 'address': 'test_4', 'reference': 'test_4', 'finished': 'test_4',
                'dateDelivery': date(2018, 5, 5), 'datePublication': date(2018, 5, 5), 'dateExpire': date(2018, 5, 5),
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            }
        ]

    def create(self, project: Project):
        self.data.append(
            {
                'id': project.id, 'description': project.description, 'idPropertyType': project.idPropertyType,
                'idStage': project.idStage, 'idProfile': project.idProfile, 'name': project.name,
                'idDepartment': project.idDepartment, 'idProvince': project.idProvince, 'idDistrict': project.idDistrict,
                'idUrbanization': project.idUrbanization, 'idBeach': project.idBeach, 'address': project.address,
                'reference': project.reference,  'finished': project.finished, 'dateDelivery': project.dateDelivery,
                'datePublication': project.datePublication, 'dateExpire': project.dateExpire, 'state': project.state
            }
        )
        return True

    def update(self, project):
        pass

    def delete(self, id):
        pass

    def find_all(self, params=None):
        resp = []
        for project in self.data:
            id = Id(project['id'])
            name = Name(project['name'])
            description = Description(project['description'])
            id_property_type = project['idPropertyType']
            id_stage = project['idStage']
            id_profile = project['idProfile']
            id_department = project['idDepartment']
            id_province = project['idProvince']
            id_district = project['idDistrict']
            id_urbanization = project['idUrbanization']
            id_beach = project['idBeach']
            address = project['address']
            reference = project['reference']
            finished = project['finished']
            towers = project['towers']
            floors = project['floors']
            units = project['units']
            elevators = project['elevators']
            garages = project['garages']
            date_delivery = project['dateDelivery']
            date_publication = project['datePublication']
            date_expire = project['dateExpire']
            state = project['state']

            resp.append(Project(id.value, name.value, description.value, id_property_type, id_stage, id_profile,
                                id_department, id_province, id_district, id_urbanization, id_beach, address, reference,
                                finished, towers, floors, units, elevators, garages, date_delivery, date_publication,
                                date_expire, state))
        return resp

    def find_by_id(self, id):
        for project in self.data:
            if project['id'] == id:
                id = Id(project['id'])
                name = Name(project['name'])
                description = Description(project['description'])
                id_property_type = project['idPropertyType']
                id_stage = project['idStage']
                id_profile = project['idProfile']
                id_department = project['idDepartment']
                id_province = project['idProvince']
                id_district = project['idDistrict']
                id_urbanization = project['idUrbanization']
                id_beach = project['idBeach']
                address = project['address']
                reference = project['reference']
                finished = project['finished']
                towers = project['towers']
                floors = project['floors']
                units = project['units']
                elevators = project['elevators']
                garages = project['garages']
                date_delivery = project['dateDelivery']
                date_publication = project['datePublication']
                date_expire = project['dateExpire']
                state = project['state']

                return Project(id.value, name.value, description.value, id_property_type, id_stage, id_profile,
                               id_department, id_province, id_district, id_urbanization, id_beach, address, reference,
                               finished, towers, floors, units, elevators, garages, date_delivery, date_publication,
                               date_expire, state)

    def shuffle(self):
        resp = []
        for project in self.data:
            id = Id(project['id'])
            name = Name(project['name'])
            description = Description(project['description'])
            id_property_type = project['idPropertyType']
            id_stage = project['idStage']
            id_profile = project['idProfile']
            id_department = project['idDepartment']
            id_province = project['idProvince']
            id_district = project['idDistrict']
            id_urbanization = project['idUrbanization']
            id_beach = project['idBeach']
            address = project['address']
            reference = project['reference']
            finished = project['finished']
            towers = project['towers']
            floors = project['floors']
            units = project['units']
            elevators = project['elevators']
            garages = project['garages']
            date_delivery = project['dateDelivery']
            date_publication = project['datePublication']
            date_expire = project['dateExpire']
            state = project['state']
            project_instance = Project(id.value, name.value, description.value, id_property_type, id_stage, id_profile,
                                       id_department, id_province, id_district, id_urbanization, id_beach,
                                       address, reference, finished, towers, floors, units, elevators, garages,
                                       date_delivery, date_publication, date_expire, state)
            resp.append(project_instance)
        return resp
