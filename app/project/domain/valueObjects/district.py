# -*- coding: utf-8 -*-
from project.domain.valueObjects import is_null


class Id(object):
    def __init__(self, id):
        self.value = id


class Name(object):
    def __init__(self, name):
        self.value = name

    def is_null(self):
        if is_null(self.value):
            raise ValueError(type(self).__name__+' cannot null')
        pass


class Alias(object):
    def __init__(self, alias):
        self.value = alias


class IdDepartment(object):
    def __init__(self, id_department):
        self.value = id_department


class IdProvince(object):
    def __init__(self, id_province):
        self.value = id_province


class Beach(object):
    def __init__(self, beach):
        self.value = beach


class Status(object):
    def __init__(self, status):
        self.value = status
