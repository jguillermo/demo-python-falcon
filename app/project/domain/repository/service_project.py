# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class ServiceProjectRepository(ABC):
    @abstractmethod
    def create(self, project):
        raise NotImplementedError

    @abstractmethod
    def find_by_project_id(self, id):
        raise NotImplementedError
