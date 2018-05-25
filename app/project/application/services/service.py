# -*- coding: utf-8 -*-

from .base import BaseAppService
from project.domain.factories.entities.service import ServiceFactory
from project.infrastructure.common.try_except import handler_except


class ServiceAppService(BaseAppService):

    def __init__(self, domain_service):
        self.__domain_service = domain_service

    @handler_except
    def find_by_id(self, id):
        return [{"method": "find_by_id"}]

    @handler_except
    def find_all(self, params=None):
        result_list = self.__domain_service.find_all(params)
        result = []

        for row_list in result_list:
            fields = params['fields'] if params['fields'] else [attr for attr in row_list.__dict__.keys() if not attr.startswith('_')]
            row = {}
            for field in fields:
                if field.startswith('date'):
                    row.update({field: str(getattr(row_list, field))})
                else:
                    row.update({field: getattr(row_list, field)})
            result.append(row)
        return result

    @handler_except
    def create(self, **kwargs):
        service = ServiceFactory.create(kwargs)
        result = self.__domain_service.create(service)
        return result

    @handler_except
    def update(self, id, **kwargs):
        service = ServiceFactory.create(kwargs, id)
        result = self.__domain_service.update(service)
        return result

    @handler_except
    def delete(self, id):
        result = self.__domain_service.delete(id)
        return result
