# -*- coding: utf-8 -*-
from project.domain.repository.service_project import ServiceProjectRepository
from project.domain.entities.service_project import ServiceProject
from project.domain.entities.service import Service


class MockServiceProjectRepository(ServiceProjectRepository):

    def __init__(self):
        self.services_project = [
            {"id": 1, "idProject": 1, "idService": 2, "nombre": "Agua", "alias": "agua"},
            {"id": 2, "idProject": 1, "idService": 3, "nombre": "Luz", "alias": "luz"},
            {"id": 3, "idProject": 1, "idService": 4, "nombre": "Guardianía", "alias": "guardiania"},
            {"id": 4, "idProject": 2, "idService": 2, "nombre": "Agua", "alias": "agua"},
        ]
        self.services = {
            2: {"id": 2, "idParent": 1, "nombre": "Agua", "alias": "agua", "level": 2, "state": 1},
            3: {"id": 3, "idParent": 1, "nombre": "Luz", "alias": "luz", "level": 2, "state": 1},
            4: {"id": 4, "idParent": 1, "nombre": "Guardinía", "alias": "guardiania", "level": 2, "state": 1}
        }

    def create(self, services_project):
        for service_project in services_project:
            name = self.services[service_project.id]['nombre']
            alias = self.services[service_project.id]['alias']
            self.services_project.append(
                {'id': len(self.services_project) + 1, 'idProject': service_project.idProject,
                 'idService': service_project.idService, 'nombre': name, 'alias': alias}
            )
        return True

    def find_by_project_id(self, project_id):
        data = []
        for index, service_project in enumerate(self.services_project):
            if service_project['idProject'] == int(project_id):
                service = self.services[service_project['idService']]
                tupla = (ServiceProject(service_project['id'], service_project['idService'], service_project['idProject']),
                         Service(service['id'], service['idParent'], service['nombre'], service['alias'], service['level'],
                         service['state']))
                data.append(tupla)
        return data
