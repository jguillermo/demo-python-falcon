# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class StageTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.stage()

    def stage_test_1_find_all(self):
        params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}}
        self.assertEqual(self.service.find_all(params),
                         [{'id': 1, 'name': 'En Pre-venta', 'alias': 'pre-venta', 'type': 1, 'state': 1},
                          {'id': 2, 'name': 'En Construcción', 'alias': 'construccion', 'type': 1, 'state': 1}
                          ])

    def stage_test_2_find_by_id(self):
        self.assertEqual(self.service.find_by_id(1),
                         [{'id': 1, 'name': 'En Pre-venta', 'alias': 'pre-venta', 'type': 1, 'state': 1}])

    def stage_test_3_create(self):
        data = {'metadata': {
            'name': 'Test1'}
        }
        self.assertTrue(self.service.create(**data['metadata']))
