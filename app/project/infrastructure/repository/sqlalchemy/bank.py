# -*- coding: utf-8 -*-
from project.domain.repository.bank import BankRepository
from project.domain.entities.bank import Bank


class BankSqlAlchemyRepository(BankRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = Bank

    def create(self, bank: Bank):
        try:
            bankid = self.__adapter.create(bank)
            return {'idBank': bankid}
        except Exception as e:
            raise e

    def update(self, bank: Bank):
        try:
            kwargs = {'name': bank.name}
            return self.__adapter.update(bank.id, **kwargs)
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

    def find_by(self, params):
        try:
            return self.__adapter.find_by(params)
        except Exception as e:
            raise e
