# -*- coding: utf-8 -*-

from project.infrastructure.common.try_except import handler_except
from project.domain.factories.entities.contact import ContactFactory


class ContactPersistsAppService:

    def __init__(self, domain_service):
        self.__domain_service = domain_service

    @handler_except
    def find_by_id(self, id_profile):
        contact = self.__domain_service.find_by_id_profile(id_profile)
        return contact if contact is None else ContactFactory.get_contact(contact)
