# -*- coding: utf-8 -*-


class ProjectDomainService(object):

    def __init__(self, repository):
        self.repository = repository

    def find_by_id(self, id):
        try:
            resp = self.repository.find_by_id(id)
            return resp
        except Exception as e:
            raise e

    def find_all(self, params):
        try:
            resp = self.repository.find_all(params)
            return resp
        except Exception as e:
            raise e

    def create(self, project):
        try:
            return self.repository.create(project)
        except Exception as e:
            raise e

    def update(self, project):
        try:
            return self.repository.update(project)
        except Exception as e:
            raise e

    def delete(self, id):
        try:
            return self.repository.delete(id)
        except Exception as e:
            raise e

    def shuffle(self):
        try:
            return self.repository.shuffle()
        except Exception as e:
            raise e
