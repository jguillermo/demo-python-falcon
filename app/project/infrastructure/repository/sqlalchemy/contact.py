# -*- coding: utf-8 -*-

from project.domain.repository.contact import ContactRepository
from project.domain.entities.contact import Contact
from project.domain.entities.contact_persist import ContactPersist


class ContactSqlAlchemyRepository(ContactRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = Contact

    def create(self, contact: Contact):
        try:
            return self.__adapter.create(contact)
        except Exception as e:
            raise e

    def update(self, id_project, **kwargs):
        result = self.__adapter.session.query(Contact).filter_by(idProject=id_project).first()
        for key, value in kwargs.items():
            setattr(result, key, value)
        self.__adapter.session.commit()
        return result.id

    def find_by_project_id(self, id_project):
        return self.__adapter.session.query(Contact).filter_by(idProject=id_project).first()

    def create_contact_persist(self, contact_persist):
        self.__adapter.entity = ContactPersist
        try:
            return self.__adapter.create(contact_persist)
        except Exception as e:
            raise e

    def update_contact_persist(self, id_profile, **kwargs):
        result = self.__adapter.session.query(ContactPersist).filter_by(idProfile=id_profile).first()
        for key, value in kwargs.items():
            setattr(result, key, value)
        return self.__adapter.session.commit()

    def find_contact_persist(self, id_profile):
        return self.__adapter.session.query(ContactPersist).filter_by(idProfile=id_profile).first()
