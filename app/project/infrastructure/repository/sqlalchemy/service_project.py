# -*- coding: utf-8 -*-
from project.domain.repository.service_project import ServiceProjectRepository
from project.domain.entities.service_project import ServiceProject
from project.domain.entities.service import Service
from project.infrastructure.adapter.sql.sqlalchemy import SqlAlchemyAdapter


class ServiceProjectSqlAlchemyRepository(ServiceProjectRepository):

    def __init__(self, adapter: SqlAlchemyAdapter):
        self.__adapter = adapter
        self.__adapter.entity = ServiceProject

    def create(self, services):
        where = (ServiceProject.idProject == services[0].idProject)
        self.__adapter.delete_with_params(where)
        self.__adapter.bulk_insert(services)
        return self.__adapter.commit()

    def find_by_project_id(self, project_id):
        return self.__adapter.session.query(ServiceProject, Service).join(Service, Service.id == ServiceProject.idService).\
            filter(ServiceProject.idProject == project_id).all()
