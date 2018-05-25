# -*- coding: utf-8 -*-
from project.domain.valueObjects import is_null


class Id(object):
    def __init__(self, id):
        self.value = id


class IdProject:
    def __init__(self, project_id):
        if is_null(project_id):
            raise ValueError(type(self).__name__ + ' cannot null')
        else:
            self.value = project_id


class IdMultimedia:
    def __init__(self, multimedia_id):
        if is_null(multimedia_id):
            raise ValueError(type(self).__name__ + ' cannot null')
        else:
            self.value = multimedia_id
