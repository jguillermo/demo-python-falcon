# -*- coding: utf-8 -*-
from .base import BaseAppService
from project.domain.factories.entities.project import ProjectFactory
from project.infrastructure.common.try_except import handler_except


class ProjectAppService(BaseAppService):

    def __init__(self, domain_service):
        self.__domain_service = domain_service

    @handler_except
    def find_by_id(self, id):
        result = []
        project = self.__domain_service.find_by_id(id)
        if project is None:
            return result

        fields = [attr for attr in project.__dict__.keys() if not attr.startswith('_')]
        row = {}
        for field in fields:
            if field.startswith('date'):
                row.update({field: getattr(project, field).strftime('%Y-%m-%d')})
            else:
                row.update({field: getattr(project, field)})
        result.append(row)
        return result

    @handler_except
    def find_all(self, params=None):
        result = []
        projects = self.__domain_service.find_all(params)
        if projects is None:
            return result

        for project in projects:
            fields = params['fields'] if params['fields'] else [attr for attr in project.__dict__.keys() if not attr.startswith('_')]
            row = {}
            for field in fields:
                if field.startswith('date'):
                    row.update({field: getattr(project, field).strftime('%Y-%m-%d')})
                else:
                    row.update({field: getattr(project, field)})
            result.append(row)
        return result

    @handler_except
    def create(self, **kwargs):
        project = ProjectFactory.create(kwargs)
        project_id = self.__domain_service.create(project)
        return {'idProject': project_id}

    @handler_except
    def update(self, id, **kwargs):
        project = ProjectFactory.create(kwargs, id)
        result = self.__domain_service.update(project)
        return result

    @handler_except
    def delete(self, id):
        result = self.__domain_service.delete(id)
        return result
