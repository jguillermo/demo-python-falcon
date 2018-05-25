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


class Abbreviation(object):
    def __init__(self, abbreviation):
        self.value = abbreviation


class Logo(object):
    def __init__(self, logo):
        self.value = logo


class State(object):
    def __init__(self, state):
        self.value = state
