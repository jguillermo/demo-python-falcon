# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class ServiceProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.service_project()

    def service_project_test_1_create(self):
        project_id = 2
        data = {'metadata': {
            "services": [2, 3, 4]
            }
        }
        self.assertTrue(self.service.create(project_id, **data['metadata']))

    def service_project_test_2_find_by_project_id(self):
        project_id = 2
        self.assertEqual(self.service.find_by_project_id(project_id),
                         {"Services": [{"alias": "agua", "idService": 2,  "nombre": "Agua", "idProject": 2}]})
