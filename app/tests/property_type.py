# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class PropertyTypeTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.property_type()

    def property_type_test_1_find_all(self):
        params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}}
        self.assertEqual(self.service.find_all(params),[
            {'id': 1, 'idParent': None, 'level': '1', 'name': 'Residencial', 'state': 1},
            {'id': 2, 'idParent': 1, 'level': 2, 'name': 'Departamentos', 'state': 1},
            {'id': 3, 'idParent': 2, 'level': 3, 'name': 'Departamento', 'state': 1},
            {'id': 4, 'idParent': 2, 'level': 3, 'name': 'Departamento Duplex', 'state': 1},
            {'id': 5, 'idParent': 2, 'level': 3, 'name': 'Departamento Triplex', 'state': 1},
            {'id': 6, 'idParent': 2, 'level': 3, 'name': 'Departamento de Playa', 'state': 1},
            {'id': 7, 'idParent': 2, 'level': 3, 'name': 'Departamento Loft', 'state': 1},
            {'id': 8, 'idParent': 2, 'level': 3, 'name': 'Departamento Penthouse', 'state': 1},
            {'id': 9, 'idParent': 1, 'level': 2, 'name': 'Casas', 'state': 1},
            {'id': 10, 'idParent': 9, 'level': 3, 'name': 'Casa', 'state': 1},
            {'id': 11, 'idParent': 9, 'level': 3, 'name': 'Casa de playa', 'state': 1},
            {'id': 12, 'idParent': 9, 'level': 3, 'name': 'Casa de playa en condominio', 'state': 1},
            {'id': 13, 'idParent': 9, 'level': 3, 'name': 'Casa de campo', 'state': 1},
            {'id': 14, 'idParent': 9, 'level': 3, 'name': 'Casa en condominio', 'state': 1},
            {'id': 15, 'idParent': None, 'level': 1, 'name': 'Comercial', 'state': 1},
            {'id': 16, 'idParent': 15, 'level': 2, 'name': 'Oficinas', 'state': 1},
            {'id': 17, 'idParent': 15, 'level': 2, 'name': 'Locales comerciales', 'state': 1},
            {'id': 18, 'idParent': None, 'level': 1, 'name': 'Lotes', 'state': 1},
            {'id': 19, 'idParent': 18, 'level': 2, 'name': 'Lotes / terrenos', 'state': 1}
        ])

    def property_type_test_2_find_by_id(self):
        self.assertEqual(self.service.find_by_id(1), [
            {'id': 1, 'idParent': None, 'level': '1', 'name': 'Residencial', 'state': 1},
        ])
