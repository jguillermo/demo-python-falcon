# -*- coding: utf-8 -*-


class BankDomainService(object):

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

    def create(self, bank):
        try:
            return self.repository.create(bank)
        except Exception as e:
            raise e

    def update(self, bank):
        try:
            return self.repository.update(bank)
        except Exception as e:
            raise e

    def delete(self, id):
        try:
            return self.repository.delete(id)
        except Exception as e:
            raise e
