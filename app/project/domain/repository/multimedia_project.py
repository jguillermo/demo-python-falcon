# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class MultimediaProjectRepository(ABC):
    @abstractmethod
    def create(self, multimedias):
        raise NotImplementedError

    @abstractmethod
    def find_by_id_project(self, id):
        raise NotImplementedError
