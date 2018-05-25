# -*- coding: utf-8 -*-
from project.domain.repository.project import ProjectRepository
from project.domain.entities.project import Project


class ProjectSqlAlchemyRepository(ProjectRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = Project

    def create(self, project: Project):
        try:
            return self.__adapter.create(project)
        except Exception as e:
            raise e

    def update(self, project: Project):
        try:
            kwargs = {'name': project.name}
            return self.__adapter.update(project.id, **kwargs)
        except Exception as e:
            raise e

    def delete(self, id):
        try:
            return self.__adapter.delete(id)
        except Exception as e:
            raise e

    def find_all(self, params):
        try:
            return self.__adapter.find_all(params)
        except Exception as e:
            raise e

    def find_by_id(self, id):
        try:
            return self.__adapter.find_by_id(id)
        except Exception as e:
            raise e

    def shuffle(self):
        try:
            sql = 'SELECT * FROM %s ORDER BY RAND()' % 'project'
            return self.__adapter.statement(sql)
        except Exception as e:
            raise e
