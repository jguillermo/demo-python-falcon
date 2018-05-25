# -*- coding: utf-8 -*-

from project.domain.repository.service_project import ServiceProjectRepository


class ServiceDomainService(object):

    def __init__(self, repository: ServiceProjectRepository):
        self.repository = repository

    def find_all(self, params):
        try:
            return self.repository.find_all(params)
        except Exception as e:
            raise e
