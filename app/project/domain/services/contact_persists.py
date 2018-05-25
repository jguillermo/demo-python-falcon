# -*- coding: utf-8 -*-


class ContactPersistsDomainService(object):

    def __init__(self, repository):
        self.repository = repository

    def find_by_id_profile(self, id_profile):
        try:
            resp = self.repository.find_by_id_profile(id_profile)
            return resp
        except Exception as e:
            raise e
