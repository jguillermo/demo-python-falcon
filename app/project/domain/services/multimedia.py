# -*- coding: utf-8 -*-
from project.domain.valueObjects.multimedia import ALIAS_TYPE, IMAGE_TYPE, PANORAMIC_TYPE, LOGO_TYPE


class MultimediaDomainService(object):

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

    def create(self, multimedia):
        try:
            multimedia_id = self.repository.create(multimedia)
            return multimedia_id
        except Exception as e:
            raise e

    def update(self, multimedia):
        try:
            return self.repository.update(multimedia)
        except Exception as e:
            raise e

    def delete(self, id):
        try:
            return self.repository.delete(id)
        except Exception as e:
            raise e
