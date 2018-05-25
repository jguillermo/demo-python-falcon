# -*- coding: utf-8 -*-


class OperationTypeDomainService(object):

    def __init__(self, repository):
        self.repository = repository

    def find_all(self, params):
        try:
            resp = self.repository.find_all(params)
            return resp
        except Exception as e:
            raise e
