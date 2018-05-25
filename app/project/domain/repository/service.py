# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class ServiceRepository(ABC):
    @abstractmethod
    def find_all(self, params):
        raise NotImplementedError
