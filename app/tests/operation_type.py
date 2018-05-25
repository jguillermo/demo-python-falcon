# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class OperationTypeTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.operation_type()

    def operation_type_test_1_find_all(self):
        params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}}
        self.assertEqual(self.service.find_all(params),
                         [{'id': 1, 'name': 'Venta', 'state': 1},
                          {'id': 2, 'name': 'Alquiler', 'state': 1}
                          ])
