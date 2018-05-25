# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class BankTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.bank()

    def bank_test_1_find_all(self):
        params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}}
        self.assertEqual(self.service.find_all(params),
                         [
                             {"id": 1, "name": "Banco de comercio", "logo": None, "abbreviation": None, "state": 1},
                             {"id": 2, "name": "Banco de Crédito", "logo": None, "abbreviation": None, "state": 1},
                             {"id": 3, "name": "Banco de la Nación", "logo": None, "abbreviation": None, "state": 1},
                             {"id": 4, "name": "Banco Falabella", "logo": None, "abbreviation": None, "state": 1},
                         ])

    def bank_test_2_find_by_id(self):
        self.assertEqual(self.service.find_by_id(2),
                         [{"id": 2,
                           "name": "Banco de Crédito",
                           "logo": None,
                           "abbreviation": None,
                           "state": 1}])

    def bank_test_3_create(self):
        data = {'metadata': {
            'name': 'Continental',
            'logo': 'continental.jpg',
            'abbreviation': 'cont',
            'state': 1
            }
        }
        self.assertTrue(self.service.create(**data['metadata']))
