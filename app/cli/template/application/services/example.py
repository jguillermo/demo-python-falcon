# -*- coding: utf-8 -*-

from .base import BaseAppService
from context.domain.factories.entities.example import ExampleFactory
from project.infrastructure.common.try_except import handler_except


class ExampleAppService(BaseAppService):

    def __init__(self, domain_service):
        self.__domain_service = domain_service

    @handler_except
    def find_by_id(self, id):
        example = self.__domain_service.find_by_id(id)
        fields = [attr for attr in example.__dict__.keys() if not attr.startswith('_')]
        result = []
        row = {}
        for field in fields:
            if field.startswith('date'):
                row.update({field: getattr(example, field).strftime('%d/%m/%Y')})
            else:
                row.update({field: getattr(example, field)})
        result.append(row)
        return result

    @handler_except
    def find_all(self, params=None):
        result_list = self.__domain_service.find_all(params)
        result = []

        for row_list in result_list:
            fields = params['fields'] if params['fields'] else [attr for attr in row_list.__dict__.keys() if not attr.startswith('_')]
            row = {}
            for field in fields:
                if field.startswith('date'):
                    row.update({field: getattr(row_list, field).strftime('%d/%m/%Y')})
                else:
                    row.update({field: getattr(row_list, field)})
            result.append(row)
        return result

    @handler_except
    def create(self, **kwargs):
        example = ExampleFactory.create(kwargs)
        return self.__domain_service.create(example)

    @handler_except
    def update(self, id, **kwargs):
        example = ExampleFactory.create(kwargs, id)
        return self.__domain_service.update(example)

    @handler_except
    def delete(self, id):
        return self.__domain_service.delete(id)
