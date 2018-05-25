# -*- coding: utf-8 -*-


class ServiceProjectDomainService(object):

    def __init__(self, repository):
        self.repository = repository

    def create(self, services):
        try:
            return self.repository.create(services)
        except Exception as e:
            raise e

    def find_by_project_id(self, id_project):
        try:
            return self.repository.find_by_project_id(id_project)
        except Exception as e:
            raise e
