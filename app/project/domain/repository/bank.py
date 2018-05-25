# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class BankRepository(ABC):
    @abstractmethod
    def create(self, bank):
        raise NotImplementedError

    @abstractmethod
    def update(self, bank):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abstractmethod
    def find_all(self, params):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id):
        raise NotImplementedError
