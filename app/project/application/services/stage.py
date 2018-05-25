# -*- coding: utf-8 -*-

from .base import BaseAppService
from project.domain.factories.entities.stage import StageFactory
from project.infrastructure.common.try_except import handler_except


class StageAppService(BaseAppService):

    def __init__(self, domain_service):
        self.__domain_service = domain_service

    @handler_except
    def find_by_id(self, id):
        result = []
        stage = self.__domain_service.find_by_id(id)
        fields = [attr for attr in stage.__dict__.keys() if not attr.startswith('_')]
        row = {}
        for field in fields:
            if field.startswith('date'):
                row.update({field: getattr(stage, field).strftime('%d/%m/%Y')})
            else:
                row.update({field: getattr(stage, field)})
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
        stage = StageFactory.create(kwargs)
        result = self.__domain_service.create(stage)
        return result

    @handler_except
    def update(self, id, **kwargs):
        stage = StageFactory.create(kwargs)
        result = self.__domain_service.update(stage)
        return result

    @handler_except
    def delete(self, id):
        result = self.__domain_service.delete(id)
        return result
