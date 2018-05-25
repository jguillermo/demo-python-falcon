# -*- coding: utf-8 -*-
from project.domain.repository.contact_persists import ContactPersistsRepository
from project.domain.entities.contact_persist import ContactPersist
from project.domain.entities.contact import Contact


class ContactPersistsSqlAlchemyRepository(ContactPersistsRepository):

    def __init__(self, adapter):
        self.__adapter = adapter

    def find_by_id_profile(self, id_profile):
        return self.__adapter.session.query(Contact).join(ContactPersist).\
            filter(ContactPersist.idProfile == id_profile).filter(ContactPersist.state == 1).first()
