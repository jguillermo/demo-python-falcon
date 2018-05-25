# -*- coding: utf-8 -*-
import unittest

from bootstrap.container import MockAppServicesInjector


class ContactTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.contact()

    def contact_test_1_find_by_id(self):
        self.assertEqual(self.service.find_by_id(1),
                         {'phoneSecond': '969939230', 'name': 'Janet Milagros', 'schedule': 'Todos los dias', 'email': 'cunya.victor@gmail.com',
                          'emailGroup': 'victor.cunya@orbis.com.pe', 'phone': '950204432', 'state': 1, 'idProject': 1,
                          'lastName': 'Huacahuasi', 'id': 1}
                         )

    def contact_test_2_create(self):
        data = {
                  'metadata': {
                    'name': 'Gerardo',
                    'lastName': 'Cunya',
                    'phone': '950204432',
                    'schedule': 'Todos los días',
                    'email': 'cunya.victor@gmail.com',
                    'persist': {
                            'idProfile': 12
                        }
                    }
                }
        self.assertTrue(self.service.create(1, **data['metadata']))
