# -*- coding: utf-8 -*-

import unittest

from bootstrap.container import MockAppServicesInjector


class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.project()

    def project_test_1_find_all(self):
        params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}}
        self.assertEqual(self.service.find_all(params), [
            {
                'id': '1', 'description': 'test_1', 'idPropertyType': '1', 'idStage': '1', 'idProfile': '1',
                'name': 'test_1', 'idDepartment': '1', 'idProvince': '1', 'idDistrict': '1', 'state': '1',
                'idUrbanization': '1', 'idBeach': '1', 'address': 'test_1', 'reference': 'test_1', 'finished': 'test_1',
                'dateDelivery': '2018-05-05', 'datePublication': '2018-05-05', 'dateExpire': '2018-05-05',
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            },
            {
                'id': '2', 'description': 'test_2', 'idPropertyType': '1', 'idStage': '1', 'idProfile': '1',
                'name': 'test_2', 'idDepartment': '1', 'idProvince': '1', 'idDistrict': '1', 'state': '1',
                'idUrbanization': '1', 'idBeach': '1', 'address': 'test_2', 'reference': 'test_2', 'finished': 'test_2',
                'dateDelivery': '2018-05-05', 'datePublication': '2018-05-05', 'dateExpire': '2018-05-05',
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            },
            {
                'id': '3', 'description': 'test_3', 'idPropertyType': '1', 'idStage': '1', 'idProfile': '1',
                'name': 'test_3', 'idDepartment': '1', 'idProvince': '1', 'idDistrict': '1', 'state': '1',
                'idUrbanization': '1', 'idBeach': '1', 'address': 'test_3', 'reference': 'test_3', 'finished': 'test_3',
                'dateDelivery': '2018-05-05', 'datePublication': '2018-05-05', 'dateExpire': '2018-05-05',
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            },
            {
                'id': '4', 'description': 'test_4', 'idPropertyType': '1', 'idStage': '1', 'idProfile': '1',
                'name': 'test_4', 'idDepartment': '1', 'idProvince': '1', 'idDistrict': '1', 'state': '1',
                'idUrbanization': '1', 'idBeach': '1', 'address': 'test_4', 'reference': 'test_4', 'finished': 'test_4',
                'dateDelivery': '2018-05-05', 'datePublication': '2018-05-05', 'dateExpire': '2018-05-05',
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            }
        ])

    def project_test_2_find_by_id(self):
        self.assertEqual(self.service.find_by_id('1'), [
            {
                'idBeach': '1', 'reference': 'test_1', 'idProfile': '1', 'description': 'test_1', 'finished': 'test_1',
                'state': '1', 'datePublication': '2018-05-05', 'idStage': '1', 'idPropertyType': '1',
                'idUrbanization': '1', 'idDistrict': '1', 'name': 'test_1', 'idProvince': '1', 'id': '1',
                'dateDelivery': '2018-05-05', 'idDepartment': '1', 'dateExpire': '2018-05-05', 'address': 'test_1',
                'towers': 10, 'floors': 13, 'elevators': 4, 'garages': 10, 'units': 20
            }
        ])

    def project_test_3_create(self):
        data = {
            'metadata':
                {
                    'idPropertyType': '1',
                    'idStage': 1,
                    'idProfile': '1',
                    'name': 'test',
                    'idDepartment': '1',
                    'idProvince': '1',
                    'idDistrict': '1',
                    'idUrbanization': '1',
                    'idBeach': '1',
                    'address': 'Address',
                    'reference': 'Reference',
                    'description': 'Description',
                    'finished': 'Falta poquito',
                    'dateDelivery': '2018-05-05',
                    'state': '1'
                }
            }
        self.assertTrue(self.service.create(**data['metadata']))
