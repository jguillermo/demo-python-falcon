# -*- coding: utf-8 -*-
from project.domain.factories.entities.department import DeparmentFactory


class MockDepartmentRepository():

    def __init__(self):
        self.data = [
            {"beach": "1", "countryId": "1", "name": "LIMA", "status": "1", "alias": "lima", "id": "1"}
        ]

    def find_by_id(self, id_department):
        for key, department in enumerate(self.data):
            if department['id'] == id_department:
                return DeparmentFactory.create(self.data[key])
