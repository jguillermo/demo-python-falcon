# -*- coding: utf-8 -*-


class ContactDomainService(object):

    def __init__(self, repository):
        self.repository = repository

    def find_by_project_id(self, id_project):
        return self.repository.find_by_project_id(id_project)

    def create(self, contact):
        return self.repository.create(contact)

    def update(self, id_project, **kwargs):
        return self.repository.update(id_project, **kwargs)

    def create_contact_persist(self, contact_persist):
        return self.repository.create_contact_persist(contact_persist)

    def update_contact_persist(self, id_profile, **kwargs):
        return self.repository.update_contact_persist(id_profile, **kwargs)

    def find_contact_persist(self, id_profile):
        return self.repository.find_contact_persist(id_profile)
