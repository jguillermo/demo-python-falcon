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


class CountryId(object):
    def __init__(self, country_id):
        self.value = country_id


class Beach(object):
    def __init__(self, beach):
        self.value = beach

class Status(object):
    def __init__(self, status):
        self.value = status
