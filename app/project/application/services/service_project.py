# -*- coding: utf-8 -*-

from builtins import set
from project.domain.factories.entities.service_project import ServiceProjectFactory
from project.infrastructure.common.try_except import handler_except


class ServiceProjectAppService:

    def __init__(self, domain_service):
        self.__domain_service = domain_service

    @handler_except
    def create(self, id, **kwargs):
        services = self._get_services(id, kwargs)
        result = self.__domain_service.create(services)
        return result

    @handler_except
    def find_by_project_id(self, project_id):
        result = {}
        res = self.__domain_service.find_by_project_id(project_id)
        for serviceProject, services in res:
            key = self.switcher(services.idParent)
            data = ServiceProjectFactory.get_services_project(serviceProject, services)
            result.setdefault(key, []).append(data)
        return result

    @staticmethod
    def _get_services(project_id, kwargs):
        groups = ['services', 'common_areas', 'generals', 'add', 'authorizations']
        services_ids = []
        services = []

        for group in kwargs:
            if group in groups:
                for service in kwargs[group]:
                    services_ids.append(service)

        services_ids = list(set(services_ids))
        for service_id in services_ids:
            services.append(ServiceProjectFactory.create(None, service_id, project_id))

        return services

    @staticmethod
    def switcher(service_parent_id):
        switcher = {
            1: "Services",
            8: "Common areas",
            29: "General",
            39: "Additional",
            43: "Authorizations"
        }
        return switcher.get(service_parent_id, None)

