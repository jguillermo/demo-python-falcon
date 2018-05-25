# -*- coding: utf-8 -*-

from project.infrastructure.common.try_except import handler_except


class OperationTypeAppService:

    def __init__(self, domain_service):
        self.__domain_service = domain_service

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
