# -*- coding: utf-8 -*-

from .base import BaseAppService
from project.domain.factories.entities.bank import BankFactory
from project.infrastructure.common.try_except import handler_except


class BankAppService(BaseAppService):

    def __init__(self, domain_service):
        self.__domain_service = domain_service

    @handler_except
    def find_by_id(self, id):
        result = []
        bank = self.__domain_service.find_by_id(id)
        fields = [attr for attr in bank.__dict__.keys() if not attr.startswith('_')]
        row = {}
        for field in fields:
            if field.startswith('date'):
                row.update({field: getattr(bank, field).strftime('%d/%m/%Y')})
            else:
                row.update({field: getattr(bank, field)})
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
                row.update({field: getattr(row_list, field)})
            result.append(row)
        return result

    @handler_except
    def create(self, **kwargs):
        bank = BankFactory.create(kwargs)
        result = self.__domain_service.create(bank)
        return result

    @handler_except
    def update(self, id, **kwargs):
        bank = BankFactory.create(kwargs, id)
        result = self.__domain_service.update(bank)
        return result

    def delete(self, id):
        result = self.__domain_service.delete(id)
        return result
