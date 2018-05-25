# -*- coding: utf-8 -*-

from project.domain.factories.entities.contact import ContactFactory
from project.domain.factories.entities.contact_persist import ContactPersistFactory
from project.infrastructure.common.try_except import handler_except


class ContactAppService:

    def __init__(self, domain_service):
        self.__domain_service = domain_service

    @handler_except
    def find_by_id(self, id_project):
        contact = self.__domain_service.find_by_project_id(id_project)
        return contact if contact is None else ContactFactory.get_contact(contact)

    @handler_except
    def create(self, id_project, **kwargs):
        params = kwargs.pop('persist')
        contact = self.__domain_service.find_by_project_id(id_project)
        if contact is not None:
            data = ContactFactory.get_contact(contact)
            return {'idContact': data['id']}
        else:
            contact = ContactFactory.create(id_project, **kwargs)
            id_contact = self.__domain_service.create(contact)
            id_persist = self.create_or_update_contact_persist(id_contact, params)
            return {'idContact': id_contact, 'idContactPersist': id_persist}

    @handler_except
    def update(self, id_project, **kwargs):
        params = kwargs.pop('persist')
        contact = ContactFactory.create(id_project, **kwargs)
        contact = ContactFactory.get_contact(contact)
        contact.pop('id')
        id_contact = self.__domain_service.update(id_project, **contact)
        id_persist = self.create_or_update_contact_persist(id_contact, params)
        return {'idContact': int(id_contact), 'idContactPersist': id_persist}

    def create_or_update_contact_persist(self, id_contact, params):
        contact_persist = self.__domain_service.find_contact_persist(params['idProfile'])
        if contact_persist is None:
            contact_persist = ContactPersistFactory.create(id_contact, **params)
            return self.__domain_service.create_contact_persist(contact_persist)
        else:
            params['idContact'] = id_contact
            self.__domain_service.update_contact_persist(params['idProfile'], **params)
            return contact_persist.id
