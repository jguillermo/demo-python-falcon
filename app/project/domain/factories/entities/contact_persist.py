# -*- coding: utf-8 -*-

from project.domain.entities.contact_persist import ContactPersist


class ContactPersistFactory:

    @staticmethod
    def create(contact_id, **kwargs):
        contact_id = contact_id
        profile_id = kwargs['idProfile']
        state = kwargs['state'] if 'state' in kwargs else 0

        return ContactPersist(contact_id, profile_id, state)
