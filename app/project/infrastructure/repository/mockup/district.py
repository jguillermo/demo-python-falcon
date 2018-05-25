# -*- coding: utf-8 -*-
from project.domain.factories.entities.district import DistrictFactory


class MockDistrictRepository():

    def __init__(self):
        self.data = [
            {"provinceId": "128", "status": "1", "name": "LA VICTORIA", "beach": "0", "alias": "la-victoria", "id": "3",
             "departmentId": "1"},
            {"beach": "0", "provinceId": "128", "departmentId": "1", "name": "CERCADO DE LIMA", "status": "1",
             "alias": "cercado-de-lima", "id": "1"}
        ]

    def find_by_id(self, id_district):
        for key, district in enumerate(self.data):
            if district['id'] == id_district:
                return DistrictFactory.create(self.data[key])
