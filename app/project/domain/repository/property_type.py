# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class PropertyTypeRepository(ABC):
    @abstractmethod
    def create(self, property_type):
        raise NotImplementedError

    @abstractmethod
    def update(self, property_type):
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
