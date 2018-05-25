# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class ContactPersistsRepository(ABC):

    @abstractmethod
    def find_by_id_profile(self, id_profile):
        raise NotImplementedError
