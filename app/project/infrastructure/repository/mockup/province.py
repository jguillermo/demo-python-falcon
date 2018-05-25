# -*- coding: utf-8 -*-
from project.domain.factories.entities.province import ProvinceFactory


class MockProvinceRepository():

    def __init__(self):
        self.data = [
            {"status": "1", "name": "CHACHAPOYAS", "beach": "1", "alias": "chachapoyas", "id": "1", "departmentId": "24"}
        ]

    def find_by_id(self, id_province):
        for key, province in enumerate(self.data):
            if province['id'] == id_province:
                return ProvinceFactory.create(self.data[key])
