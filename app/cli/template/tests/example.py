# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.example()

    def example_test_1_find_all(self):
        params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}}
        self.assertEqual(self.service.find_all(params),
                         [{'id': 1, 'name': 'Escalera al cielo'},
                          {'id': 2, 'name': 'Dulce hogar'}
                          ])

    def example_test_2_find_by_id(self):
        self.assertEqual(self.service.find_by_id(1), [{'id': 1, 'name': 'Escalera al cielo'}])

    def example_test_3_create(self):
        data = {'metadata': {
            'name': 'Test1'}
        }
        self.assertTrue(self.service.create(**data['metadata']))
