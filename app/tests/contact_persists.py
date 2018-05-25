# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class ContactPersistsTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.contact_persists()

    def contact_persists_test_1_find_by_id(self):
        self.assertEqual(self.service.find_by_id(1), {
            'id': 1, 'idProject': 1, 'name': 'Janet Milagros', 'lastName': 'Huacahuasi', 'phone': '950204432',
            'phoneSecond': '969939230', 'schedule': 'Todos los dias', 'email': 'cunya.victor@gmail.com',
            'emailGroup': 'victor.cunya@orbis.com.pe', 'state': 1
        })
