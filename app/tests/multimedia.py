# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class MultimediaTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.multimedia()

    def multimedia_test_1_find_all(self):
        params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}}
        self.assertEqual(self.service.find_all(params),
            [{"state": 1, "url": "img", "name": "368490_plgalaxy.jpg", "id": 1, "type": 5},
            {"state": 1, "url": "img", "name": "368490_imagencasatest.jpg", "id": 2, "type": 1},
            {"state": 1, "url": "img", "name": "368490_plgalaxy.jpg", "id": 3, "type": 5}
                          ])

    def multimedia_test_2_find_by_id(self):
        self.assertEqual(self.service.find_by_id(1),
                         [{"state": 1, "url": "img", "name": "368490_plgalaxy.jpg", "id": 1, "type": 5}])

    def multimedia_test_3_create(self):
        data = {'metadata': {
            'name': 'Test1'}
        }
        self.assertTrue(self.service.create(**data['metadata']))
