# -*- coding: utf-8 -*-


class MultimediaProjectDomainService(object):

    def __init__(self, repository):
        self.repository = repository

    def find_by_id_project(self, id):
        try:
            resp = self.repository.find_by_id_project(id)
            return resp
        except Exception as e:
            raise e

    def create(self, multimedias):
        try:
            return self.repository.create(multimedias)
        except Exception as e:
            raise e
