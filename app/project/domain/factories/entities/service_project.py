# -*- coding: utf-8 -*-

from project.domain.entities.service_project import ServiceProject
from project.domain.entities.service import Service
from project.domain.valueObjects.service_project import Id, IdProject, IdService


class ServiceProjectFactory:

    @staticmethod
    def create(id, service_id, project_id):
        id = Id(id)
        service_id = IdService(service_id)
        project_id = IdProject(project_id)

        service_id.is_null()
        project_id.is_null()

        return ServiceProject(id.value, service_id.value, project_id.value)

    @staticmethod
    def get_services_project(service_project: ServiceProject, service: Service):
        return {
            'idProject': service_project.idProject,
            'idService': service_project.idService,
            'nombre': service.name,
            'alias': service.alias
        }
