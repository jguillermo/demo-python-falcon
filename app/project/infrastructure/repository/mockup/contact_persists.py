# -*- coding: utf-8 -*-

from project.domain.repository.contact_persists import ContactPersistsRepository
from project.domain.factories.entities.contact import ContactFactory


class MockContactPersistsRepository(ContactPersistsRepository):

    def __init__(self):
        self.data = [
            {
                'id': 1, 'idProject': 1, 'name': 'Janet Milagros', 'lastName': 'Huacahuasi', 'phone': '950204432',
                'phoneSecond': '969939230', 'schedule': 'Todos los dias', 'email': 'cunya.victor@gmail.com',
                'emailGroup': 'victor.cunya@orbis.com.pe', 'state': 1, 'persist': {'idProfile': 1}
            },
            {
                'id': 2, 'idProject': 2, 'name': 'Luis Miguel', 'lastName': 'Reyes', 'phone': '969967241',
                'phoneSecond': '969978541', 'schedule': 'Todos los dias', 'email': 'luis.reyes@gmail.com',
                'emailGroup': 'luis.reyes@orbis.com.pe', 'state': 1, 'persist': {'idProfile': 2}
            },
        ]

    def find_by_id_profile(self, id_profile):
        for contact in self.data:
            persist = contact.pop('persist')
            if persist.pop('idProfile') == id_profile:
                return ContactFactory.create(contact.pop('idProject'), **contact)
