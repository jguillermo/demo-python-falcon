# -*- coding: utf-8 -*-
from project.domain.valueObjects import is_null


class Id:
    def __init__(self, id):
        self.value = id


class IdProject:
    def __init__(self, project_id):
        self.value = project_id

    def is_null(self):
        if is_null(self.value):
            raise ValueError('El id del proyecto no puede ser nulo')
        pass


class IdService:
    def __init__(self, service_id):
        self.value = service_id

    def is_null(self):
        if is_null(self.value):
            raise ValueError('El id del servicio no puede ser nulo')
        pass

