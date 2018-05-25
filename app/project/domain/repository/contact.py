# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class ContactRepository(ABC):
    @abstractmethod
    def create(self, contact):
        raise NotImplementedError

    @abstractmethod
    def update(self, id_project, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def find_by_project_id(self, id_project):
        raise NotImplementedError

    @abstractmethod
    def create_contact_persist(self, contact_persist):
        raise NotImplementedError

    @abstractmethod
    def update_contact_persist(self, id_profile, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def find_contact_persist(self, id_profile):
        raise NotImplementedError
