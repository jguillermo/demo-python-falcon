# -*- coding: utf-8 -*-
from project.domain.repository.contact import ContactRepository
from project.domain.factories.entities.contact import ContactFactory
from project.domain.entities.contact import Contact
from project.domain.entities.contact_persist import ContactPersist


class MockContactRepository(ContactRepository):

    def __init__(self):
        self.contacts = [
            {
                'id': 1, 'idProject': 1, 'name': 'Janet Milagros', 'lastName': 'Huacahuasi', 'phone': '950204432',
                'phoneSecond': '969939230', 'schedule': 'Todos los dias', 'email': 'cunya.victor@gmail.com',
                'emailGroup': 'victor.cunya@orbis.com.pe', 'state': 1
            },
            {
                'id': 2, 'idProject': 2, 'name': 'Luis Miguel', 'lastName': 'Reyes', 'phone': '969967241',
                'phoneSecond': '969978541', 'schedule': 'Todos los dias', 'email': 'luis.reyes@gmail.com',
                'emailGroup': 'luis.reyes@orbis.com.pe', 'state': 1
            },
            {
                'id': 3, 'idProject': 3, 'name': 'Oscar Derulo', 'lastName': 'Glucosa', 'phone': '9741287489',
                'phoneSecond': '9875634152', 'schedule': 'Todos los dias', 'email': 'oscar.derulo@gmail.com',
                'emailGroup': 'oscar.derulo@orbis.com.pe', 'state': 1
            }
        ]

    def create(self, contact: Contact):
        self.contacts.append(
            {
                'id': contact.id, 'idProject': contact.idProject, 'name': contact.name, 'lastName': contact.lastName,
                'phone': contact.phone, 'phoneSecond': contact.phoneSecond, 'schedule': contact.schedule,
                'email': contact.email, 'emailGroup': contact.emailGroup,  'state': contact.state
            }
        )
        return True

    def update(self, contact_id, **kwargs):
        pass

    def find_by_project_id(self, id_project):
        for contact in self.contacts:
            if contact['idProject'] == id_project:
                return ContactFactory.create(id_project, **contact)

    def create_contact_persist(self, contact_persist: ContactPersist):
        pass

    def update_contact_persist(self, contact_id, **kwargs):
        pass

    def find_contact_persist(self, id_profile):
        pass
